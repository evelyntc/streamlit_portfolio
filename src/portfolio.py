import streamlit as st
from pydantic import BaseModel
from typing import Optional
import numpy as np

st.set_page_config(layout="wide")
st.title("Portfolio")


class PortfolioProject(BaseModel):
    title: str
    url: Optional[str] = ""
    description: str


class PortolioCollection(BaseModel):
    projects: list[PortfolioProject]


portfolio = PortolioCollection(
    projects=[
        PortfolioProject(
            title="Bad Bunny Spotify Music Analysis",
            url="https://badbunnydashboard.streamlit.app/",
            description="Streamlit dashboard highlighting the artists music stream data",
        ),
        PortfolioProject(
            title="Sample Project Two",
            url="https://google.com",
            description="Sample Project two description",
        ),
        PortfolioProject(
            title="Sample Project Three",
            url="https://google.com",
            description="Sample Project 3 description",
        ),
        PortfolioProject(
            title="Sample Project Four",
            url="https://google.com",
            description="Sample Project 4 description",
        ),
    ]
)


def project_card(data: dict):
    with st.container(border=True):
        st.subheader(data.get("title"), anchor=False, divider=True)
        st.write(data.get("description"))
        st.link_button("", icon=":material/link:", url=data.get("url"))


projects_list = portfolio.model_dump().get("projects")
project_count = len(projects_list)
columns = 3
rows = int(project_count / columns + 1)
matrix = columns * rows
if project_count < matrix:
    blanks = [False for i in range(int(matrix) - int(project_count))]
    projects_list.extend(blanks)
portfolio_map = np.arange(matrix).reshape(rows, columns)
for row in portfolio_map:
    row_col = st.columns(columns)
    for index, col in enumerate(row):
        if projects_list[col]:
            with row_col[index]:
                project_card(data=projects_list[col])
