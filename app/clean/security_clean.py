import pandas as pd


def clean_data():
    # Load the data
    df = pd.read_csv('datasets/security-historic-dataset.csv', encoding='latin1')

    # Function to extract year and month from "Unite temps"
    def parse_time(unit):
        if pd.isna(unit):  # Check if the value is NaN
            return pd.Series({"Year": None, "Month": None})
        if "T" in unit:  # This is a quarter
            year = unit[:4]
            quarter = int(unit[-1])
            month = (quarter - 1) * 3 + 1  # Convert quarter to starting month
        elif "M" in unit:  # This is a month
            year, month = unit.split("M")
        else:  # This is a year
            year = unit
            month = None
        return pd.Series({"Year": int(year), "Month": month})

    # Apply the function to the "Unite temps" column
    df[["Year", "Month"]] = df["Unite temps"].apply(parse_time)

    # Correct the 'Zone_geographique' column values to remove the numbers and the '-' at the beginning of the string.
    df['Zone_geographique'] = df['Zone_geographique'].str.split('-').str[-1]

    # Correct the 'Unite_de_compte' column values by making them all lowercase and making all values containing
    # 'victime' to 'victime'.
    df['Unite_de_compte'] = df['Unite_de_compte'].str.lower()
    df.loc[df['Unite_de_compte'].str.contains('victime', na=False), 'Unite_de_compte'] = 'Victimes'

    # Drop the "Unite temps" column
    df.drop(columns=["Unite temps"], inplace=True)

    # Convert "Month" column to integer data type
    df["Month"] = df["Month"].astype(float).astype("Int32")

    # Convert "Valeurs" column to float data type
    df["Valeurs"] = pd.to_numeric(df["Valeurs"], errors='coerce')

    # Convert Taux pour 1000 to number
    taux_mask = df['Statistique'].str.contains('Taux pour 1000')
    df.loc[taux_mask, 'Valeurs'] = df.loc[taux_mask, 'Valeurs'] * 1000

    # Remove rows where "Valeurs" column value is empty
    df = df[df["Valeurs"].notna()]

    # Remove rows where "Zone_geographique" column values start with "France"
    df = df[~df["Zone_geographique"].str.startswith("France")]

    # Convert "Valeurs" column to integers
    df["Valeurs"] = df["Valeurs"].astype(int)
    df['Year'] = df['Year'].astype(int)

    # Drop the "Sous_indicateur" and "Statistique" column
    df.drop(columns=["Sous_indicateur", "Statistique"], inplace=True)

    # Save the cleaned dataframe
    df.to_csv('datasets/security-historic-dataset-cleaned.csv', index=False, encoding='latin1')

    print('Dataset cleaned successfully!')

    # Checking unique values in 'Zone_geographique' column:
    print(df['Zone_geographique'].value_counts())
    # Checking unique values in 'Periodicite' column:
    print(df['Periodicite'].value_counts())
    # Checking unique values in 'Unite_de_compte' column:
    print(df['Unite_de_compte'].value_counts())
    # Checking unique values in 'Indicateur' column:
    print(df['Indicateur'].value_counts())

    # return the cleaned dataframe
    return df
