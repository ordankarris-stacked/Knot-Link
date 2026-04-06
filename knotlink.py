import streamlit as st
from datetime import datetime
import random

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Knot-Link // Proxy Network",
    page_icon="🕸️",
    layout="wide",
)

# --- CUSTOM CSS (HIGH-CONTRAST TECH AESTHETIC) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');

    /* Main Background */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 2px 2px, #111 1px, transparent 0);
        background-size: 24px 24px;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Top Left Title Branding */
    .brand-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    .brand-title {
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -1.5px;
        text-transform: uppercase;
        font-style: italic;
    }
    .brand-title span {
        color: #E2FF00;
    }

    /* Top Navigation Bar Styling */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 10px 0;
        gap: 10px;
    }

    /* Card Styling */
    .card-container {
        background-color: #111111;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #222;
        margin-bottom: 10px;
        position: relative;
        height: 480px;
        display: flex;
        flex-direction: column;
        transition: transform 0.2s, border-color 0.2s, background-color 0.2s;
        text-align: left;
    }
    
    .card-container:hover {
        border-color: #E2FF00;
        transform: translateY(-5px);
        background-color: #161616;
    }

    .card-image-box {
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
        background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.4) 70%, transparent 100%);
        padding: 20px;
    }

    .post-title {
        font-weight: 800;
        font-size: 16px;
        line-height: 1.2;
        margin-bottom: 8px;
        color: #FFFFFF;
    }

    .post-content-preview {
        color: #CCC;
        font-size: 12px;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-footer {
        background-color: #1A1A1A;
        padding: 12px 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-top: 1px solid #222;
    }

    .author-avatar {
        width: 28px;
        height: 28px;
        background-color: #222;
        border-radius: 50%;
        border: 1px solid #E2FF00;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
    }

    .author-name {
        font-weight: 700;
        font-size: 12px;
        color: #FFF;
    }

    /* Transmission Form Panel */
    .transmit-panel {
        background: #111;
        border: 2px solid #E2FF00;
        padding: 30px;
        border-radius: 20px;
        margin-top: 20px;
    }

    /* Detail View Styling */
    .detail-comment-box {
        background: #111;
        border-left: 3px solid #E2FF00;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 0 10px 10px 0;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0A0A0A !important;
        border-right: 1px solid #222;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 101,
            "author": "GlobalWatcher", 
            "title": "[Post] Did y'all hear? Porcelumex's CEO just got the boot!", 
            "content": "Heard Porcelumex's CEO Ferox got taken down. Anyone know if this is legit or just rumors?",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1560179707-f14e90ef3623?q=80&w=400",
            "replies": [
                {"author": "ChopChop", "text": "Who? Why should we give a Denny about any of this?"}, 
                {"author": "Anonymous", "text": "Something must be happening in the Waifei Peninsula. This situation is fishy."},
                {"author": "Beardy", "text": "Now that he's out of the picture, what about Lucro?"}
            ]
        },
        {
            "id": 103,
            "author": "SpaceXplorer", 
            "title": "[News] New Artemis II Mission Photos Released", 
            "content": "NASA has just published high-res imagery from the latest lunar orbiter. The clarity of the south pole craters is unprecedented.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=400",
            "replies": []
        },
        {
            "id": 104,
            "author": "SysAdmin_Help", 
            "title": "[Question] How to quickly secure your cloud environment?", 
            "content": "Just started a small startup. We use AWS and Azure. What are the 'Carrot' essentials to prevent ransomware?",
            "faction": "Help Info", 
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?q=80&w=400",
            "replies": []
        }
    ]

if "view_mode" not in st.session_state:
    st.session_state.view_mode = "board" # board, detail, transmit

if "selected_post" not in st.session_state:
    st.session_state.selected_post = None

if "current_filter" not in st.session_state:
    st.session_state.current_filter = "All"

# --- TOP HEADER ---
header_col1, header_col2 = st.columns([1, 2.5])
with header_col1:
    st.markdown('<div class="brand-container"><div class="brand-title">KNOT-<span>LINK</span></div></div>', unsafe_allow_html=True)

with header_col2:
    # Use actual Streamlit buttons for navigation to handle state changes
    nav_cols = st.columns([1, 1, 1, 1])
    with nav_cols[1]:
        if st.button("NOTIFICATIONS", use_container_width=True):
            st.toast("Accessing encrypted notifications...")
    with nav_cols[2]:
        is_board = st.session_state.view_mode == "board"
        if st.button("INTEL BOARD", type="primary" if is_board else "secondary", use_container_width=True):
            st.session_state.view_mode = "board"
            st.session_state.selected_post = None
            st.rerun()
    with nav_cols[3]:
        is_transmit = st.session_state.view_mode == "transmit"
        if st.button("TRANSMIT 📡", type="primary" if is_transmit else "secondary", use_container_width=True):
            st.session_state.view_mode = "transmit"
            st.session_state.selected_post = None
            st.rerun()

# --- SIDEBAR (Persistent Info) ---
with st.sidebar:
    st.markdown("### 🛰️ ACCESS")
    st.markdown(f"**Logon Status:** <span style='color:#E2FF00;'>Anonymous User</span>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 📊 NETWORK STATS")
    st.caption("Active Proxies: 12,402")
    st.caption("Latency: 24ms")
    st.caption("Signal Strength: High")

# --- MAIN CONTENT LOGIC ---

# 1. TRANSMIT MODE (NEW FUNCTION)
if st.session_state.view_mode == "transmit":
    st.markdown("## 📡 TRANSMIT NEW SIGNAL")
    st.markdown("Broadcast your findings to the network. Use clear titles for better visibility.")
    
    with st.container():
        st.markdown('<div class="transmit-panel">', unsafe_allow_html=True)
        with st.form("main_transmit_form", clear_on_submit=True):
            t_name = st.text_input("SIGNAL NAME", placeholder="e.g. [Alert] Unusual activity in Sector 6")
            t_freq = st.selectbox("FREQUENCY", ["General", "Help Info"])
            t_body = st.text_area("CONTENT", placeholder="Enter the detailed report here...", height=200)
            
            t_col1, t_col2 = st.columns([1, 4])
            with t_col1:
                t_submit = st.form_submit_button("INITIATE BROADCAST", use_container_width=True, type="primary")
            
            if t_submit:
                if t_name.strip() and t_body.strip():
                    new_post = {
                        "id": random.randint(1000, 9999),
                        "author": "Anonymous User",
                        "title": t_name,
                        "content": t_body,
                        "faction": t_freq,
                        "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=400",
                        "replies": []
                    }
                    st.session_state.posts.insert(0, new_post)
                    st.session_state.view_mode = "board"
                    st.success("Signal broadcasted successfully!")
                    st.rerun()
                else:
                    st.error("Signal requires both a name and content.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Cancel & Return"):
        st.session_state.view_mode = "board"
        st.rerun()

# 2. DETAIL MODE
elif st.session_state.view_mode == "detail" and st.session_state.selected_post:
    post = st.session_state.selected_post
    if st.button("← RETURN TO BOARD"):
        st.session_state.view_mode = "board"
        st.session_state.selected_post = None
        st.rerun()
    
    st.markdown(f"### {post.get('title')}")
    detail_img_col, detail_text_col = st.columns([1, 1.2])
    
    with detail_img_col:
        st.image(post.get('image', ""), use_container_width=True)
    
    with detail_text_col:
        st.markdown(f"**Posted by:** `{post.get('author')}`")
        st.info(post.get('content'))
        st.write("---")
        st.markdown("**COMMUNITY LOGS**")
        if not post.get('replies'):
            st.write("*No logs found on this frequency.*")
        for i, r in enumerate(post.get('replies', [])):
            st.markdown(f"""
                <div class="detail-comment-box">
                    <div style="font-size:10px; color:#E2FF00; margin-bottom:5px;">{i+1}F // {r.get('author')}</div>
                    <div style="font-size:13px;">{r.get('text')}</div>
                </div>
            """, unsafe_allow_html=True)

# 3. BOARD MODE (GRID VIEW)
else:
    # FILTER TABS
    f_col1, f_col2, f_col3, f_col4 = st.columns([0.6, 0.8, 1, 5.6])
    filters = ["All", "General", "Help Info"]

    for idx, f_name in enumerate(filters):
        with [f_col1, f_col2, f_col3][idx]:
            is_active = st.session_state.current_filter == f_name
            if st.button(f_name, key=f"tab_filter_{f_name}", type="primary" if is_active else "secondary", use_container_width=True):
                st.session_state.current_filter = f_name
                st.rerun()

    st.write("") 

    display_posts = st.session_state.posts
    if st.session_state.current_filter != "All":
        display_posts = [p for p in st.session_state.posts if p.get('faction') == st.session_state.current_filter]

    if display_posts:
        rows = [display_posts[i:i + 4] for i in range(0, len(display_posts), 4)]
        for row in rows:
            cols = st.columns(4)
            for idx, post in enumerate(row):
                with cols[idx]:
                    card_html = f"""
                        <div class="card-container">
                            <div class="card-image-box" style="background-image: url('{post.get('image')}');">
                                <div class="card-overlay">
                                    <div class="post-title">{post.get('title')}</div>
                                    <div class="post-content-preview">{post.get('content')}</div>
                                </div>
                            </div>
                            <div class="card-footer">
                                <div class="author-avatar">⚡</div>
                                <div class="author-name">{post.get('author')}</div>
                            </div>
                        </div>
                    """
                    if st.button(f"READ SIGNAL #{post.get('id')}", key=f"btn_{post.get('id')}", use_container_width=True):
                        st.session_state.selected_post = post
                        st.session_state.view_mode = "detail"
                        st.rerun()
                    
                    st.markdown(f'<div style="margin-top:-60px; pointer-events:none;">{card_html}</div>', unsafe_allow_html=True)
    else:
        st.warning("No active signals found on this frequency.")
