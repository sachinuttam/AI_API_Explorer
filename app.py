"""
app.py
-------
AI API Explorer

Search for any topic (weather, news, finance, AI/ML, movies, etc.) and get
the top matching public APIs, each clickable to open its official docs.

Run locally with:
    streamlit run app.py
"""

import streamlit as st
from search_utils import search_apis, get_featured_apis, get_all_categories

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="AI API Explorer",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS — dark, glowing, animated "space / tech" background
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Base dark canvas */
    .stApp {
        background: #05060f;
        overflow: hidden;
    }

    /* Starfield layer */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            radial-gradient(1.5px 1.5px at 20px 30px, #ffffff55, transparent),
            radial-gradient(1.5px 1.5px at 90px 120px, #ffffff44, transparent),
            radial-gradient(2px 2px at 160px 60px, #ffffff66, transparent),
            radial-gradient(1px 1px at 210px 150px, #ffffff33, transparent),
            radial-gradient(1.5px 1.5px at 260px 40px, #ffffff55, transparent),
            radial-gradient(1px 1px at 320px 200px, #ffffff33, transparent),
            radial-gradient(2px 2px at 40px 220px, #ffffff44, transparent);
        background-repeat: repeat;
        background-size: 380px 260px;
        animation: drift 90s linear infinite;
        z-index: 0;
        pointer-events: none;
    }

    @keyframes drift {
        from { background-position: 0 0; }
        to   { background-position: -1000px 600px; }
    }

    /* Floating glowing orbs */
    .orb {
        position: fixed;
        border-radius: 50%;
        filter: blur(70px);
        opacity: 0.55;
        z-index: 0;
        pointer-events: none;
    }
    .orb-1 {
        width: 420px; height: 420px;
        top: -120px; left: -100px;
        background: radial-gradient(circle, #7f5af0, transparent 70%);
        animation: floatA 22s ease-in-out infinite;
    }
    .orb-2 {
        width: 380px; height: 380px;
        bottom: -140px; right: -80px;
        background: radial-gradient(circle, #2cb1ff, transparent 70%);
        animation: floatB 26s ease-in-out infinite;
    }
    .orb-3 {
        width: 300px; height: 300px;
        top: 40%; left: 60%;
        background: radial-gradient(circle, #ff2cd0, transparent 70%);
        animation: floatC 30s ease-in-out infinite;
    }

    @keyframes floatA {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(60px, 80px) scale(1.15); }
    }
    @keyframes floatB {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-70px, -50px) scale(1.1); }
    }
    @keyframes floatC {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-40px, 60px) scale(1.2); }
    }

    /* Make sure real content sits above the background layers */
    .block-container {
        position: relative;
        z-index: 1;
    }

    /* Header */
    .hero-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #7f5af0, #2cb1ff, #ff2cd0);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 6s linear infinite;
        margin-bottom: 0;
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }
    .hero-subtitle {
        text-align: center;
        color: #b8bcd9;
        font-size: 1.05rem;
        margin-top: 0.4rem;
        margin-bottom: 2rem;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Search input styling */
    .stTextInput input {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(127, 90, 240, 0.5) !important;
        border-radius: 14px !important;
        color: #fff !important;
        font-size: 1.1rem !important;
        padding: 0.9rem 1.1rem !important;
        box-shadow: 0 0 25px rgba(127, 90, 240, 0.15);
    }
    .stTextInput input:focus {
        border: 1px solid #2cb1ff !important;
        box-shadow: 0 0 25px rgba(44, 177, 255, 0.35);
    }
    .stTextInput label {
        color: #b8bcd9 !important;
        font-family: 'JetBrains Mono', monospace;
    }

    /* API glass cards */
    .api-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 1.3rem 1.2rem 1rem 1.2rem;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border 0.2s ease;
    }
    .api-card:hover {
        transform: translateY(-6px);
        border: 1px solid rgba(124, 90, 240, 0.7);
        box-shadow: 0 10px 30px rgba(124, 90, 240, 0.35);
    }
    .api-icon {
        font-size: 2.2rem;
    }
    .api-name {
        color: #ffffff;
        font-weight: 700;
        font-size: 1.15rem;
        margin: 0.4rem 0 0.15rem 0;
    }
    .api-category {
        display: inline-block;
        color: #2cb1ff;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        background: rgba(44, 177, 255, 0.12);
        border-radius: 20px;
        padding: 0.15rem 0.7rem;
        margin-bottom: 0.6rem;
    }
    .api-desc {
        color: #cfd2ee;
        font-size: 0.92rem;
        line-height: 1.4rem;
        min-height: 3.4rem;
    }
    .api-free {
        color: #8f97c9;
        font-size: 0.78rem;
        font-family: 'JetBrains Mono', monospace;
        margin-top: 0.5rem;
    }

    div.stLinkButton > a {
        width: 100%;
        background: linear-gradient(90deg, #7f5af0, #2cb1ff);
        color: white !important;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        text-align: center;
        margin-top: 0.6rem;
    }
    div.stLinkButton > a:hover {
        filter: brightness(1.15);
    }

    .section-label {
        color: #8f97c9;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin: 1.6rem 0 0.8rem 0;
    }

    footer {visibility: hidden;}
    </style>

    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown('<p class="hero-title">🛰️ AI API Explorer</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-subtitle">Search any topic — weather, news, finance, AI, movies, '
    'crypto — and discover the top APIs for it, instantly.</p>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Search bar
# ---------------------------------------------------------------------------
col_a, col_b, col_c = st.columns([1, 3, 1])
with col_b:
    query = st.text_input(
        "🔍 Search for an API topic",
        placeholder="Try: weather, finance, machine learning, movies, crypto...",
        label_visibility="visible",
    )

    with st.expander("Browse by category"):
        categories = get_all_categories()
        cat_cols = st.columns(3)
        for i, cat in enumerate(categories):
            cat_cols[i % 3].markdown(f"- {cat}")


# ---------------------------------------------------------------------------
# Render a row of API cards (up to 5)
# ---------------------------------------------------------------------------
def render_api_cards(apis):
    cols = st.columns(len(apis)) if apis else []
    for col, api in zip(cols, apis):
        with col:
            st.markdown(
                f"""
                <div class="api-card">
                    <div class="api-icon">{api['icon']}</div>
                    <div class="api-name">{api['name']}</div>
                    <div class="api-category">{api['category']}</div>
                    <div class="api-desc">{api['description']}</div>
                    <div class="api-free">{api['free_tier']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.link_button("🚀 Visit API", api["docs_url"], use_container_width=True)


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
if query.strip():
    results = search_apis(query, top_n=5)
    if results:
        st.markdown(
            f'<p class="section-label">Top {len(results)} APIs for "{query}"</p>',
            unsafe_allow_html=True,
        )
        render_api_cards(results)
    else:
        st.info(
            "No matching APIs found. Try a broader term like 'weather', "
            "'finance', 'AI', 'music', or 'sports'."
        )
else:
    st.markdown('<p class="section-label">✨ Featured APIs</p>', unsafe_allow_html=True)
    render_api_cards(get_featured_apis())

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<p style="text-align:center; color:#6b6f99; font-size:0.8rem; margin-top:2.5rem;">'
    'Built with Streamlit &bull; Search covers 15+ categories and 45+ real public APIs</p>',
    unsafe_allow_html=True,
)
