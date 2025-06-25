import streamlit as st
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="evelyntc portfolio")

pages = [
    st.Page(page="welcome.py", title="Welcome", icon=":material/home:", default=True),
    st.Page(page="portfolio.py", title="Portfolio", icon=":material/folder:"),
    st.Page(page="articles.py", title="Articles", icon=":material/article:"),
]


navigation = st.navigation(pages=pages, position="top", expanded=True)
social_icons = st.columns((4, 3))

with social_icons[1]:
    linkedin, medium, github = st.columns(3)
    with linkedin:
        st.page_link(
            "https://www.linkedin.com/in/evelyntcates/",
            label="LinkedIn",
            icon=":material/link:",
        )
    with medium:
        st.page_link(
            "https://evelyntc.medium.com/",
            label="Medium",
            icon=":material/link:",
        )
    with github:
        st.page_link(
            "https://github.com/evelyntc",
            label="GitHub",
            icon=":material/link:",
        )
navigation.run()

# --- STATCOUNTER ---
st.html(
    """
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
""",
)
