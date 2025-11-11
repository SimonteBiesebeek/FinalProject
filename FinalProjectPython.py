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

st.title("⚽ Football Dominance Surface (Precomputed)")

# Load precomputed data
with open("dominance_data.pkl", "rb") as f:
    data = pickle.load(f)

seasonal_data = data["seasonal_data"]
xx = data["xx"]
yy = data["yy"]
probs = data["probs"]

# Plotly 3D surface + matches
surface = go.Surface(x=xx, y=yy, z=probs, colorscale='RdYlGn', opacity=0.85)
bubbles = go.Scatter3d(
    x=seasonal_data["ShotDiff"],
    y=seasonal_data["ShotOnTargetDiff"],
    z=seasonal_data["HomeWin"]+0.01,
    mode='markers',
    marker=dict(
        size=(seasonal_data["TotalShots"])**0.5 * 1.5,
        color=seasonal_data["HomeWin"],
        colorscale="RdYlGn",
        line=dict(width=1, color="white")
    ),
    text=[f"FTR: {r}" for r in seasonal_data["FTR"]],
    hoverinfo="text"
)

fig = go.Figure(data=[surface, bubbles])
fig.update_layout(
    title="⚽ Precomputed 3D Football Dominance",
    scene=dict(
        xaxis_title="Shot Difference",
        yaxis_title="Shots on Target Difference",
        zaxis_title="Home-Win Probability",
    ),
    template="plotly_dark",
    height=700
)

st.plotly_chart(fig, use_container_width=True)