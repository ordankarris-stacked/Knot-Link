import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & THEMING ---
st.set_page_config(
    page_title="KNOT-LINK // PHAETHON GATEWAY",
    page_icon="🟠",
    layout="wide"
)

# Initialize Session State for Filter and Posts
if 'filter' not in st.session_state:
    st.session_state.filter = "All"

if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "author": "r/politics",
            "title": "Trump issues warning to Iran",
            "content": "Trump Vows To Strike Civilian Infrastructure...",
            "img": "https://picsum.photos/seed/trump/400/300",
            "category": "General",
            "timestamp": time.time()
        },
        {
            "author": "r/worldnews",
            "title": "US rescues missing pilot",
            "content": "U.S. forces rescue second crew member...",
            "img": "https://picsum.photos/seed/pilot/400/300",
            "category": "General",
            "timestamp": time.time() - 3600
        },
        {
            "author": "r/spaceporn",
            "title": "New Artemis II photos",
            "content": "New Image from NASA: For the first tim...",
            "img": None,
            "category": "General",
            "timestamp": time.time() - 7200
        },
        {
            "author": "r/Music",
            "title": "Pepsi pulls out of Wi...",
            "content": "Pepsi Cancels Sponsorship c...",
            "img": "https://picsum.photos/seed/pepsi/400/300",
            "category": "General",
            "timestamp": time.time() - 10000
        },
        {
            "author": "MetisIntelligence",
            "title": "[News] Vision's shocking scandal exposed",
            "content": "Charles Perlman, chief executive of Vision Corp, was caught in a fraud scheme...",
            "img": "https://picsum.photos/seed/vision/400/300",
            "category": "Help Request Info",
            "timestamp": time.time() - 15000
        },
        {
            "author": "Hollow_Rabbit",
            "title": "Anyone seen a runaway 'Security' Bangboo?",
            "content": "Lost my modified Butler unit in the back alleys of 6th Street. Reward: Noodle Box.",
            "img": None, 
            "category": "Help Request Info",
            "timestamp": time.time() - 20000
        }
    ]

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
        background-color: #000; /* Black out fallback */
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
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
st.markdown("""
    <div class="top-nav">
        <div class="nav-item active">Notifications</div>
        <div class="nav-item">Intel Board</div>
        <div class="nav-item">Schedule</div>
    </div>
""", unsafe_allow_html=True)

# Functional Sub-Category Filter
filter_cols = st.columns([2, 1, 1, 1, 2])
with filter_cols[1]:
    if st.button("All", use_container_width=True, type="primary" if st.session_state.filter == "All" else "secondary"):
        st.session_state.filter = "All"
        st.rerun()
with filter_cols[2]:
    if st.button("General", use_container_width=True, type="primary" if st.session_state.filter == "General" else "secondary"):
        st.session_state.filter = "General"
        st.rerun()
with filter_cols[3]:
    if st.button("Help Info", use_container_width=True, type="primary" if st.session_state.filter == "Help Request Info" else "secondary"):
        st.session_state.filter = "Help Request Info"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# --- FILTER LOGIC ---
display_posts = st.session_state.posts
if st.session_state.filter != "All":
    display_posts = [p for p in st.session_state.posts if p.get("category") == st.session_state.filter]

# --- MAIN GRID ---
if not display_posts:
    st.info(f"No posts found in category: {st.session_state.filter}")
else:
    cols = st.columns(3)
    for idx, post in enumerate(display_posts):
        image_url = post.get('img')
        image_style = f"background-image: url('{image_url}');" if image_url else ""
        
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="knot-card">
                    <div class="card-image" style="{image_style}"></div>
                    <div class="card-content">
                        <div class="author-info">
                            <div class="avatar">👤</div>
                            <span style="font-size: 0.75rem; font-weight: bold; color: #aaa;">{post.get('author', 'Unknown')}</span>
                        </div>
                        <div class="card-title">{post.get('title', 'No Title')}</div>
                        <div class="card-preview">{post.get('content', '')[:80]}...</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- POSTING INTERFACE (FLOATING ACTION) ---
with st.sidebar:
    st.markdown('<h2 style="font-family: Orbitron; color: #f0e600;">KNOT-LINK</h2>', unsafe_allow_html=True)
    st.write("---")
    with st.form("new_post", clear_on_submit=True):
        st.write("Create New Thread")
        new_title = st.text_input("Title")
        new_content = st.text_area("Description")
        new_category = st.selectbox("Category", ["General", "Help Request Info"])
        new_img_seed = st.text_input("Image Keyword (Leave blank for no image)", "")
        submitted = st.form_submit_button("PUBLISH")
        
        if submitted and new_title:
            final_img = f"https://picsum.photos/seed/{new_img_seed}/400/300" if new_img_seed.strip() else None
            
            new_post = {
                "author": "PHAETHON",
                "title": new_title,
                "content": new_content,
                "img": final_img,
                "category": new_category,
                "timestamp": time.time()
            }
            st.session_state.posts.insert(0, new_post)
            st.rerun()

    st.write("---")
    st.caption(f"Logged in: PHAETHON")
    st.caption(f"Active Filter: {st.session_state.filter}")
    st.success("SYNC: ACTIVE")
