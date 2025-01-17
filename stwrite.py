# st.write - writing text, display dict and dataframe, plots, graphs,frigures from matplotlib, plotly, altair, graphviz, bokeh

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header('st.write')

# Example 1

st.header('Display header')

st.write('Hello, *World* :sunglasses:')

# Example 2

st.header('Display numbers')

st.write(1234)

# Example 3

st.header('Display DataFrame')

df = pd.DataFrame({
	'first column' : [1,2,3,4],
	'second column' : [10,20,30,40]
})
st.write(df)

# Example 4

st.header('Accept multiple arguments like print func')

st.write("Below is a DataFrame", df, 'Above is a dataframe')

# Example 5

st.header('Display charts')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a','b','c']
)
st.write(c)
