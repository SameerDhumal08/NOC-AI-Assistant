# 🖥️ NOC AI Assistant using Hybrid RAG

An AI-powered Network Operations Center (NOC) Assistant built using **Retrieval-Augmented Generation (RAG)**. The assistant helps IT support engineers quickly troubleshoot infrastructure alerts by retrieving relevant SOPs, historical incidents, and operational guides before generating an AI-powered response.

---

## 🚀 Features

- 🤖 AI-powered NOC Assistant
- 🔍 Hybrid RAG Architecture
- 📄 PDF SOP Knowledge Base
- 📊 Historical NOC Ticket Search
- 📑 NOC FAQ Retrieval
- ⚡ Fast inference using Groq API
- 🧠 Qwen3-32B Large Language Model
- 💬 Interactive Streamlit Chat Interface
- 🗂️ Chroma Vector Database
- 🔎 Semantic Search using HuggingFace Embeddings

---

# 🏗️ Architecture

```
                    User

                      │

                      ▼

            Streamlit Chat UI

                      │

                      ▼

                RAG Chain

                      │

        ┌─────────────┼─────────────┐

        ▼             ▼             ▼

   NOC FAQ      NOC Tickets      SOP PDF

        │             │             │

        └─────────────┼─────────────┘

                      ▼

             Chroma Vector Database

                      │

                      ▼

        HuggingFace Embedding Model

                      │

                      ▼

            Groq API (Inference)

                      │

                      ▼

              Qwen3-32B LLM

                      │

                      ▼

               AI Generated Answer
```

---

# 📂 Project Structure

```
rag-telecom-chatbot/
│
├── app.py
├── main.py
├── rag_chain.py
├── retriever.py
│
├── ingest_noc_faq.py
├── ingest_noc_tickets.py
├── ingest_noc_pdf.py
│
├── chroma_store/
│
├── data/
│   ├── noc.csv
│   ├── noc_tickets.db
│   ├── noc_guide.pdf
│   └── seed_noc_tickets.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Framework |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Semantic Embeddings |
| Groq | LLM Inference Platform |
| Qwen3-32B | Large Language Model |
| SQLite | Historical Ticket Database |

---

# 📚 Knowledge Sources

The assistant retrieves information from three sources:

### 1. NOC FAQ

Contains:

- CPU Alerts
- Memory Alerts
- Disk Alerts
- Network Alerts
- Firewall Alerts
- Database Alerts
- Windows Alerts
- Linux Alerts

---

### 2. Historical NOC Tickets

Contains resolved incidents such as:

- CPU Utilization High
- Memory Utilization High
- Port Down
- Link Flapping
- Database Listener Down
- Firewall Interface Down
- SNMP Failure
- Application Down
- Backup Failure
- Server Down

---

### 3. NOC SOP PDF

Contains operational documentation including:

- Standard Operating Procedures
- Troubleshooting Steps
- Root Cause Analysis
- Resolution Process
- Escalation Matrix
- Best Practices

---

# ⚙️ How RAG Works

```
User Question

      │

      ▼

Retriever searches

• FAQ

• Historical Tickets

• SOP PDF

      │

      ▼

Relevant Documents

      │

      ▼

Prompt Template

      │

      ▼

Qwen3-32B

      │

      ▼

AI Generated Response
```

---

# 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/SameerDhumal08/RAGFlow.git
```

Move into the project

```bash
cd RAGFlow
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```
GROQ_API_KEY=your_api_key
```

---

# 📥 Ingest Knowledge Base

Load FAQ

```bash
python ingest_noc_faq.py
```

Load Historical Tickets

```bash
python data/seed_noc_tickets.py
python ingest_noc_tickets.py
```

Load SOP PDF

```bash
python ingest_noc_pdf.py
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 💬 Example Questions

- CPU utilization above 95% on Linux server
- Windows server memory utilization high
- Oracle listener is down
- Cisco switch port down
- Link flapping detected
- Disk utilization exceeded threshold
- Firewall interface down
- SNMP service not responding
- Application service stopped
- Backup job failed

---

# 🎯 Use Cases

- NOC Operations
- IT Infrastructure Monitoring
- Incident Management
- SOP Automation
- AI Service Desk
- ITSM Automation
- L1 Support Automation
- Historical Incident Retrieval

---

# 🔮 Future Enhancements

- Hybrid Search (Vector + Keyword)
- Multi-LLM Support
- Jira / ServiceNow Integration
- ManageEngine Integration
- Auto Ticket Creation
- Root Cause Analysis
- AI Incident Summarization
- Grafana & Prometheus Integration
- Voice-enabled NOC Assistant

---

# 👨‍💻 Author

**Sameer Dhumal**

IT Professional | NOC Engineer | AI & RAG Enthusiast

GitHub:
https://github.com/SameerDhumal08

LinkedIn:
https://www.linkedin.com/in/sameerdhumal14/

---

# ⭐ If you found this project useful, consider giving it a star!
<img width="1901" height="871" alt="image" src="https://github.com/user-attachments/assets/f8f1e310-a63e-4fcd-b745-5664c5bf1b4b" />
