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

import streamlit as st
import pickle
import plotly.graph_objs as go

st.set_page_config(page_title="Dutch Windmill Map", layout="wide")
st.title("🌷⚽ Dutch League Windmill Map")

# Load precomputed data
with open("dominance_data.pkl", "rb") as f:
    data = pickle.load(f)

seasonal_data = data["seasonal_data"]
xx, yy, probs = data["xx"], data["yy"], data["probs"]

# --- Heatmap for probability surface ---
contour = go.Contour(
    x=xx[0],
    y=yy[:,0],
    z=probs,
    colorscale="RdYlGn",
    opacity=0.85,
    showscale=True,
    colorbar=dict(title="🏠 Home Win Probability", tickformat=".0%"),
    contours=dict(showlines=False)
)

# --- Tulip markers (matches) with full-time score ---
bubbles = go.Scatter(
    x=seasonal_data['ShotDiff'],
    y=seasonal_data['ShotOnTargetDiff'],
    mode='markers',
    marker=dict(
        size=np.sqrt(seasonal_data['TotalShots']) * 2,
        color=seasonal_data['HomeWin'],
        colorscale='RdYlGn',
        symbol='diamond-tall',
        line=dict(width=1, color='white'),
        opacity=0.9,
        cmin=0, cmax=1,
        showscale=False
    ),
    text=[
        (
            f"<b>{ht}</b> vs <b>{at}</b><br>"
            f"Shots: {hs}-{as_}<br>"
            f"On Target: {hst}-{ast}<br>"
            f"Score: {fthg}-{ftag}<br>"
            f"Result: {res}"
        )
        for ht, at, hs, as_, hst, ast, fthg, ftag, res in zip(
            seasonal_data['HomeTeam'],
            seasonal_data['AwayTeam'],
            seasonal_data['HS'],
            seasonal_data['AS'],
            seasonal_data['HST'],
            seasonal_data['AST'],
            seasonal_data['FTHG'],
            seasonal_data['FTAG'],
            seasonal_data['FTR']
        )
    ],
    hoverinfo='text'
)

# --- Decision boundary ---
boundary = go.Contour(
    x=xx[0],
    y=yy[:,0],
    z=probs,
    contours=dict(start=0.5, end=0.5, size=0.01, coloring='lines'),
    showscale=False,
    line=dict(color='white', width=3, dash='dot'),
    hoverinfo='skip'
)

# --- Layout (windmill / tulip theme) ---
layout = go.Layout(
    title=dict(
        text="🌷⚽ Dutch League Windmill Map<br>Shot Dominance & Home-Win Probability",
        x=0.5, xanchor='center'
    ),
    xaxis=dict(title='Shot Difference (Home − Away)', zeroline=True, zerolinecolor='white'),
    yaxis=dict(title='Shots on Target Difference (Home − Away)', zeroline=True, zerolinecolor='white'),
    paper_bgcolor='#2b7a3d',
    plot_bgcolor='#3c9a52',
    hovermode='closest',
    template='plotly_dark',
    height=750
)

fig = go.Figure(data=[contour, boundary, bubbles], layout=layout)

st.plotly_chart(fig, use_container_width=True)
