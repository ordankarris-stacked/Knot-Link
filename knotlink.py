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

    /* Post Card Grid Styling - Redesigned for News/User Style */
    .card-container {
        background-color: #111111;
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #222222;
        margin-bottom: 20px;
        transition: transform 0.2s;
        position: relative;
    }
    
    .card-container:hover {
        transform: scale(1.02);
        border-color: #444;
    }

    .card-image {
        height: 250px;
        background-size: cover;
        background-position: center;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        /* Blackout effect for missing images */
        background-color: #050505; 
        position: relative;
    }

    /* Gradient overlay for text readability on images */
    .card-overlay {
        background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);
        padding: 15px;
        width: 100%;
    }

    .post-title {
        font-weight: bold;
        font-size: 16px;
        line-height: 1.3;
        margin-bottom: 4px;
        color: #FFFFFF;
    }

    .post-content {
        color: #BBBBBB;
        font-size: 12px;
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-footer {
        background-color: #0F0F0F;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-top: 1px solid #1A1A1A;
    }

    .author-avatar {
        width: 20px;
        height: 20px;
        background-color: #E2FF00;
        border-radius: 50%;
        display: inline-block;
        flex-shrink: 0;
    }

    .author-name {
        font-weight: bold;
        font-size: 12px;
        color: #EEEEEE;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .author-suffix {
        color: #666;
        font-size: 12px;
    }

    /* Input Styling */
    .stTextArea textarea, .stTextInput input {
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
        {"author": "r/politics", "title": "Trump issues warning to Iran", "content": "Trump Vows To Strike Civilian Infrastruct...", "faction": "Global News", "image": None},
        {"author": "r/worldnews", "title": "US rescues missing pilot", "content": "U.S. forces rescue second crew member...", "faction": "Military", "image": None},
        {"author": "r/spaceporn", "title": "New Artemis II photos", "content": "New image from NASA: For the first tim...", "faction": "Science", "image": None},
        {"author": "r/Music", "title": "Pepsi pulls out of Wi...", "content": "Pepsi Cancels Sponsorship c...", "faction": "Industry", "image": None},
        {"author": "Ghost_In_The_Hollow", "title": "[Notice] Vision's shocking scandal exposed!", "content": "Evidence of corruption in the Sixth Street sector has surfaced...", "faction": "Legendary Proxy", "image": None},
        {"author": "Ether_Drifter", "title": "A new Hollow on Fourteenth Street!", "content": "High ether concentration detected. Avoid the subway entrance.", "faction": "Pathfinder", "image": None}
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
        <div class="sub-nav-item">News</div>
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
                "author": f"r/{st.session_state.user_id}",
                "title": new_title,
                "content": new_post,
                "faction": "User Post",
                "image": None
            }
            st.session_state.posts.insert(0, entry)
            st.rerun()

# --- FEED RENDERER (GRID) ---
cols = st.columns(3)

for idx, post in enumerate(st.session_state.posts):
    col_idx = idx % 3
    
    # Image logic: If image exists use it, otherwise use 'blackout' styling
    img_url = post.get('image')
    bg_style = f"background-image: url('{img_url}');" if img_url else "background-color: #050505;"
    
    with cols[col_idx]:
        st.markdown(f"""
            <div class="card-container">
                <div class="card-image" style="{bg_style}">
                    <div class="card-overlay">
                        <div class="post-title">{post.get('title', 'Untitled')}</div>
                        <div class="post-content">{post.get('content', 'No content available.')}</div>
                    </div>
                </div>
                <div class="card-footer">
                    <div class="author-avatar"></div>
                    <span class="author-name">{post.get('author', 'Unknown')}</span>
                    <span class="author-suffix">以及更多</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Footer/UID
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 20px; color: #444; font-size: 10px;">
        UID: 1302948125 📶
    </div>
""", unsafe_allow_html=True)
