import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path
from git import Repo

import plotly


st.set_page_config("Final Project", layout="wide")
st.title("Final Project: Data Analysis with Python")

ROOT = Path(__file__).parent
df_merged = pd.read_csv(ROOT / "MergedDutchLeagueData.csv")

ROOT = Path(__file__).parent
df_premier_merged = pd.read_csv(ROOT / "MergedPremierLeagueData.csv")
st.header("Project Introduction")

st.subheader("Project Motivation")
keywords = [
    "Alternative for stock market",
    "Imperfect prices",
    "Bookmakers have all data available",
    "Odds adjusted by betting frequency",
    "Dutch & English league",
    "Estimating which company and which league yield higher betting returns"
]

for kw in keywords:
    st.markdown(f"- **{kw}**")
st.header("League Data Comparison")
col_dutch, col_english = st.columns(2)

with col_dutch:
    st.subheader("Dutch League")
    st.dataframe(df_merged)

with col_english:
    st.subheader("English League")
    st.dataframe(df_premier_merged)

with open("win_fig.pkl", "rb") as f:
    win_fig = pickle.load(f)

with open("loss_fig.pkl", "rb") as f:
    loss_fig = pickle.load(f)

st.subheader("Win and Loss Analysis")
st.plotly_chart(win_fig, use_container_width=True)
st.plotly_chart(loss_fig, use_container_width=True)

with open("win_fig.prem", "rb") as f:
    win_fig_prem = pickle.load(f)

with open("loss_fig.prem", "rb") as f:
    loss_fig_prem = pickle.load(f)

st.plotly_chart(win_fig_prem, use_container_width=True)
st.plotly_chart(loss_fig_prem, use_container_width=True)
st.subheader("Key Insights from Win/Loss Analysis")
keywords = [
    "In general, home advantage can be observed in both leagues.",
    "For big teams, the home advantage is less pronounced.",
    "Teams that only played in the league for one season sometimes show biased results",
    "Sample too small to draw conclusions, but helpful to get an overview of general patterns",
   ]

for kw in keywords:
    st.markdown(f"- **{kw}**")

st.subheader("Shots and Shots on Target Dominance")
with open("match_dominance_fig.pkl", "rb") as f:
    fig = pickle.load(f)

st.plotly_chart(fig, use_container_width=True)

st.write("Premier League Version")
with open("match_dominance_fig_prem.pkl", "rb") as f:
    fig_prem_shots = pickle.load(f)

st.plotly_chart(fig_prem_shots, use_container_width=True)
st.subheader("Key Insights from Shots Analysis")
keywords = [
    "As expected, positive relationship between both shots and shots on target on win probability",
    "Shots on target more significant.",
    "Relationship weaker than expected, mainly draws in extreme cases, few home losses",
    "Positive slope in graph unexpected, probably indicating that something is missing",
   ]

for kw in keywords:
    st.markdown(f"- **{kw}**")
st.subheader("Corner Kick Heatmaps")
with open("corner_heatmap_fig.pkl", "rb") as f:
    fig_cornersDutch = pickle.load(f)

st.plotly_chart(fig_cornersDutch, use_container_width=True)

st.subheader("Premier League Corner Kick Heatmaps")
with open("corner_heatmapPremier_fig.pkl", "rb") as f:
    fig_cornersPremier = pickle.load(f)

st.plotly_chart(fig_cornersPremier, use_container_width=True)
st.subheader("Key Insights from Corner Analysis")
keywords = [
    "Corners seem to be a weak predictor for match outcomes.",
    "Away team wins relatively more often in case of a large corner deficit.",
    "Interesting statistic for managers and set-piece specialists",
    "Probably because corners take the speed out of the game and also indicate that a shot was missed",
   ]

for kw in keywords:
    st.markdown(f"- **{kw}**")
st.subheader("Bookmaker Probabilities Visualization")
with open("model_vs_bookmaker_plot.pkl", "rb") as f:
    fig_betting = pickle.load(f)

st.plotly_chart(fig_betting, use_container_width=True, key="book_prob_plot")

st.write("Premier League Model")
with open("model_vs_bookmaker_premier_plot.pkl", "rb") as f:
    fig_premier_betting = pickle.load(f)

st.plotly_chart(fig_premier_betting, use_container_width=True, key="book_prob_plot_premier")  

st.subheader("Key Insights from Model vs Bookmaker Analysis")
keywords = [
    "Model outperforms bookmaker odds"
    "1XBet outperforms Bet365 in both markets.",
    "Both companies provide higher odds in Premier League",
    "Model mainly predicts higher probabilities for low probability cases",
    "Hypothesis: People bet safely on favorites, leading to odds being adjusted upwards for underdogs and downwards for favorites",
    "As a result, standard deviation is high",
    "Law of large numbers still makes it considerable to bet based on this model",
    ]

for kw in keywords:
    st.markdown(f"- **{kw}**")