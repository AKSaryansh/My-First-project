import streamlit as st
import joblib
model = joblib.load('HEART DISEASE DETECTOR')
st.title('Come! Have your Heart Checked')
input_list = []
a1 = eval(st.text_input('Enter your age'))
a2 = eval(st.text_input('Enter your sex'))
a3 = eval(st.text_input('Enter your cp'))
a4 = eval(st.text_input('Enter your trestbps'))
a5 = eval(st.text_input('Enter your chol'))
a6 = eval(st.text_input('Enter your fbs'))
a7 = eval(st.text_input('Enter your restecg'))
a8 = eval(st.text_input('Enter your thalach'))
a9 = eval(st.text_input('Enter your exang'))
a10 = eval(st.text_input('Enter your oldpeak'))
a11 = eval(st.text_input('Enter your slope'))
a12 = eval(st.text_input('Enter your ca'))
a13 = eval(st.text_input('Enter your thal'))
input_list = [[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13]]
op = model.predict(input_list)
if st.button('Predict'):
  st.title(str(op[0]))
