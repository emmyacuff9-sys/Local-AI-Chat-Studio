# Emmy’s World AI

A local-first AI chat UI with multi-provider support (OpenRouter and Venice AI), system prompt management, conversation history, token tracking, and theme switching. Designed for experimenting with models, prompts, and parameters without frameworks or unnecessary bloat.

To run this code make sure the index.html file and main.py file are in the same directory. Also be sure you signup with Openrouter and or Venice AI to create your own API keys. Simply type python3 main.py in your CLI to run the code and click the link displayed to goto the UI. It is very easy to use.

---

## API Keys & Providers

You must sign up for **at least one provider** and create an API key for the chatbot to function.

- **OpenRouter signup:**  
  https://openrouter.ai/signup

- **Venice AI signup:**  
  https://venice.ai

This AI chatbot **will not respond** unless at least one API key is added through the settings menu.  
API keys, chat history, and settings are stored **locally in your browser** for privacy and security.

---

## About This Project

I used Gemini AI to generate and debug all of the code for this project. I did not manually write or debug the code myself. The goal was to improve my AI prompting skills while building something genuinely useful.

This project is intended for people on a tight budget who want to test and compare different AI models without spending much money, or any money at all.

---

## Free Usage Details

### OpenRouter
- Free tier allows up to **50 messages per day** without adding funds
- Adding **$10** grants **1,000 free prompts per day**
- As long as only free models are used, the $10 balance remains untouched

### Venice AI
- Provides **$10.00 in free credits** (≈ 1,000 credits)
- Offers several budget-friendly models
- One Venice model costs **less than $0.01 for ~18,000 tokens**
- Free credits last a long time with moderate usage

---

## Why This Repo Is Simple on Purpose

Parts of this README were AI-generated based on the code, with minimal edits.  
I intentionally kept this project beginner-friendly and avoided overwhelming users with thousands of lines of code.

Advanced developers can easily extend or modify the project to add features.  
This repo is meant to be **easy to understand, easy to run, and easy to modify**.

---

## AI-Generated README (Original, Unedited)

A sleek, local-first AI chat UI with multi-provider support (OpenRouter & Venice), system prompt management, conversation history, token tracking, and theme switching. Designed for experimenting with models, prompts, and parameters without frameworks or bloat.

A lightweight, local-first AI chat interface with a FastAPI backend.  
Built for experimenting with AI models, system prompts, and generation parameters using OpenRouter or Venice AI, without frameworks or build tools.

---

## Features

- Multi-provider support (OpenRouter & Venice AI)
- System prompt management (add, edit, toggle on/off)
- Conversation history stored locally
- Token and context window tracking
- Adjustable generation parameters
- Syntax highlighting for code responses
- Dark mode with sliding drawer UI
- No frontend frameworks
- No build step

---

## installation instructions

- Clone the repo
- Create a virtual environment (recommended),
``` python3 -m venv venv ```
Activate the environment:,
Windows
```venv\Scripts\activate```
macOS / Linux
```source venv/bin/activate```
- Install required packages, 
```pip install -r requirements.txt```
- Run the FastAPI server, ```python main.py```


## Architecture Overview

```text
Frontend (index.html)
 ├─ Chat UI
 ├─ Prompt Manager
 ├─ Token Counter
 └─ Settings Panel
        │
        │  POST /api/chat
        │  POST /api/models
        ▼
Backend (main.py / FastAPI)
 ├─ API Key Proxy
 ├─ Provider Routing
 └─ CORS Bypass
        │
        ├─ OpenRouter API
        └─ Venice AI API

