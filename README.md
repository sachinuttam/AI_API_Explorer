# 🛰️ AI API Explorer

A web app where you type any topic — weather, news, finance, AI & ML,
movies, crypto, sports, and more — and instantly get the **top 5 matching
public APIs**, each one clickable to open its official documentation.
Built with **Streamlit** and a glowing animated dark-space background.

---

## 🗂️ Project structure

```
ai-api-explorer/
├── app.py               # Streamlit web app (search bar + result cards)
├── search_utils.py      # Search/ranking engine (keyword + fuzzy matching)
├── data/
│   └── apis_data.py     # Curated database of 50 real public APIs
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ▶️ Run it locally in VS Code

1. **Unzip** this project and open the folder in VS Code.

2. **Create a virtual environment** (recommended) and activate it:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

   Your browser opens automatically at `http://localhost:8501`. Type a
   topic into the search bar (e.g. `weather`, `finance`, `machine
   learning`, `movies`, `crypto`) and press Enter to see the top 5
   matching APIs. Click **🚀 Visit API** on any card to open its docs in a
   new tab. If you don't type anything, 5 featured APIs are shown by
   default.

---

## 🌍 Deploy it for free (Streamlit Community Cloud)

1. **Create a GitHub repository** and push the whole project folder to it.

   ```bash
   git init
   git add .
   git commit -m "AI API Explorer project"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

2. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in
   with GitHub.

3. Click **"New app"**, then select:
   - **Repository:** the repo you just pushed
   - **Branch:** `main`
   - **Main file path:** `app.py`

4. Click **Deploy**. You'll get a public link like:
   ```
   https://<your-app-name>.streamlit.app
   ```
   Share it with your teacher and classmates — anyone can search and try
   it, no installation needed.

---

## 🧠 How the search works

`search_utils.py` uses a lightweight, transparent **weighted keyword
search** — no heavy ML model or training required, so it runs instantly:

- Each API has a name, category, description, and a list of tags.
- Your search query is split into keywords and matched against all four
  fields, with matches in the **name** weighted highest, then
  **category**, then **tags**, then **description**.
- A small fuzzy-matching bonus (via `difflib`) helps catch near-misses
  and typos.
- The 5 highest-scoring APIs are returned and displayed as cards.

This makes the search fast, easy to understand, and easy to extend.

---

## ✏️ Ideas to extend the project (optional, for extra credit)

- Add more APIs to `data/apis_data.py` — just follow the existing
  dictionary format (name, category, description, docs_url, tags, icon,
  free_tier).
- Add a "Copy example request" button showing a sample `curl` or Python
  snippet for each API.
- Track and display the most-searched topics using `st.session_state`.
- Add a "Random API" button to discover something new.
- Let users filter results by category using the sidebar.
- Replace the keyword search with a TF-IDF or embedding-based search for
  smarter matching on longer, more natural queries.

> Note: API documentation links can change over time — if a link ever
> breaks, just search for the API name to find its current docs page.
