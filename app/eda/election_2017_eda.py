# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Read in the dataset
df = pd.read_csv("datasets/election_2017.csv")


# Function to generate a download link for the dataset
def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


# The main function where we define and run our streamlit app
def main():
    st.title('Exploratory Data Analysis - French Presidential Elections 2017')

    # Provide a data summary
    st.subheader("Data Summary")
    st.write(f"Number of Rows: {df.shape[0]}")
    st.write(f"Number of Columns: {df.shape[1]}")

    # Print column names for debugging
    st.write(df.columns)

    # Allow user to select a candidate
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
    candidate = st.selectbox("Select a candidate to view", candidates)

    # Show a histogram for selected candidate
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(df[candidate], bins=20, color="blue", alpha=0.7)
    plt.xlabel("Votes")
    plt.ylabel("Count")
    plt.title(f"Distribution of votes for {candidate}")
    st.pyplot(fig)

    # Show abstention statistics
    st.subheader("Abstention statistics")
    st.write(df["Abstentions"].describe())

    # Show voter turnout statistics
    st.subheader("Voter turnout statistics")
    st.write(df["Votants"].describe())

    # Show a scatter plot of abstention vs selected candidate
    st.subheader("Scatter plot: abstention vs selected candidate")
    fig, ax = plt.subplots()
    ax.scatter(df["Abstentions"], df[candidate], alpha=0.5)
    plt.xlabel("Abstentions")
    plt.ylabel("Votes")
    plt.title(f"Abstentions vs Votes for {candidate}")
    st.pyplot(fig)

    # Add an option to select a specific department
    departments = df["Département"].unique().tolist()
    selected_dept = st.multiselect("Select a department", departments)

    # Filter data based on selected department
    if selected_dept:
        df_filtered = df[df["Département"].isin(selected_dept)]
        st.write(df_filtered)

    # Correlation matrix
    st.subheader("Correlation Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(df[candidates].corr(), annot=True, ax=ax, cmap="coolwarm")
    st.pyplot(fig)

    # Provide download link for the data
    if st.button("Download Dataframe as CSV"):
        tmp_download_link = download_link(
            df, "YOUR_DF.csv", "Click here to download your data!"
        )
        st.markdown(tmp_download_link, unsafe_allow_html=True)


# Ensure the script runs on streamlit run
if __name__ == "__main__":
    main()
