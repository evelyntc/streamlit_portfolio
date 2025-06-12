import streamlit as st
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="evelyntc portfolio", layout="wide")

# --- Top Navigation Bar ---
st.markdown(
    """
    <style>
    .top-nav {
        display: flex;
        justify-content: flex-end;
        padding: 20px 40px 0 0;
        background-color: transparent;
    }
    .top-nav a {
        margin-left: 30px;
        text-decoration: none;
        font-weight: 500;
        color: white;
        font-size: 18px;
    }
    .top-nav a:hover {
        color: #cccccc;
    }
    </style>
    <div class="top-nav">
        <a href="?section=about">About Me</a>
        <a href="?section=projects">Projects</a>
        <a href="?section=resume">Resume & Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Section Handling ---
query_params = st.query_params
section = query_params.get("section", "about")

# --- ABOUT SECTION ---
if section == "about":
    st.title("Hi, I'm Evelyn")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("headshot.png", width=250)
    with col2:
        st.markdown("""
            <div style="
                background-color: #FAF0ED;
                padding: 16px;
                border-radius: 10px;
                border-left: 6px solid #EDE7E3;
                font-size: 16px;
                color: #000000;
            ">
            <p>
            I’m a data analyst who sits at the intersection of data and business.
            I love working with data and translating it into clear, actionable insights through compelling storytelling.
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.subheader("That's the short version though... It didn't start this way. Here's the whole story ⤵️")

    timeline_entries = [
        {
            "year": "2011",
            "title": "Joined Disney",
            "desc": "Worked across Attractions, Entertainment, Resorts, and Guest Research.",
            "img": "https://via.placeholder.com/600x200?text=Disney"
        },
        {
            "year": "2014",
            "title": "Graduated UCF",
            "desc": "Earned a Bachelor's degree in Marketing.",
            "img": "https://via.placeholder.com/600x200?text=UCF+Graduation"
        },
        {
            "year": "2015–2018",
            "title": "Exploration & Discovery",
            "desc": "Figured out what comes next, attended Disney Data Conference.",
            "img": "https://via.placeholder.com/600x200?text=Analytics+Conference"
        },
        {
            "year": "2021",
            "title": "Master’s in Data Science",
            "desc": "Graduated and dove deep into Python, SQL, and analytics.",
            "img": "https://via.placeholder.com/600x200?text=Graduated+M.S.+in+Data+Science"
        },
        {
            "year": "2023",
            "title": "Sr. Consumer Insights Analyst",
            "desc": "Blending business and data to understand consumer behavior.",
            "img": "https://via.placeholder.com/600x200?text=Consumer+Insights"
        },
    ]

    st.markdown("## 📍 Career Timeline")
    for item in timeline_entries:
        with st.expander(f"**{item['year']} — {item['title']}**", expanded=False):
            st.image(item["img"], use_column_width=True)
            st.write(item["desc"])

# --- PROJECTS SECTION ---
elif section == "projects":
    st.header("🚧 Projects Under Construction 🚧")
    st.write("This section is still under construction. In the meantime, here are a few links:")
    st.markdown("[Grad School Portfolio](https://evelyntc.github.io/Portfolio/projects.html)  \n"
                "[Medium Blog](https://evelyntc.medium.com/)")

# --- RESUME SECTION ---
elif section == "resume":
    st.header("📝 Resume & Contact")
    drive_file_id = "1OUIPE0JB5_5-wsiJMeQlj5QAQaZZVG2z"
    embed_link = f"https://drive.google.com/file/d/{drive_file_id}/preview"
    components.iframe(embed_link, height=800)
    st.write("[Connect with me on LinkedIn](https://linkedin.com/in/evelyntcates)")

# --- STATCOUNTER ---
st.markdown("""
<!-- Statcounter Code -->
<script type="text/javascript">
var sc_project=13141013; 
var sc_invisible=1; 
var sc_security="1e0c10d8"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="web counter"
href="https://statcounter.com/" target="_blank"><img
class="statcounter"
src="https://c.statcounter.com/13141013/0/1e0c10d8/1/"
alt="web counter"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
""", unsafe_allow_html=True)
