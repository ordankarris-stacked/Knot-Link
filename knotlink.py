import streamlit as st
from datetime import datetime
import random

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Knot-Link // Inter-Knot",
    page_icon="🕸️",
    layout="wide",
)

# --- CUSTOM CSS (ACCURATE INTER-KNOT GUI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');

    /* Global Overrides */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Branding Header */
    .brand-container {
        display: flex;
        align-items: center;
        padding: 10px 0;
    }
    .brand-title {
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -1px;
    }
    .brand-title span { color: #E2FF00; }

    /* Post Card Styling */
    .post-card {
        background: #121212;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #222;
        transition: transform 0.2s, border-color 0.2s;
        margin-bottom: 20px;
        position: relative;
    }
    .post-card:hover {
        border-color: #E2FF00;
        transform: scale(1.02);
    }
    .post-img-container {
        height: 200px;
        background-size: cover;
        background-position: center;
        position: relative;
        padding: 15px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }
    .post-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(transparent, rgba(0,0,0,0.9));
    }
    .post-text-content {
        position: relative;
        z-index: 1;
        padding: 10px;
    }
    .post-card-title {
        font-weight: 800;
        font-size: 14px;
        line-height: 1.2;
        margin-bottom: 5px;
    }
    .post-card-desc {
        font-size: 11px;
        color: #888;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    /* GUI DETAIL VIEW (image_62f445.jpg style) */
    .gui-window {
        background-color: #0c0c0c;
        border: 2px solid #222;
        border-radius: 24px;
        padding: 20px;
        margin-top: 10px;
    }
    .gui-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .user-pill {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .user-avatar-circle {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background: #333;
        border: 2px solid #666;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
    .user-info-text { font-weight: 800; }
    .like-count {
        background: #222;
        border-radius: 10px;
        padding: 2px 10px;
        font-size: 12px;
        color: #aaa;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .close-btn {
        background: #ff3b30;
        border: none;
        width: 40px;
        height: 40px;
        border-radius: 12px;
        color: white;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    /* Content Area */
    .content-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }
    .content-left {
        background: #1a1a1a;
        border-radius: 15px;
        padding: 0;
        overflow: hidden;
    }
    .content-right {
        background: rgba(255,255,255,0.03);
        border-radius: 15px;
        padding: 15px;
    }
    .read-badge {
        background: rgba(255,255,255,0.9);
        color: black;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: 800;
        font-size: 12px;
        position: absolute;
        bottom: 15px;
        right: 15px;
    }

    /* Comment Styling */
    .comment-item {
        display: flex;
        gap: 12px;
        margin-bottom: 15px;
        padding-bottom: 15px;
        border-bottom: 1px solid #222;
        position: relative;
    }
    .comment-floor {
        position: absolute;
        top: 0;
        right: 0;
        background: #333;
        font-size: 10px;
        padding: 2px 6px;
        border-radius: 5px;
        color: #888;
    }
    .comment-author { font-weight: 800; font-size: 13px; margin-bottom: 4px; }
    .comment-text { font-size: 12px; color: #ccc; line-height: 1.4; }

    /* Nav Buttons */
    .stButton>button {
        background-color: #222;
        color: white;
        border: 1px solid #333;
        border-radius: 10px;
        font-weight: 700;
    }
    .stButton>button:hover {
        border-color: #E2FF00;
        color: #E2FF00;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIAL STATE ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 101,
            "author": "GlobalWatcher", 
            "title": "[Post] Did y'all hear? Porcelumex's CEO just got the boot!", 
            "content": "Heard Porcelumex's CEO Ferox got taken down. Anyone know if this is legit or just rumors? The market is going crazy right now.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1560179707-f14e90ef3623?q=80&w=600",
            "likes": 15,
            "replies": [
                {"author": "ChopChop", "text": "Who? Why should we give a Denny about any of this?", "floor": "1F"}, 
                {"author": "Anonymous", "text": "I don't know what's going on, but something must be happening in the Waifei Peninsula. Several TOPS higher-ups have been canceling their events...", "floor": "2F"},
                {"author": "Beardy", "text": "Now that he's out of the picture, what about Lucro?", "floor": "3F"}
            ]
        },
        {
            "id": 103,
            "author": "SpaceXplorer", 
            "title": "[News] New Artemis II Mission Photos Released", 
            "content": "NASA has just published high-res imagery from the latest lunar orbiter. The clarity of the south pole craters is unprecedented.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=600",
            "likes": 42,
            "replies": [
                {"author": "StarGazer", "text": "The resolution is insane. Look at those shadows!", "floor": "1F"}
            ]
        },
        {
            "id": 104,
            "author": "SysAdmin_Help", 
            "title": "[Question] How to quickly secure your cloud environment?", 
            "content": "Just started a small startup. We use AWS and Azure. What are the 'Carrot' essentials to prevent ransomware?",
            "faction": "Help Info", 
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?q=80&w=600",
            "likes": 8,
            "replies": []
        }
    ]

if "view" not in st.session_state:
    st.session_state.view = "board"
if "selected_idx" not in st.session_state:
    st.session_state.selected_idx = None

# --- HEADER ---
h_col1, h_col2 = st.columns([1, 1])
with h_col1:
    st.markdown('<div class="brand-container"><div class="brand-title">KNOT-<span>LINK</span></div></div>', unsafe_allow_html=True)
with h_col2:
    n_cols = st.columns([1, 1])
    with n_cols[0]:
        if st.button("NOTIFICATIONS", use_container_width=True): pass
    with n_cols[1]:
        if st.button("INTEL BOARD", type="primary", use_container_width=True):
            st.session_state.view = "board"
            st.rerun()

# --- MAIN LOGIC ---

# 1. BOARD VIEW
if st.session_state.view == "board":
    # Faction filter tabs
    t1, t2, t3, t4 = st.columns([0.4, 0.4, 0.4, 3])
    with t1: st.button("All", type="primary")
    with t2: st.button("General")
    with t3: st.button("Help Info")

    st.write("")
    
    # Grid of posts
    cols = st.columns(4)
    for i, post in enumerate(st.session_state.posts):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="post-card">
                    <div class="post-img-container" style="background-image: url('{post['image']}');">
                        <div class="post-overlay"></div>
                        <div class="post-text-content">
                            <div class="post-card-title">{post['title']}</div>
                            <div class="post-card-desc">{post['content']}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Clickable Button overlaying the aesthetic
            if st.button(f"READ SIGNAL #{post['id']}", key=f"btn_{i}", use_container_width=True):
                st.session_state.selected_idx = i
                st.session_state.view = "gui"
                st.rerun()
            st.markdown(f'<div style="margin-top:-10px; font-size:10px; color:#444; padding-left:5px;">👤 {post["author"]}</div>', unsafe_allow_html=True)

# 2. GUI DETAIL VIEW
elif st.session_state.view == "gui":
    post = st.session_state.posts[st.session_state.selected_idx]
    
    # Render the Window
    st.markdown(f"""
        <div class="gui-window">
            <div class="gui-header">
                <div class="user-pill">
                    <div class="user-avatar-circle">🐷</div>
                    <div>
                        <div class="user-info-text">{post['author']}</div>
                        <div class="like-count">❤️ {post['likes']}</div>
                    </div>
                </div>
                <div style="display:flex; gap:10px;">
                    <div style="color:#666; font-size:12px; align-self:center;">#{post['id']}</div>
                </div>
            </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1])
    
    with c1:
        # Left side: Image and Text
        st.markdown(f"""
            <div style="position:relative; border-radius:15px; overflow:hidden; border:1px solid #333;">
                <img src="{post['image']}" style="width:100%; display:block;">
                <div class="read-badge">Read</div>
            </div>
            <div style="padding:15px 0;">
                <h4 style="margin:0; font-weight:800;">{post['title']}</h4>
                <p style="color:#aaa; font-size:14px; margin-top:10px; line-height:1.5;">{post['content']}</p>
            </div>
        """, unsafe_allow_html=True)
        
    with c2:
        # Right side: Comments
        st.markdown('<div class="content-right">', unsafe_allow_html=True)
        for r in post['replies']:
            st.markdown(f"""
                <div class="comment-item">
                    <div class="comment-floor">{r['floor']}</div>
                    <div class="user-avatar-circle" style="width:32px; height:32px; font-size:14px;">👤</div>
                    <div>
                        <div class="comment-author">{r['author']}</div>
                        <div class="comment-text">{r['text']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Reply section
        st.write("---")
        with st.form("reply_form", clear_on_submit=True):
            r_text = st.text_input("Transmitting reply...", placeholder="Say something to this proxy...")
            if st.form_submit_button("SEND LOG"):
                if r_text:
                    new_floor = f"{len(post['replies']) + 1}F"
                    st.session_state.posts[st.session_state.selected_idx]['replies'].append({
                        "author": "NetworkProxy",
                        "text": r_text,
                        "floor": new_floor
                    })
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Close button logic
    if st.button("❌ CLOSE INTERFACE", use_container_width=True):
        st.session_state.view = "board"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer info
st.markdown("""
    <div style="position:fixed; bottom:10px; left:20px; font-size:10px; color:#333;">
        SECURE CONNECTION // PROTOCOL KNOT_V2
    </div>
""", unsafe_allow_html=True)
