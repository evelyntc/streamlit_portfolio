import streamlit as st
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="evelyntc portfolio", layout="wide")

# --- Global Dark Mode ---
st.markdown(
    """
    <style>
    body {
        background-color: #000000 !important;
        color: white !important;
    }
    .stApp {
        background-color: #000000 !important;
        color: white !important;
    }
    .block-container {
        background-color: #000000 !important;
    }
    .css-1d391kg, .css-18e3th9 {
        background-color: #000000 !important;
    }
    .css-1cpxqw2, .stMarkdown {
        color: white !important;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
    }
    a {
        color: #EDE7E3 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
            background-color: #000000;
            padding: 16px;
            border-radius: 10px;
            border-left: 6px solid #EDE7E3;
            border-right: 6px solid #EDE7E3;
            font-size: 16px;
            color: #000000;
            margin-bottom: -10px;
        ">
        <p style="margin: 0;">
        🎬 Hi, I’m Evelyn. A data analyst with a deep love for entertainment and a sharp eye for sentiment. I specialize in uncovering how people feel, act, and engage with media from theme parks to movie reviews. With a background rooted in guest experience and consumer research, I bring data to life through clear, actionable insights and approachable storytelling.
        <br><br>
        Whether I’m analyzing audience sentiment, designing dashboards, or simplifying complex findings, I’m most energized when helping teams understand their users and make confident, human-centered decisions.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: -10px;">
        <h3 style="margin: 0;">
            That's the short version though... It didn't start this way. Here's the whole career journey ⤵️
        </h3>
    </div>
    """, unsafe_allow_html=True)

    timeline_entries = [
        {
            "year": "2011",
            "title": "Joined Disney",
            "desc": "Began my career working at Walt Disney World, working across Attractions, Entertainment, Resorts, and Guest Research. This is where I first became curious about how consumers interact with experiences and what becomes memorable during their vacation.",
            "img": ["nemo.jpeg"]
        },
        {
            "year": "2014",
            "title": "Got my first data job and graduated from University of Central Florida",
            "desc": "Started working in Revenue Mgmt doing data entry for resort inventory and I earned a Bachelor's degree in Marketing, where I gained a foundation in consumer behavior and brand strategy.",
            "img": ["welcome.jpeg", "ucfgrad.jpeg"]
        },
        {
            "year": "2015–2018",
            "title": "Exploration & Discovery",
            "desc": "Spent this period reconnecting with what I valued most—creativity, people, and storytelling. Attended the Disney Data & Analytics Conference, where I discovered a new path in data. This led me to diving into the world of data and getting my masters degree in data science.",
            "img": ["ddac16.jpg", "trad.jpeg"]
        },
        {
            "year": "2021",
            "title": "10 year work anniversary at Disney and got my Master’s in Data Science",
            "desc": "Graduated with a Master’s in Data Science from Bellevue University. Built a strong foundation in Python, SQL, and Data Storytelling. Also got my 10 year plaque at Disney!",
            "img": ["10yr.jpeg"]
        },
        {
            "year": "2023",
            "title": "Consumer Insights Sr. Analyst",
            "desc": "In my current role, I blend business strategy and data analytics to uncover what drives consumer decisions—translating complex data into actionable stories.",
            "img": ["https://via.placeholder.com/600x200?text=Consumer+Insights"]
        },
    ]

    st.markdown("## 📍 Career Timeline")

    for item in timeline_entries:
        with st.expander(f"**{item['year']} — {item['title']}**", expanded=False):
            images = item["img"] if isinstance(item["img"], list) else [item["img"]]
            columns = st.columns(len(images))
            for col, img_path in zip(columns, images):
                with col:
                    st.image(img_path, width=250)
                    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)
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
