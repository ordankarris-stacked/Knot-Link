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
        text-transform: uppercase;
        border: none;
    }

    .nav-item-active {
        background-color: #E2FF00;
        color: black !important;
    }

    /* Sub-tabs Styling (Fixed st.button error by targeting div) */
    div.stButton > button {
        background-color: #1A1A1A;
        color: #888;
        padding: 4px 20px;
        border-radius: 15px;
        font-size: 12px;
        border: none;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        border-color: #E2FF00;
        color: #E2FF00;
    }

    /* Post Card Grid Styling (Vertical Card Style from image) */
    .card-container {
        background-color: #111111;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #222;
        margin-bottom: 20px;
        position: relative;
        height: 450px; /* Fixed height for vertical look */
        display: flex;
        flex-direction: column;
    }
    
    .card-container:hover {
        border-color: #E2FF00;
    }

    .card-image {
        flex: 1;
        background-size: cover;
        background-position: center;
        width: 100%;
        background-color: #1a1a1a;
        position: relative;
    }

    .card-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,1) 0%, rgba(0,0,0,0.6) 60%, transparent 100%);
        padding: 15px;
    }

    .post-title {
        font-weight: bold;
        font-size: 14px;
        line-height: 1.2;
        margin-bottom: 6px;
        color: #FFFFFF;
    }

    .post-content-preview {
        color: #999;
        font-size: 11px;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-footer {
        background-color: #111111;
        padding: 12px 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .author-avatar {
        width: 28px;
        height: 28px;
        background-color: #E2FF00;
        border-radius: 50%;
        border: 2px solid #333;
    }

    .author-name {
        font-weight: bold;
        font-size: 12px;
        color: #FFF;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    /* Detail View Styling */
    .detail-container {
        background-color: #151515;
        border: 2px solid #333;
        border-radius: 20px;
        overflow: hidden;
        margin-top: 10px;
    }

    .detail-header {
        background-color: #222;
        padding: 15px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .detail-body {
        display: flex;
        min-height: 500px;
    }

    .detail-left {
        flex: 1;
        padding: 30px;
        border-right: 1px solid #333;
    }

    .detail-right {
        width: 350px;
        background-color: #0A0A0A;
        padding: 20px;
    }

    .comment-item {
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px solid #222;
    }

    .comment-author {
        font-weight: bold;
        font-size: 12px;
        color: #E2FF00;
        display: flex;
        justify-content: space-between;
        margin-bottom: 4px;
    }

    .comment-text {
        font-size: 12px;
        color: #AAA;
    }

    /* Fixed Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0F0F0F !important;
        border-right: 1px solid #222;
    }

    </style>
""", unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "author": "MetisIntel", 
            "title": "[Post] Vision's shocking scandal exposed — Perlman is going to jail!", 
            "content": "Charles Perlman, chief of logistics, has been found guilty of misusing Ether resources in the Sixth Street sector. Evidence of corruption has finally surfaced after months of internal investigation by the H.I.A.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1514467950401-6d88ff3f1cce?auto=format&fit=crop&q=80&w=400", # News/Industrial vibe
            "replies": [
                {"author": "StreetSmart", "text": "Finally some justice on 6th street."},
                {"author": "Worrybot", "text": "Will this affect the local delivery routes?"}
            ]
        },
        {
            "id": 2,
            "author": "Worrybot", 
            "title": "A new Hollow on Fourteenth Street!", 
            "content": "A Companion Hollow has manifested near the residential district. High ether concentration detected. Avoid the subway entrance until the E.P.S. issues a clear notice.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?auto=format&fit=crop&q=80&w=400",
            "replies": [
                {"author": "Citizen_A", "text": "Again? That's the third time this month."},
                {"author": "Proxy_X", "text": "Looking for a squad to scout the outer rim."}
            ]
        },
        {
            "id": 3,
            "author": "Friend2Proxies", 
            "title": "[Info] Proxy Must-Knows: Carrots", 
            "content": "Investigators and Proxies alike: remember that Carrots are your lifeline. Don't rely on outdated grid maps when the Hollow is shifting rapidly.",
            "faction": "Help Request Info", 
            "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&q=80&w=400",
            "replies": [
                {"author": "Neon_Rabbit", "text": "Does anyone have a reliable map for the industrial sector?"}
            ]
        },
        {
            "id": 4,
            "author": "Anonymous", 
            "title": "[Warning] Beware of the Proxy called Freeman's Antlers", 
            "content": "What a pain! This Proxy has been leading teams into high-hazard zones without proper equipment. Steer clear if you value your life.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?auto=format&fit=crop&q=80&w=400",
            "replies": [
                {"author": "ThreeSeven", "text": "I've heard similar stories. Stay safe out there."}
            ]
        }
    ]

if "selected_post" not in st.session_state:
    st.session_state.selected_post = None

if "current_filter" not in st.session_state:
    st.session_state.current_filter = "All"

# --- NAVIGATION ---
nav_cols = st.columns([6, 1, 1, 1])
with nav_cols[1]:
    st.markdown('<div class="nav-item">Notifications</div>', unsafe_allow_html=True)
with nav_cols[2]:
    st.markdown('<div class="nav-item nav-item-active" style="text-align:center;">Intel Board</div>', unsafe_allow_html=True)
with nav_cols[3]:
    st.markdown('<div class="nav-item">Schedule</div>', unsafe_allow_html=True)

# --- FILTER TABS ---
st.write("") # Spacer
tab_cols = st.columns([1, 1, 1, 5])
with tab_cols[0]:
    if st.button("All", key="btn_all"):
        st.session_state.current_filter = "All"
        st.session_state.selected_post = None
        st.rerun()
with tab_cols[1]:
    if st.button("Fairy Picks", key="btn_fairy"):
        st.session_state.current_filter = "General"
        st.session_state.selected_post = None
        st.rerun()
with tab_cols[2]:
    if st.button("Help Info", key="btn_help"):
        st.session_state.current_filter = "Help Request Info"
        st.session_state.selected_post = None
        st.rerun()

# --- SIDEBAR (Transmission) ---
with st.sidebar:
    st.markdown("### 🛰️ TRANSMISSION")
    st.markdown(f"**Logon:** `Anonymous User`")
    st.write("---")
    new_title = st.text_input("Signal Title")
    new_content = st.text_area("Signal Body", placeholder="Broadcast a message...")
    post_category = st.selectbox("Frequency", ["General", "Help Request Info"])
    if st.button("SEND SIGNAL", use_container_width=True):
        if new_content.strip() and new_title.strip():
            st.session_state.posts.insert(0, {
                "id": random.randint(1000, 9999),
                "author": "Anonymous User",
                "title": new_title,
                "content": new_content,
                "faction": post_category,
                "image": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?auto=format&fit=crop&q=80&w=400",
                "replies": []
            })
            st.rerun()

# --- CONTENT AREA ---
if st.session_state.selected_post:
    # DETAIL VIEW
    post = st.session_state.selected_post
    if st.button("← Back to Board"):
        st.session_state.selected_post = None
        st.rerun()

    st.markdown(f"""
        <div class="detail-container">
            <div class="detail-header">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div class="author-avatar"></div>
                    <span style="font-weight:bold; color:#E2FF00;">{post['author']}</span>
                </div>
                <div style="color:#555; font-size:10px;">REF: {post['id']}</div>
            </div>
            <div class="detail-body">
                <div class="detail-left">
                    <h2 style="color:#FFF; margin-bottom:15px; font-size:1.5rem;">{post['title']}</h2>
                    <p style="color:#999; line-height:1.7; font-size:14px;">{post['content']}</p>
                    <div style="margin-top:50px; border-top:1px solid #222; padding-top:20px; color:#444; font-size:10px;">
                        [ SIGNAL TRACE COMPLETED ]
                    </div>
                </div>
                <div class="detail-right">
                    <div style="font-size:11px; color:#666; margin-bottom:20px; letter-spacing:1px;">REPLIES</div>
    """, unsafe_allow_html=True)
    
    for i, reply in enumerate(post['replies']):
        st.markdown(f"""
            <div class="comment-item">
                <div class="comment-author">
                    <span>{reply['author']}</span>
                    <span style="color:#444;">{i+1}F</span>
                </div>
                <div class="comment-text">{reply['text']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    with st.container():
        rep_col1, rep_col2 = st.columns([4, 1])
        with rep_col1:
            reply_text = st.text_input("Enter reply...", label_visibility="collapsed")
        with rep_col2:
            if st.button("REPLY", use_container_width=True):
                if reply_text:
                    post['replies'].append({"author": "Anonymous User", "text": reply_text})
                    st.rerun()

else:
    # GRID VIEW (Vertical Cards)
    display_posts = st.session_state.posts
    if st.session_state.current_filter != "All":
        display_posts = [p for p in st.session_state.posts if p['faction'] == st.session_state.current_filter]

    cols = st.columns(4)
    for idx, post in enumerate(display_posts):
        with cols[idx % 4]:
            img_url = post.get('image', "https://images.unsplash.com/photo-1614728263952-84ea256f9679?auto=format&fit=crop&q=80&w=400")
            st.markdown(f"""
                <div class="card-container">
                    <div class="card-image" style="background-image: url('{img_url}');">
                        <div class="card-overlay">
                            <div class="post-title">{post['title']}</div>
                            <div class="post-content-preview">{post['content']}</div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <div class="author-avatar"></div>
                        <div class="author-name">{post['author']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Open Intel {post['id']}", key=f"open_{post['id']}", use_container_width=True):
                st.session_state.selected_post = post
                st.rerun()

# --- FOOTER ---
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 20px; color: #444; font-size: 10px; z-index: 100;">
        UID: 1302948125 📶
    </div>
""", unsafe_allow_html=True)
