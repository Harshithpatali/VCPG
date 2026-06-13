<div align="center">

<!-- Animated Banner -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=VCPG&fontSize=90&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Vibe%20Coding%20Prompt%20Generator&descAlignY=60&descAlign=50&descSize=22&descColor=a78bfa"/>

<!-- Badges Row -->
<p>
  <a href="https://github.com/Harshithpatali/VCPG/stargazers">
    <img src="https://img.shields.io/github/stars/Harshithpatali/VCPG?style=for-the-badge&logo=starship&color=f59e0b&labelColor=1a1a2e" alt="Stars"/>
  </a>
  <a href="https://github.com/Harshithpatali/VCPG/network/members">
    <img src="https://img.shields.io/github/forks/Harshithpatali/VCPG?style=for-the-badge&logo=git&color=8b5cf6&labelColor=1a1a2e" alt="Forks"/>
  </a>
  <a href="https://github.com/Harshithpatali/VCPG/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge&logo=opensourceinitiative&logoColor=white&labelColor=1a1a2e" alt="License"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e" alt="Python"/>
  <img src="https://img.shields.io/badge/Status-Live-00d084?style=for-the-badge&logo=vercel&logoColor=white&labelColor=1a1a2e" alt="Status"/>
</p>

<!-- Live Links -->
<p>
  <a href="https://vcpgv1.streamlit.app/dashboard">
    <img src="https://img.shields.io/badge/🚀%20Live%20App-Streamlit-FF4B4B?style=for-the-badge&labelColor=1a1a2e"/>
  </a>
  <a href="https://vcpg.onrender.com">
    <img src="https://img.shields.io/badge/⚡%20Backend%20API-Render-46E3B7?style=for-the-badge&labelColor=1a1a2e"/>
  </a>
  <a href="https://vcpg.onrender.com/docs">
    <img src="https://img.shields.io/badge/📖%20API%20Docs-Swagger-85ea2d?style=for-the-badge&labelColor=1a1a2e"/>
  </a>
</p>

<br/>

> **Transform a simple project idea into a professional-grade AI mega prompt — in seconds.**  
> Powered by a multi-agent architecture with OpenRouter + Groq orchestration.

<br/>

</div>

---

## ✨ What is VCPG?

**VCPG** is a production-ready AI application that takes your raw project idea and generates a **complete, structured implementation mega prompt** — covering architecture, tech stack, folder structure, development roadmap, and deployment strategies.

```
"Build me an AI resume analyzer" 
           ↓  VCPG  ↓
📐 Architecture  •  🛠️ Tech Stack  •  📁 Folder Structure
🗺️ Dev Roadmap  •  🚀 Deployment Guide  •  💡 Mega Prompt
```

---

## ⚡ Key Features

<table>
<tr>
<td width="50%">

**🤖 AI-Powered Generation**
- Project idea analysis
- Architecture recommendation
- Technology stack suggestion
- Folder structure generation
- Development roadmap
- Deployment guidance

</td>
<td width="50%">

**🔗 Multi-Agent Workflow**
- OpenRouter Agent (Blueprint)
- Groq Agent (Refinement)
- Orchestration Layer
- Agent-to-agent pipeline
- Structured output handling

</td>
</tr>
<tr>
<td width="50%">

**🏗️ Production Ready**
- FastAPI REST backend
- Streamlit interactive frontend
- Render cloud deployment
- Swagger API documentation
- Environment-based config

</td>
<td width="50%">

**📈 Scalable Design**
- Modular architecture
- Service layer abstraction
- Future ML integration support
- Pydantic data validation
- Clean separation of concerns

</td>
</tr>
</table>

---

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        USER                             │
└──────────────────────────┬──────────────────────────────┘
                           │  Project Idea + Config
                           ▼
┌─────────────────────────────────────────────────────────┐
│              STREAMLIT FRONTEND                         │
│    Dashboard  •  Generator  •  Results Viewer           │
└──────────────────────────┬──────────────────────────────┘
                           │  POST /generate-prompt
                           ▼
┌─────────────────────────────────────────────────────────┐
│              FASTAPI BACKEND                            │
│    Routes  •  Schemas  •  Services  •  Utils            │
└──────────────────────────┬──────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
┌─────────────────────┐   ┌─────────────────────────────┐
│  OPENROUTER AGENT   │   │       GROQ AGENT            │
│  Blueprint          │──▶│  Prompt Refinement          │
│  Generation         │   │  & Finalization             │
└─────────────────────┘   └──────────────┬──────────────┘
                                          │
                                          ▼
                          ┌───────────────────────────┐
                          │   PROFESSIONAL MEGA PROMPT │
                          │   Returned to Frontend     │
                          └───────────────────────────┘
```

---

## 🛠️ Technology Stack

<div align="center">

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![HTTPX](https://img.shields.io/badge/HTTPX-000000?style=for-the-badge&logo=python&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)

### AI Providers
![OpenAI](https://img.shields.io/badge/OpenRouter-412991?style=for-the-badge&logo=openai&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)

### DevOps & Deployment
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)
![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![UV](https://img.shields.io/badge/UV-DE5FE9?style=for-the-badge&logo=astral&logoColor=white)

</div>

---

## 📁 Project Structure

```
VCPG/
│
├── 🔧 backend/
│   ├── 🤖 agents/
│   │   ├── openrouter_agent.py     # Blueprint generation agent
│   │   ├── groq_agent.py           # Prompt refinement agent
│   │   └── orchestrator.py         # Multi-agent orchestration
│   │
│   ├── 🛣️ routes/
│   │   └── prompt_routes.py        # API route definitions
│   │
│   ├── 📐 schemas/
│   │   └── prompt_schema.py        # Pydantic data models
│   │
│   ├── ⚙️ services/
│   │   ├── openrouter_service.py   # OpenRouter API service
│   │   ├── groq_service.py         # Groq API service
│   │   └── prompt_loader.py        # Prompt template loader
│   │
│   ├── 🔍 utils/
│   │   └── logger.py               # Application logging
│   │
│   ├── config.py                   # Environment configuration
│   └── main.py                     # FastAPI app entry point
│
├── 🎨 frontend/
│   ├── 🧩 components/
│   │   ├── hero.py                 # Landing hero section
│   │   ├── metrics.py              # Stats & metrics display
│   │   ├── prompt_viewer.py        # Generated prompt viewer
│   │   ├── sidebar.py              # Navigation sidebar
│   │   └── stepper.py              # Step progress indicator
│   │
│   ├── 📄 pages/
│   │   ├── dashboard.py            # Main dashboard page
│   │   ├── generator.py            # Prompt generator page
│   │   └── results.py              # Results display page
│   │
│   ├── 🎨 styles/
│   │   └── theme.css               # Custom UI theme
│   │
│   ├── 🔌 utils/
│   │   └── api_client.py           # Backend API client
│   │
│   └── app.py                      # Streamlit app entry point
│
├── 📝 prompts/
│   ├── architect_prompt.txt        # Blueprint system prompt
│   └── refinement_prompt.txt       # Refinement system prompt
│
├── 📦 exports/                     # Generated prompt exports
├── 📚 docs/                        # Documentation
├── 🧪 tests/                       # Test suite
├── .github/                        # GitHub Actions workflows
│
├── .env.example                    # Environment template
├── pyproject.toml                  # Project config & dependencies
├── render.yaml                     # Render deployment config
└── README.md
```

---

## 🚀 Getting Started

### 1 · Clone the Repository

```bash
git clone https://github.com/Harshithpatali/VCPG.git
cd VCPG
```

### 2 · Create a Virtual Environment

```bash
# macOS / Linux
python3 -m venv venv && source venv/bin/activate

# Windows
python -m venv venv && venv\Scripts\activate
```

### 3 · Install Dependencies

```bash
pip install uv
uv sync
```

### 4 · Configure Environment

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
GROQ_API_KEY=your_groq_api_key

ENVIRONMENT=development
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
LOG_LEVEL=INFO
```

### 5 · Run the Application

```bash
# Terminal 1 — Start backend
uvicorn backend.main:app --reload
# → http://127.0.0.1:8000
# → http://127.0.0.1:8000/docs (Swagger UI)

# Terminal 2 — Start frontend
streamlit run frontend/app.py
# → http://localhost:8501
```

---

## 📡 API Reference

### `POST /generate-prompt`

Generate a professional mega prompt from a project idea.

**Request**
```json
{
  "project_idea": "AI Resume Analyzer",
  "os": "Windows",
  "language": "Python",
  "purpose": "Portfolio Project",
  "explanation": true,
  "backend_deployment": "Render",
  "frontend_deployment": "Streamlit Cloud"
}
```

**Response**
```json
{
  "success": true,
  "final_prompt": "## Project: AI Resume Analyzer\n\n### Architecture\n..."
}
```

---

## ☁️ Deployment

<table>
<tr>
<th>Layer</th>
<th>Platform</th>
<th>Start Command</th>
</tr>
<tr>
<td>🔧 Backend</td>
<td>

![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black)

</td>
<td>

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

</td>
</tr>
<tr>
<td>🎨 Frontend</td>
<td>

![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</td>
<td>

Set secret: `BACKEND_URL = "https://vcpg.onrender.com"`

</td>
</tr>
</table>

---

## 🗺️ Roadmap

```
v1.0  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ✅ RELEASED
       Multi-agent workflow  •  FastAPI + Streamlit
       OpenRouter + Groq  •  Render + Streamlit Cloud

v2.0  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  🔜 PLANNED
       User authentication  •  Prompt history
       Database integration  •  Usage analytics
       Prompt templates  •  ML personalization

v3.0  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  🔮 FUTURE
       Team collaboration  •  Workspace management
       Prompt marketplace  •  Enterprise integrations
       Advanced AI orchestration
```

---

## 🧠 Engineering Principles

| Principle | Implementation |
|-----------|---------------|
| 🧩 Modular Architecture | Independent agents, services, and routes |
| 🔌 API-First Design | All features exposed via REST endpoints |
| 🔒 Strong Typing | Pydantic schemas for all I/O validation |
| ⚙️ Config Management | dotenv-based environment configuration |
| 🤖 Agent Orchestration | Decoupled multi-agent pipeline pattern |
| 📂 Separation of Concerns | Services, routes, schemas, utils isolated |

---

## 👨‍💻 Author

<div align="center">

<img src="https://github.com/Harshithpatali.png" width="120" style="border-radius:50%"/>

### Harshith Devraj

**M.S. Applied Mathematics & Computing**  
Data Science · Artificial Intelligence · Machine Learning · MLOps

[![GitHub](https://img.shields.io/badge/GitHub-Harshithpatali-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Harshithpatali)

</div>

---

## 📄 License

```
MIT License — free to use, modify, and distribute.
See LICENSE for full terms.
```

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer"/>

**⭐ If VCPG helped you, consider starring the repo!**

</div>
