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
    }

    .nav-item-active {
        background-color: #E2FF00;
        color: black;
    }

    /* Sub-tabs Styling */
    .stButton > button.sub-tab-btn {
        background-color: #1A1A1A !important;
        color: #888 !important;
        padding: 4px 20px !important;
        border-radius: 15px !important;
        font-size: 12px !important;
        border: none !important;
        height: auto !important;
        width: auto !important;
        margin-left: 10px !important;
    }

    .stButton > button.sub-tab-active {
        background-color: #E2FF00 !important;
        color: black !important;
    }

    /* Post Card Grid Styling */
    .card-container {
        background-color: #111111;
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #222222;
        margin-bottom: 20px;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .card-container:hover {
        transform: translateY(-5px);
        border-color: #E2FF00;
    }

    .card-image {
        height: 200px;
        background-size: cover;
        background-position: center;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        background-color: #050505; 
        position: relative;
    }

    .card-overlay {
        background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.4) 70%, transparent 100%);
        padding: 15px;
        width: 100%;
    }

    .post-title {
        font-weight: bold;
        font-size: 15px;
        line-height: 1.3;
        margin-bottom: 4px;
        color: #FFFFFF;
    }

    .post-content-preview {
        color: #888;
        font-size: 11px;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-footer {
        background-color: #0F0F0F;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-top: 1px solid #1A1A1A;
    }

    /* Modal / Detail View Styling (Replica of the Commission UI) */
    .detail-container {
        background-color: #151515;
        border: 2px solid #333;
        border-radius: 20px;
        padding: 0;
        overflow: hidden;
        margin-top: 20px;
    }

    .detail-header {
        background-color: #222;
        padding: 15px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #333;
    }

    .detail-body {
        display: flex;
        height: 500px;
    }

    .detail-left {
        flex: 1;
        padding: 30px;
        border-right: 1px solid #333;
        overflow-y: auto;
    }

    .detail-right {
        width: 350px;
        background-color: #0A0A0A;
        display: flex;
        flex-direction: column;
    }

    .comment-section {
        flex: 1;
        overflow-y: auto;
        padding: 20px;
    }

    .comment-item {
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid #1A1A1A;
    }

    .comment-author {
        font-weight: bold;
        font-size: 12px;
        color: #E2FF00;
        display: flex;
        justify-content: space-between;
    }

    .comment-text {
        font-size: 12px;
        color: #DDD;
        margin-top: 5px;
    }

    .floor-badge {
        background: #333;
        color: #888;
        font-size: 10px;
        padding: 2px 6px;
        border-radius: 4px;
    }

    .author-avatar {
        width: 22px;
        height: 22px;
        background-color: #E2FF00;
        border-radius: 50%;
        display: inline-block;
    }

    /* Input Styling */
    .stTextArea textarea, .stTextInput input {
        background-color: #0A0A0A !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 10px !important;
    }
    
    .stButton button.main-action-btn {
        background-color: #E2FF00 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
    }

    </style>
""", unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "author": "r/NewEriduNews", 
            "title": "Obsidian Blade: Strategic Eradication", 
            "content": "Hollow activity has drastically diminished. Maximum alert level has now been temporarily lifted! I am the captain of a mercenary troupe hired by Obsidian Division. Hollow activity has crossed the warning threshold, and Obsidian Division have adopted the most extreme suppression program: Indiscriminate extermination of all living things inside...",
            "faction": "General", 
            "image": None,
            "replies": [
                {"author": "Kitty_Freak", "text": "That's terrifying... I'm keeping well away from the Hollows for now!"},
                {"author": "Fantastical_Balut", "text": "There's no room for argument with Obsidian Division... *sigh* It is what it is though."},
                {"author": "Doomed_Once_Daily", "text": "Doesn't really sound as though OP has any choice..."},
                {"author": "ThreeSeven", "text": "Who would dream of taking on such a commission?"}
            ]
        },
        {
            "id": 2,
            "author": "r/politics", 
            "title": "Trump issues warning to Iran", 
            "content": "Trump Vows To Strike Civilian Infrastructure... World leaders express concern as tensions rise in the region. Global markets react with volatility.",
            "faction": "General", 
            "image": None,
            "replies": [
                {"author": "Anon99", "text": "This frequency is for Hollow intel, why is this here?"},
                {"author": "HistoryBuff", "text": "Significant if true, but check your sources."}
            ]
        },
        {
            "id": 3,
            "author": "Neon_Rabbit", 
            "title": "[Question] Proxy Must-Knows: Carrots", 
            "content": "Does anyone have a reliable map for the shifting grid in the industrial sector? The standard carrots are failing me.",
            "faction": "Help Request Info", 
            "image": None,
            "replies": []
        },
        {
            "id": 4,
            "author": "Ghost_In_The_Hollow", 
            "title": "Vision's shocking scandal exposed!", 
            "content": "Evidence of corruption in the Sixth Street sector has surfaced... Perlman is going to jail! Charles Perlman, chief of logistics, found guilty.",
            "faction": "General", 
            "image": None,
            "replies": [
                {"author": "StreetSmart", "text": "Finally some justice on 6th street."}
            ]
        }
    ]

if "selected_post" not in st.session_state:
    st.session_state.selected_post = None

if "current_filter" not in st.session_state:
    st.session_state.current_filter = "All"

# --- NAVIGATION ---
st.markdown("""
    <div class="nav-container">
        <div class="nav-item">Notifications</div>
        <div class="nav-item nav-item-active">Intel Board</div>
        <div class="nav-item">Schedule</div>
    </div>
""", unsafe_allow_html=True)

# --- TABS ---
sub_nav_cols = st.columns([1, 1, 1, 1, 4])
with sub_nav_cols[1]:
    if st.button("All", key="tab_all", class_name="sub-tab-active sub-tab-btn" if st.session_state.current_filter == "All" else "sub-tab-btn"):
        st.session_state.current_filter = "All"
        st.session_state.selected_post = None
        st.rerun()
with sub_nav_cols[2]:
    if st.button("General", key="tab_general", class_name="sub-tab-active sub-tab-btn" if st.session_state.current_filter == "General" else "sub-tab-btn"):
        st.session_state.current_filter = "General"
        st.session_state.selected_post = None
        st.rerun()
with sub_nav_cols[3]:
    if st.button("Help Info", key="tab_help", class_name="sub-tab-active sub-tab-btn" if st.session_state.current_filter == "Help Request Info" else "sub-tab-btn"):
        st.session_state.current_filter = "Help Request Info"
        st.session_state.selected_post = None
        st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛰️ TRANSMISSION")
    st.markdown(f"**Logon Status:** `Anonymous User`")
    new_title = st.text_input("Title")
    new_content = st.text_area("Content", placeholder="Broadcast a message...")
    post_category = st.selectbox("Category", ["General", "Help Request Info"])
    if st.button("SEND SIGNAL", class_name="main-action-btn"):
        if new_content.strip() and new_title.strip():
            st.session_state.posts.insert(0, {
                "id": random.randint(1000, 9999),
                "author": "Anonymous User",
                "title": new_title,
                "content": new_content,
                "faction": post_category,
                "image": None,
                "replies": []
            })
            st.rerun()

# --- MAIN FEED / DETAIL VIEW ---
if st.session_state.selected_post:
    # DETAIL VIEW (Modal Replica)
    post = st.session_state.selected_post
    
    if st.button("← Back to Feed", key="back_btn"):
        st.session_state.selected_post = None
        st.rerun()

    st.markdown(f"""
        <div class="detail-container">
            <div class="detail-header">
                <div style="display:flex; align-items:center; gap:15px;">
                    <div class="author-avatar"></div>
                    <span style="font-weight:bold; color:#E2FF00;">{post['author']}</span>
                </div>
                <div style="color:#666; font-size:12px;">POST ID: {post['id']}</div>
            </div>
            <div class="detail-body">
                <div class="detail-left">
                    <h2 style="color:#E2FF00; margin-bottom:20px;">{post['title']}</h2>
                    <p style="line-height:1.6; color:#BBB; font-size:14px;">{post['content']}</p>
                    <div style="margin-top:40px; padding:20px; border:1px dashed #333; border-radius:10px; text-align:center; color:#555;">
                        [ End of Transmission Content ]
                    </div>
                </div>
                <div class="detail-right">
                    <div class="comment-section">
                        <div style="font-size:10px; color:#444; margin-bottom:15px; letter-spacing:2px; text-transform:uppercase;">Thread Replies</div>
    """, unsafe_allow_html=True)
    
    for i, reply in enumerate(post['replies']):
        st.markdown(f"""
            <div class="comment-item">
                <div class="comment-author">
                    <span>{reply['author']}</span>
                    <span class="floor-badge">{i+1}F</span>
                </div>
                <div class="comment-text">{reply['text']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Reply box inside detail view
    with st.container():
        reply_text = st.text_input("Add a reply...", key="reply_box", label_visibility="collapsed")
        if st.button("Post Reply", key="submit_reply"):
            if reply_text:
                post['replies'].append({"author": "Anonymous User", "text": reply_text})
                st.rerun()
    
    st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # GRID VIEW
    display_posts = st.session_state.posts
    if st.session_state.current_filter != "All":
        display_posts = [p for p in st.session_state.posts if p.get('faction') == st.session_state.current_filter]

    cols = st.columns(3)
    for idx, post in enumerate(display_posts):
        col_idx = idx % 3
        with cols[col_idx]:
            # Create a clickable card using a button trick or just rendering
            st.markdown(f"""
                <div class="card-container">
                    <div class="card-image">
                        <div class="card-overlay">
                            <div class="post-title">{post['title']}</div>
                            <div class="post-content-preview">{post['content']}</div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <div class="author-avatar"></div>
                        <span class="author-name">{post['author']}</span>
                        <span class="author-suffix">以及更多</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Simple button to 'open' the post since we can't capture div clicks in pure Streamlit easily
            if st.button(f"View Transmission {post['id']}", key=f"view_{post['id']}", use_container_width=True):
                st.session_state.selected_post = post
                st.rerun()

# Footer
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 20px; color: #444; font-size: 10px;">
        UID: 1302948125 📶
    </div>
""", unsafe_allow_html=True)
