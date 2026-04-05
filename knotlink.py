import streamlit as st
from datetime import datetime
import random

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Knot-Link // Tech Network",
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

    .nav-btn {
        background-color: #333333;
        color: #FFFFFF;
        padding: 10px 25px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        cursor: pointer;
        border: none;
        white-space: nowrap;
    }

    .nav-btn-active {
        background-color: #E2FF00;
        color: #000000 !important;
    }

    /* Clickable Card Styling */
    .stButton > button[kind="secondaryFormSubmit"], .stButton > button[kind="secondary"] {
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
        width: 100% !important;
        transition: none !important;
    }

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

    /* Detail View Styling */
    .detail-comment-box {
        background: #111;
        border-left: 3px solid #E2FF00;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 0 10px 10px 0;
    }

    /* Filter Tabs styling fix */
    .filter-btn-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }

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
            "id": 201,
            "author": "GlobalWatcher", 
            "title": "[Post] Did y'all hear? Tech Giant's CEO just got the boot!", 
            "content": "Word on the street is the CEO of the leading chip manufacturer was taken down after a secret board meeting. Stock market is reacting already.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1560179707-f14e90ef3623?q=80&w=400",
            "replies": [
                {"author": "ChopChop", "text": "Who? Why should we give a damn about any of this?"}, 
                {"author": "Anonymous", "text": "Something must be happening in the silicon valley hub. Fishy situation."},
                {"author": "Beardy", "text": "What about the new GPU lineup?"}
            ]
        },
        {
            "id": 202,
            "author": "SpaceXplorer", 
            "title": "[News] New Artemis II Mission Photos Released", 
            "content": "NASA has just published high-res imagery from the latest lunar orbiter. The clarity of the south pole craters is unprecedented.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=400",
            "replies": [{"author": "MoonLover", "text": "The lighting in these is incredible."}]
        },
        {
            "id": 203,
            "author": "SysAdmin_Help", 
            "title": "[Question] How to quickly secure your cloud environment?", 
            "content": "Just started a small startup. We use AWS and Azure. What are the 'Carrot' essentials to prevent ransomware?",
            "faction": "Help Info", 
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?q=80&w=400",
            "replies": [{"author": "Kitty_Freak", "text": "Enable MFA everywhere. That's step one. Don't skip it!"}]
        },
        {
            "id": 204,
            "author": "MarketPulse", 
            "title": "[Alert] Major Beverage Brand pulls out of Sponsorship", 
            "content": "The blue and red soda brand has officially terminated its contract with the largest esports league.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=400",
            "replies": []
        }
    ]

if "selected_post" not in st.session_state:
    st.session_state.selected_post = None

if "current_filter" not in st.session_state:
    st.session_state.current_filter = "All"

# --- TOP HEADER ---
header_col1, header_col2 = st.columns([1, 2])
with header_col1:
    st.markdown('<div class="brand-container"><div class="brand-title">KNOT-<span>LINK</span></div></div>', unsafe_allow_html=True)

with header_col2:
    st.markdown("""
        <div class="nav-container">
            <div class="nav-btn">Notifications</div>
            <div class="nav-btn nav-btn-active">Intel Board</div>
            <div class="nav-btn">Schedule</div>
        </div>
    """, unsafe_allow_html=True)

# --- FILTER TABS ---
f_col1, f_col2, f_col3, f_col4 = st.columns([0.8, 1, 1.2, 5])
filters = ["All", "General", "Help Info"]

for idx, f_name in enumerate(filters):
    with [f_col1, f_col2, f_col3][idx]:
        is_active = st.session_state.current_filter == f_name
        if st.button(f_name, key=f"tab_filter_{f_name}", type="primary" if is_active else "secondary", use_container_width=True):
            st.session_state.current_filter = f_name
            st.session_state.selected_post = None
            st.rerun()

st.write("") 

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛰️ TRANSMISSION")
    st.markdown(f"**Logon:** <span style='color:#E2FF00;'>Verified_Node_77</span>", unsafe_allow_html=True)
    st.write("---")
    new_title = st.text_input("Signal Title", placeholder="e.g. [Alert] News...")
    new_content = st.text_area("Signal Body", placeholder="Broadcast a message...")
    post_category = st.selectbox("Frequency", ["General", "Help Info"])
    if st.button("SEND SIGNAL", use_container_width=True, type="primary"):
        if new_content.strip() and new_title.strip():
            st.session_state.posts.insert(0, {
                "id": random.randint(1000, 9999),
                "author": "Verified_Node_77",
                "title": new_title,
                "content": new_content,
                "faction": post_category,
                "image": "https://images.unsplash.com/photo-1516245834210-c4c142787335?q=80&w=400",
                "replies": []
            })
            st.session_state.selected_post = None
            st.rerun()

# --- MAIN CONTENT ---
if st.session_state.selected_post:
    post = st.session_state.selected_post
    if st.button("← RETURN TO BOARD"):
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
        for i, r in enumerate(post.get('replies', [])):
            st.markdown(f"""
                <div class="detail-comment-box">
                    <div style="font-size:10px; color:#E2FF00; margin-bottom:5px;">{i+1}F // {r.get('author')}</div>
                    <div style="font-size:13px;">{r.get('text')}</div>
                </div>
            """, unsafe_allow_html=True)

else:
    # GRID VIEW
    display_posts = st.session_state.posts
    if st.session_state.current_filter != "All":
        display_posts = [p for p in st.session_state.posts if p.get('faction') == st.session_state.current_filter]

    if display_posts:
        rows = [display_posts[i:i + 4] for i in range(0, len(display_posts), 4)]
        for row in rows:
            cols = st.columns(4)
            for idx, post in enumerate(row):
                with cols[idx]:
                    # Create the visual card inside the button to make the whole card clickable
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
                    # We wrap the UI in a button. By CSS we hide the button borders so it looks like a card.
                    if st.button("", key=f"card_btn_{post.get('id')}", use_container_width=True):
                        st.session_state.selected_post = post
                        st.rerun()
                    
                    # Overlay the HTML visually at the same position
                    st.markdown(f'<div style="margin-top:-60px; pointer-events:none;">{card_html}</div>', unsafe_allow_html=True)
