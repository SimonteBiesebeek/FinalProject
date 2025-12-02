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

st.subheader("Win and Loss Analysis")
st.plotly_chart(win_fig, use_container_width=True)
st.plotly_chart(loss_fig, use_container_width=True)

with open("win_fig.prem", "rb") as f:
    win_fig_prem = pickle.load(f)

with open("loss_fig.prem", "rb") as f:
    loss_fig_prem = pickle.load(f)

st.plotly_chart(win_fig_prem, use_container_width=True)
st.plotly_chart(loss_fig_prem, use_container_width=True)


st.subheader("Shots and Shots on Target Dominance")
with open("match_dominance_fig.pkl", "rb") as f:
    fig = pickle.load(f)

st.plotly_chart(fig, use_container_width=True)

st.write("Premier League Version")
with open("match_dominance_fig_prem.pkl", "rb") as f:
    fig_prem_shots = pickle.load(f)

st.plotly_chart(fig_prem_shots, use_container_width=True)

st.subheader("Corner Kick Heatmaps")
with open("corner_heatmap_fig.pkl", "rb") as f:
    fig_cornersDutch = pickle.load(f)

st.plotly_chart(fig_cornersDutch, use_container_width=True)

st.subheader("Premier League Corner Kick Heatmaps")
with open("corner_heatmapPremier_fig.pkl", "rb") as f:
    fig_cornersPremier = pickle.load(f)

st.plotly_chart(fig_cornersPremier, use_container_width=True)

st.subheader("Bookmaker Probabilities Visualization")
with open("model_vs_bookmaker_plot.pkl", "rb") as f:
    fig_betting = pickle.load(f)

st.plotly_chart(fig_betting, use_container_width=True, key="book_prob_plot")

st.write("Premier League Model")
with open("model_vs_bookmaker_premier_plot.pkl", "rb") as f:
    fig_premier_betting = pickle.load(f)

st.plotly_chart(fig_premier_betting, use_container_width=True, key="book_prob_plot_premier")  