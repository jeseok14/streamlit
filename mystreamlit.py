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

grade_ba = pd.DataFrame({
    'semester': [str(i) + '학기' for i in range(1, 9)],
    'grade': [3.57, 2.79, 4.28, 4.36, 4.43, 4.50, 4.50, 4.25],
    'earned': [15, 14, 24, 23, 22, 21, 12, 8]
})

grade_ms = pd.DataFrame({
    'semester' : [str(i) + '학기' for i in range(1,5)],
    'grade' : [4.5,4.5,4.5,np.nan],
    'earned' : [9,9,6,np.nan]
})

chart1 = alt.Chart(grade_ba).mark_circle().encode(
    x = 'semester',
    y = alt.Y('grade', scale = alt.Scale(domain = [1, 5.0])),
    size = 'earned',
    color = 'earned'
).interactive()

chart2 = alt.Chart(grade_ms).mark_circle().encode(
    x = 'semester',
    y = alt.Y('grade', scale = alt.Scale(domain = [1, 5.0])),
    size = 'earned',
    color = 'earned'
).interactive()


col1, col2 = st.columns(2)
with col1:
    st.write('학부 학기별 성적', grade_ba)
    st.altair_chart(chart1, theme = 'streamlit', use_container_width = True)
with col2:
    st.write('석사 학기별 성적', grade_ms)
    st.altair_chart(chart2, theme = 'streamlit', use_container_width = True)

tab1, tab2 = st.tabs(['Streamlit theme(default)', 'Altair native theme'])

with tab1:
    st.altair_chart(chart1, theme = 'streamlit', use_container_width = True)
with tab2:
    st.altair_chart(chart1, theme = None, use_container_width = True)

option = st.selectbox(
    'How would you like to be contacted?',
    ("Email", "Mobile phone"),
    index = None
)

st.write('You selected :', option)

st.write('감사합니다.')
