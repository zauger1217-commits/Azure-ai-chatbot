# ☁️ Azure AI Chatbot 🤖

A cloud-deployed AI chatbot using **FastAPI**, **Azure OpenAI**, and **Azure Container Apps**.  
This project demonstrates building, containerizing, and deploying an AI service in Azure with Infrastructure-as-Code.

---

## ✨ Features

- Chatbot API using Azure OpenAI GPT deployment  
- FastAPI backend with `/chat` and `/health` endpoints  
- Containerized with Docker 🐳 (built in Azure via ACR)  
- Hosted in **Azure Container Apps** ☁️ with a public endpoint  
- Includes root endpoint (`/`) with a friendly message 😄

---

## 🛠️ Prerequisites

- Azure subscription 🌐  
- Azure CLI installed ⚡  
- Git and GitHub account 🐱‍💻  
- Optional: Visual Studio Code for editing 🖥️  

---

## 🚀 Quick Start: Deploy Locally in Azure

1. **Clone the repo**:

```bash
git clone https://github.com/YOUR_USERNAME/azure-ai-chatbot.git
cd azure-ai-chatbot
```

2. **Set environment variables**:

```bash
set AZURE_OPENAI_ENDPOINT=https://YOUR_RESOURCE.openai.azure.com/
set AZURE_OPENAI_KEY=YOUR_KEY
set AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

3. **Register Azure providers (bump #1 & #2)**:

```bash
az provider register --namespace Microsoft.ContainerRegistry --wait
az provider register --namespace Microsoft.OperationalInsights --wait
```

> These are required for **Azure Container Registry** 🏷️ and **Log Analytics** 📊.

4. **Create a resource group** (if not done already):

```bash
az group create --name azure-ai-chatbot-rg --location eastus
```

5. **Create a Container Apps environment**:

```bash
az containerapp env create \
  --name azure-ai-chatbot-env \
  --resource-group azure-ai-chatbot-rg \
  --location eastus
```

> Log Analytics workspace is automatically created during this step.

6. **Build Docker image in Azure Container Registry (no local Docker needed)**:

```bash
az acr build \
  --registry azureaichatbotacr \
  --image chatbot:latest \
  .
```

7. **Deploy Container App**:

```bash
az containerapp create \
  --name azure-ai-chatbot \
  --resource-group azure-ai-chatbot-rg \
  --environment azure-ai-chatbot-env \
  --image azureaichatbotacr.azurecr.io/chatbot:latest \
  --target-port 8000 \
  --ingress external \
  --registry-server azureaichatbotacr.azurecr.io \
  --min-replicas 0 \
  --max-replicas 1 \
  --env-vars \
    AZURE_OPENAI_ENDPOINT=$AZURE_OPENAI_ENDPOINT \
    AZURE_OPENAI_KEY=$AZURE_OPENAI_KEY \
    AZURE_OPENAI_DEPLOYMENT=$AZURE_OPENAI_DEPLOYMENT
```

8. **Get the live URL** 🌐:

```bash
az containerapp show \
  --name azure-ai-chatbot \
  --resource-group azure-ai-chatbot-rg \
  --query properties.configuration.ingress.fqdn \
  -o tsv
```

- Open `<URL>/docs` for Swagger UI 📖  
- Open `<URL>/` for friendly root endpoint 😄  

---

## ⚠️ Common Issues & Roadblocks

1. **Git setup & commits**  
- Ensure `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"` are set before committing  

2. **Docker not installed locally** 🐳  
- Solved using `az acr build` → builds in Azure, no Docker needed locally  

3. **Subscription not registered for Microsoft.ContainerRegistry**  
- Fixed with: `az provider register --namespace Microsoft.ContainerRegistry --wait`  

4. **Subscription not registered for Microsoft.OperationalInsights** 📊  
- Fixed with: `az provider register --namespace Microsoft.OperationalInsights --wait`  

5. **Deployment failed due to missing Container Apps environment**  
- Always create environment first:  
  `az containerapp env create --name azure-ai-chatbot-env --resource-group azure-ai-chatbot-rg`  

6. **Root endpoint returned “Not Found”**  
- Added a `/` route in `main.py`:

```python
@app.get("/")
def read_root():
    return {"message": "Azure AI Chatbot is running! Visit /docs to see API endpoints."}
```

---

## 📁 Project Structure

```
azure-ai-chatbot/
│
├─ app/
│  ├─ main.py          # FastAPI backend
│  └─ requirements.txt
├─ Dockerfile 🐳
├─ main.bicep ☁️       # Azure IaC template
└─ README.md 📖
```

---

## 📝 Notes

- **main.bicep**: Keep as a template for deploying infrastructure with placeholders:

```bicep
param azure_openai_endpoint string = 'REPLACE_ME'
param azure_openai_key string = 'REPLACE_ME'
```

- **Environment variables** must be replaced with your actual Azure OpenAI deployment info.

