# Azure AI Chatbot

AI-powered chatbot built using Azure OpenAI, FastAPI, and Azure App Service.

## Architecture
- Azure OpenAI
- FastAPI backend
- Azure App Service
- GitHub Actions CI/CD
- Infrastructure as Code (Bicep)

## Endpoints
- GET /health
- POST /chat

## Deployment
```bash
az deployment group create \
  --resource-group rg-chatbot \
  --template-file infra/main.bicep \
  --parameters appName=azure-ai-chatbot
