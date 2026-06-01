# AI-DataSuite: A Comprehensive AI & Data Suite

This modular AI suite orchestrates autonomous agents via **OpenClaw**, utilizes **embedding** models for semantic intelligence, and leverages **ChromaDB** for persistent, local vector storage and **LangChain** for fully offline Retrieval-Augmented Generation (RAG).

---

## 🚀 Key Modules

### 🤖 Autonomous AI Agents (OpenClaw)
 [📊 View Autonomous Multi-Agent ](https://panxiaoyan225-sudo.github.io/AI-DataSuite/Openclaw.html)
*   **Autonomous Multi-Agent Framework**: An objective-driven system utilizing **OpenClaw** where independent agents (**Mei, John, Sam**) execute complex tasks through collaborative or independent workflows.
*   **Isolated Workspaces**: Ensures data security by running each agent within a dedicated local file-system environment.
*   **API Gateway Orchestration**: Centralized routing via **OpenRouter** and **Ollama**, transitioning from simple chatbots to goal-oriented autonomous systems.

### 🧬 Semantic Search & Embeddings
*   **Local_Embeddings.py**: High-performance text vectorization using `all-MiniLM-L6-v2` running locally.
*   **Vector Similarity Engine**: Pure **NumPy** implementation of Cosine Similarity for document comparison without external API dependencies.
*   **Precision Chunking**: Implements `RecursiveCharacterTextSplitter` to maintain semantic integrity by breaking documents at natural paragraph and sentence boundaries.

### 📦 Vector Databases & RAG (LangChain)
*   **chromaDB_model.py**: Implementation of a persistent local vector store using **ChromaDB** for cross-session data retrieval.
*   **Local RAG Application**: A complete pipeline built with **LangChain** and **Ollama** (Llama 3) that retrieves relevant local context to answer queries without any cloud API calls.
*   **Automated Indexing**: Handles document loading, recursive chunking, and metadata tagging to build a private knowledge base.

### 🧠 Natural Language Processing (NLP)
*   **NLP_Sentiment.py**: Emotional tone analysis powered by Hugging Face **Transformers**.
*   **Text Classification**: Tools for categorizing text data into custom labels using state-of-the-art LLMs.
*   **LangChain Orchestration**: Modular "Chain" workflows for custom prompt management and agent logic.

### 📈 Financial Intelligence
*   **Stock_app.py**: Streamlit dashboard featuring **LSTM** neural networks for historical price prediction.
*   **Genai_Agent.py**: Modern AI agent leveraging **Gemini 2.0 Flash** with function calling for real-time market insights via `yfinance`.

### 🎙️ Speech & Travel Intelligence
*   **ASR_Audio_Transcriber.py**: Automated speech-to-text transcription using OpenAI’s **Whisper**.
*   **Gtts_TextToAudio.py**: Converts text to natural speech via Google Text-to-Speech (gTTS).
*   **Flight_Search_App.py**: GenAI Agent that identifies the top 3 cheapest flights with real-time pricing and direct booking links.

---

## 🛠️ Technical Stack

*   **Languages**: Python, HTML/CSS
*   **Agent Frameworks**: OpenClaw, OpenRouter, Ollama
*   **Vector DB & RAG**: ChromaDB, LangChain, Ollama (Llama 3, Nomic-Embed)
*   **AI/ML Frameworks**: PyTorch, Sentence-Transformers, Hugging Face, Google GenAI
*   **Data & Math**: NumPy, Pandas, Scikit-learn, YFinance
*   **Deployment**: Docker, Windows/WSL2, GitHub Actions
