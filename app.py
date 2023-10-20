import streamlit as st
import pandas as pd
import matplotlib.pyplot as plot

from importing import return_even

st.title("Try this!")
st.write("And this!")
usage_list = [i for i in range(20)]

all_even = return_even(usage_list)

st.write(all_even)
