import streamlit as st
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="evelyntc portfolio", layout="wide")

# --- Sidebar navigation ---
st.sidebar.title("Start Here ⤵️")
page = st.sidebar.selectbox("Go to", ["About Me", "Projects", "Resume & Contact"])

# --- About Me Page ---
if page == "About Me":
    st.title("Hi, I'm Evelyn")

    # --- Headshot and Intro ---
    col1, col2 = st.columns([1,3])
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
        I’m a data analyst who sits at the intersection of data and business. I love working with data and translating it into clear, actionable insights through compelling storytelling.
        <br><br>
        I'm passionate about people—understanding consumers, their experiences, and how they engage with products.
        </p>
        </div>
        """, unsafe_allow_html=True)
        st.subheader("That's the short version though... It didn't start this way. Here's the whole story ⤵️")

    # --- Journey Header ---
    st.markdown("- - - -")
    st.header("🚘 My Journey")

    # --- Timeline Data ---
    timeline = [
        {
            "year": "🏰 2011",
            "title": "Joined Disney",
            "desc": "Worked across teams in Attractions, Entertainment, Resorts, and Guest Research. Learned how to measure and improve experiences.",
        },
        {
            "year": "🎓 2014",
            "title": "Graduated with a Marketing Degree",
            "desc": "Started my journey in consumer behavior and branding.",
        },
        {
            "year": "🤔 2015-2018",
            "title": "Figuring out what comes next",
            "desc": "Explored various career paths before finding my passion in data.",
        },
        {
            "year": "📚 2021",
            "title": "Earned my Master’s in Data Science",
            "desc": "Decided to get technical—diving into Python, SQL, and analytics to build real insights.",
        },
        {
            "year": "🚀 Now",
            "title": "Data Analyst & Storyteller",
            "desc": "Today, I blend business context with technical skill to help companies understand their customers and make data-driven decisions.",
        },
    ]

    # --- Down Arrow Between Entries ---
    arrow_html = """
    <div style="text-align:center; font-size:32px; margin: -16px 0 16px 0;">⬇️</div>
    """

    # --- Display Timeline ---
    for i, item in enumerate(timeline):
        with st.container():
            st.markdown(f"""
                <div style="
                    border-left: 4px solid #E0D4C9;
                    padding: 16px;
                    margin-bottom: 20px;
                    background-color: #FFFCFA;
                    border-radius: 6px;
                    color: #000000;
                ">
                    <h4 style="margin-bottom: 0; color: #000000;">{item['year']} — {item['title']}</h4>
                    <p style="margin-top: 4px; color: #000000;">{item['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

        if i < len(timeline) - 1:
            st.markdown(arrow_html, unsafe_allow_html=True)
            st.markdown("<hr style='border-top: 1px dashed #CCC;'>", unsafe_allow_html=True)

# --- Projects Page ---
elif page == "Projects":
    st.title("🚧 Projects Under Construction 🚧")
    st.subheader("In the meantime, check out previous work I've done 👇")
    st.markdown("[Grad School Portfolio](https://evelyntc.github.io/Portfolio/projects.html) | [Medium Blog](https://evelyntc.medium.com/)")

# --- Resume & Contact Page ---
elif page == "Resume & Contact":
    st.title("📝 Resume & Contact")
    drive_file_id = "1OUIPE0JB5_5-wsiJMeQlj5QAQaZZVG2z"
    embed_link = f"https://drive.google.com/file/d/{drive_file_id}/preview"
    components.iframe(embed_link, height=800)

    st.info("📥 Want a copy? Feel free to contact me directly.")

    st.subheader("Contact")
    st.write("[Connect with me on LinkedIn](https://linkedin.com/in/evelyntcates)")
