import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

st.title("Final Project: Data Analysis and Visualization")

st.header("Data")

ROOT = Path(__file__).parent
df_merged = pd.read_csv(ROOT / "MergedDutchLeagueData.csv")
df_merged = pd.read_csv("MergedDutchLeagueData.csv")

st.dataframe(df_merged.head())