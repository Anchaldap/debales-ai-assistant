# debales-ai-assistant
A smart AI-powered assistant built using LangGraph, Retrieval-Augmented Generation (RAG), and SERP API that answers questions about Debales AI and general topics with high accuracy and no hallucination.
🤖 Debales AI Assistant

LangGraph + RAG + SERP API Powered Chatbot

📌 Overview

Debales AI Assistant is an intelligent chatbot that answers both Debales AI-specific queries and general knowledge questions using a hybrid architecture.

It combines:

📚 RAG (Retrieval-Augmented Generation) for domain-specific answers
🌐 SERP API (Google Search) for real-time external knowledge
🔄 LangGraph workflow for smart routing of queries

The system ensures high accuracy and minimal hallucination by grounding responses in real data.

🚀 Features
✅ RAG pipeline using scraped Debales AI website content
✅ SERP API integration for real-time web search
✅ LLM-based intelligent query routing (RAG / SERP / BOTH)
✅ Streamlit interactive UI
✅ FAISS vector database for fast semantic retrieval
✅ Fallback mechanism ("I don’t know") to avoid hallucination
✅ Clean and modular code structure
🧠 How It Works
User Query
    ↓
LangGraph Router (LLM-based)
    ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
RAG           SERP API         BOTH
 ↓               ↓               ↓
Context       Web Results     Combined Context
        ↓
     LLM Response
🛠️ Tech Stack
Python
LangChain
LangGraph
FAISS (Vector DB)
OpenAI (LLM)
SerpAPI (Google Search)
BeautifulSoup (Web Scraping)
Streamlit (UI)
📁 Project Structure
debales-ai-assistant/
│
├── app.py                 # Streamlit UI
├── graph.py               # LangGraph workflow
├── rag.py                 # RAG pipeline
├── scraper.py             # Website scraping
├── serp_tool.py           # SERP API integration
├── router.py              # Query routing logic
├── config.py              # Environment config
│
├── data/content.txt       # Scraped data
├── vectorstore/           # FAISS index
│
├── requirements.txt
├── .env.example
└── README.md
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-url>
cd debales-ai-assistant
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
SERP_API_KEY=your_serpapi_key
4️⃣ Run Data Pipeline
python scraper.py
python -c "from rag import build_vectorstore; build_vectorstore()"
5️⃣ Launch Application
streamlit run app.py
