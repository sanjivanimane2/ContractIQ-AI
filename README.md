# ContractIQ-AI 
ContractIQ-AI is an end-to-end intelligent legal document processing system built using GenAI, NLP, and Azure services. The system automates the analysis of legal contracts by extracting structured insights such as document type, key clauses, and critical business attributes.
The application enables users to upload legal documents (e.g., MSA, SOW, NDA), which are then processed through an AI-powered pipeline involving OCR, large language models, and semantic search. The extracted data is structured into JSON and can be further queried using a Retrieval-Augmented Generation (RAG) approach.

## 🔥 Features

- 📄 Document Classification (MSA, SOW, NDA)
- 📑 Clause Extraction (structured JSON)
- 🧾 Attribute Extraction (Effective Date, Parties, etc.)
- ☁️ Azure Blob Storage (file storage)
- 🧠 Azure OpenAI (LLM processing)
- 🔍 Azure Cognitive Search (RAG)
- 🧩 Prompt Versioning System
- 🎯 Few-shot Prompting for accuracy

## 🧠 Tech Stack

- FastAPI
- Azure OpenAI
- Azure Blob Storage
- Azure Document Intelligence
- Azure Cognitive Search
- spaCy (NLP)
## ⚙️ Setup

```bash
git clone https://github.com/your-username/contractiq-ai.git
cd contractiq-ai
cp .env.example .env
