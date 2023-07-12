import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.write("Current working directory:", os.getcwd())
st.write("Directory contents:", os.listdir())
dataset_path = "datasets/election_2017.csv"
# Load your data (adjust the path to your data file)
df = pd.read_csv(dataset_path, sep=",", quotechar='"')

st.title("French Election Data Analysis")

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
