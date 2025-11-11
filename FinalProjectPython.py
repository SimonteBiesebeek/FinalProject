import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path


import plotly


st.set_page_config("Final Project", layout="wide")
st.title("Final Project: Data Analysis and Visualization")

ROOT = Path(__file__).parent
df_merged = pd.read_csv(ROOT / "MergedDutchLeagueData.csv")
df_merged = pd.read_csv("MergedDutchLeagueData.csv")

ROOT = Path(__file__).parent
df_premier_merged = pd.read_csv(ROOT / "MergedPremierLeagueData.csv")
df_premier_merged = pd.read_csv("MergedPremierLeagueData.csv")
st.header("Project Introduction")



col_data, _, col_chart = st.columns((0.8, 0.05, 1))

with col_data:
    st.subheader("Raw Data")
    st.dataframe(df_merged)

with col_chart:
    st.subheader("Data Overview")
    st.markdown("Placeholder for chart")


with open("win_fig.pkl", "rb") as f:
    win_fig = pickle.load(f)

with open("loss_fig.pkl", "rb") as f:
    loss_fig = pickle.load(f)

# Display in Streamlit
st.plotly_chart(win_fig, use_container_width=True)
st.plotly_chart(loss_fig, use_container_width=True)

with open("win_fig.prem", "rb") as f:
    win_fig_prem = pickle.load(f)

with open("loss_fig.prem", "rb") as f:
    loss_fig_prem = pickle.load(f)

st.plotly_chart(win_fig_prem, use_container_width=True)
st.plotly_chart(loss_fig_prem, use_container_width=True)

with open("dominance_data.pkl", "rb") as f:
    data = pickle.load(f)

#graph shots/shots on target dominance

st.set_page_config(page_title="Football Dominance Map", layout="wide")
st.title("⚽ Football Dominance Map (2D)")
st.write("Visualizing how shooting dominance affects the chance of a home win.")

seasonal_data = data["seasonal_data"]
xx, yy, probs = data["xx"], data["yy"], data["probs"]

# --- Build the 2D plot ---
heatmap = go.Contour(
    x=xx[0],
    y=yy[:, 0],
    z=probs,
    colorscale='RdYlGn',
    opacity=0.85,
    contours=dict(showlabels=True),
    colorbar=dict(title="Home-Win<br>Probability"),
)

points = go.Scatter(
    x=seasonal_data["ShotDiff"],
    y=seasonal_data["ShotOnTargetDiff"],
    mode="markers",
    marker=dict(
        size=(seasonal_data["TotalShots"])**0.4 * 4,
        color=seasonal_data["HomeWin"],
        colorscale="RdYlGn",
        line=dict(width=1, color="white"),
        opacity=0.8,
        cmin=0, cmax=1
    ),
    text=[
        f"<b>{r}</b> — Shots Δ: {sd}, On Target Δ: {sotd}"
        for r, sd, sotd in zip(
            seasonal_data["FTR"],
            seasonal_data["ShotDiff"],
            seasonal_data["ShotOnTargetDiff"]
        )
    ],
    hoverinfo="text"
)

fig = go.Figure(data=[heatmap, points])

fig.update_layout(
    title="⚽  Football Dominance Map<br><sup>Shot & Shots-on-Target Difference vs Home-Win Probability</sup>",
    xaxis=dict(
        title="Shot Difference (Home − Away)",
        showgrid=True,
        zeroline=True,
        zerolinecolor="white",
    ),
    yaxis=dict(
        title="Shots-on-Target Difference (Home − Away)",
        showgrid=True,
        zeroline=True,
        zerolinecolor="white",
    ),
    plot_bgcolor="#175e33",   # football-pitch green
    paper_bgcolor="#154f2d",
    template="plotly_dark",
    height=700,
)

st.plotly_chart(fig, use_container_width=True)