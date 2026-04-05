import streamlit as st
from datetime import datetime
import random

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Knot-Link // Proxy Network",
    page_icon="🕸️",
    layout="wide",
)

# --- CUSTOM CSS (ZZZ AESTHETIC REPLICATION) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

    /* Main Background */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Top Navigation Bar */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        background-color: transparent;
        padding: 10px 0;
        margin-bottom: 20px;
    }

    .nav-item {
        background-color: #333333;
        color: white;
        padding: 8px 30px;
        border-radius: 20px;
        margin-left: 10px;
        font-weight: bold;
        font-size: 14px;
        cursor: pointer;
        text-transform: uppercase;
    }

    .nav-item-active {
        background-color: #E2FF00; /* Distinctive Yellow from ZZZ */
        color: black;
    }

    /* Sub-tabs */
    .sub-nav-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 30px;
    }

    .sub-nav-item {
        background-color: #1A1A1A;
        color: #888;
        padding: 4px 20px;
        border-radius: 15px;
        margin-left: 10px;
        font-size: 12px;
    }

    .sub-nav-active {
        background-color: #E2FF00;
        color: black;
    }

    /* Post Card Grid Styling */
    .card-container {
        background-color: #111111;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #222222;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    
    .card-container:hover {
        transform: scale(1.02);
        border-color: #444;
    }

    .card-image {
        height: 200px;
        background-size: cover;
        background-position: center;
        width: 100%;
        display: flex;
        align-items: flex-end;
        padding: 10px;
    }

    .card-footer {
        background-color: #1A1A1A;
        padding: 15px;
        min-height: 120px;
    }

    .author-badge {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 10px;
    }

    .author-avatar {
        width: 24px;
        height: 24px;
        background-color: #E2FF00;
        border-radius: 50%;
        display: inline-block;
    }

    .author-name {
        font-weight: bold;
        font-size: 13px;
        color: #DDD;
    }

    .post-title {
        font-weight: bold;
        font-size: 15px;
        line-height: 1.2;
        margin-bottom: 5px;
    }

    .post-content {
        color: #888;
        font-size: 12px;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    /* Input Styling */
    .stTextArea textarea {
        background-color: #0A0A0A !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 10px !important;
    }
    
    .stButton button {
        background-color: #E2FF00 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
    }

    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {"author": "Ghost_In_The_Hollow", "title": "[Notice] Vision's shocking scandal exposed!", "content": "Evidence of corruption in the Sixth Street sector has surfaced...", "faction": "Legendary Proxy", "color": "#2c3e50"},
        {"author": "Ether_Drifter", "title": "A new Hollow on Fourteenth Street!", "content": "High ether concentration detected. Avoid the subway entrance.", "faction": "Pathfinder", "color": "#1a1a1a"},
        {"author": "Neon_Rabbit", "title": "[Question] Proxy Must-Knows: Carrots", "content": "How do you navigate the shifting grid patterns efficiently?", "faction": "Hearsay Hunter", "color": "#d35400"},
        {"author": "MetisIntel", "title": "The Red Fang Gang's doomsday?!", "content": "Internal power struggles are tearing the faction apart.", "faction": "Intel Node", "color": "#27ae60"},
        {"author": "Worrybot", "title": "[Info] Beware of 'Freeman's Antlers'", "content": "Reports of a dangerous entity roaming the zero zone.", "faction": "Alert Bot", "color": "#c0392b"},
        {"author": "QuQ", "title": "How to quickly level up IK account?", "content": "Beginner guide for new Proxies hitting New Eridu.", "faction": "Guide", "color": "#8e44ad"}
    ]

if "user_id" not in st.session_state:
    prefixes = ["Signal", "Static", "Void", "Cipher", "Data"]
    st.session_state.user_id = f"{random.choice(prefixes)}_Proxy_{random.randint(100, 999)}"

# --- TOP NAVIGATION BAR ---
st.markdown("""
    <div class="nav-container">
        <div class="nav-item nav-item-active">Notifications</div>
        <div class="nav-item">Intel Board</div>
        <div class="nav-item">Schedule</div>
    </div>
    <div class="sub-nav-container">
        <div class="sub-nav-item sub-nav-active">All</div>
        <div class="sub-nav-item">Fairy Picks</div>
        <div class="sub-nav-item">Help Request Info</div>
    </div>
""", unsafe_allow_html=True)

# --- BROADCAST INPUT (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🛰️ TRANSMISSION")
    st.markdown(f"**ID:** `{st.session_state.user_id}`")
    new_title = st.text_input("Title")
    new_post = st.text_area("Content", placeholder="Broadcast a message...")
    if st.button("SEND SIGNAL"):
        if new_post.strip() and new_title.strip():
            entry = {
                "author": st.session_state.user_id,
                "title": new_title,
                "content": new_post,
                "faction": "Active Proxy",
                "color": "#333333"
            }
            st.session_state.posts.insert(0, entry)
            st.rerun()

# --- FEED RENDERER (MASONRY GRID) ---
cols = st.columns(3)

for idx, post in enumerate(st.session_state.posts):
    col_idx = idx % 3
    # Use .get() to avoid KeyError if 'color' is missing from old session data
    bg_color = post.get('color', '#1a1a1a')
    with cols[col_idx]:
        st.markdown(f"""
            <div class="card-container">
                <div class="card-image" style="background-color: {bg_color};">
                    <div class="author-badge">
                        <div class="author-avatar"></div>
                        <span class="author-name">{post['author']}</span>
                    </div>
                </div>
                <div class="card-footer">
                    <div class="post-title">{post.get('title', 'Untitled')}</div>
                    <div class="post-content">{post.get('content', 'No content available.')}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Footer/UID
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 20px; color: #444; font-size: 10px;">
        UID: 1302948125 📶
    </div>
""", unsafe_allow_html=True)
