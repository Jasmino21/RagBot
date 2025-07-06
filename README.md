# 🧠 Modular RAG PDF Chatbot with FastAPI, ChromaDB & Streamlit

This project is a modular **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and chat with an AI assistant that answers queries based on the document content. It features a microservice architecture with a decoupled **FastAPI backend** and **Streamlit frontend**, using **ChromaDB** as the vector store and **Groq's LLaMA3 model** as the LLM.

---

## 📂 Project Structure

```
ragbot2.0/
├── client/         # Streamlit Frontend
│   |──components/
|   |  |──chatUI.py
|   |  |──history_download.py
|   |  |──upload.py
|   |──utils/
|   |  |──api.py
|   |──app.py
|   |──config.py
├── server/         # FastAPI Backend
│   ├── chroma_store/ ....after run
|   |──modules/
│      ├── load_vectorestore.py
│      ├── llm.py
│      ├── pdf_handler.py
│      ├── query_handlers.py
|   |──uploaded_pdfs/ ....after run
│   ├── logger.py
│   └── main.py
└── README.md
```

---

## ✨ Features

- 📄 Upload and parse PDFs
- 🧠 Embed document chunks with HuggingFace embeddings
- 💂️ Store embeddings in ChromaDB
- 💬 Query documents using LLaMA3 via Groq
- 🌍 Microservice architecture (Streamlit client + FastAPI server)


## 🌟 Credits

- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)


