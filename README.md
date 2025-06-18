
# FinWise 💰

**FinWise** is a full-stack financial assistant application designed to help users manage expenses, visualize spending, and interact with AI-powered insights.

This monorepo includes both frontend and backend code:

- `finance-ai-frontend/` — Built with **Next.js / React**
- `finance-ai-backend/` — Powered by **Django + Django REST Framework**

---

## 📁 Project Structure

```

FinWise/
├── finance-ai-frontend/     # React/Next.js frontend
├── finance-ai-backend/      # Django backend (REST API)
├── .gitignore
├── requirements.txt         # Python dependencies
└── README.md                # You're here!

````



## 🚀 Getting Started

### 🔧 Backend Setup (`finance-ai-backend`)

## Navigate to backend directory:
   ```bash
   cd finance-ai-backend
````

## Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Install dependencies:

   ```bash
   pip install -r ../requirements.txt
   ```

## Apply migrations and run server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

### 💻 Frontend Setup (`finance-ai-frontend`)

## Navigate to frontend directory:

   ```bash
   cd finance-ai-frontend
   ```

## Install dependencies:

   ```bash
   npm install
   ```

## Run the development server:

   ```bash
   npm run dev
   ```

## Visit: `http://localhost:3000`

---

## 🔐 Authentication Flow

# > ⚠️ NOTE: Authentication flow is currently a work in progress.

Planned features:

* JWT-based auth using Django REST
* Login and registration in frontend
* Token storage and refresh logic

---

## 📦 Technologies Used

### Frontend

* React
* Next.js
* Tailwind CSS (optional)
* Axios / Fetch API

### Backend

* Django
* Django REST Framework
* SQLite (can be upgraded to PostgreSQL)

---

## ✅ TODO

* [ ] Fix authentication integration between frontend and backend
* [ ] Add unit and integration tests
* [ ] Dockerize the app
* [ ] Deploy to Vercel (frontend) and Railway/Render (backend)

---

## 📄 License

MIT License. See `LICENSE` file for more info.

---

## 🙌 Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork the project and submit a pull request.

---

## 🧠 Maintainer
### Payal Lenka

