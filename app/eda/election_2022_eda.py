import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Load data
df = pd.read_csv("datasets/election-dataset-2022-cleaned.csv")

# Calculate the abstention rate in each department
df["Abstention_rate"] = 100 - (df["Votants"] / df["Votants"].sum() * 100)

# Get the list of candidates
candidates = [col.replace("_percent", "") for col in df.columns if "_percent" in col]

# Set up main function
def main():
    st.title("2022 French Presidential Election Data Analysis")

    # TreeMap for abstention rates across departments
    st.header("Abstention Rates Across Departments")
    st.markdown(
        """
        This TreeMap displays the abstention rates across all departments in the 2022 French Presidential Election.
        Each rectangle represents a department, and the size of the rectangle indicates the abstention rate.
        """
    )
    fig = px.treemap(df, path=["Département"], values="Abstention_rate")
    st.plotly_chart(fig)

    # Ask user to select a department
    department = st.selectbox(
        "Select a Department", options=df["Département"].unique()
    )

    # Percentage of votes for each candidate across departments
    st.header(f"Votes Distribution in {department}")

    df_department = df[df["Département"] == department]
    votes = [df_department[f"{candidate}_percent"].values[0] for candidate in candidates]
    fig, ax = plt.subplots()
    sns.barplot(x=candidates, y=votes, ax=ax)
    plt.xticks(rotation=90)
    ax.set_ylabel("Percentage of Votes (%)")
    st.pyplot(fig)

    # Button to save aggregated data
    if st.button('Save Aggregated Data (2022)'):
        save_path = 'datasets/election-dataset-2022-cleaned.csv'
        df.to_csv(save_path, index=False)
        st.success(f"Data saved to {save_path}")

if __name__ == "__main__":
    main()
