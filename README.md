


🧠 Local RAG Architect v1.0

![Python](https://img.shields.io/badge/python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NVIDIA](https://img.shields.io/badge/nvidiao-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

An optimized **Retrieval-Augmented Generation (RAG)** system designed for high-performance PDF analysis on consumer-grade hardware (**NVIDIA RTX 3060 - 6GB VRAM**). This project ensures 100% data privacy by running entirely offline using **Llama-3.1-8B**.

## 📸 Demo & UI
<p align="center">
  <img src="assets/before.png" width="45%" alt="Initial UI" />
  <img src="assets/after.png" width="45%" alt="RAG in Action" />
</p>

## 🚀 Key Features
- **Zero-Cloud Privacy:** No data ever leaves your machine. Ideal for confidential technical documents.
- **Hardware Optimized:** Custom implementation using 4-bit quantization (GGUF) and CPU-offloaded embeddings to fit within 6GB VRAM limits.
- **Industrial Interface:** A modern, high-contrast dashboard built with **Gradio 6.0** for better readability.
- **Smart Context:** Uses `RecursiveCharacterTextSplitter` and `ChromaDB` for high-precision semantic search.

## 🛠 Tech Stack
- **LLM:** Llama-3.1-8B (via Ollama)
- **Vector Database:** ChromaDB
- **Orchestration:** LangChain
- **UI Framework:** Gradio 6.0
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2`

## 📥 Quick Start

1. **Clone the Repository:**
```bash
git clone [https://github.com/isacanercal/Local-RAG-Architect.git](https://github.com/isacanercal/Local-RAG-Architect.git)
cd Local-RAG-Architect
```

2. **Install Dependencies:**   

```pip install -r requirements.txt
```

3. **Prepare the Model:**

```ollama pull llama3.1
```

 4.**Launch the Architect:**

```python src/app.py
```

 Note: You can find a sample technical report in the sample_data/ folder to test the system's indexing capabilities immediately.
 
Developed by İsa Caner Çal | Computer Engineering Student
