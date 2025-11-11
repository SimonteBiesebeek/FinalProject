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

ROOT = Path(__file__).parent
df_premier_merged = pd.read_csv(ROOT / "MergedPremierLeagueData.csv")
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


#graph shots/shots on target dominance

with open("dominance_data.pkl", "rb") as f:
    data = pickle.load(f)

seasonal_data = data["seasonal_data"]
xx, yy, probs = data["xx"], data["yy"], data["probs"]

heatmap = go.Contour(
    x=xx[0],
    y=yy[:,0],
    z=probs,
    colorscale="RdYlGn",
    opacity=0.85,
    showscale=True,
    colorbar=dict(title="🏠 Home Win Probability", tickformat=".0%"),
    contours=dict(showlines=False)
)

matches = go.Scatter(
    x=seasonal_data['ShotDiff'],
    y=seasonal_data['ShotOnTargetDiff'],
    mode='markers',
    marker=dict(
        size=np.sqrt(seasonal_data['TotalShots']) * 2,
        color=seasonal_data['HomeWin'],
        colorscale="RdYlGn",
        line=dict(width=1, color='white'),
        opacity=0.8,
        cmin=0, cmax=1,
        showscale=False
    ),
)
text = [
    f"<b>{ht}</b> vs <b>{at}</b><br>Shots: {hs}-{as_}<br>On Target: {hst}-{ast}<br>Score: {fthg}-{ftag}<br>Result: {res}"
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
]

matches = go.Scatter(
    x=seasonal_data['ShotDiff'],
    y=seasonal_data['ShotOnTargetDiff'],
    mode='markers',
    marker=dict(
        size=np.sqrt(seasonal_data['TotalShots']) * 2,
        color=seasonal_data['HomeWin'],
        colorscale="RdYlGn",
        line=dict(width=1, color='white'),
        opacity=0.8,
        cmin=0, cmax=1,
        showscale=False
    ),
    text=text,
    hoverinfo='text'
)

layout = go.Layout(
    title="⚽ Shot Dominance vs Home Win Probability",
    xaxis=dict(title='Shot Difference (Home − Away)'),
    yaxis=dict(title='Shots on Target Difference (Home − Away)'),
    template='plotly_dark',
    height=700,
    hovermode='closest'
)

fig = go.Figure(data=[heatmap, matches], layout=layout)

st.plotly_chart(fig, use_container_width=True)
