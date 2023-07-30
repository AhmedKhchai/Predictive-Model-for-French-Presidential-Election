import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Load data
df = pd.read_csv("datasets/election_2022.csv")

# Aggregate data by department
# Select columns that start with '%'
percentage_columns = df.columns[df.columns.str.startswith('%')]

# Groupby 'Libellé du département' and calculate mean of these columns
df_departments = df.groupby("Libellé du département")[percentage_columns].mean().reset_index()

df_departments.reset_index(level=0, inplace=True)


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
    fig = px.treemap(df_departments, path=["Libellé du département"], values="% Abs/Ins")
    st.plotly_chart(fig)

    # Ask user to select a department
    department = st.selectbox(
        "Select a Department", options=df_departments["Libellé du département"].unique()
    )

    # Percentage of votes for each candidate across departments
    st.header(f"Votes Distribution in {department}")

    df_department = df[df["Libellé du département"] == department]

    # Get the vote columns
    # Get the vote, name, and % Voix/Ins columns
    vote_columns = [col for col in df.columns if 'Voix' in col]
    name_columns = [col for col in df.columns if 'Nom' in col]
    vote_percentage_columns = [col for col in df.columns if '% Voix/Ins' in col]

    votes = []
    candidates = []
    vote_percentages = []

    for vote_col, name_col, vote_percentage_col in zip(vote_columns, name_columns, vote_percentage_columns):
        votes.append(df_department[vote_col].sum())
        candidates.append(df_department[name_col].unique()[0])
        vote_percentages.append(df_department[vote_percentage_col].sum())

    vote_data = pd.DataFrame({'Candidate': candidates, 'Votes': votes, 'Vote Percentage': vote_percentages})
    vote_data.sort_values('Vote Percentage', ascending=False, inplace=True)

    fig, ax = plt.subplots()
    sns.barplot(x='Vote Percentage', y='Candidate', data=vote_data, ax=ax)
    plt.xlabel("Vote Percentage")
    st.pyplot(fig)
    plt.clf()


if __name__ == "__main__":
    main()
