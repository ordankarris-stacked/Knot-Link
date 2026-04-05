import streamlit as st
import time

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="KNOT-LINK // GATEWAY",
    page_icon="🟠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STATE MANAGEMENT ---
if 'filter' not in st.session_state:
    st.session_state.filter = "All"

if 'active_post_id' not in st.session_state:
    st.session_state.active_post_id = None

# Initial Post Data
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "author": "MetisIntelligence",
            "title": "[Post] Vision's shocking scandal exposed — Perlman is going to jail!",
            "content": "Charles Perlman, chief executive of Vision Corp, has been indicted on multiple counts of fraud and money laundering following a whistle-blower report.",
            "img": "https://images.unsplash.com/photo-1585829365234-781fdb509147?q=80&w=800",
            "category": "General",
            "replies": [
                {"user": "Proxy_X", "text": "Finally, justice for the workers."},
                {"user": "Anon99", "text": "I bet he has a backup plan."}
            ]
        },
        {
            "id": 2,
            "author": "Worrybot",
            "title": "A new Hollow on Fourteenth Street!",
            "content": "Observers report a sudden surge in Ether activity near the old subway entrance. Residents are advised to evacuate immediately.",
            "img": "https://images.unsplash.com/photo-1478720143022-10dca8de9cc1?q=80&w=800",
            "category": "General",
            "replies": [
                {"user": "Cpt_Safety", "text": "Avoid the area at all costs."}
            ]
        },
        {
            "id": 3,
            "author": "Friend2Proxy",
            "title": "[Info] Proxy Must-Knows: Carrots",
            "content": "Did you know that 'Carrots' aren't just for eating? In the Hollows, they refer to specialized navigational lures. Here is how to use them.",
            "img": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?q=80&w=800",
            "category": "Help Info",
            "replies": []
        },
        {
            "id": 4,
            "author": "gawadaw",
            "title": "[Question] How to quickly level up your IK account?",
            "content": "I've been stuck at Level 30 for weeks. Any high-yield commissions I should look out for?",
            "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800",
            "category": "Help Info",
            "replies": [
                {"user": "IK_Master", "text": "Focus on the daily login challenges and priority 'General' posts."}
            ]
        }
    ]

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    .stApp { background-color: #0d0d0d; color: #ffffff; font-family: 'JetBrains Mono', monospace; }
    
    /* Hide standard streamlit elements */
    header, footer { visibility: hidden; }

    /* Navigation Bar */
    .top-nav { display: flex; justify-content: flex-end; gap: 5px; margin-bottom: 20px; }
    
    /* Interactive Card Styling */
    .knot-card {
        background-color: #1a1a1a;
        border: 2px solid #333;
        border-radius: 15px;
        overflow: hidden;
        cursor: pointer;
        transition: 0.2s ease-in-out;
        margin-bottom: 10px;
        height: 420px;
        display: flex;
        flex-direction: column;
    }
    .knot-card:hover {
        border-color: #f0e600;
        background-color: #222;
        transform: scale(1.02);
    }
    
    .card-img {
        height: 200px;
        background-size: cover;
        background-position: center;
    }
    
    .card-body {
        padding: 15px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }

    .card-meta {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 0.75rem;
        color: #888;
        margin-bottom: 10px;
    }
    
    .avatar-circle {
        width: 24px; height: 24px; background: #444; border-radius: 50%;
    }

    .card-title {
        font-weight: bold;
        font-size: 1rem;
        line-height: 1.3;
        margin-bottom: 10px;
        color: #fff;
    }

    .card-preview {
        font-size: 0.8rem;
        color: #aaa;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
    }

    /* Modal Styling */
    .detail-view {
        background: #151515;
        border: 1px solid #333;
        border-radius: 20px;
        padding: 30px;
    }
    
    .comment-thread {
        background: #1e1e1e;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
nav_col1, nav_col2 = st.columns([1, 1])

with nav_col2:
    st.markdown('<div class="top-nav">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("All", type="primary" if st.session_state.filter == "All" else "secondary", use_container_width=True):
            st.session_state.filter = "All"
            st.session_state.active_post_id = None
            st.rerun()
    with c2:
        if st.button("General", type="primary" if st.session_state.filter == "General" else "secondary", use_container_width=True):
            st.session_state.filter = "General"
            st.session_state.active_post_id = None
            st.rerun()
    with c3:
        if st.button("Help Info", type="primary" if st.session_state.filter == "Help Info" else "secondary", use_container_width=True):
            st.session_state.filter = "Help Info"
            st.session_state.active_post_id = None
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONTENT DISPLAY ---
if st.session_state.active_post_id:
    # --- POST DETAIL VIEW ---
    post = next((p for p in st.session_state.posts if p["id"] == st.session_state.active_post_id), None)
    
    if post:
        if st.button("⬅ Back to Board"):
            st.session_state.active_post_id = None
            st.rerun()
            
        st.markdown('<div class="detail-view">', unsafe_allow_html=True)
        col_img, col_txt = st.columns([1, 1.2])
        
        with col_img:
            st.image(post["img"], use_container_width=True)
        
        with col_txt:
            st.caption(f"Posted by {post['author']} • {post['category']}")
            st.title(post["title"])
            st.write(post["content"])
            
            st.markdown("---")
            st.subheader("Replies")
            for r in post["replies"]:
                st.markdown(f"**@{r['user']}**: {r['text']}")
            
            with st.form("comment_form", clear_on_submit=True):
                new_comment = st.text_input("Post a reply...", placeholder="Be helpful or get out.")
                if st.form_submit_button("REPLY") and new_comment:
                    post["replies"].append({"user": "You", "text": new_comment})
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- FEED VIEW ---
    filtered_posts = st.session_state.posts if st.session_state.filter == "All" else [p for p in st.session_state.posts if p["category"] == st.session_state.filter]
    
    cols = st.columns(3)
    for index, post in enumerate(filtered_posts):
        with cols[index % 3]:
            # The entire card is now the button
            st.markdown(f"""
                <div class="knot-card">
                    <div class="card-img" style="background-image: url('{post['img']}');"></div>
                    <div class="card-body">
                        <div class="card-meta">
                            <div class="avatar-circle"></div>
                            <span>{post['author']}</span>
                        </div>
                        <div class="card-title">{post['title']}</div>
                        <div class="card-preview">{post['content']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Invisible button overlaying the card logic
            if st.button("Open", key=f"post_{post['id']}", use_container_width=True, label_visibility="collapsed"):
                st.session_state.active_post_id = post["id"]
                st.rerun()

# --- SIDEBAR (Intel Stats) ---
with st.sidebar:
    st.markdown('<h2 style="color:#f0e600;">INTER-KNOT</h2>', unsafe_allow_html=True)
    st.metric("IK Level", "60", "MAX")
    st.write("---")
    st.markdown("### Active Comms")
    st.info("No active hollow emergencies in your immediate district.")
