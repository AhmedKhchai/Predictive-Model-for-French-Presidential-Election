import streamlit as st
import pandas as pd
from app.clean.security_clean import clean_data
import plotly.express as px

# Load the uncleaned data
unclean_df = pd.read_csv('datasets/security-historic-dataset.csv', encoding='latin1')


def main():
    st.title("Historic Security Data Analysis, Cleaning and Visualisation")

    st.header("Data Before Cleaning")

    # Show the outputs of the data analysis on the original dataset
    st.table(unclean_df.head())
    st.markdown('**Unique values in Statistique column:**')
    st.table(unclean_df['Statistique'].value_counts().to_frame())

    st.markdown('**Unique values in Zone_geographique column:**')
    st.table(unclean_df['Zone_geographique'].value_counts().to_frame())

    st.markdown('**Unique values in Periodicite column:**')
    st.table(unclean_df['Periodicite'].value_counts().to_frame())

    st.markdown('**Unique values in Unite_de_compte column:**')
    st.table(unclean_df['Unite_de_compte'].value_counts().to_frame())

    st.markdown('**Unique values in Indicateur column:**')
    st.table(unclean_df['Indicateur'].value_counts().to_frame())

    # Explanation for cleaning the data
    st.subheader("Why is data cleaning needed?")
    st.markdown("""
    We need to clean the data because...

    1. **Inconsistent Formats:** Your 'Unite_de_compte' and 'Zone_geographique' columns appear to have inconsistent formatting. For instance, in the 'Unite_de_compte' column, some rows have the word 'Victime' with a capital 'V', some have 'victimes', some have 'Victimes', etc. These should be standardized to ensure that when you perform operations or queries on the data, it behaves as expected.

    2. **Unnecessary Information:** In the 'Zone_geographique' column, there are numerical prefixes attached to the zone names. This information is not needed for geographical analysis and hence it's better to remove this.

    3. **Improving Readability and Processing:** In the 'Unite temps' column, the information is not in a readable or easily processable format. Breaking it down into separate 'Year' and 'Month' columns can make it easier to understand and allows for more straightforward temporal analysis.

    4. **Handling Missing or NA values:** The script contains code to handle NaN values, which are common in real-world data. It's important to decide how to handle these: whether to exclude them, fill them with a default value, or some other method.

    5. **Standardization:** Certain rows contain French terms (like 'Annuelle', 'Mensuelle', 'Trimestrielle') which might need to be translated or standardized to English, especially if this data needs to be integrated with other data sources or presented to an international audience.
    """)

    # Button to run cleaning script and load cleaned data
    if st.button("Clean Data"):
        st.text("Cleaning data...")
        cleaned_df = clean_data()
        st.header("Data After Cleaning")
        st.write(cleaned_df.head())

    df = pd.read_csv('datasets/security-historic-dataset-cleaned.csv', encoding='latin1')

    selected_indicator = st.selectbox('Select an indicator to filter the data', df['Indicateur'].unique())
    # Filter the dataframe based on the selected indicator
    df_filtered = df[df['Indicateur'] == selected_indicator]

    # Line chart for yearly trend
    st.subheader(f"Yearly Trend of 'Valeurs' for {selected_indicator}")
    yearly_values = df_filtered.groupby('Year').sum()['Valeurs'].reset_index()
    fig2 = px.line(yearly_values, x='Year', y='Valeurs', title=f"Yearly Trend of Valeurs for {selected_indicator}")
    st.plotly_chart(fig2)

    # Bar chart for top zones with highest values
    st.subheader(f"Top Zones with Highest 'Valeurs' for {selected_indicator}")
    top_zones = df_filtered.groupby('Zone_geographique').sum()['Valeurs'].nlargest(10).reset_index()
    fig3 = px.bar(top_zones, x='Zone_geographique', y='Valeurs',
                  title=f"Top Zones with Highest Valeurs for {selected_indicator}")
    st.plotly_chart(fig3)

    selected_year = st.selectbox('Select a year to filter the data', df['Year'].unique())

    # Pie chart for values distribution by `Indicateur` for a selected year
    st.subheader(f"Values Distribution by 'Indicateur' for {selected_year}")
    df_filtered_by_year = df[df['Year'] == selected_year]
    indicator_distribution = df_filtered_by_year.groupby('Indicateur').sum()['Valeurs'].reset_index()
    fig4 = px.pie(indicator_distribution, names='Indicateur', values='Valeurs',
                  title=f"Distribution by Indicateur for {selected_year}")
    st.plotly_chart(fig4)


if __name__ == "__main__":
    main()
