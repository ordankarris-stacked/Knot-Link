import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & THEMING ---
st.set_page_config(
    page_title="KNOT-LINK // PHAETHON GATEWAY",
    page_icon="🟠",
    layout="wide"
)

# Initialize Session State for Filter, Posts, and Active Post (for modal view)
if 'filter' not in st.session_state:
    st.session_state.filter = "All"

if 'active_post_id' not in st.session_state:
    st.session_state.active_post_id = None

if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "author": "r/politics",
            "title": "Trump issues warning to Iran",
            "content": "Trump Vows To Strike Civilian Infrastructure if threats continue. Tensions rise in the region as diplomatic efforts stall.",
            "img": "https://picsum.photos/seed/trump/400/300",
            "category": "General",
            "replies": [
                {"user": "Citizen_X", "text": "This is getting serious..."},
                {"user": "GlobalWatcher", "text": "Hoping for a peaceful resolution."}
            ]
        },
        {
            "id": 2,
            "author": "Obsidian_Blade",
            "title": "[Commission] Obsidian: Strategic Eradication",
            "content": "Hollow activity has drastically diminished. Maximum alert level has now been temporarily lifted! I am the captain of a mercenary troupe...",
            "img": "https://picsum.photos/seed/obsidian/400/300",
            "category": "Help Request Info",
            "replies": [
                {"user": "Kitty_Freak", "text": "That's terrifying... I'm keeping well away from the Hollows for now!"},
                {"user": "Fantastical_Balut", "text": "There's no room for argument with Obsidian Division... *sigh*"},
                {"user": "Doomed_Once_Daily", "text": "Doesn't really sound as though OP has any choice..."},
                {"user": "ThreeSeven", "text": "Who would dream of taking on such a commission"}
            ]
        },
        {
            "id": 3,
            "author": "r/worldnews",
            "title": "US rescues missing pilot",
            "content": "U.S. forces rescue second crew member after a daring overnight operation in hostile territory.",
            "img": "https://picsum.photos/seed/pilot/400/300",
            "category": "General",
            "replies": []
        },
        {
            "id": 4,
            "author": "r/spaceporn",
            "title": "New Artemis II photos",
            "content": "New Image from NASA: For the first time, we see the far side of the moon in high definition.",
            "img": None,
            "category": "General",
            "replies": [{"user": "StarGazer", "text": "Simply breathtaking."}]
        },
        {
            "id": 5,
            "author": "MetisIntelligence",
            "title": "[News] Vision's shocking scandal exposed",
            "content": "Charles Perlman, chief executive of Vision Corp, was caught in a fraud scheme involving hollow-tech smuggling.",
            "img": "https://picsum.photos/seed/vision/400/300",
            "category": "Help Request Info",
            "replies": []
        }
    ]

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background-color: #0d0d0d;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
    }

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
        background: #f0e600;
        color: #000000;
        border: none;
    }

    .knot-card {
        background-color: #1a1a1a;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 20px;
        border: 1px solid #222;
        transition: transform 0.2s ease;
        cursor: pointer;
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
        background-color: #000;
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

    /* Modal Overlay Styling */
    .modal-overlay {
        background-color: rgba(0,0,0,0.85);
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #444;
    }
    .reply-item {
        background: #222;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 3px solid #f0e600;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("""
    <div class="top-nav">
        <div class="nav-item active">Notifications</div>
        <div class="nav-item">Intel Board</div>
        <div class="nav-item">Schedule</div>
    </div>
""", unsafe_allow_html=True)

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

# --- MODAL VIEW (If a post is selected) ---
if st.session_state.active_post_id:
    post = next((p for p in st.session_state.posts if p["id"] == st.session_state.active_post_id), None)
    if post:
        st.markdown("---")
        m_col1, m_col2 = st.columns([1, 1])
        
        with m_col1:
            if post["img"]:
                st.image(post["img"], use_container_width=True)
            else:
                st.markdown("<div style='height:300px; background:#000; border-radius:10px; display:flex; align-items:center; justify-content:center;'>NO SIGNAL</div>", unsafe_allow_html=True)
            st.subheader(post["title"])
            st.write(post["content"])
            if st.button("CLOSE THREAD"):
                st.session_state.active_post_id = None
                st.rerun()

        with m_col2:
            st.markdown("### Replies")
            for reply in post["replies"]:
                st.markdown(f"""
                    <div class="reply-item">
                        <strong style="color:#f0e600; font-size:0.8rem;">{reply['user']}</strong><br>
                        <span style="font-size:0.9rem;">{reply['text']}</span>
                    </div>
                """, unsafe_allow_html=True)
            
            with st.form("reply_form", clear_on_submit=True):
                reply_text = st.text_input("Add a reply...")
                if st.form_submit_button("REPLY"):
                    if reply_text:
                        post["replies"].append({"user": "Anonymous User", "text": reply_text})
                        st.rerun()
        st.markdown("---")

# --- MAIN GRID ---
display_posts = st.session_state.posts
if st.session_state.filter != "All":
    display_posts = [p for p in st.session_state.posts if p.get("category") == st.session_state.filter]

if not display_posts:
    st.info(f"No posts found in category: {st.session_state.filter}")
else:
    cols = st.columns(3)
    for idx, post in enumerate(display_posts):
        image_url = post.get('img')
        image_style = f"background-image: url('{image_url}');" if image_url else ""
        
        with cols[idx % 3]:
            # Container for post
            st.markdown(f"""
                <div class="knot-card">
                    <div class="card-image" style="{image_style}"></div>
                    <div class="card-content">
                        <div class="author-info">
                            <div class="avatar">👤</div>
                            <span style="font-size: 0.75rem; font-weight: bold; color: #aaa;">{post.get('author', 'Unknown')}</span>
                        </div>
                        <div class="card-title">{post.get('title', 'No Title')}</div>
                        <div class="card-preview">{post.get('content', '')[:60]}...</div>
                        <div style="font-size:0.7rem; color:#f0e600; margin-top:10px;">💬 {len(post['replies'])} Replies</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Read Thread ##{post['id']}", key=f"btn_{post['id']}", use_container_width=True):
                st.session_state.active_post_id = post['id']
                st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<h2 style="font-family: Orbitron; color: #f0e600;">KNOT-LINK</h2>', unsafe_allow_html=True)
    st.write("---")
    with st.form("new_post", clear_on_submit=True):
        st.write("Create New Thread")
        new_title = st.text_input("Title")
        new_content = st.text_area("Description")
        new_category = st.selectbox("Category", ["General", "Help Request Info"])
        new_img_seed = st.text_input("Image Keyword", "")
        submitted = st.form_submit_button("PUBLISH")
        
        if submitted and new_title:
            final_img = f"https://picsum.photos/seed/{new_img_seed}/400/300" if new_img_seed.strip() else None
            new_id = max([p["id"] for p in st.session_state.posts]) + 1
            new_post = {
                "id": new_id,
                "author": "Anonymous User",
                "title": new_title,
                "content": new_content,
                "img": final_img,
                "category": new_category,
                "replies": []
            }
            st.session_state.posts.insert(0
