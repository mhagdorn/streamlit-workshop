import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import scipy.stats

def normal_distribution():
    param_range = st.sidebar.slider('Range', value=20.0, min_value=0.0,
                                    max_value=100.0, step=0.1, format='%.1f')
    param_mean = st.sidebar.slider('Mean', value=0.0, min_value=-30.0,
                                   max_value=30.0, step=0.1, format='%.1f')
    param_std = st.sidebar.slider('Standard deviation', value=3.0,
                                  min_value=0.1, max_value=20.0, step=0.1,
                                  format='%.1f')

    x = np.linspace(start=-param_range, stop=param_range, num=400)
    y = scipy.stats.norm.pdf(x, param_mean, param_std)
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

    
    y = scipy.stats.norm.cdf(x, param_mean, param_std)
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

    with st.expander('Formulae', expanded=False):
        st.markdown(r'''Parameters:
- mean: $\mu\in\mathbb{R}$
- standard deviation: $\sigma\in\mathbb{R}^+$
---
Support:
- $x\in\mathbb{R}$
---
Moments:
- $\mathrm{E}(X) = \mu$
- $\mathrm{Var}(X) = \sigma^2$
---
Probability density function (PDF):

$$
f(x|\mu,\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}}\text{exp}\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$
---
Cumulative distribution function (CDF):

$$
F(x|\mu,\sigma) = \frac{1}{2}\left[1+\text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
$$

where

$$
\text{erf}(x) = \frac{2}{\sqrt{\pi}}\int_{0}^{x} e^{-t^2}\mathrm{d}t
$$
is the error function.
''')
    with st.expander('LaTeX', expanded=False):
        st.markdown(r'''Moments:
```latex
\mathrm{E}(X) = \mu
```
```latex
\mathrm{Var}(X) = \sigma^2
```
---
Probability density function (PDF):
```latex
f(x|\mu,\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}}\text{exp}\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
```
---
Cumulative distribution function (CDF):
```latex
F(x|\mu,\sigma) = \frac{1}{2}\left[1+\text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
```
where
```latex
\text{erf}(x) = \frac{2}{\sqrt{\pi}}\int_{0}^{x} e^{-t^2}\mathrm{d}t
```
is the error function.
''')
