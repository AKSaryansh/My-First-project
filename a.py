import streamlit as st
import joblib
model = joblib.load('HEART DISEASE DETECTOR')
st.title('Come! Have your Heart Checked')
input_list = []
a1 = st.text_input('Enter your age')
a2 = st.text_input('Enter your sex')
a3 = st.text_input('Enter your cp')
a4 = st.text_input('Enter your trestbps')
a5 = st.text_input('Enter your chol')
a6 = st.text_input('Enter your fbs')
a7 = st.text_input('Enter your restecg')
a8 = st.text_input('Enter your thalach')
a9 = st.text_input('Enter your exang')
a10 = st.text_input('Enter your oldpeak')
a11 = st.text_input('Enter your slope')
a12 = st.text_input('Enter your ca')
a13 = st.text_input('Enter your thal')
input_list = [[int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11),int(a12),int(a13)]]
op = model.predict(input_list)
if st.button('Predict'):
  st.title(str(op[0]))
