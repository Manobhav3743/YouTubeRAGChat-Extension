# YouTube Chat Extension

This project is a YouTube chat extension that utilizes Langchain to extract transcripts from YouTube videos and build a retrieval-augmented generation (RAG) system. The system chunks the transcripts, embeds them, and stores them in a vector store for efficient retrieval using the Hugging Face LLAMA model for generation and embeddings.

## Project Structure

```
youtube-chat-extension
├── src
│   ├── main.py                # Entry point of the application
│   ├── youtube
│   │   ├── transcript_extractor.py  # Extracts transcripts from YouTube videos
│   │   └── __init__.py
│   ├── rag
│   │   ├── chunker.py         # Chunks transcripts for processing
│   │   ├── embedder.py        # Generates embeddings for chunks
│   │   ├── vector_store.py     # Stores embeddings in a vector store
│   │   ├── retriever.py       # Retrieves relevant chunks based on queries
│   │   └── __init__.py
│   ├── llm
│   │   ├── llama_client.py     # Interacts with the Hugging Face LLAMA model
│   │   └── __init__.py
│   └── utils
│       └── helpers.py         # Utility functions for various tasks
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-chat-extension
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

- To run the application, execute the following command:
  ```
  python src/main.py
  ```

- The application will initialize the extension and allow interaction with YouTube videos to extract transcripts and generate responses.

## Functionality Overview

- **Transcript Extraction**: The `TranscriptExtractor` class fetches and extracts transcripts from YouTube video URLs.
- **Chunking**: The `Chunker` class splits the transcripts into manageable chunks for processing.
- **Embedding**: The `Embedder` class generates embeddings for the chunks using the Hugging Face LLAMA model.
- **Vector Store**: The `VectorStore` class stores the embeddings for efficient retrieval.
- **Retrieval**: The `Retriever` class fetches relevant chunks based on user queries.
- **Response Generation**: The `LlamaClient` class interacts with the LLAMA model to generate responses based on input prompts.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.