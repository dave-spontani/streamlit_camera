########Now we get the concrete calls. This file will define how to call and save the data#####
import pandas as pd 
import requests
import streamlit as st

####We can pack everything into one function - this program is not too complicated
def get_data(query_input):
    #Old call for testing:
    # second_query = 'https://api.fda.gov/drug/event.json?search=(receivedate:[20040101+TO+20231207])+AND+patient.drug.medicinalproduct:"ASPIRIN"&limit=50'

    res_02 = requests.get(query_input).json()

    # We need to create the dataframe from scratch, since the results json is strange. We 
    # build a two-dimensional list which we can turn into a dataframe. Every sublist containst
    # all of the information we want for the line - every object will have the attributes 
    # "Serious, weight, sex, date, reactions"
    # We iterate over every result / patient and create their corresponding line into the df for later!
    dataframe_setup = []

    for patient in range(0,len(res_02["results"])):
        ##Create a new line
        line = []

        # Simplified: Serious, weight, sex, date, reactions get appended immdeiately without specification
        # Here, we need to rely on try/except statements due to the possibility of N/A's
        reactions = []
        for reaction in range(0,len(res_02["results"][patient]["patient"]['reaction'])):
            reactions.append(res_02["results"][patient]["patient"]['reaction'][reaction]['reactionmeddrapt'])
            
        try:
            line.append(res_02["results"][patient]["serious"])
        except:
            line.append("N/A")
        try:
            line.append(res_02["results"][patient]["patient"]["patientweight"])
        except: 
            line.append("N/A")
        try:
            line.append(res_02["results"][patient]["patient"]["patientsex"])
        except:
            line.append("N/A")
        try:    
            line.append(res_02["results"][patient]["receivedate"])
        except:
            line.append("N/A")
        try:
            line.append(reactions)
        except:
            line.append("N/A")

        ###Append Line to dataframe_setup
        dataframe_setup.append(line)

    #######DataFrame input should be finished here###############

    #######Create Dataframe from two-dimensional list############

    patients = pd.DataFrame(dataframe_setup, columns =['Serious', 'Weight', "sex", "date", "reactions"]) 

    #print(patients.head())
    # Here, we save the reactions as a list, and flatten it. We then use a list comprehension to count the 
    # elements and their number of occurrences, and save that in a dictionary later in order to use the 
    # reaction as the key, and prepare the correct format for the visualization later.

    reactions = patients["reactions"].tolist()

    reactions_list = [j for sub in reactions for j in sub]

    final_react_count = [[x,reactions_list.count(x)] for x in set(reactions_list)]

    print(final_react_count)

    final_react_dict =  {}

    for elem in range(0, len(final_react_count)):
        final_react_dict[final_react_count[elem][0]] = final_react_count[elem][1]

    # Sorted Dictionary in descending order. This code was written by ChatGPT

    ##############CODE Written by ChatGPT!#######################
    sorted_reactions = sorted(final_react_dict.items(), key=lambda x:x[1], reverse=True)
    final_react_dict_sorted = dict(sorted_reactions )
    #############END Code written by CHatGPT#####################


    st.write("Done")

    # Finally, we return the Dataframe and the Sorted Dictionary
    return patients, final_react_dict_sorted
