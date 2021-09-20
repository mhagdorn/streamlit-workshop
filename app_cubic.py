import streamlit as st
import numpy
import pandas
import altair as alt

st.title('Hello, world')
st.write('playing with a cubic function')


st.markdown(r'''
$$
f(x)=ax^3+bx^2+cx+d
$$
''')


a = st.slider("a", min_value=-10., max_value=10.0,
              value=5.0, step=0.1, format="%.1f")
b = st.slider("b", min_value=-10., max_value=10.0,
              value=5.0, step=0.1, format="%.1f")
c = st.slider("c", min_value=-10.0, max_value=10.0,
              value=5.0, step=0.1, format="%.1f")
d = st.slider("d", min_value=-10.0, max_value=10.0,
              value=5.0, step=0.1, format="%.1f")

data = pandas.DataFrame()
data['x']= numpy.arange(-10,10)
data['y']=a*data['x']**3+b*data['x']**2+c*data['x']+d

st.write(a,b,c)

line_chart = alt.Chart(data).mark_line().encode(
    x='x',
    y='y',
    tooltip=['x', 'y'],
)
st.altair_chart(line_chart.interactive(), use_container_width=True)



