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

    /* Top Left Title Branding - Adjusted for Streamlit Layout */
    .brand-title {
        font-size: 28px;
        font-weight: 900;
        color: #FFFFFF;
        letter-spacing: -1px;
        margin-bottom: 10px;
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
        gap: 15px;
    }

    .nav-btn {
        background-color: #333333;
        color: #AAAAAA;
        padding: 8px 30px;
        border-radius: 25px;
        font-weight: bold;
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

    /* Sub-tabs Styling (Yellow Pill shape for active) */
    div.stButton > button {
        background-color: #1A1A1A;
        color: #888;
        padding: 5px 20px;
        border-radius: 20px;
        font-size: 13px;
        border: none;
        transition: 0.3s;
        width: 100%;
        text-transform: uppercase;
        font-weight: bold;
    }

    /* Target the specific "Active" button styles via Streamlit's secondary button class if possible, 
       but for this build we'll use a specific logic in the Python loop. */

    /* Vertical Card Style */
    .card-container {
        background-color: #111111;
        border-radius: 15px;
        overflow: hidden;
        border: 2px solid #222;
        margin-bottom: 25px;
        position: relative;
        height: 480px;
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
        background-color: #222; /* Fallback color to prevent KeyError visual breaks */
    }

    .card-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 60%, transparent 100%);
        padding: 15px;
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
        padding: 12px 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-top: 1px solid #222;
    }

    .author-avatar {
        width: 28px;
        height: 28px;
        background-color: #E2FF00;
        border-radius: 50%;
        border: 2px solid #333;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
    }

    .author-name {
        font-weight: bold;
        font-size: 12px;
        color: #FFF;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F0F0F !important;
        border-right: 2px solid #222;
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
            "author": "MetisIntel", 
            "title": "[Post] Vision's shocking scandal exposed — Perlman is going to jail!", 
            "content": "Charles Perlman, chief of logistics, has been found guilty of misusing Ether resources in the Sixth Street sector. Evidence of corruption has finally surfaced after months of internal investigation.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1514467950401-6d88ff3f1cce?auto=format&fit=crop&q=80&w=400",
            "replies": [{"author": "StreetSmart", "text": "Finally some justice."}, {"author": "Worrybot", "text": "Delivery routes?"}]
        },
        {
            "id": 102,
            "author": "Worrybot", 
            "title": "A new Hollow on Fourteenth Street!", 
            "content": "A Companion Hollow has manifested near the residential district. High ether concentration detected. Avoid the subway entrance until the E.P.S. issues a clear notice.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?auto=format&fit=crop&q=80&w=400",
            "replies": []
        },
        {
            "id": 103,
            "author": "Friend2Proxies", 
            "title": "[Info] Proxy Must-Knows: Carrots", 
            "content": "Investigators and Proxies alike: remember that Carrots are your lifeline. Don't rely on outdated grid maps when the Hollow is shifting rapidly.",
            "faction": "Help Info", 
            "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&q=80&w=400",
            "replies": []
        },
        {
            "id": 104,
            "author": "Anonymous", 
            "title": "[Warning] Beware of Freeman's Antlers", 
            "content": "What a pain! This Proxy has been leading teams into high-hazard zones without proper equipment. Steer clear if you value your life.",
            "faction": "General", 
            "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?auto=format&fit=crop&q=80&w=400",
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
    st.markdown('<div class="brand-title">KNOT-<span>LINK</span></div>', unsafe_allow_html=True)

with header_col2:
    st.markdown("""
        <div class="nav-container">
            <div class="nav-btn">Notifications</div>
            <div class="nav-btn nav-btn-active">Intel Board</div>
            <div class="nav-btn">Schedule</div>
        </div>
    """, unsafe_allow_html=True)

# --- FILTER TABS ---
# To simulate the yellow pill for active tab, we use a slightly different button style logic
tab_cols = st.columns([0.8, 1, 1, 5])
filters = ["All", "General", "Help Info"]

for idx, f_name in enumerate(filters):
    with tab_cols[idx]:
        is_active = st.session_state.current_filter == f_name
        # Using custom styling for the active state
        btn_label = f_name
        if st.button(btn_label, key=f"tab_{f_name}", type="primary" if is_active else "secondary"):
            st.session_state.current_filter = f_name
            st.session_state.selected_post = None
            st.rerun()

st.write("") 

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛰️ TRANSMISSION")
    st.markdown(f"**Logon:** <span style='color:#E2FF00;'>Anonymous User</span>", unsafe_allow_html=True)
    st.write("---")
    new_title = st.text_input("Signal Title", placeholder="e.g. [Question] Leveling up...")
    new_content = st.text_area("Signal Body", placeholder="Broadcast a message...")
    post_category = st.selectbox("Frequency", ["General", "Help Info"])
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

# --- MAIN CONTENT ---
if st.session_state.selected_post:
    post = st.session_state.selected_post
    if st.button("← Back to Board"):
        st.session_state.selected_post = None
        st.rerun()
    
    # Detailed post view (simplified for stability)
    st.image(post['image'], use_container_width=True)
    st.title(post['title'])
    st.write(post['content'])
    st.write("---")
    st.subheader("Replies")
    for r in post['replies']:
        st.markdown(f"**{r['author']}**: {r['text']}")

else:
    # GRID VIEW
    display_posts = st.session_state.posts
    if st.session_state.current_filter != "All":
        display_posts = [p for p in st.session_state.posts if p['faction'] == st.session_state.current_filter]

    rows = [display_posts[i:i + 4] for i in range(0, len(display_posts), 4)]
    
    for row in rows:
        cols = st.columns(4)
        for idx, post in enumerate(row):
            with cols[idx]:
                # Error prevention: ensure 'image' and 'title' keys exist
                img_url = post.get('image', "")
                p_title = post.get('title', "Untitled Signal")
                p_author = post.get('author', "Unknown")
                p_content = post.get('content', "")

                st.markdown(f"""
                    <div class="card-container">
                        <div class="card-image" style="background-image: url('{img_url}');">
                            <div class="card-overlay">
                                <div class="post-title">{p_title}</div>
                                <div class="post-content-preview">{p_content}</div>
                            </div>
                        </div>
                        <div class="card-footer">
                            <div class="author-avatar">🛡️</div>
                            <div class="author-name">{p_author}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"View Intel #{post['id']}", key=f"view_{post['id']}", use_container_width=True):
                    st.session_state.selected_post = post
                    st.rerun()
