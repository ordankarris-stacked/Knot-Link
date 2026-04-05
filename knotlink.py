import streamlit as st
import pandas as pd
from datetime import datetime

# --- SETTINGS & CONFIG ---
st.set_page_config(
    page_title="INTER-KNOT // Proxy Network",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR INTER-KNOT AESTHETIC ---
st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp {
        background-color: #0a0a0a;
        color: #e0e0e0;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d0d0d;
        border-right: 1px solid #333;
    }

    /* Post Card Styling */
    .knot-card {
        background-color: #151515;
        border-left: 4px solid #ff6b00;
        padding: 20px;
        border-radius: 0px 10px 10px 0px;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .knot-card:hover {
        transform: translateX(5px);
        background-color: #1a1a1a;
    }

    /* Typography */
    h1, h2, h3 {
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .proxy-tag {
        color: #ff6b00;
        font-weight: bold;
        font-size: 0.8rem;
    }
    
    .status-badge {
        background-color: #333;
        color: #888;
        padding: 2px 8px;
        font-size: 0.7rem;
        border-radius: 4px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_headers=True)

# --- SESSION STATE (MOCK DATABASE) ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "author": "Weh-nah-noo",
            "title": "[Post] Did y'all hear? Porcelumex's CEO just got the boot!",
            "content": "Heard Porcelumex's CEO Ferox got taken down. Anyone know if this is legit or just rumors?",
            "time": "2024-05-20 14:30",
            "likes": 42,
            "category": "General"
        },
        {
            "id": 2,
            "author": "MetisIntelligence",
            "title": "[News] Federal Reserve signals potential rate cut in Q3",
            "content": "In a surprising move, the Federal Reserve Chair indicated that inflation targets are nearing the 2% threshold.",
            "time": "2024-05-20 15:45",
            "likes": 128,
            "category": "General"
        }
    ]

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color: #ff6b00;'>INTER-KNOT</h1>", unsafe_allow_headers=True)
    st.caption("v4.0.5-STABLE // Node: New Eridu")
    
    st.divider()
    
    menu = st.radio(
        "NETWORK NAVIGATION",
        ["Lounge (Feed)", "Intel Sharing", "Profile"],
        index=0
    )
    
    st.divider()
    st.markdown("### 👤 PROXY_INFO")
    st.markdown("**ID:** PHAETHON")
    st.markdown("**RANK:** <span style='color:#3b82f6'>Legendary (LV.60)</span>", unsafe_allow_headers=True)
    
    if st.button("🔄 REFRESH SYNC"):
        st.rerun()

# --- APP LOGIC ---

if menu == "Lounge (Feed)":
    st.markdown("## // THE PROXY LOUNGE")
    
    # NEW POST SECTION
    with st.expander("➕ CREATE NEW ENCRYPTED BROADCAST"):
        with st.form("new_post_form", clear_on_submit=True):
            title = st.text_input("Thread Title")
            content = st.text_area("Intel Content")
            submit = st.form_submit_button("CONFIRM BROADCAST")
            
            if submit and title and content:
                new_entry = {
                    "id": len(st.session_state.posts) + 1,
                    "author": "PHAETHON",
                    "title": title,
                    "content": content,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "likes": 0,
                    "category": "General"
                }
                st.session_state.posts.insert(0, new_entry)
                st.success("Thread synchronized with Inter-Knot.")
                st.rerun()

    # FILTER SEARCH
    search = st.text_input("🔍 Search network threads...", "")

    # DISPLAY POSTS
    for post in st.session_state.posts:
        if search.lower() in post['title'].lower() or search.lower() in post['content'].lower():
            st.markdown(f"""
                <div class="knot-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="proxy-tag">@{post['author']}</span>
                        <span class="status-badge">#{post['id']:03d}</span>
                    </div>
                    <h3 style="margin-top: 10px;">{post['title']}</h3>
                    <p style="font-size: 0.9rem; color: #aaa;">{post['content']}</p>
                    <div style="margin-top: 15px; display: flex; gap: 20px; font-size: 0.7rem; color: #555;">
                        <span>📅 {post['time']}</span>
                        <span>❤️ {post['likes']} LIKES</span>
                        <span style="color: #ff6b00;">[ACCESS_DATA]</span>
                    </div>
                </div>
            """, unsafe_allow_headers=True)

elif menu == "Intel Sharing":
    st.markdown("## // INTEL SHARING")
    st.info("Searching for high-value Hollow commissions...")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800", caption="Encrypted Data Stream")
    st.warning("Warning: Connection to Outpost 01 is currently unstable.")

elif menu == "Profile":
    st.markdown("## // PROXY PROFILE: PHAETHON")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Inter-Knot Credits", "45,200", "+1,200")
        st.metric("Successful Commissions", "142")
    with col2:
        st.metric("Trust Level", "MAX", "Fairy Sync: 99%")
        st.metric("Hollow Zero Keys", "3")

# --- FOOTER ---
st.markdown("---")
st.caption("Unauthorized access to Inter-Knot is punishable by H.A.N.D. regulation. Stay safe, Proxy.")
