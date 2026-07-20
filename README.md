# Multi-Agent AI System

An Autonomous Multi-Agent AI application built using **Python, LangChain, LangGraph, Groq LLM, Tavily Search, Docker, and Streamlit**. The system understands user requests, creates an execution plan, performs AI-powered research, and generates structured responses through a web interface.

---

## 🚀 Features

* Multi-Agent Architecture
* AI-powered Task Planning & Execution
* Groq LLM Integration
* Tavily Web Search Integration
* Streamlit Web Interface
* Docker Containerization
* AWS EC2 Deployment
* Environment Variable Support (.env)
* Modular Python Code

---

## 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* Groq API
* Tavily Search API
* Streamlit
* Docker
* AWS EC2
* python-dotenv

---

## 📂 Project Structure

```
Multi-Agent-System/
│── agent.py
│── app.py
│── pipeline.py
│── tools.py
│── Dockerfile
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Jishanshk/multi-agent-system.git
cd multi-agent-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Run the application

```bash
streamlit run app.py
```

---

## 🐳 Docker

### Build Docker Image

```bash
docker build -t multi-agent-system .
```

### Run Docker Container

```bash
docker run -d -p 8501:8501 --env-file .env multi-agent-system
```

---

## ☁️ AWS Deployment

This application has been successfully deployed on **AWS EC2** using **Docker**.

Deployment workflow:

```
GitHub
   ↓
AWS EC2 (Ubuntu)
   ↓
Docker Container
   ↓
Streamlit Application
```
## 🌐 Deployment

- Successfully deployed on AWS EC2 using Docker
- Streamlit application accessible through a public IP
---

## 📌 Future Improvements

* GitHub Actions CI/CD
* MLflow Integration
* Agent Memory
* Multiple LLM Providers
* File Upload Support
* Monitoring Dashboard
* Kubernetes Deployment

---

## 👨‍💻 Author

**Jishan Wasim Shaikh**

AI/ML Engineer | Generative AI | LangChain | LangGraph | RAG | Docker | AWS | Python

