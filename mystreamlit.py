import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header('Jeseok')

if st.button('hello'):
    st.write('my name is jeseok')
else:
    st.write('please click the button')

st.write('저는 학사와 석사과정동안 통계학을 전공했습니다.')

st.subheader('나이')

age = st.slider('제 나이는 ', 0, 130, 29)
st.write('저는 ', age, '살 입니다.')

st.subheader('통계학')

s1, s2 = st.select_slider(
    '저는', 
    options = [
        '고등학교',
        '학사과정',
        '석사과정'
    ],
    value = ('학사과정', '석사과정')
    )

st.write(f'저는 {s1}과 {s2}동안 통계학을 전공했습니다.')

st.subheader('학점')

grade = pd.DataFrame({
    'semester': [str(i) + '학기' for i in range(1, 9)],
    'grade': [3.57, 2.79, 4.28, 4.36, 4.43, 4.50, 4.50, 4.25],
    'earned': [15, 14, 24, 23, 22, 21, 12, 8]
})

st.write('학기별 성적', grade)

chart = alt.Chart(grade).mark_circle().encode(
    x = 'semester',
    y = alt.Y('grade', scale = alt.Scale(domain = [1, 5.0])),
    size = 'earned',
    color = 'earned'
).interactive()

tab1, tab2 = st.tabs(['Streamlit theme(default)', 'Altair native theme'])

with tab1:
    st.altair_chart(chart, theme = 'streamlit', use_container_width = True)
with tab2:
    st.altair_chart(chart, theme = None, use_container_width = True)

st.write('감사합니다.')
