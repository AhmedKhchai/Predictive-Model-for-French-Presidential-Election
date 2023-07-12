# Exploratory Data Analysis

### **EDA plan**
1. **Load the Dataset:** The first step will be to load the dataset into a pandas dataframe for easy manipulation and analysis.
    
2. **Inspect the Dataset:** Examine the dataset's structure and content to understand what data is available.
    
3. **Data Cleaning:** If there are any missing or inconsistent data, we should clean it up before proceeding with the analysis.
    
4. **Descriptive Statistics:** Calculate basic statistics for the dataset to gain insights into the distributions of votes, voter turnouts, abstentions, and other variables of interest.
    
5. **Visualization:** Create visualizations to understand the data better and identify patterns and relationships between different variables.
    
6. **Deep-Dive Analyses:** Depending on the results from the initial exploratory analyses, we might want to dig deeper into specific areas.

### Load the Dataset

```python 
# Import necessary libraries

import pandas as pd

# Load the dataset

election_df = pd.read_csv('election_2017.csv')

# Display the first few rows of the dataframe

print(election_df.head())
```

### **Data Cleaning**

```python 
# Check for missing values

print("Missing values for each column:")

print(election_df.isnull().sum())


# Check for duplicate rows

print("Duplicate rows:")

print(election_df.duplicated().sum())


# Check data types

print("Data types:")

print(election_df.dtypes)
```

### **Descriptive Statistics**

```python
# Basic statistics for all numeric variables
df.describe()
```
`df.describe()` provides a lot of useful information. Let's break down a few of these:

- The `count` row shows that all numeric columns have 577 rows, confirming that there are no missing values in these columns.
- The `mean` row gives the average value for each column. For example, the average number of registered voters (`Inscrits`) per circumscription is around **84,485**.
- The `std` row tells us about the standard deviation, which measures the amount of variation or dispersion in the set of values. A low standard deviation indicates that the values tend to be close to the mean, while a high standard deviation indicates that the values are spread out over a wider range.
- The `min`, `25%`, `50%` (or median), `75%`, and `max` rows provide a five-number summary of the distribution of each column. This can give you a sense of the spread and skewness of the data.

```python 
candidates = ["ARTHAUD", "ROUSSEL", "MACRON", "LASSALLE", "LE PEN", "ZEMMOUR", "MÉLENCHON", "HIDALGO", "JADOT", "PÉCRESSE", "POUTOU", "DUPONT-AIGNAN"]
for candidate in candidates:
    print(f"{candidate} unique value count: \n{election_df[candidate].value_counts()}\n")

print("Abstentions statistics: \n", election_df['Abstentions'].describe())
print("Voter turnout statistics: \n", election_df['Votants'].describe())

for candidate in candidates:
    print(f"Total votes for {candidate}: {election_df[candidate].sum()}")

``` 

This data analysis gives a detailed overview of the number of votes each candidate received, voter turnout, and abstentions.

Based on the total votes received, the candidates can be ranked from highest to lowest as follows:

1. MACRON: 9,783,058 votes
2. LE PEN: 8,133,828 votes
3. MÉLENCHON: 7,712,520 votes
4. ROUSSEL: 802,422 votes
5. ZEMMOUR: 2,485,226 votes
6. PÉCRESSE: 1,679,001 votes
7. LASSALLE: 1,101,387 votes
8. JADOT: 1,627,853 votes
9. DUPONT-AIGNAN: 725,176 votes
10. HIDALGO: 616,478 votes
11. ARTHAUD: 197,094 votes
12. POUTOU: 268,904 votes

These results suggest that MACRON, LE PEN, and MÉLENCHON were the most popular candidates in this election, with MACRON receiving the highest number of votes.

The voter turnout statistics indicate that the mean number of voters was about 62,259 with a standard deviation of about 14,507. The highest voter turnout in a single circonscription was 103,907 and the lowest was just 2,773.

Similarly, the abstention statistics show that on average, about 22,225 voters abstained from voting, with a standard deviation of 11,549. The maximum number of abstentions in a single circonscription was 161,601.

```python 
print("Abstentions statistics: \n", df['Abstentions'].describe())
print("Voter turnout statistics: \n", df['Votants'].describe())
```

These statistics offer a snapshot of both voter turnout (Votants) and abstentions for the elections.

**Voter Turnout (Votants):**

The average voter turnout across all the constituencies ('circonscriptions') is around 62,259 voters, with a standard deviation of approximately 14,507. This means that the number of voters in most circonscriptions varied within a range of about 14,507 from the average. The maximum turnout observed in any single circonscription was 103,907 voters, and the minimum was quite low at 2,773 voters. 

The quartiles provide further information:

- 25% of circonscriptions had a turnout of less than 54,306 voters.
- 50% (the median) had a turnout of less than 62,592 voters, suggesting that half the circonscriptions had more than 62,592 voters and half had fewer.
- 75% of circonscriptions had a turnout of less than 71,357 voters.

**Abstentions:**

The average number of abstentions across all the circonscriptions was about 22,225, with a standard deviation of approximately 11,549. This means that in most circonscriptions, the number of abstentions varied within a range of about 11,549 from the average. The maximum number of abstentions in any single circonscription was quite high at 161,601, whereas the minimum was relatively low at 2,272 abstentions.

The quartiles provide further details:

- 25% of circonscriptions had fewer than 17,746 abstentions.
- 50% (the median) had fewer than 20,246 abstentions, indicating that half the circonscriptions had more than 20,246 abstentions and half had fewer.
- 75% of circonscriptions had fewer than 22,800 abstentions.
