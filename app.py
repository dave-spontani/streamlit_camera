import streamlit as st
import cv2
import numpy as np

# Create the streamlit Title and camera_input
st.title(f'A sample input')
img_file_buffer = st.camera_input(f"Take a picture!")
