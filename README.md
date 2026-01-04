# 🧠 Local RAG Architect v1.0

![Python](https://img.shields.io/badge/python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NVIDIA](https://img.shields.io/badge/nvidiao-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

An optimized **Retrieval-Augmented Generation (RAG)** system designed to run on **NVIDIA RTX 3060 (6GB VRAM)**. This project enables secure, offline analysis of technical PDF documents using **Llama-3.1-8B**.

## 📸 Demo
<p align="center">
  <img src="assets/before.png" width="45%" alt="Initial UI" />
  <img src="assets/after.png" width="45%" alt="RAG in Action" />
</p>

## 🚀 Key Features
- **100% Private:** No data leaves your local machine (powered by Ollama).
- **VRAM Optimized:** 4-bit quantization and CPU-offloaded embeddings.
- **Precision Retrieval:** Built with ChromaDB and LangChain for high-accuracy technical queries.

## 🛠 Tech Stack
- **LLM:** Llama-3.1-8B
- **Vector DB:** ChromaDB
- **UI:** Gradio 6.0
- **Embedding:** HuggingFace `all-MiniLM-L6-v2`

## 📥 Setup
1. `git clone https://github.com/isacanercal/pdf_okuyan_rag_projesi.git`
2. `pip install -r requirements.txt`
3. `ollama pull llama3.1`
4. `python src/app.py`

---
Developed by **İsa Caner Çal** | Computer Engineering 
