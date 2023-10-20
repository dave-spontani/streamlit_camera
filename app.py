import streamlit as st
from importing import return_even
from backup import return_odd

st.title("Try this!")

first_list = [i for i in range(10)]

all_odd = return_odd(first_list)

all_even = return_even(first_list)

st.write(all_odd)

st.write(all_even)

st.write("This is a cool update")
st.write("This is yet another update")