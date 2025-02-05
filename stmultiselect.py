import streamlit as st

options = st.multiselect(
    "What are your favoirte colors",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected :', options)

st.write("선택된 것은 딕셔너링 형태로 저장됨.")

st.write('Select box와 같이 여러가지 값들 중에서 선택 가능')