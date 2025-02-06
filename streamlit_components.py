import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport  # ✅ 최신 패키지 사용
from streamlit_pandas_profiling import st_profile_report

st.header("Pandas Profiling in Streamlit")

# 데이터 불러오기
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

# 프로파일링 리포트 생성
pr = ProfileReport(df, explorative=True)  # ✅ 최신 문법 적용

# Streamlit에서 리포트 출력
st_profile_report(pr)
