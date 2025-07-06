import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEmbeddings
from huggingface_hub import InferenceClient


from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

# Add this after app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QARequest(BaseModel):
    video_url: str
    question: str


@app.post("/ask")
def ask(req: QARequest):
    answer = RAG(req.video_url, req.question)
    return {"answer": answer}

# Load environment variables
load_dotenv()

def RAG(video_url,question):
    client = InferenceClient(
    provider="auto",
    api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    )
    #TRANCSCRIPT EXTRACTOR
    video_id = video_url.split("v=")[-1].split("&")[0]
    try:
        # If you don’t care which language, this returns the “best” one
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en","hi"])
        # Flatten it to plain text
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        print(transcript)

    except TranscriptsDisabled:
        print("No captions available for this video.")
        exit(1)
    
    #SPLITTER
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    #VECTOR STORE THE EMBEDDINGS OF THE CHUNKS
    vector_store = FAISS.from_documents(chunks, embeddings)
    #RETRIEVER
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 8})
    #THE MODEL
    llm = HuggingFaceEndpoint(
        repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation"
    )
    model=ChatHuggingFace(llm=llm)
    prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)
    print(f"Question: {question}")
    
    retrieved_docs    = retriever.invoke(question)
    
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    final_prompt = prompt.invoke({"context": context_text, "question": question})

    res = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": str(final_prompt)
        }
    ],
)
    return (res.choices[0].message.content)

