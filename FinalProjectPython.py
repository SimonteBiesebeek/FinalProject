import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path


import plotly
st.write("Plotly version:", plotly.__version__)


st.set_page_config("Final Project", layout="wide")
st.title("Final Project: Data Analysis and Visualization")

ROOT = Path(__file__).parent
df_merged = pd.read_csv(ROOT / "MergedDutchLeagueData.csv")
df_merged = pd.read_csv("MergedDutchLeagueData.csv")


st.header("Project Introduction")



col_data, _, col_chart = st.columns((0.8, 0.05, 1))

with col_data:
    st.subheader("Raw Data")
    st.dataframe(df_merged)

with col_chart:
    st.subheader("Data Overview")
    st.markdown("Placeholder for chart")


# --- Compute win/loss % when leading/losing at HT ---
df_merged['HT_leader'] = df_merged.apply(
    lambda x: 'Home' if x['HTHG'] > x['HTAG'] else ('Away' if x['HTHG'] < x['HTAG'] else 'Draw'),
    axis=1
)

# Win %
home_leads = df_merged[df_merged['HT_leader']=='Home'].groupby('HomeTeam').agg(
    games_leading=('HomeTeam','count'),
    wins_when_leading=('FTR', lambda x: (x=='H').sum())
)
home_leads['home_win_pct'] = 100*home_leads['wins_when_leading']/home_leads['games_leading']

away_leads = df_merged[df_merged['HT_leader']=='Away'].groupby('AwayTeam').agg(
    games_leading=('AwayTeam','count'),
    wins_when_leading=('FTR', lambda x: (x=='A').sum())
)
away_leads['away_win_pct'] = 100*away_leads['wins_when_leading']/away_leads['games_leading']

team_win_pct = pd.concat([home_leads['home_win_pct'], away_leads['away_win_pct']], axis=1).fillna(0)

# --- Plotly figure ---
win_fig = go.Figure(data=[
    go.Bar(name='Home', x=team_win_pct.index, y=team_win_pct['home_win_pct'], marker_color='royalblue'),
    go.Bar(name='Away', x=team_win_pct.index, y=team_win_pct['away_win_pct'], marker_color='orange')
])
win_fig.update_layout(
    title='Win % When Leading at Half Time',
    xaxis_title='Team',
    yaxis_title='Win Percentage (%)',
    barmode='group',
    template='plotly_white',
    xaxis_tickangle=-45,
    height=600
)

# Display in Streamlit
st.plotly_chart(win_fig, use_container_width=True)