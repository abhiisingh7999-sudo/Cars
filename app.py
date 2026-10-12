import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('Cars_cleaned.csv')
st.title("Used Cars Data Analysis")
st.table(df.head())
