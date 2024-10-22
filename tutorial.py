import streamlit as st
import pandas as pd 


st.set_page_config(
    page_title="Python Crash Kurs",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded")


# Begrüßung
st.title("Willkommen auf meiner Streamlit Seite, der Blockwoche")
st.write("Wir erstellen hier interessante Daten getrieben Visualsiierungen und Machine Learning Algorithmen")

#Data Settings for Upload 
Data_settings = st.sidebar.expander("Daten einstellungen")
with Data_settings:
    file_separator = st.selectbox("Wähle den Seprator aus", options=[",",";"," "])

# Upload oprtunnity for user
upload_file = st.sidebar.file_uploader("Lade bitte deine Daten hoch")
# Check if a file is uploaded
if bool(upload_file):
    df = pd.read_csv(upload_file, 
                     sep=file_separator)

else:
    df = None
    st.sidebar.info('Please upload your dataset')
    st.info("""**Start by uploading your own data** 📁""")
    st.stop()

st.dataframe(df, use_container_width=True)

Data_manipulation_tab, data_vis_tab, ml_tab = st.tabs(["Data Manipulation", "Data Vis", "Machine Learning"])

with Data_manipulation_tab:
    st.write("Hier Programmierung Daten filterung evtl.")

with data_vis_tab:
    st.write("Hier Programmiere die Visuallisierung")

with ml_tab:
    st.write("Hier Programmierung dein Machine Learning Algo")