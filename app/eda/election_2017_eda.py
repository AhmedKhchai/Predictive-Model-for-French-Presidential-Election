import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

# Load data
df = pd.read_csv("datasets/election_2017.csv")

# Aggregate data by department
df_departments = df.groupby("Département").sum()
df_departments["Abstention_rate"] = (
    df_departments["Abstentions"] / df_departments["Inscrits"] * 100
)
df_departments.reset_index(inplace=True)


# Set up main function
def main():
    st.title("2017 French Presidential Election Data Analysis")

    # TreeMap for abstention rates across departments
    st.header("Abstention Rates Across Departments")
    st.markdown(
        """
        This TreeMap displays the abstention rates across all departments in the 2017 French Presidential Election.
        Each rectangle represents a department, and the size of the rectangle indicates the abstention rate.
    """
    )
    fig = px.treemap(df_departments, path=["Département"], values="Abstention_rate")
    st.plotly_chart(fig)

    # Ask user to select a department
    department = st.selectbox(
        "Select a Department", options=df_departments["Département"].unique()
    )

    # Percentage of votes for each candidate across departments
    st.header(f"Votes Distribution in {department}")

    candidates = [
        "ARTHAUD",
        "ROUSSEL",
        "MACRON",
        "LASSALLE",
        "LE PEN",
        "ZEMMOUR",
        "MÉLENCHON",
        "HIDALGO",
        "JADOT",
        "PÉCRESSE",
        "POUTOU",
        "DUPONT-AIGNAN",
    ]

    df_department = df[df["Département"] == department]
    votes = [
        df_department[candidate].sum() / df_department["Inscrits"].sum() * 100
        for candidate in candidates
    ]
    fig, ax = plt.subplots()
    sns.barplot(x=candidates, y=votes, ax=ax)
    plt.xticks(rotation=90)
    ax.set_ylabel("Percentage of Votes (%)")
    st.pyplot(fig)
    plt.clf()

    # "Blancs" and "Nuls" votes across departments
    st.header(f"'Blancs' and 'Nuls' Votes in {department}")
    blancs_nuls = ["Blancs", "Nuls"]
    bn_votes = [
        df_department[bn].sum() / df_department["Inscrits"].sum() * 100
        for bn in blancs_nuls
    ]
    fig, ax = plt.subplots()
    sns.barplot(x=blancs_nuls, y=bn_votes, ax=ax)
    ax.set_ylabel("Percentage of Votes (%)")
    st.pyplot(fig)
    plt.clf()


if __name__ == "__main__":
    main()
