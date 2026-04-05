import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & THEMING ---
st.set_page_config(
    page_title="KNOT-LINK // PHAETHON GATEWAY",
    page_icon="🟠",
    layout="wide"
)

# Custom CSS for the Masonry Grid and Game UI look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    /* Main Background */
    .stApp {
        background-color: #0d0d0d;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Top Navigation Bar */
    .top-nav {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 30px;
        padding-top: 10px;
    }
    .nav-item {
        background: #1a1a1a;
        color: #ffffff;
        padding: 8px 30px;
        border-radius: 20px;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.9rem;
        cursor: pointer;
        border: 1px solid #333;
    }
    .nav-item.active {
        background: #f0e600; /* ZZZ Yellow */
        color: #000000;
        border: none;
    }

    /* Post Cards - Grid Style */
    .knot-card {
        background-color: #1a1a1a;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 20px;
        border: 1px solid #222;
        transition: transform 0.2s ease;
    }
    .knot-card:hover {
        transform: translateY(-5px);
        border-color: #f0e600;
    }
    
    .card-image {
        width: 100%;
        height: 180px;
        background-size: cover;
        background-position: center;
        border-bottom: 1px solid #222;
    }

    .card-content {
        padding: 15px;
    }

    .author-info {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 10px;
    }
    .avatar {
        width: 24px;
        height: 24px;
        background: #333;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 10px;
        border: 1px solid #444;
    }

    .card-title {
        font-weight: bold;
        font-size: 1rem;
        line-height: 1.2;
        margin-bottom: 8px;
        color: #eee;
    }
    .card-preview {
        font-size: 0.8rem;
        color: #888;
        line-height: 1.4;
    }

    /* Fairy / Status Bar */
    .status-bar {
        background: #000;
        padding: 5px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #222;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
st.markdown("""
    <div class="top-nav">
        <div class="nav-item active">Notifications</div>
        <div class="nav-item">Intel Board</div>
        <div class="nav-item">Schedule</div>
    </div>
    <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 40px;">
        <span style="background: #f0e600; color: black; padding: 2px 15px; border-radius: 10px; font-size: 0.7rem; font-weight: bold;">All</span>
        <span style="color: white; font-size: 0.7rem; padding: 2px 10px;">Fairy Picks</span>
        <span style="color: white; font-size: 0.7rem; padding: 2px 10px;">Help Request Info</span>
    </div>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "author": "MetisIntelligence",
            "title": "[Post] Vision's shocking scandal exposed — Perlman is going to jail!",
            "content": "Charles Perlman, chief executive of Vision Corp, was caught in a multi-level fraud scheme...",
            "img": "https://picsum.photos/seed/vision/400/300",
            "timestamp": time.time()
        },
        {
            "author": "Worrybot",
            "title": "A new Hollow on Fourteenth Street!",
            "content": "A Companion Hollow has appeared. Residents are advised to seek shelter immediately.",
            "img": "https://picsum.photos/seed/hollow/400/300",
            "timestamp": time.time() - 3600
        },
        {
            "author": "Friend2Proxy",
            "title": "[Info] Proxy Must-Knows: Carrots",
            "content": "Investigators and Proxies often overlook the importance of specialized carrot data in grid navigation.",
            "img": "https://picsum.photos/seed/carrot/400/300",
            "timestamp": time.time() - 7200
        },
        {
            "author": "Anonymous",
            "title": "[Warning] Beware of the Proxy called Freeman's Antlers",
            "content": "What a pain! This Proxy has been stealing commissions in the Lumina Square area.",
            "img": "https://picsum.photos/seed/warning/400/300",
            "timestamp": time.time() - 10000
        },
        {
            "author": "QuQ",
            "title": "[Question] How to quickly level up your IK account?",
            "content": "See title - I just started and I want to reach the legendary rank as fast as possible.",
            "img": "https://picsum.photos/seed/question/400/300",
            "timestamp": time.time() - 15000
        },
        {
            "author": "gawadaw",
            "title": "[Post] Some long-lost dimensions",
            "content": "Does anyone remember the sector that used to be near the old railway? It's completely gone now.",
            "img": "https://picsum.photos/seed/dimension/400/300",
            "timestamp": time.time() - 20000
        }
    ]

# --- MAIN GRID ---
cols = st.columns(3)

for idx, post in enumerate(st.session_state.posts):
    with cols[idx % 3]:
        st.markdown(f"""
            <div class="knot-card">
                <div class="card-image" style="background-image: url('{post['img']}');"></div>
                <div class="card-content">
                    <div class="author-info">
                        <div class="avatar">👤</div>
                        <span style="font-size: 0.75rem; font-weight: bold; color: #aaa;">{post['author']}</span>
                    </div>
                    <div class="card-title">{post['title']}</div>
                    <div class="card-preview">{post['content'][:80]}...</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- POSTING INTERFACE (FLOATING ACTION) ---
with st.sidebar:
    st.markdown('<h2 class="header-text">KNOT-LINK</h2>', unsafe_allow_html=True)
    st.write("---")
    with st.form("new_post", clear_on_submit=True):
        st.write("Create New Thread")
        new_title = st.text_input("Title")
        new_content = st.text_area("Description")
        new_img_seed = st.text_input("Image Keyword", "tech")
        submitted = st.form_submit_button("PUBLISH")
        
        if submitted and new_title:
            new_post = {
                "author": "PHAETHON",
                "title": new_title,
                "content": new_content,
                "img": f"https://picsum.photos/seed/{new_img_seed}/400/300",
                "timestamp": time.time()
            }
            st.session_state.posts.insert(0, new_post)
            st.rerun()

    st.write("---")
    st.caption("Logged in: PHAETHON")
    st.success("SYNC: ACTIVE")
