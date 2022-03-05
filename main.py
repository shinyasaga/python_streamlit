import streamlit as st
from PIL import Image

st.title('streamlit　超入門')
st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

condition = st.slider('あなたの調子は？',0,100,50)
