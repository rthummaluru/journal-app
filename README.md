# 📝 My Daily Journal App

A full-stack journal web app built with **React (frontend)** and **FastAPI (backend)** using **SQLite** for persistent storage.

Users can:
- Write daily journal entries
- Save them to a local database
- View all previously saved entries on page load

---

## ⚙️ Tech Stack

| Layer       | Technology      |
|-------------|-----------------|
| Frontend    | React + Vite + Tailwind CSS |
| Backend     | FastAPI         |
| Database    | SQLite          |
| API Protocol| REST            |

---

## 🚀 Features

- ✅ Create journal entries with title and body
- ✅ Save entries to a SQLite database via FastAPI
- ✅ Load saved entries on page load
- ✅ Fully connected frontend ↔ backend
- ✅ CORS properly configured for local dev

---

## 📌 Future Features

- 🖊 Edit existing entries  
- 🗑 Delete entries  
- 🧠 AI Insights on journal entries *(see below)*  
- 🔒 User authentication  
- 📱 Responsive mobile layout  
- 🌍 Deploy to Vercel (frontend) + Render/Railway (backend)

---

## 🧠 AI Insights (Upcoming)

One of the next key goals is to add an **AI-powered reflection system** that analyzes your journal entries and surfaces:
- Emotional tone (happy, stressed, reflective)
- Summaries of your week/month
- Personal growth trends or recurring patterns
- Suggestions or affirmations based on your writing

This could be built using:
- OpenAI's API or Claude (Anthropic)
- Embeddings + vector search for memory/context
- A separate `POST /analyze` endpoint and a dedicated AI service layer

> This feature aims to turn your journal into an intelligent self-reflection tool — not just a record of thoughts, but a feedback loop for personal growth.