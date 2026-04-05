import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & THEMING ---
st.set_page_config(
    page_title="KNOT-LINK // GATEWAY",
    page_icon="🟠",
    layout="wide"
)

# Initialize Session State for Filter, Posts, and Active Post (for modal view)
if 'filter' not in st.session_state:
    st.session_state.filter = "All"

if 'active_post_id' not in st.session_state:
    st.session_state.active_post_id = None

if 'posts' not in st.session_state:
    # Categories: "General", "Help Request Info"
    st.session_state.posts = [
        {
            "id": 1,
            "author": "Reuters_Global",
            "title": "[News] Federal Reserve signals potential rate cut in Q3",
            "content": "In a surprising move, the Federal Reserve Chair indicated that inflation targets are nearing the 2% threshold, suggesting a shift in monetary policy to support labor market stability.",
            "img": "https://picsum.photos/seed/finance/800/600",
            "category": "General",
            "replies": [
                {"user": "MarketWatcher", "text": "About time, the housing market needs some breathing room."},
                {"user": "EconStudent_99", "text": "Will this impact the dollar index significantly?"}
            ]
        },
        {
            "id": 2,
            "author": "TechCrunch_Official",
            "title": "[Tech] New generative AI model breaks benchmarks for reasoning",
            "content": "The latest model from leading research labs demonstrates unprecedented capabilities in mathematical proofing and complex coding tasks, raising questions about future software automation.",
            "img": "https://picsum.photos/seed/ai_robot/800/600",
            "category": "Help Request Info",
            "replies": [
                {"user": "Dev_Lead", "text": "I tried the beta, the context window is actually insane."},
                {"user": "Privacy_First", "text": "What about the training data transparency?"}
            ]
        },
        {
            "id": 3,
            "author": "Climate_Monitor",
            "title": "[Alert] Record-breaking heatwave predicted for Northern Hemisphere",
            "content": "Meteorologists warn that El Niño patterns combined with rising sea surface temperatures will likely lead to the hottest summer on record for North America and Europe.",
            "img": "https://picsum.photos/seed/weather/800/600",
            "category": "General",
            "replies": []
        },
        {
            "id": 5,
            "author": "CyberSecurity_Net",
            "title": "[Security] Critical vulnerability found in widely used open-source library",
            "content": "Security researchers have identified a zero-day exploit in the standard logging library used by 70% of enterprise web applications. Patching is required immediately.",
            "img": "https://picsum.photos/seed/security/800/600",
            "category": "Help Request Info",
            "replies": [{"user": "SysAdmin_Pro", "text": "Coffee is going to be my best friend tonight while I patch these servers."}]
        },
        {
            "id": 6,
            "author": "r/politics",
            "title": "Trump issues warning to Iran regarding maritime trade",
            "content": "Donald Trump Vows To Strike Civilian Infrastructure if regional threats continue to escalate. Tensions rise in the region as diplomatic efforts face new challenges.",
            "img": "https://picsum.photos/seed/trump/800/600",
            "category": "General",
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

    /* Main Navigation Styling */
    .top-nav {
        display: flex;
        justify-content: flex-end;
        gap: 0px;
        margin-bottom: 20px;
        padding: 10px 0;
        background: transparent;
    }
    .nav-item {
        background: transparent;
        color: #ffffff;
        padding: 10px 40px;
        font-weight: bold;
        font-style: italic;
        text-transform: none;
        font-size: 1.2rem;
        font-family: 'Orbitron', sans-serif;
        border-radius: 30px;
        margin-left: -15px;
        transition: 0.3s;
    }
    .nav-item.active {
        background: #f0e600;
        color: #000000;
        z-index: 2;
    }

    /* Post Cards - Image Overlay Style */
    .knot-card {
        position: relative;
        height: 350px;
        background-color: #1a1a1a;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 20px;
        border: 2px solid #222;
        transition: transform 0.2s ease, border-color 0.2s;
    }
    .knot-card:hover {
        transform: scale(1.02);
        border-color: #f0e600;
    }
    
    .card-bg {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-size: cover;
        background-position: center;
        z-index: 1;
    }

    .card-overlay {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);
        z-index: 2;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }

    .author-tag {
        display: flex;
        align-items: center; gap: 8px; background: rgba(0,0,0,0.7);
        padding: 4px 10px; border-radius: 15px; width: fit-content;
        margin-bottom: 10px; border: 1px solid #444;
    }
    
    .avatar-mini {
        width: 18px; height: 18px; background: #f0e600; border-radius: 50%;
    }

    .card-title {
        font-weight: bold; font-size: 1.05rem; line-height: 1.2;
        margin-bottom: 5px; color: #ffffff;
    }
    .card-preview {
        font-size: 0.8rem; color: #bbb; line-height: 1.3;
        max-height: 3.9em; overflow: hidden;
    }

    .reply-item {
        background: #151515; padding: 15px; border-radius: 10px;
        margin-bottom: 12px; border-left: 4px solid #f0e600;
        font-family: 'JetBrains Mono', monospace;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION BAR ---
st.markdown("""
    <div class="top-nav">
        <div class="nav-item active">Notifications</div>
        <div class="nav-item">Intel Board</div>
        <div class="nav-item">Schedule</div>
    </div>
""", unsafe_allow_html=True)

# Sub-Category Filter
filter_cols = st.columns([5, 1, 1, 1])
with filter_cols[1]:
    if st.button("All", key="btn_all", use_container_width=True, type="primary" if st.session_state.filter == "All" else "secondary"):
        st.session_state.filter = "All"
        st.rerun()
with filter_cols[2]:
    if st.button("General", key="btn_gen", use_container_width=True, type="primary" if st.session_state.filter == "General" else "secondary"):
        st.session_state.filter = "General"
        st.rerun()
with filter_cols[3]:
    if st.button("Help Info", key="btn_help", use_container_width=True, type="primary" if st.session_state.filter == "Help Request Info" else "secondary"):
        st.session_state.filter = "Help Request Info"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# --- MODAL VIEW (Post Detail) ---
if st.session_state.active_post_id:
    post = next((p for p in st.session_state.posts if p["id"] == st.session_state.active_post_id), None)
    if post:
        st.markdown("""<div style="background:#111; padding:20px; border-radius:15px; border:1px solid #333;">""", unsafe_allow_html=True)
        m_col1, m_col2 = st.columns([1.2, 1])
        
        with m_col1:
            img_val = post.get("img", "https://picsum.photos/seed/err/800/600")
            st.image(img_val, use_container_width=True)
            st.title(post.get("title", "Untitled"))
            st.write(post.get("content", "No content available."))
            if st.button("← BACK TO LIST", key="back_btn", use_container_width=True):
                st.session_state.active_post_id = None
                st.rerun()

        with m_col2:
            replies = post.get('replies', [])
            st.markdown(f"### 💬 Replies ({len(replies)})")
            for reply in replies:
                st.markdown(f"""
                    <div class="reply-item">
                        <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                            <span style="color:#f0e600; font-weight:bold;">@{reply['user']}</span>
                            <span style="color:#666; font-size:0.7rem;">Verified Member</span>
                        </div>
                        <div style="color:#eee; font-size:0.9rem;">{reply['text']}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with st.form("reply_form", clear_on_submit=True):
                reply_text = st.text_input("Comment...", placeholder="Type your message here...")
                if st.form_submit_button("POST REPLY"):
                    if reply_text:
                        post["replies"].append({"user": "WebUser_714", "text": reply_text})
                        st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN GRID ---
display_posts = st.session_state.posts
if st.session_state.filter != "All":
    display_posts = [p for p in st.session_state.posts if p.get("category") == st.session_state.filter]

if not display_posts:
    st.info(f"No threads found in '{st.session_state.filter}'")
else:
    cols = st.columns(3)
    for idx, post in enumerate(display_posts):
        post_id = post.get('id', idx)
        image_url = post.get('img', 'https://picsum.photos/seed/default/800/600')
        author = post.get('author', 'Unknown')
        title = post.get('title', 'Untitled Thread')
        content = post.get('content', '')
        
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="knot-card">
                    <div class="card-bg" style="background-image: url('{image_url}');"></div>
                    <div class="card-overlay">
                        <div class="author-tag">
                            <div class="avatar-mini"></div>
                            <span style="font-size: 0.7rem; font-weight: bold; color: #fff;">{author}</span>
                        </div>
                        <div class="card-title">{title}</div>
                        <div class="card-preview">{content[:75]}...</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"OPEN THREAD ##{post_id}", key=f"read_{post_id}_{idx}", use_container_width=True):
                st.session_state.active_post_id = post_id
                st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<h1 style="font-family: Orbitron; color: #f0e600; letter-spacing: 2px;">KNOT-LINK</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #888; font-size: 0.8rem;">ADMINISTRATIVE CONSOLE</p>', unsafe_allow_html=True)
    st.write("---")
    
    with st.form("new_post", clear_on_submit=True):
        st.write("PUBLISH NEW INTEL")
        new_title = st.text_input("Report Title")
        new_content = st.text_area("Intel Summary")
        new_category = st.selectbox("Assign Category", ["General", "Help Request Info"])
        new_img_keyword = st.text_input("Visual Seed (Keyword)")
        submitted = st.form_submit_button("BROADCAST")
        
        if submitted and new_title:
            final_img = f"https://picsum.photos/seed/{new_img_keyword}/800/600" if new_img_keyword.strip() else "https://picsum.photos/seed/post/800/600"
            max_id = max([p["id"] for p in st.session_state.posts]) if st.session_state.posts else 0
            new_entry = {
                "id": max_id + 1,
                "author": "Verified Source",
                "title": new_title,
                "content": new_content,
                "img": final_img,
                "category": new_category,
                "replies": []
            }
            st.session_state.posts.insert(0, new_entry)
            st.rerun()

    st.write("---")
    st.markdown(f"""
        <div style="background: #111; padding: 15px; border-radius: 10px; border: 1px solid #333;">
            <div style="font-size: 0.7rem; color: #666;">LOGGED AS</div>
            <div style="color: #f0e600; font-weight: bold; font-family: Orbitron;">ANONYMOUS_OPERATOR</div>
            <div style="font-size: 0.7rem; color: #00ff00; margin-top: 5px;">● ENCRYPTION ACTIVE</div>
        </div>
    """, unsafe_allow_html=True)
