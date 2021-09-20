import streamlit as st
from distributions import *

st.title('Statistical distributions')

dist_selector = st.sidebar.selectbox(
    "Pick a distribution:",
    ("Beta", "Normal"),
    index=1
)

st.header(dist_selector)


if dist_selector == 'Normal':
    normal_distribution()
elif dist_selector == 'Beta':
    beta_distribution()
