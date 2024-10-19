import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Python Crash Kurs",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to my Webpage")

# File uploader
upload_file = st.sidebar.file_uploader(label="Upload your data", type=["csv"])

# Separator selection
file_separator = st.sidebar.selectbox("Pick your separator", 
                                      [",", ";", ":", " "])

# Check if a file is uploaded
if bool(upload_file):
    df = pd.read_csv(upload_file, 
                     sep=file_separator)

else:
    df = None
    st.sidebar.info('Please upload your dataset')
    st.info("""**Start by uploading your own data** 📁""")
    st.stop()

    

# ####################################################################
# ################# S H O W _ D A T A ################################
# ####################################################################
st.subheader("Your DataFrame: ")
st.dataframe(df, use_container_width=True)
st.divider()

# ##Contiune with VIS


        