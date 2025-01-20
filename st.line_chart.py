import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header('Line Chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)


st.write('그릴 데이터 확인', chart_data)

st.line_chart(chart_data)

st.header('Altair Chart')

st.subheader('단순 차트 그리기')

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a','b','c'])
)

st.altair_chart(c, use_container_width = True)

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )  
df = st.session_state.data

point_selector = alt.selection_point('point_selection')
interval_selector = alt.selection_interval('interval_selection')
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x = 'a',
        y = 'b',
        size = 'c',
        color = 'c',
        tooltip = ['a', 'b', 'c'],
        fillOpacity = alt.condition(point_selector, alt.value(1), alt.value(0.3))
    )
    .add_params(point_selector, interval_selector)
)

event = st.altair_chart(chart, key = 'alt_chart', on_select = 'rerun')


import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
		x = 'Horsepower',
		y = 'Miles_per_Gallon',
		color = 'Origin',
).interactive()

tab1, tab2 = st.tabs(['Streamlit themedefault)', 'Altair native theme'])

with tab1:
	# User the streamlit theme
	# This is the default. So you can also omit the theme argument.
	st.altair_chart(chart, theme = 'streamlit', use_container_width = True)
with tab2:
	# Use the native Altair theme.
	st.altair_chart(chart, theme = None, use_container_width = True)