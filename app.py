import streamlit as st
import requests
import pandas as pd
from feature_01 import get_data
from feature_02 import query_builder
import matplotlib.pyplot as plt

st.title("Adverse Effects of Medicine")

query_url = "https://api.fda.gov/drug/event.json?search=receivedate:[20220101+TO+20231207]&count=patient.drug.medicinalproduct.exact"

res = requests.get(query_url).json()

####Get a full list of all the drug names first. We can use them to look for adverse effects later

names_list = []

for item in range(0,len(res["results"])):
    names_list.append(res["results"][item]["term"])

print(names_list)

st.write("Please select the name of the Medicine whose adverse effect you want to know more about:")

med = st.selectbox('How would you like to be contacted?',names_list)

st.write("Please select any other parameters you want to add!")

start = st.slider('How far back shall we search?', min_value = 2014, max_value = 2022, step = 1)

finish = st.slider('Until when should we search?', min_value = 2015, max_value = 2023, step = 1)

sex_input = st.radio("Male/Female", ["", "1", "2"], captions = ["Both","Male", "Female"])

speed_raw = st.radio("Do you want comprehensive or fast results?",["Very fast!", "Fast!", "Take your time", "Mother of all analysis"])

speed_dict = {"Very fast!": "100", "Fast!": "200", "Take your time": "400", "Mother of all analysis": "1000"}

speed_input = speed_dict[speed_raw]

if st.button('Start search!'):

    query = query_builder(start, finish, med, speed_input, sex_input)

    st.write(query)

    res_df, react_dict = get_data(query)


    # st.write(react_dict)

    # st.write(res_df.head())

    labels = list(react_dict.keys())
    sizes = list(react_dict.values())

    # st.write(labels)
    # st.write(sizes)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes[:10], labels=labels[:10], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)


    st.write("Do you want to see the full list of symptoms? Click here"):
    st.write(react_dict)


