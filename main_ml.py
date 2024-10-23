import streamlit as st

pages = {
    "Information": [
        st.Page("streamlit_pages/Welcome_page.py", title="about my self"),
        #st.Page("manage_account.py", title="Manage your account"),
    ],
    "Portfolio": [
        st.Page("streamlit_pages/Machine_Learning.py", title="Machine Learning"),
        #st.Page("streamlit_pages/Welcome_page.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()