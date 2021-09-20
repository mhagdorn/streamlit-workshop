import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import scipy.stats

def beta_distribution():
    alpha = st.sidebar.slider('alpha', value=0.5, min_value=0.1,
                              max_value=10.0, step=0.1, format='%.1f')
    beta = st.sidebar.slider('beta', value=0.5,
                             min_value=0.1, max_value=10.0, step=0.1,
                             format='%.1f')

    x = np.linspace(start=0, stop=1, num=400)
    y = scipy.stats.beta.pdf(x, alpha, beta)
    pdf_data = pd.DataFrame.from_dict({
        'x': x,
        'probability density': y,
    })
    line_chart = alt.Chart(pdf_data).mark_line().encode(
        x='x',
        y='probability density',
        tooltip=['x', 'probability density'],
    )
    with st.expander('Plot of PDF', expanded=True):
        st.altair_chart(line_chart.interactive(), use_container_width=True)

    y = scipy.stats.beta.cdf(x, alpha, beta)
    cdf_data = pd.DataFrame.from_dict({
        'x': x,
        'cumulative density': y,
    })
    line_chart = alt.Chart(cdf_data).mark_line().encode(
        x='x',
        y='cumulative density',
        tooltip=['x', 'cumulative density'],
    )
    with st.expander('Plot of CDF', expanded=False):
        st.altair_chart(line_chart.interactive(), use_container_width=True)
