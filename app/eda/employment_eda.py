import streamlit as st
import pandas as pd
import plotly.express as px
import os
import numpy as np

# Columns for data type conversion and capping
conversion_columns_map = {
    '2015': ['Projets de recrutement totaux', 'Projets de recrutement difficiles',
             'Projets de recrutement saisonniers'],
    '2016': ['met', 'xmet', 'smet'],
    '2017': ['met', 'xmet', 'smet']
}

# Mapping for department code and name columns across datasets
dept_columns_map = {
    '2015': ['Code département', 'Nom Departement'],
    '2016': ['Département', 'NomDept'],
    '2017': ['Dept', 'NomDept']
}

import numpy as np


def load_data(path, year):
    # Load the dataset
    data = pd.read_csv(path, encoding='latin1')
    # Convert specific columns to appropriate data types
    conversion_columns = conversion_columns_map[year]

    for col in conversion_columns:
        if data[col].dtype == 'object':  # Check if the column is of object (string) type
            data[col] = data[col].str.strip().replace(['-', ' - '], np.nan).str.replace(',', '').astype(float)
        else:
            data[col] = data[col].replace(['-', ' - '], np.nan).astype(float)

    # Apply the capping method to handle outliers
    for col in conversion_columns:
        data = cap_outliers(data, col)
    return data


def aggregate_data(data, year):
    # Determine the columns present in the dataset
    available_columns = data.columns.intersection(conversion_columns_map[year]).tolist()

    # Aggregate the data by department
    return data.groupby(dept_columns_map[year])[available_columns].sum().reset_index()


def cap_outliers(df, col):
    threshold = df[col].quantile(0.95)
    df[col] = df[col].apply(lambda x: threshold if x > threshold else x)
    return df


def main():
    st.title("Employment Data Analysis, Cleaning, and Aggregation")

    # Choose the dataset year for visualization
    year = st.selectbox('Select the dataset year:', ['2015', '2016', '2017'])
    data_path = f'datasets/employment-dataset-{year}.csv'

    # Load the data
    data = load_data(data_path, year)

    # Aggregate the data
    aggregated_data = aggregate_data(data, year)

    # Display the cleaned and aggregated data
    st.subheader(f"Aggregated Employment Data ({year})")
    st.write(aggregated_data.head())

    # Explanation about the columns' relevance to model building
    st.subheader("Relevance to Model Building:")
    st.markdown("""
    - **Projets de recrutement totaux (Total Recruitment Projects)**: Represents the overall employment demand in a region or department. A high value might suggest a thriving economy with many job opportunities, possibly influencing voters' decisions in favor of the incumbent or economically competent party.

    - **Projets de recrutement difficiles (Difficult Recruitment Projects)**: Indicates challenges in the job market, such as a skills mismatch. Voters in areas with significant skills gaps might lean towards candidates or parties promising educational, training, or job matching initiatives.

    - **Projets de recrutement saisonniers (Seasonal Recruitment Projects)**: Provides insights into regions relying heavily on seasonal industries. Populations in areas with significant tourism or agriculture sectors might have different concerns and voting behaviors compared to more urban or industrialized regions.
    """)

    # Box plot to visualize the cleaned data
    for col in conversion_columns_map[year]:
        fig = px.box(aggregated_data, y=col, title=f'Box Plot for {col} (Cleaned and Aggregated Data)')
        st.plotly_chart(fig)

    # Option to save the cleaned and aggregated dataset
    if st.button(f'Save Aggregated Data ({year})'):
        save_path = f'datasets/employment-dataset-{year}-cleaned.csv'
        aggregated_data.to_csv(save_path, index=False)
        st.success(f"Data saved to {save_path}")


if __name__ == "__main__":
    main()
