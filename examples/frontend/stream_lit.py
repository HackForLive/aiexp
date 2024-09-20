import streamlit as st
import json
import requests

st.title("Basic calculator app")

# taking user input
option = st.selectbox('What operation would you like to perform?', 
                      options=('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.write("")
st.write("Select the numbers from slider bellow:")
x = st.slider(label="X", min_value=0, max_value=100, value=20)
y = st.slider(label="Y", min_value=0, max_value=130, value=10)

# converting inputs into json format
inputs = {"operation": option, "x": x, "y": y}

# When user clicks on button it will fetch the API
if st.button(label='Calculate'):
    res=requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(inputs))
    st.subheader(f"Reponse from API: {res.text}")
