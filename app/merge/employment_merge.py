import streamlit as st


def main():
    st.title("Employment Data Merging")

    st.header("Why Merge Data?")
    st.markdown("""
    Merging employment datasets from different years allows us to examine recruitment trends across various French departments over time.
    """)

    st.header("Data Sources")
    st.markdown("""
    1. **Employment Data 2015**
    2. **Employment Data 2016**
    3. **Employment Data 2017**
    """)

    st.header("Modifications for Merging")
    st.markdown("""
    To successfully merge the datasets from 2015, 2016, and 2017, the following modifications were made:

    1. **Column Standardization**: Renamed and standardized the department code and name columns across all datasets for uniformity.
    2. **Column Selection**: Selected only the relevant columns that include total and seasonal recruitment projects for each year.
    3. **Data Merging**: Performed an outer merge based on the standardized department code and name. This ensures that all available data is included, even if some departments are missing in certain years.

    These modifications ensure a seamless and meaningful merge, facilitating subsequent analyses.
    """)


if __name__ == "__main__":
    main()
