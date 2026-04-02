# ⚖️ Digital Lawyer (ChatGPT + Gradio)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenAI](https://img.shields.io/badge/API-OpenAI-green)
![UI](https://img.shields.io/badge/UI-Gradio-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

An interactive AI-powered legal assistant built with Python, leveraging OpenAI's language models and a Gradio web interface. The app simulates a lawyer persona to answer legal-related questions in real time.

---

## ✨ Demo Overview

- 💬 Chat with an AI lawyer in real time  
- ⚖️ Provides legal-style responses  
- 🌐 Runs in a browser via Gradio  
- 🔁 Maintains conversation context  

---

## 🚀 Features

- 🤖 AI chatbot powered by OpenAI  
- 🧠 Context-aware conversations using message history  
- 🎭 Custom system prompt (“You are a lawyer”)  
- 🖥️ Simple and clean web UI with Gradio  
- 🔗 Shareable public link (`share=True`)  

---

## 🏗️ Architecture
User Input (Browser)
↓
Gradio Interface
↓
CustomChatGPT Function
↓
OpenAI ChatCompletion API
↓
AI Response (Lawyer Style)
↓
Display in Web UI


---

## 🛠️ Tech Stack

| Category      | Technology |
|--------------|----------|
| Language     | Python |
| AI Model     | OpenAI GPT |
| UI Framework | Gradio |
| API Type     | REST |

---

## ⚙️ Configuration

### 🔑 API Key Setup

Replace this line:

python
openai.api_key = "YOUR_API_KEY"
