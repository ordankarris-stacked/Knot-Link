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

    /* Main Background with Diagonal Stripes */
    .stApp {
        background-color: #000000;
        background-image: linear-gradient(135deg, #0a0a0a 25%, transparent 25%), 
                          linear-gradient(225deg, #0a0a0a 25%, transparent 25%), 
                          linear-gradient(45deg, #0a0a0a 25%, transparent 25%), 
                          linear-gradient(315deg, #0a0a0a 25%, #000000 25%);
        background-position: 10px 0, 10px 0, 0 0, 0 0;
        background-size: 20px 20px;
        background-repeat: repeat;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Top Left Title Branding */
    .brand-title {
        position: absolute;
        top: 20px;
        left: 0;
        font-size: 24px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -1px;
        z-index: 1000;
    }
    .brand-title span {
        color: #E2FF00;
    }

    /* Top Navigation Bar Styling */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 20px 0;
        gap: 15px;
    }

    .nav-btn {
        background-color: #333333;
        color: #AAAAAA;
        padding: 10px 35px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 14px;
        text-transform: uppercase;
        cursor: pointer;
        border: none;
    }

    .nav-btn-active {
        background-color: #E2FF00;
        color: #000000 !important;
    }

    /* Sub-tabs Styling */
    div.stButton > button {
        background-color: #1A1A1A;
        color: #888;
        padding: 5px 25px;
        border-radius: 20px;
        font-size: 13px;
        border: 2px solid transparent;
        transition: 0.3s;
        width: 100%;
    }

    div.stButton > button:hover {
        border-color: #E2FF00;
        color: #E2FF00;
    }

    /* Vertical Card Style */
    .card-container {
        background-color: #111111;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #222;
        margin-bottom: 25px;
        position: relative;
        height: 500px;
        display: flex;
        flex-direction: column;
        transition: transform 0.2s;
    }
    
    .card-container:hover {
        border-color: #E2FF00;
        transform: translateY(-5px);
    }

    .card-image {
        flex: 1;
        background-size: cover;
        background-position: center;
        width: 100%;
        position: relative;
    }

    .card-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 70%, transparent 100%);
        padding: 20px;
    }

    .post-title {
        font-weight: bold;
        font-size: 15px;
        line-height: 1.3;
        margin-bottom: 8px;
        color: #FFFFFF;
    }

    .post-content-preview {
        color: #BBB;
        font-size: 11px;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-footer {
        background-color: #181818;
        padding: 15px 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        border-top: 1px solid #222;
    }

    .author-avatar {
        width: 32px;
        height: 32px;
        background-color: #E2FF00;
        border-radius: 50%;
        border: 2px solid #333;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .author-name {
        font-weight: bold;
        font-size: 13px;
        color: #FFF;
    }

    /* Detail View / Commission Modal Styling */
    .commission-modal {
        background-color: #151515;
        border: 3px solid #222;
        border-radius: 25px;
        padding: 0;
        overflow: hidden;
        margin-top: 20px;
    }

    .modal-header {
        background-color: #222222;
        padding: 20px 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #333;
    }

    .modal-body {
        display: flex;
        flex-wrap: wrap;
    }

    .modal-left {
        flex: 1;
        min-width: 350px;
        padding: 30px;
        border-right: 1px solid #333;
    }

    .modal-right {
        width: 400px;
        background-color: #0D0D0D;
        padding: 25px;
        max-height: 600px;
        overflow-y: auto;
    }

    .floor-badge {
        background-color: #333;
        color: #FFF;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 10px;
        margin-left: auto;
    }

    .comment-item {
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #222;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F0F0F !important;
        border-right: 2px solid #222;
    }

    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 101,
            "author": "MetisIntel", 
            "title": "[Post] Vision's shocking scandal exposed — Perlman is going to jail!", 
            "content": "Charles Perlman, chief of logistics, has been found guilty of misusing Ether resources in the Sixth Street sector. Evidence of corruption has finally surfaced after months of internal investigation by the H.I.A.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1514467950401-6d88ff3f1cce?auto=format&fit=crop&q=80&w=400",
            "replies": [
                {"author": "StreetSmart", "text": "Finally some justice on 6th street."},
                {"author": "Worrybot", "text": "Will this affect the local delivery routes?"}
            ]
        },
        {
            "id": 102,
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
            "id": 103,
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
            "id": 104,
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

# --- TOP NAVIGATION & BRANDING ---
st.markdown('<div class="brand-title">KNOT-<span>LINK</span></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="nav-container">
        <div class="nav-btn">Notifications</div>
        <div class="nav-btn nav-btn-active">Intel Board</div>
        <div class="nav-btn">Schedule</div>
    </div>
""", unsafe_allow_html=True)

# --- FILTER TABS ---
st.write("") 
tab_cols = st.columns([1, 1, 1, 5])
with tab_cols[0]:
    if st.button("All", key="btn_all"):
        st.session_state.current_filter = "All"
        st.session_state.selected_post = None
        st.rerun()
with tab_cols[1]:
    if st.button("General", key="btn_general"):
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
    st.markdown(f"**Logon:** <span style='color:#E2FF00;'>Anonymous User</span>", unsafe_allow_html=True)
    st.write("---")
    new_title = st.text_input("Signal Title", placeholder="e.g. [Question] Leveling up...")
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
    # COMMISSION DETAIL VIEW
    post = st.session_state.selected_post
    if st.button("← Back to Board"):
        st.session_state.selected_post = None
        st.rerun()

    st.markdown(f"""
        <div class="commission-modal">
            <div class="modal-header">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div class="author-avatar">👤</div>
                    <span style="font-weight:bold; color:#FFF;">{post['author']}</span>
                </div>
                <div style="background-color:#D32F2F; color:white; padding:4px 10px; border-radius:4px; font-weight:bold; cursor:pointer;">X</div>
            </div>
            <div class="modal-body">
                <div class="modal-left">
                    <img src="{post['image']}" style="width:100%; border-radius:15px; margin-bottom:20px; border: 2px solid #333;">
                    <h2 style="color:#FFF; margin-bottom:15px; font-size:1.4rem;">{post['title']}</h2>
                    <p style="color:#CCC; line-height:1.6; font-size:14px; white-space: pre-wrap;">{post['content']}</p>
                    <div style="margin-top:30px; display:inline-block; background:#333; padding:5px 15px; border-radius:15px; font-size:12px; color:#E2FF00;">
                        Commission Rank: S
                    </div>
                </div>
                <div class="modal-right">
                    <div style="font-size:12px; color:#666; margin-bottom:20px; font-weight:bold;">REPLIES</div>
    """, unsafe_allow_html=True)
    
    for i, reply in enumerate(post['replies']):
        st.markdown(f"""
            <div class="comment-item">
                <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
                    <div style="width:24px; height:24px; background:#444; border-radius:50%;"></div>
                    <span style="font-weight:bold; color:#E2FF00; font-size:12px;">{reply['author']}</span>
                    <span class="floor-badge">{i+1}F</span>
                </div>
                <div style="font-size:12px; color:#AAA; padding-left:32px;">{reply['text']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    # Reply input
    with st.container():
        rep_col1, rep_col2 = st.columns([4, 1])
        with rep_col1:
            reply_text = st.text_input("Enter comment...", label_visibility="collapsed")
        with rep_col2:
            if st.button("SUBMIT", use_container_width=True):
                if reply_text:
                    post['replies'].append({"author": "Anonymous User", "text": reply_text})
                    st.rerun()

else:
    # INTEL BOARD GRID VIEW
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
                        <div class="author-avatar">🛡️</div>
                        <div class="author-name">{post['author']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"View Intel #{post['id']}", key=f"view_{post['id']}", use_container_width=True):
                st.session_state.selected_post = post
                st.rerun()
