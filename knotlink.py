import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & THEMING ---
st.set_page_config(
    page_title="Inter-Knot // Proxy Terminal",
    page_icon="🟠",
    layout="wide"
)

# Custom CSS to force the ZZZ aesthetic onto Streamlit components
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    /* Main Background */
    .stApp {
        background-color: #0a0a0a;
        color: #e0e0e0;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Header Styling */
    .header-text {
        font-family: 'Orbitron', sans-serif;
        color: #ff6b00;
        letter-spacing: -1px;
        text-transform: uppercase;
    }

    /* Post Cards */
    .knot-card {
        background-color: #1a1a1a;
        border-left: 4px solid #333;
        padding: 20px;
        margin-bottom: 15px;
        transition: 0.2s;
    }
    .knot-card:hover {
        border-left-color: #ff6b00;
        background-color: #222;
    }

    /* Status Tags */
    .status-tag {
        font-size: 0.7rem;
        padding: 2px 8px;
        text-transform: uppercase;
        border: 1px solid #ff6b00;
        color: #ff6b00;
        border-radius: 2px;
    }

    /* Fairy Eye Animation */
    .fairy-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    .fairy-eye {
        width: 12px;
        height: 12px;
        background: #ff6b00;
        border-radius: 50%;
        box-shadow: 0 0 10px #ff6b00;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.3; }
        100% { opacity: 1; }
    }
    
    /* Input Overrides */
    .stTextArea textarea, .stTextInput input {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE (MOCK DATABASE) ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "author": "GhostInTheGrid",
            "title": "Safety tips for the Lumina Square Hollow exit",
            "content": "Notice: The usual path near the parking garage is getting unstable. Saw some Ethereals camping the extraction point.",
            "tags": ["Intel", "Safety"],
            "timestamp": time.time()
        },
        {
            "author": "Rookie_Proxy_04",
            "title": "Why does my Bangboo keep pointing at the ceiling?",
            "content": "I've been in the Hollow for 2 hours and my E-Series won't stop looking up. There's nothing there.",
            "tags": ["Help", "Bangboo"],
            "timestamp": time.time() - 3600
        }
    ]

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("""
        <div class="fairy-container">
            <div class="fairy-eye"></div>
            <h2 class="header-text" style="font-size: 1.5rem; margin: 0;">INTER-KNOT</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.button("🌐 Proxy Lounge", use_container_width=True)
    st.button("📡 Intel Sharing", use_container_width=True)
    st.button("⚙️ Gear Talk", use_container_width=True)
    st.button("🔍 Rumor Mill", use_container_width=True)
    
    st.write("---")
    st.caption("LOGGED IN AS")
    st.subheader("PHAETHON")
    st.success("● SECURE CONNECTION")

# --- MAIN CONTENT ---
st.markdown('<h1 class="header-text">The Proxy Lounge</h1>', unsafe_allow_html=True)
st.caption("// Anonymous discussion and intel exchange for verified Proxies.")

# Posting Interface
with st.expander("➕ START NEW THREAD", expanded=False):
    with st.form("new_post_form", clear_on_submit=True):
        title = st.text_input("Thread Title", placeholder="Enter a descriptive title...")
        content = st.text_area("Content", placeholder="Share your intel...")
        tags = st.multiselect("Tags", ["Intel", "Safety", "Help", "Bangboo", "General"], default=["General"])
        submit = st.form_submit_button("SUBMIT TO INTER-KNOT")
        
        if submit and title and content:
            new_entry = {
                "author": "PHAETHON",
                "title": title,
                "content": content,
                "tags": tags,
                "timestamp": time.time()
            }
            st.session_state.posts.insert(0, new_entry)
            st.rerun()

st.write("") # Spacer

# Feed Rendering
for post in st.session_state.posts:
    dt_object = datetime.fromtimestamp(post['timestamp']).strftime('%Y-%m-%d %H:%M')
    
    # HTML template for each post card
    tags_html = "".join([f'<span class="status-tag" style="margin-left:5px">{tag}</span>' for tag in post['tags']])
    
    st.markdown(f"""
        <div class="knot-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="width: 24px; height: 24px; background: #333; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #ff6b00; font-size: 10px; border: 1px solid #ff6b00;">P</div>
                    <span style="color: #ff6b00; font-weight: bold; font-size: 0.8rem;">@{post['author']}</span>
                </div>
                <div>{tags_html}</div>
            </div>
            <h3 style="margin: 10px 0 5px 0;">{post['title']}</h3>
            <p style="color: #aaa; font-size: 0.9rem; margin-bottom: 15px;">{post['content']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.7rem; color: #555; border-top: 1px solid #333; pt-10px; margin-top: 10px;">
                <div>Like • Reply • Share</div>
                <div style="font-style: italic;">{dt_object} // VERIFIED_ENTRY</div>
            </div>
        </div>
    """, unsafe_allow_html=True)