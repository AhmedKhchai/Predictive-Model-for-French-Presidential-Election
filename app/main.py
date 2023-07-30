import streamlit as st
from eda import security_eda, employment_eda, election_2022_eda, election_2017_eda

st.set_page_config(
    page_title="Prediction Model - Presidential Election",
)


# Define functions for each page/section
def page_overview():
    st.markdown(
        """
        # Prediction Model - Presidential Election

        This project aims to create a predictive model for the French presidential elections. 
        Using the historical data from the 2017 election as well as data on employment and security, 
        the model will be trained to predict the outcome of the 2022 elections.
        """
    )


# Dictionary of pages and their corresponding functions
pages = {
    "Overview": page_overview,
    "EDA - 2017 Elections Dataset": election_2017_eda.main,
    "EDA - 2022 Elections Dataset": election_2022_eda.main,
    "EDA - Historic Security Dataset": security_eda.main,
    # "Employment Data": employment_eda.main,
}

# Use a selectbox for navigation
page = st.sidebar.selectbox("Navigate", list(pages.keys()))

# Run the app corresponding to the selected page
pages[page]()
