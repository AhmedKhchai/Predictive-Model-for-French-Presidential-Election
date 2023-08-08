
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned data
df = pd.read_csv('/mnt/data/security-historic-dataset-cleaned_v3.csv', encoding='latin1')

def main():
    st.title("Historic Security Data Analysis and Visualisation")

    st.header("Data Overview")
    st.write(df.head())

    # Histogram for the distribution of "Valeurs"
    st.subheader("Distribution of 'Valeurs'")
    fig1 = px.histogram(df, x="Valeurs", title="Distribution of Valeurs")
    st.plotly_chart(fig1)

    # Line chart for yearly trend
    st.subheader("Yearly Trend of 'Valeurs'")
    yearly_values = df.groupby('Year').sum()['Valeurs'].reset_index()
    fig2 = px.line(yearly_values, x='Year', y='Valeurs', title="Yearly Trend of Valeurs")
    st.plotly_chart(fig2)

    # Bar chart for top zones with highest values
    st.subheader("Top Zones with Highest 'Valeurs'")
    top_zones = df.groupby('Zone_geographique').sum()['Valeurs'].nlargest(10).reset_index()
    fig3 = px.bar(top_zones, x='Zone_geographique', y='Valeurs', title="Top Zones with Highest Valeurs")
    st.plotly_chart(fig3)

    # Pie chart for values distribution by `Indicateur`
    st.subheader("Values Distribution by 'Indicateur'")
    indicator_distribution = df.groupby('Indicateur').sum()['Valeurs'].reset_index()
    fig4 = px.pie(indicator_distribution, names='Indicateur', values='Valeurs', title="Distribution by Indicateur")
    st.plotly_chart(fig4)

    # Monthly distribution for a selected year
    selected_year = st.selectbox('Select Year for Monthly Distribution', df['Year'].dropna().unique().astype(int).tolist())
    monthly_data = df[df['Year'] == selected_year].groupby('Month').sum()['Valeurs'].reset_index()
    fig5 = px.bar(monthly_data, x='Month', y='Valeurs', title=f"Monthly Distribution for {selected_year}")
    st.plotly_chart(fig5)

if __name__ == "__main__":
    main()
