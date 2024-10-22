import streamlit as st
import pandas as pd


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


###################################################################
################# G R E E T I N G  ################################
###################################################################


st.write("👋 **Willkommen auf meiner Streamlit-Seite!** 🎉", unsafe_allow_html=True)
st.write("🌟 **Entdecke spannende Inhalte, Features und vieles mehr!** 🌟", unsafe_allow_html=True)
st.write("😊 **Lass uns gemeinsam etwas Großartiges erschaffen!** 🚀", unsafe_allow_html=True)

    

# ####################################################################
# ################# S H O W _ D A T A ################################
# ####################################################################
st.divider()
st.subheader("Your DataFrame: ")
st.dataframe(df, use_container_width=True)
st.divider()






with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)

tab1, tab2, tab3 = st.tabs(["Data Imputation", "Data Vis", "Machine Learning"])
with tab1:
    st.write("Tab1")

with tab2:
    data_expander = st.expander("Dataframe")
    with data_expander:
        st.dataframe(df, use_container_width=True)

    vis_line, vis_boxplot = st.columns(2)
    with vis_line:
        fig_line = px.line(data_frame=df, 
                x="Year", 
                y="Unemployment Rate (%)", 
                title='Unemployment Rate (%) in Germany', 
                color='Country')
        st.plotly_chart(figure_or_data=fig_line, use_container_width=False)

    with vis_boxplot:
        fig_box = px.box(data_frame=df, 
                x="Unemployment Rate (%)", 
                title='Unemployment Rate (%) in Germany', 
                color='Country')
        st.plotly_chart(figure_or_data=fig_box, use_container_width=False)

with tab3:
    st.write("Tab1")
