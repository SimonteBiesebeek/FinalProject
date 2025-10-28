import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("Final Project: Data Analysis and Visualization")

st.header("Data")

df_merged = pd.read_csv("MergedDutchLeagueData.csv")