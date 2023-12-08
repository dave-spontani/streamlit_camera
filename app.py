#######This is the main appp file where we call the functions and use them in streamlit######
# Import the necessary modules:
import streamlit as st
import requests
import pandas as pd
from feature_01 import get_data
from feature_02 import query_builder
import matplotlib.pyplot as plt

# We need to set up the streamlit page. First, we need to import the most common
# drugs in order to show them on the select button
st.title("Adverse Effects of Medicine")

query_url = "https://api.fda.gov/drug/event.json?search=receivedate:[20220101+TO+20231207]&count=patient.drug.medicinalproduct.exact"

res = requests.get(query_url).json()

names_list = []

for item in range(0,len(res["results"])):
    names_list.append(res["results"][item]["term"])

# Now that we have the names, we start building the webapp where we get our parameters
######Webapp part######

st.write("Please select the name of the Medicine whose adverse effect you want to know more about:")

med = st.selectbox('How would you like to be contacted?',names_list)

st.write("Please select any other parameters you want to add!")

start = st.slider('How far back shall we search?', min_value = 2014, max_value = 2022, step = 1)

finish = st.slider('Until when should we search?', min_value = 2015, max_value = 2023, step = 1)

sex_input = st.radio("Male/Female", ["", "1", "2"], captions = ["Both","Male", "Female"])

speed_raw = st.radio("Do you want comprehensive or fast results?",["Very fast!", "Fast!", "Take your time", "Mother of all analysis"])

speed_dict = {"Very fast!": "100", "Fast!": "200", "Take your time": "400", "Mother of all analysis": "1000"}

speed_input = speed_dict[speed_raw]

########Execution!###############
# After working on the inputs, the user now presses a button to execute the search

if st.button('Start search!'):

    # Build the query
    query = query_builder(start, finish, med, speed_input, sex_input)

    st.write(query)
    # Get back the data in the format we want
    res_df, react_dict = get_data(query)


    # Pepare the effects and counts for a pie-chart. We get the keys as the labels, and the elements as the sizes! 
    labels = list(react_dict.keys())
    sizes = list(react_dict.values())

    # st.write(labels)
    # st.write(sizes)

    # Here, we build the plot, and take only the top ten entries

    st.write(f"Out of {speed_input} people, these were the most common adverse effects")
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes[:10], labels=labels[:10], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the plot
    st.pyplot(fig1)

    # Optional full list of symptoms at the bottom.
    st.write("Do you want to see the full list of symptoms? See here")
    st.write(react_dict)


