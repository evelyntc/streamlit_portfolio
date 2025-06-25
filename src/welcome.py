import streamlit as st
from pydantic import BaseModel
from typing import Optional
import json


class TimelineEntry(BaseModel):
    year: int
    title: str
    desc: str
    img: Optional[str] = ""


class TimelineEntries(BaseModel):
    entries: list[TimelineEntry]


def timeline_change(next: int):
    st.session_state["current_timeline"] = next


st.set_page_config(layout="centered")


st.title("Hi, I'm Evelyn")
photo, welcome_msg = st.columns((1, 2.5), vertical_alignment="center")
with photo:
    st.image("images/headshot.png")
with welcome_msg:
    st.write(
        """ 🎬 Hi, I’m Evelyn. A data analyst with a deep love for entertainment and a sharp eye for sentiment. I specialize in uncovering how people feel, act, and engage with media from theme parks to movie reviews. With a background rooted in guest experience and consumer research, I bring data to life through clear, actionable insights and approachable storytelling.
Whether I’m analyzing audience sentiment, designing dashboards, or simplifying complex findings, I’m most energized when helping teams understand their users and make confident, human-centered decisions.
"""
    )

st.subheader(
    "That's the short version though... It didn't start this way. Here's the whole career journey :material/arrow_downward:",
    anchor=False,
)
if "timeline_data" not in st.session_state:
    with open("src/timeline_entries.json", "r") as te:
        st.session_state["timeline_data"] = json.loads(te.read()).get("entries")


timeline_entries = (
    TimelineEntries(
        entries=[
            TimelineEntry(
                year=i.get("year"),
                title=i.get("title"),
                desc=i.get("desc"),
                img=i.get("img"),
            )
            for i in st.session_state["timeline_data"]
        ]
    )
    .model_dump()
    .get("entries")
)


def timeline_object(data: dict):
    with st.container(border=True):
        year, info = st.columns((1, 4), vertical_alignment="top")
        with year:
            st.header(data.get("year"), anchor=False)
            st.image(data.get("img"))
        with info:
            st.subheader(rf"**{data.get('title')}**", anchor=False, divider=True)
            st.write(data.get("desc"))


if "current_timeline" not in st.session_state:
    st.session_state["current_timeline"] = 0

max_timelines = len(timeline_entries) - 1
prev, data, nxt = st.columns((0.5, 4, 0.5), vertical_alignment="center")


with prev:
    st.button(
        "",
        icon=":material/arrow_back:",
        disabled=st.session_state["current_timeline"] == 0,
        on_click=timeline_change,
        args=[st.session_state["current_timeline"] - 1],
    )
with data:
    timeline_object(data=timeline_entries[st.session_state["current_timeline"]])

with nxt:
    st.button(
        "",
        icon=":material/arrow_forward:",
        disabled=st.session_state["current_timeline"] == max_timelines,
        on_click=timeline_change,
        args=[st.session_state["current_timeline"] + 1],
    )
