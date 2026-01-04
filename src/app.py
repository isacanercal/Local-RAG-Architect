import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

# 1. EMBEDDING: Bellek dostu model (CPU'da çalışır)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = None

def process_pdf(pdf_file):
    global vectorstore
    if pdf_file is None: return "❌ Hata: Dosya seçilmedi!"
    loader = PyPDFLoader(pdf_file.name)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embedding_model)
    return "✅ Knowledge Base Updated!"

def rag_chat(message, history):
    global vectorstore
    llm = Ollama(model="llama3.1")
    
    if vectorstore is None:
        # PDF yüklenmemişse direkt LLM'e sor
        prompt = f"Question: {message}\n\nAnswer:"
        return llm.invoke(prompt)
    
    # PDF yüklenmişse RAG kullan
    docs = vectorstore.similarity_search(message, k=3)
    context = "\n\n".join([d.page_content for d in docs])
    prompt = f"Context: {context}\n\nQuestion: {message}\n\nAnswer:"
    return llm.invoke(prompt)

# --- MODERN ARAYÜZ CSS ---
custom_css = """
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}
.app-container {
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
}
.header-box {
    background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
    padding: 40px;
    border-radius: 20px;
    margin-bottom: 30px;
    border: 2px solid #533483;
    box-shadow: 0 8px 32px rgba(83, 52, 131, 0.3);
}
.main-title {
    color: #ffffff !important;
    font-size: 3em !important;
    font-weight: 900 !important;
    text-align: center !important;
    margin-bottom: 10px !important;
    background: linear-gradient(90deg, #00d9ff, #00ff88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.subtitle {
    color: #b8b8b8 !important;
    font-size: 1.1em !important;
    text-align: center !important;
    font-weight: 400 !important;
}
.upload-section {
    background: #1e1e2e;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #2d2d44;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}
.btn-primary {
    background: linear-gradient(90deg, #00d9ff, #00ff88) !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 15px !important;
    font-size: 1.1em !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 20px rgba(0, 217, 255, 0.4) !important;
    transition: all 0.3s ease !important;
}
.btn-primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 30px rgba(0, 217, 255, 0.6) !important;
}
.chat-section {
    background: #1e1e2e;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2d2d44;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}
.status-display {
    background: #16213e !important;
    color: #00ff88 !important;
    border: 1px solid #00d9ff !important;
    font-family: 'Courier New', monospace !important;
    font-size: 0.95em !important;
    padding: 12px !important;
    border-radius: 8px !important;
}
.specs-box {
    background: #16213e !important;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #00d9ff;
    margin-top: 15px;
}
.specs-box .label-wrap {
    background: #16213e !important;
}
.specs-box p, .specs-box ul, .specs-box li, .specs-box strong, .specs-box span, .specs-box div {
    color: #ffffff !important;
}
.specs-box strong {
    color: #00ff88 !important;
    font-weight: 700 !important;
}
.specs-box .markdown {
    color: #ffffff !important;
}
/* Accordion içeriği için */
.accordion {
    background: #16213e !important;
}
.accordion .label-wrap span {
    color: #ffffff !important;
}
.accordion-content {
    background: #16213e !important;
    color: #ffffff !important;
}
"""

with gr.Blocks() as demo:
    # Header
    with gr.Group(elem_classes="header-box"):
        gr.Markdown("# 🤖 RAG Intelligence System", elem_classes="main-title")
        gr.Markdown("*Yapay zeka destekli PDF analiz ve soru-cevap sistemi*", elem_classes="subtitle")
    
    with gr.Row():
        # Sol Panel - PDF Yükleme
        with gr.Column(scale=1):
            with gr.Group(elem_classes="upload-section"):
                gr.Markdown("### 📁 Belge Yönetimi")
                pdf_input = gr.File(
                    label="PDF Dosyasını Yükle", 
                    file_types=[".pdf"],
                    file_count="single"
                )
                analyze_btn = gr.Button(
                    "⚡ Analiz Başlat",
                    variant="primary",
                    elem_classes="btn-primary",
                    size="lg"
                )
                status_output = gr.Textbox(
                    label="📊 Durum",
                    elem_classes="status-display",
                    interactive=False,
                    lines=2
                )
            
            with gr.Accordion("⚙️ Sistem Bilgileri", open=False, elem_classes="specs-box"):
                gr.Markdown("""
                **Aktif Konfigürasyon:**
                - 🧠 Model: Llama-3.1-8B
                - 🎯 Embedding: MiniLM-L6-v2
                - 💾 Veritabanı: ChromaDB
                - 🖥️ GPU: RTX 3060 (6GB)
                - 📊 Chunk Size: 800 tokens
                """)
        
        # Sağ Panel - Chat
        with gr.Column(scale=2):
            with gr.Group(elem_classes="chat-section"):
                gr.Markdown("### 💬 Akıllı Sohbet Asistanı")
                chatbot = gr.ChatInterface(
                    fn=rag_chat,
                    examples=[
                        "Bu belge ne hakkında?",
                        "Ana konuları özetle",
                        "Önemli noktalar neler?"
                    ],
                    chatbot=gr.Chatbot(height=800)
                )
    
    # Event Handlers (Backend bağlantıları)
    analyze_btn.click(
        fn=process_pdf,
        inputs=pdf_input,
        outputs=status_output
    )

if __name__ == "__main__":
    demo.launch(
        share=True,
        css=custom_css,
        theme=gr.themes.Soft(primary_hue="cyan", secondary_hue="purple")
    )