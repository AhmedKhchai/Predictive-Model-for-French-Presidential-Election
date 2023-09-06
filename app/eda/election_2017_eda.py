import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Load data
df = pd.read_csv("datasets/election-dataset-2017.csv")

# Aggregate data by department
df_departments = df.groupby("Département").sum()
df_departments["Abstention_rate"] = (
        df_departments["Abstentions"] / df_departments["Inscrits"] * 100
)
df_departments.reset_index(inplace=True)

# Calculate the percentage of votes each candidate received in each department
candidates = [
    "ARTHAUD", "ROUSSEL", "MACRON", "LASSALLE", "LE PEN", "ZEMMOUR",
    "MÉLENCHON", "HIDALGO", "JADOT", "PÉCRESSE", "POUTOU", "DUPONT-AIGNAN"
]

for candidate in candidates:
    df_departments[f'{candidate}_percent'] = (df_departments[candidate] / df_departments["Inscrits"]) * 100


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

    df_department = df_departments[df_departments["Département"] == department]
    votes = [df_department[f"{candidate}_percent"].values[0] for candidate in candidates]
    fig, ax = plt.subplots()
    sns.barplot(x=candidates, y=votes, ax=ax)
    plt.xticks(rotation=90)
    ax.set_ylabel("Percentage of Votes (%)")
    st.pyplot(fig)
    plt.clf()
    # List of columns to remove
    columns_to_remove = [
        "CodeCirco", "NumeroCirco", "Circonscription", "Inscrits", "Abstentions", "Abstentions_ins", "Votants_ins",
        "Blancs_ins", "Blancs_vot", "Nuls", "Nuls_ins", "Nuls_vot", "Exprimés_ins", "Exprimés_vot", "ARTHAUD.ins",
        "ROUSSEL.ins", "MACRON.ins", "LASSALLE.ins", "LE PEN.ins", "ZEMMOUR.ins", "MÉLENCHON.ins", "HIDALGO.ins",
        "JADOT.ins", "PÉCRESSE.ins", "POUTOU.ins", "DUPONT-AIGNAN.ins", "ARTHAUD.exp", "ROUSSEL.exp", "MACRON.exp",
        "LASSALLE.exp", "LE PEN.exp", "ZEMMOUR.exp", "MÉLENCHON.exp", "HIDALGO.exp", "JADOT.exp", "PÉCRESSE.exp",
        "POUTOU.exp", "DUPONT-AIGNAN.exp"
    ]

    # Remove specified columns
    clean_df = df_departments.drop(columns=columns_to_remove, errors='ignore')

    # Button to save aggregated data
    if st.button('Save Aggregated Data (2017)'):
        save_path = 'datasets/election-dataset-2017-cleaned.csv'
        clean_df.to_csv(save_path, index=False, encoding='latin1')
        st.success(f"Data saved to {save_path}")


if __name__ == "__main__":
    main()
