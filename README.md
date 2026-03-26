# ContractIQ-AI is an end-to-end intelligent legal document processing system built using GenAI, NLP, and Azure services. The system automates the analysis of legal contracts by extracting structured insights such as document type, key clauses, and critical business attributes.

The application enables users to upload legal documents (e.g., MSA, SOW, NDA), which are then processed through an AI-powered pipeline involving OCR, large language models, and semantic search. The extracted data is structured into JSON and can be further queried using a Retrieval-Augmented Generation (RAG) approach.

**Workflow**
Upload Document
→ Azure Blob Storage
→ OCR (Document Intelligence)
→ LLM (Classification + Extraction)
→ Structured Output (JSON)
→ Indexing (Cognitive Search)
→ Query (RAG)
