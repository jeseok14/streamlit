import streamlit as st

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
    '제 타임라인은', 
    options = [
        '고등학교',
        '학사과정',
        '석사과정'
    ],
    value = ('학사과정', '석사과정')
    )

st.write(f'저는 {s1}과 {s2}동안 통계학을 전공했습니다.')
st.write('감사합니다.')
