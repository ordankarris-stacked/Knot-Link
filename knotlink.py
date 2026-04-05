import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & THEMING ---
st.set_page_config(
    page_title="KNOT-LINK // GATEWAY",
    page_icon="🟠",
    layout="wide"
)

# Initialize Session State
if 'filter' not in st.session_state:
    st.session_state.filter = "All"

if 'active_post_id' not in st.session_state:
    st.session_state.active_post_id = None

# Sample Data with Real Life Information
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "id": 101,
            "author": "TechCrunch",
            "title": "[News] OpenAI reveals 'Sora' text-to-video capabilities",
            "content": "The new model can generate up to a minute of high-fidelity video from text prompts. Experts are discussing the implications for the film industry and deepfake detection.",
            "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800",
            "category": "General",
            "replies": [
                {"user": "VFX_Artist", "text": "This is both terrifying and exciting for my career."},
                {"user": "CinemaLover", "text": "Will we ever know what's real anymore?"}
            ]
        },
        {
            "id": 102,
            "author": "Reuters_Finance",
            "title": "[Market] Global markets rally on cooling inflation data",
            "content": "Stocks across Asia and Europe saw a 2% jump today after the latest CPI reports suggested central banks might pause rate hikes earlier than expected.",
            "img": "https://images.unsplash.com/photo-1611974717482-bc12301f9d69?auto=format&fit=crop&q=80&w=800",
            "category": "General",
            "replies": [
                {"user": "BullRun24", "text": "My portfolio is finally green again!"}
            ]
        },
        {
            "id": 103,
            "author": "IT_Support_Global",
            "title": "[Help] How to secure your home network against IoT exploits",
            "content": "Recent reports show a 300% increase in smart-fridge botnets. Follow this guide to segment your VLANs and update your router firmware immediately.",
            "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?auto=format&fit=crop&q=80&w=800",
            "category": "Help Request Info",
            "replies": [
                {"user": "HomeLabber", "text": "Great guide. Most people forget to change the default admin password."},
                {"user": "SafetyFirst", "text": "Is WPA3 enough or should I stick to wired?"}
            ]
        },
        {
            "id": 104,
            "author": "SpaceX_Watch",
            "title": "[Intel] Starship Flight 4 scheduled for next month",
            "content": "Internal documents suggest the next launch attempt will focus on soft landing the booster in the Gulf of Mexico. Testing at Starbase is intensifying.",
            "img": "https://images.unsplash.com/photo-1517976487492-5750f3195933?auto=format&fit=crop&q=80&w=800",
            "category": "General",
            "replies": []
        },
        {
            "id": 105,
            "author": "GreenTech_Daily",
            "title": "[Info] Solid-state battery breakthrough reported in Japan",
            "content": "Researchers claim a 1,000km range with a 10-minute charge time. This could be the tipping point for the global transition to electric vehicles.",
            "img": "https://images.unsplash.com/photo-1593941707882-a5bba14938c7?auto=format&fit=crop&q=80&w=800",
            "category": "Help Request Info",
            "replies": [
                {"user": "EV_Fan", "text": "I've been hearing '5 years away' for 10 years, hope this is real."}
            ]
        }
    ]

# Custom CSS for UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background-color: #0d0d0d;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Top Nav Style */
    .nav-container {
        display: flex;
        justify-content: flex-end;
        gap: 0px;
        margin-bottom: 25px;
    }
    .nav-btn {
        background: transparent;
        color: #fff;
        padding: 10px 30px;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        font-size: 1.1rem;
        border-radius: 25px;
        margin-left: -10px;
        border: none;
    }
    .nav-btn.active {
        background: #f0e600;
        color: #000;
        z-index: 5;
    }

    /* Card Styling */
    .knot-card {
        position: relative;
        height: 380px;
        background-color: #1a1a1a;
        border-radius: 18px;
        overflow: hidden;
        margin-bottom: 20px;
        border: 2px solid #252525;
        transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .knot-card:hover {
        transform: translateY(-5px);
        border-color: #f0e600;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    
    .card-img-box {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-size: cover;
        background-position: center;
        z-index: 1;
    }

    .card-gradient {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.95) 15%, rgba(0,0,0,0.2) 60%, transparent 100%);
        z-index: 2;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }

    .user-pill {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(0,0,0,0.75);
        padding: 5px 12px;
        border-radius: 20px;
        width: fit-content;
        margin-bottom: 12px;
        border: 1px solid #444;
        font-size: 0.75rem;
    }
    
    .avatar-icon {
        width: 16px; height: 16px; background: #f0e600; border-radius: 50%;
    }

    .card-title-text {
        font-weight: bold; font-size: 1.1rem; line-height: 1.25;
        margin-bottom: 8px; color: #fff;
    }
    .card-desc-text {
        font-size: 0.85rem; color: #aaa; line-height: 1.4;
        display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    }

    /* Modal Styling */
    .modal-overlay {
        background: #121212;
        border: 2px solid #333;
        border-radius: 20px;
        padding: 25px;
        position: relative;
    }
    
    .reply-box {
        background: #181818;
        border-left: 4px solid #f0e600;
        padding: 12px 18px;
        margin-bottom: 10px;
        border-radius: 0 8px 8px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
def set_filter(category):
    st.session_state.filter = category
    st.session_state.active_post_id = None # Return to list when changing categories

st.markdown("""
    <div class="nav-container">
        <div class="nav-btn active">Notifications</div>
        <div class="nav-btn">Intel Board</div>
        <div class="nav-btn">Schedule</div>
    </div>
""", unsafe_allow_html=True)

# Category Jump Buttons
f_col1, f_col2, f_col3, f_col4 = st.columns([5, 1, 1, 1])
with f_col2:
    if st.button("All", use_container_width=True, type="primary" if st.session_state.filter == "All" else "secondary"):
        set_filter("All")
        st.rerun()
with f_col3:
    if st.button("General", use_container_width=True, type="primary" if st.session_state.filter == "General" else "secondary"):
        set_filter("General")
        st.rerun()
with f_col4:
    if st.button("Help Info", use_container_width=True, type="primary" if st.session_state.filter == "Help Request Info" else "secondary"):
        set_filter("Help Request Info")
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# --- POST DETAIL VIEW ---
if st.session_state.active_post_id:
    # Find post carefully to avoid KeyErrors
    active_post = next((p for p in st.session_state.posts if p["id"] == st.session_state.active_post_id), None)
    
    if active_post:
        st.markdown('<div class="modal-overlay">', unsafe_allow_html=True)
        det_col1, det_col2 = st.columns([1.5, 1])
        
        with det_col1:
            st.image(active_post.get("img", ""), use_container_width=True)
            st.title(active_post.get("title", "Untitled"))
            st.write(active_post.get("content", ""))
            if st.button("↩ BACK TO FEED", use_container_width=True):
                st.session_state.active_post_id = None
                st.rerun()

        with det_col2:
            st.markdown(f"### 💬 Comments")
            for r in active_post.get("replies", []):
                st.markdown(f"""
                    <div class="reply-box">
                        <div style="color:#f0e600; font-size:0.8rem; font-weight:bold; margin-bottom:4px;">@{r['user']}</div>
                        <div style="font-size:0.9rem;">{r['text']}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with st.form("add_reply", clear_on_submit=True):
                comment_txt = st.text_input("Add a comment...")
                if st.form_submit_button("SEND") and comment_txt:
                    active_post["replies"].append({"user": "Operator_01", "text": comment_txt})
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.session_state.active_post_id = None
        st.rerun()

# --- MAIN LIST VIEW ---
else:
    # Filter posts based on current selection
    if st.session_state.filter == "All":
        filtered_posts = st.session_state.posts
    else:
        filtered_posts = [p for p in st.session_state.posts if p["category"] == st.session_state.filter]

    if not filtered_posts:
        st.info(f"No intelligence found under the '{st.session_state.filter}' filter.")
    else:
        grid_cols = st.columns(3)
        for i, post in enumerate(filtered_posts):
            p_id = post["id"]
            with grid_cols[i % 3]:
                # Card HTML
                st.markdown(f"""
                    <div class="knot-card">
                        <div class="card-img-box" style="background-image: url('{post.get('img', '')}');"></div>
                        <div class="card-gradient">
                            <div class="user-pill">
                                <div class="avatar-icon"></div>
                                <span>{post.get('author', 'Anon')}</span>
                            </div>
                            <div class="card-title-text">{post.get('title', 'No Title')}</div>
                            <div class="card-desc-text">{post.get('content', '')}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Use a unique key with ID to avoid StreamlitDuplicateElementKey
                if st.button(f"READ REPORT #{p_id}", key=f"btn_p_{p_id}", use_container_width=True):
                    st.session_state.active_post_id = p_id
                    st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<h1 style="font-family: Orbitron; color: #f0e600;">KNOT-LINK</h1>', unsafe_allow_html=True)
    st.markdown('**NODE STATUS:** <span style="color:#00ff00;">ONLINE</span>', unsafe_allow_html=True)
    st.write("---")
    
    with st.form("broadcast_intel"):
        st.write("📢 BROADCAST NEW INTEL")
        b_title = st.text_input("Title")
        b_cat = st.selectbox("Category", ["General", "Help Request Info"])
        b_text = st.text_area("Content")
        b_img = st.text_input("Image Keyword (e.g. city, space, tech)")
        
        if st.form_submit_button("TRANSMIT"):
            if b_title and b_text:
                new_id = int(time.time())
                img_url = f"https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800"
                if b_img:
                    img_url = f"https://picsum.photos/seed/{b_img}/800/600"
                
                new_post = {
                    "id": new_id,
                    "author": "Current_Operator",
                    "title": f"[Alert] {b_title}",
                    "content": b_text,
                    "img": img_url,
                    "category": b_cat,
                    "replies": []
                }
                st.session_state.posts.insert(0, new_post)
                st.rerun()
    
    st.write("---")
    st.caption("Ver. 2.5.0-GLOBAL")
