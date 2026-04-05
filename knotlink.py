import streamlit as st
from datetime import datetime
import random

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Knot-Link // Proxy Network",
    page_icon="🕸️",
    layout="centered",
)

# --- CUSTOM CSS (ZZZ AESTHETIC) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0D0D0E;
        color: #FFFFFF;
    }
    
    /* Header Styling */
    .header-container {
        border-bottom: 2px solid #FF6B00;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    .header-title {
        color: #FF6B00;
        font-family: 'monospace';
        letter-spacing: 2px;
        font-weight: bold;
        font-size: 24px;
    }

    /* Post Card Styling */
    .post-card {
        background-color: #161617;
        border: 1px solid #27272A;
        border-left: 4px solid #FF6B00;
        padding: 15px;
        border-radius: 2px;
        margin-bottom: 10px;
    }
    
    .post-author {
        color: #00E5FF;
        font-family: 'monospace';
        font-weight: bold;
        font-size: 14px;
    }
    
    .post-faction {
        background-color: rgba(255, 107, 0, 0.1);
        color: #FF6B00;
        padding: 2px 6px;
        font-size: 10px;
        border: 1px solid #FF6B00;
        margin-left: 10px;
        text-transform: uppercase;
    }

    .post-time {
        color: #666;
        font-size: 11px;
        float: right;
    }

    /* Input Area */
    .stTextArea textarea {
        background-color: #1A1A1B !important;
        color: white !important;
        border: 1px solid #27272A !important;
    }
    
    /* Button Styling */
    .stButton button {
        background-color: #FF6B00 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100%;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {"author": "Ghost_In_The_Hollow", "content": "Signal strength confirmed. Welcome to the Node.", "faction": "Legendary Proxy", "time": "SYSTEM_START"},
        {"author": "Ether_Drifter", "content": "Anyone seeing weird distortions near the construction site?", "faction": "Pathfinder", "time": "10:42 AM"},
        {"author": "Neon_Rabbit", "content": "Found a discarded Bangboo unit near the noodle shop. Anyone lost one?", "faction": "Hearsay Hunter", "time": "09:15 AM"}
    ]

if "user_id" not in st.session_state:
    # Generate a more interesting default proxy name
    prefixes = ["Signal", "Static", "Void", "Cipher", "Data"]
    st.session_state.user_id = f"{random.choice(prefixes)}_Proxy_{random.randint(100, 999)}"

# --- HEADER ---
st.markdown('<div class="header-container"><span class="header-title">KNOT-LINK // NETWORK</span></div>', unsafe_allow_html=True)
st.markdown(f"**Current Signal ID:** `{st.session_state.user_id}`")

# --- BROADCAST INPUT ---
with st.container():
    new_post = st.text_area("", placeholder="Broadcast a message to the network...", label_visibility="collapsed")
    if st.button("REPLY"):
        if new_post.strip():
            entry = {
                "author": st.session_state.user_id,
                "content": new_post,
                "faction": "Active Proxy",
                "time": datetime.now().strftime("%I:%M %p")
            }
            # Insert at the top of the list
            st.session_state.posts.insert(0, entry)
            st.rerun()

st.markdown("---")

# --- FEED RENDERER ---
for post in st.session_state.posts:
    st.markdown(f"""
        <div class="post-card">
            <span class="post-author">{post['author']}</span>
            <span class="post-faction">{post['faction']}</span>
            <span class="post-time">{post['time']}</span>
            <div style="margin-top: 10px; font-size: 16px;">{post['content']}</div>
        </div>
    """, unsafe_allow_html=True)
