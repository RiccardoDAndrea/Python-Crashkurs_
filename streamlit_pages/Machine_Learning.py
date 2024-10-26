import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from streamlit_lottie import st_lottie
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Python Crash Kurs",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded"
)

###################################################################################################
###################################################################################################
###################################################################################################
def load_lottieurl(url:str):
    """ 
    The follwing function request a url from the homepage
    lottie files if status is 200 he will return
    instand we can use this func to implement lottie files for 
    our Homepage
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

no_date_col = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_0pgmwzt3.json')
removed_date_column = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_ovo7L6.json')
no_data_avaible = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_rjn0esjh.json')
question_with_NaN_values = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_lKvkGl.json')
no_X_variable_lottie = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_ydo1amjm.json')
value_is_zero_in_train_size = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_usmfx6bp.json')
wrong_data_type_ML = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_2frpohrv.json')
rocket_for_cv = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_atskiwym.json')
###################################################################################################
###################################################################################################
###################################################################################################

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
    st_lottie(no_date_col)
    st.stop()


###################################################################
################# G R E E T I N G  ################################
###################################################################


st.write("👋 **Willkommen auf meiner Streamlit-Seite!** 🎉", unsafe_allow_html=True)


# ####################################################################
# ################# S H O W _ D A T A ################################
# ####################################################################
st.divider()
st.subheader("Your DataFrame: ")
st.dataframe(df, use_container_width=True)
st.divider()



# Create the tabs for different functionalities
data_manipulation, visualisation, machine_learning = st.tabs(["Data Imputation", "Data Vis", "Machine Learning"])

# Inside the 'Data Imputation' tab
with data_manipulation:
    
    # Column selection for dropping columns
    col_drop = st.multiselect("Which columns to drop?", options=df.columns)
    
    # Drop the selected columns
    if col_drop:
        df = df.drop(columns=col_drop)
        st.dataframe(df)
    else:
        st.dataframe(df)

    # Display a divider
    st.divider()
    
    # Show the number of missing values per column
    is_na_col, replace_na_col = st.columns(2)
    with is_na_col:
        st.write("Your missing values")
        st.dataframe(df.isna().sum(), use_container_width=True)
    with replace_na_col:
        
        remove_nan = st.selectbox("How to continue with NaN values", options=["Mean", "Drop"])
        
        # Handle imputation or dropping of NaN values
        if remove_nan == "Mean":
            # Fill NaN with the mean for numeric columns
            df = df.fillna(df.select_dtypes(include="number").mean())
            st.success("NaN values filled with column mean.")
            st_lottie(rocket_for_cv, width=250, height=200)
            
        elif remove_nan == "Drop":
            # Drop rows with NaN values
            df = df.dropna()
            st.success("Rows with NaN values dropped.")
            st_lottie(rocket_for_cv, width=400, height=200)
    st.dataframe(df, use_container_width=True)        
        # Display the updated dataframe


with visualisation:
    visualisation_select = st.multiselect("Chose your Viszulisation", options=[
        "Line-Chart",
        "Bar-Chart",
        "Histogramm",
        "Pie-Chart",
        "Boxplot"
    ], key="col to drop")

    # LinienDiagramm
    if "Line-Chart" in visualisation_select:
        x_line_col1, y_line_col1 = st.columns(2)
        with x_line_col1: 
            x_axis_val_line = st.selectbox('Select X-Axis Value', 
                                           options=df.columns,
                                            key='x_axis_line_multiselect')
        with y_line_col1:
            y_axis_val_line = st.selectbox('Select X-Axis Value', 
                                           options=df.columns,
                                        key='y_axis_line_multiselect')
        fig_line = px.line(data_frame=df, 
                x=x_axis_val_line, 
                y=y_axis_val_line, 
                title='Unemployment Rate (%) in Germany')
        st.plotly_chart(figure_or_data=fig_line, use_container_width=False)


    
    # BarDiagramm  
    if "Bar-Chart" in visualisation_select:
        
        x_bar_col1, y_bar_col1 = st.columns(2)
        with x_bar_col1: 
            x_axis_val_bar = st.selectbox('Select X-Axis Value', options=df.columns,
                                                            key='x_axis_bar_multiselect')
        with y_bar_col1:
            y_axis_val_bar = st.selectbox('Select X-Axis Value', options=df.columns,
                                                            key='y_axis_bar_multiselect')
        fig_box = px.box(data_frame=df, 
                x=x_axis_val_bar,
                y=y_axis_val_bar,
                title='Unemployment Rate (%) in Germany')
        st.plotly_chart(figure_or_data=fig_box, use_container_width=False)

    

    if "Histogramm" in visualisation_select:
        # Histogramm
        x_hist_col1, y_hist_col1 = st.columns(2)
        with x_hist_col1: 
            x_axis_val_hist = st.selectbox('Select X-Axis Value', options=df.columns,
                                                            key='x_hist_line_multiselect')
        with y_hist_col1:
            y_axis_val_hist = st.selectbox('Select X-Axis Value', options=df.columns,
                                                            key='y_hist_line_multiselect')
        fig_line = px.box(data_frame=df, 
                x=x_axis_val_hist, 
                y=y_axis_val_hist, 
                title='Unemployment Rate (%) in Germany')
        st.plotly_chart(figure_or_data=fig_line, use_container_width=False, key="")

with machine_learning:
    # Select prediction (target) variable
    pred_var = st.selectbox("Choose your prediction variable", options=df.columns)

    # Select dependent (predictor) variables
    dep_var = st.multiselect("Choose your dependent variables", options=df.columns)

    # Only proceed if both pred_var and dep_var are selected
    if pred_var and dep_var:
        X = df[dep_var]
        y = df[pred_var]

        # Add constant (intercept) to the independent variables
        X = sm.add_constant(X)

        # Fit the OLS regression model
        model_stats = sm.OLS(y, X).fit()

        # Display the model summary
        st.write(model_stats.summary())

        # Dynamically create user input fields for each dependent variable
        user_inputs = []
        for var in dep_var:
            user_input = st.text_input(f"Enter value for {var}", value="")
            try:
                # Convert input to float, defaulting to 0.0 if empty or invalid
                user_input = float(user_input) if user_input else 0.0
            except ValueError:
                st.error(f"Invalid input for {var}. Please enter a valid number.")
                user_input = 0.0  # Default to 0 if input is invalid
            user_inputs.append(user_input)

        # Perform the prediction using model parameters
        if user_inputs:
            # Start with the intercept (constant term)
            pred = model_stats.params[0]

            # Add each parameter (coefficient) multiplied by the corresponding user input value
            for i, input_value in enumerate(user_inputs):
                pred += model_stats.params[i + 1] * input_value

            # Display the prediction
            st.write(f"Your predicted value is: {pred}")
    else:
        st.write("Please select both a prediction variable and at least one dependent variable.")
        st_lottie(question_with_NaN_values, width=200, height=200)