# 🎥 YouTubeRAGChat-Extension

A Chrome Extension that enables conversational interaction with YouTube videos using RAG (Retrieval-Augmented Generation) powered by **LangChain**, served via a **FastAPI** backend.

---

## 🚀 Features

- 🧠 Ask questions about YouTube videos (e.g., “What’s the main idea?”, “Summarize in 3 points”)
- 🔍 Automatic transcript extraction from YouTube videos
- ⚙️ FastAPI-powered backend for inference and document indexing
- 🧩 Seamless Chrome Extension interface
- 🔗 LangChain for chaining prompts and retrieval from vector stores

---

---

## 🛠️ Installation & Setup

### 🧩 1. Load Chrome Extension

1. Open **Chrome** → `chrome://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked** and select the `extension/` folder

### 🚀 2. Start FastAPI Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
The backend will run at http://localhost:8000.
