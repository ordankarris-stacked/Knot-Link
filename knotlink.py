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
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');

    /* Main Background with Diagonal Stripes */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 2px 2px, #111 1px, transparent 0);
        background-size: 24px 24px;
        color: #FFFFFF;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Top Left Title Branding - Enhanced ZZZ Style */
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

    /* Sub-tabs Styling (Yellow Pill shape for active) */
    .stButton > button {
        border-radius: 20px !important;
        text-transform: uppercase !important;
        font-weight: 700 !important;
        font-size: 12px !important;
        transition: 0.2s all !important;
    }
    
    /* Force primary button to be the signature yellow */
    button[kind="primary"] {
        background-color: #E2FF00 !important;
        color: black !important;
        border: none !important;
    }
    
    button[kind="secondary"] {
        background-color: #1A1A1A !important;
        color: #888 !important;
        border: none !important;
    }

    /* Vertical Card Style (Zenless Zone Zero Style) */
    .card-container {
        background-color: #111111;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #222;
        margin-bottom: 20px;
        position: relative;
        height: 520px;
        display: flex;
        flex-direction: column;
        transition: transform 0.2s, border-color 0.2s;
    }
    
    .card-container:hover {
        border-color: #E2FF00;
        transform: translateY(-8px);
    }

    .card-image-box {
        flex: 1;
        background-size: cover;
        background-position: center;
        width: 100%;
        position: relative;
        border-radius: 18px 18px 0 0;
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
        margin-bottom: 10px;
        color: #FFFFFF;
    }

    .post-content-preview {
        color: #CCC;
        font-size: 12px;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-footer {
        background-color: #1A1A1A;
        padding: 15px 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        border-top: 1px solid #222;
    }

    .author-avatar {
        width: 32px;
        height: 32px;
        background-color: #222;
        border-radius: 50%;
        border: 2px solid #E2FF00;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }

    .author-name {
        font-weight: 700;
        font-size: 13px;
        color: #FFF;
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
# Sub-tabs styling with yellow pill for active state
tab_cols = st.columns([0.8, 1, 1.2, 5])
filters = ["All", "General", "Help Info"]

for idx, f_name in enumerate(filters):
    with tab_cols[idx]:
        is_active = st.session_state.current_filter == f_name
        if st.button(f_name, key=f"tab_filter_{f_name}", type="primary" if is_active else "secondary", use_container_width=True):
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
    if st.button("SEND SIGNAL", use_container_width=True, type="primary"):
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
    
    st.image(post.get('image', ""), use_container_width=True)
    st.title(post.get('title', "Untitled Signal"))
    st.write(post.get('content', ""))
    st.write("---")
    st.subheader("Replies")
    for r in post.get('replies', []):
        st.markdown(f"**{r.get('author', '??')}**: {r.get('text', '')}")

else:
    # GRID VIEW
    display_posts = st.session_state.posts
    if st.session_state.current_filter != "All":
        display_posts = [p for p in st.session_state.posts if p.get('faction') == st.session_state.current_filter]

    # Calculate rows (4 columns grid)
    rows = [display_posts[i:i + 4] for i in range(0, len(display_posts), 4)]
    
    for row in rows:
        cols = st.columns(4)
        for idx, post in enumerate(row):
            # SAFE DATA ACCESS to prevent KeyError crashes
            p_id = post.get('id', random.randint(0, 9999))
            img_url = post.get('image', "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400")
            p_title = post.get('title', "Untitled Signal")
            p_author = post.get('author', "Unknown")
            p_content = post.get('content', "Signal strength confirmed. Welcome to the Node.")

            with cols[idx]:
                st.markdown(f"""
                    <div class="card-container">
                        <div class="card-image-box" style="background-image: url('{img_url}');">
                            <div class="card-overlay">
                                <div class="post-title">{p_title}</div>
                                <div class="post-content-preview">{p_content}</div>
                            </div>
                        </div>
                        <div class="card-footer">
                            <div class="author-avatar">🕶️</div>
                            <div class="author-name">{p_author}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Use a specific key to ensure uniqueness
                if st.button(f"OPEN INTEL #{p_id}", key=f"btn_view_{p_id}", use_container_width=True):
                    st.session_state.selected_post = post
                    st.rerun()
