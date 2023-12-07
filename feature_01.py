########Now we get the concrete calls:
import pandas as pd 
import requests
import streamlit as st


def get_data(query_input):
    #second_query = 'https://api.fda.gov/drug/event.json?search=(receivedate:[20040101+TO+20231207])+AND+patient.drug.medicinalproduct:"ASPIRIN"&limit=50'

    res_02 = requests.get(query_input).json()

    #print(res_02["results"][0])

    #Trial DF

    dataframe_setup = []

    for patient in range(0,len(res_02["results"])):
        #print(patient)
        ##Create a new line
        line = []

        ###Simplified: Serious, weight, sex, date, reactions get appended inndeiately without specification
        reactions = []
        for reaction in range(0,len(res_02["results"][patient]["patient"]['reaction'])):
            reactions.append(res_02["results"][patient]["patient"]['reaction'][reaction]['reactionmeddrapt'])
            #print(res_02["results"][patient]["patient"]['reaction'][reaction]['reactionmeddrapt'])

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

        #print(line)

        ###Append Line to dataframe_setup
        dataframe_setup.append(line)


    #print(dataframe_setup)
    #######Create Dataframe:

    patients = pd.DataFrame(dataframe_setup, columns =['Serious', 'Weight', "sex", "date", "reactions"]) 

    print(patients.head())

    reactions = patients["reactions"].tolist()

    reactions_list = [j for sub in reactions for j in sub]

    final_react_count = [[x,reactions_list.count(x)] for x in set(reactions_list)]

    print(final_react_count)

    final_react_dict =  {}

    for elem in range(0, len(final_react_count)):
        final_react_dict[final_react_count[elem][0]] = final_react_count[elem][1]


    sorted_reactions = sorted(final_react_dict.items(), key=lambda x:x[1], reverse=True)
    final_react_dict_sorted = dict(sorted_reactions )

    st.write("Done")

    return patients, final_react_dict_sorted
