import streamlit as st
from bs4 import BeautifulSoup
import feedparser
from pydantic import BaseModel
from textwrap import shorten

st.set_page_config(layout="centered")
st.title("Medium Articles")


class MediumArticle(BaseModel):
    title: str
    link: str
    published: str
    tags: list
    content: str


def get_medium_articles():
    """RSS Feed into Medium"""
    try:
        feed_url = "https://medium.com/feed/@evelyntc"
        feed = feedparser.parse(feed_url)
        arts = []
        for entry in feed.get("entries"):
            row = MediumArticle(
                title=entry.get("title"),
                link=entry.get("link", ""),
                published=entry.get("published"),
                tags=[tag.get("term") for tag in entry.get("tags", [])],
                content=BeautifulSoup(entry.get("summary"), "html.parser").get_text(),
            )
            arts.append(dict(row))
        return arts
    except Exception as e:
        st.error(f"Could not parse Medium feed {e}")
        return []


if "medium_articles" not in st.session_state:
    st.session_state["medium_articles"] = get_medium_articles()


def medium_card(data: dict):
    with st.container(border=True):
        st.subheader(data.get("title"), anchor=False, divider=True)
        st.caption(data.get("published"))
        st.write(shorten(data.get("content"), 100, placeholder=" ..."))
        st.link_button(
            "Read Article",
            icon=":material/link:",
            url=data.get("link"),
        )
        if tags := data.get("tags"):
            st.pills(
                "Tags",
                options=tags,
                disabled=True,
                key=shorten(data.get("title"), 20),
            )


for article in st.session_state["medium_articles"]:
    medium_card(data=article)
