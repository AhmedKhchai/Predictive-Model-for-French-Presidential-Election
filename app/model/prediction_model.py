import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def main():
    st.title("Prediction Model - Presidential Election")

    # Load datasets
    election_data_2017 = pd.read_csv('datasets/election-dataset-2017-cleaned.csv')
    employment_data = pd.read_csv('datasets/merged-employment-dataset.csv')
    security_data = pd.read_csv('datasets/security-historic-dataset-cleaned.csv', encoding='latin1')

    # Data Merging and Cleaning

    # Standardize the department names across all datasets
    election_data_2017['Département'] = election_data_2017['Département'].str.upper()
    employment_data['DeptName'] = employment_data['DeptName'].str.upper()
    security_data['Zone_geographique'] = security_data['Zone_geographique'].str.upper()

    # Filter the employment and security data for the year 2017
    employment_data_2017 = employment_data[['DeptName', 'Projets de recrutement totaux_2017']]
    security_data_2017 = security_data[security_data['Year'] == 2017]

    # Aggregate security data by department
    security_data_2017_aggregated = security_data_2017.groupby('Zone_geographique').agg(
        {'Valeurs': 'sum'}).reset_index()

    # Merge the datasets
    merged_data_1 = pd.merge(election_data_2017, employment_data_2017, left_on='Département', right_on='DeptName',
                             how='left')
    final_merged_data = pd.merge(merged_data_1, security_data_2017_aggregated, left_on='Département',
                                 right_on='Zone_geographique', how='left')

    # Drop redundant columns
    final_merged_data.drop(columns=['DeptName', 'Zone_geographique'], inplace=True)

    # Fill missing values with the mean
    mean_employment = final_merged_data['Projets de recrutement totaux_2017'].mean()
    mean_security = final_merged_data['Valeurs'].mean()
    final_merged_data['Projets de recrutement totaux_2017'].fillna(mean_employment, inplace=True)
    final_merged_data['Valeurs'].fillna(mean_security, inplace=True)

    # Create a new column indicating the winner in 2017 for each department
    final_merged_data['Winner_2017'] = final_merged_data[['ARTHAUD', 'ROUSSEL', 'MACRON', 'LASSALLE',
                                                          'LE PEN', 'ZEMMOUR', 'MÉLENCHON', 'HIDALGO',
                                                          'JADOT', 'PÉCRESSE', 'POUTOU', 'DUPONT-AIGNAN']].idxmax(
        axis=1)

    # Select features based on earlier criteria
    selected_features = ['LE PEN', 'LE PEN_percent', 'DUPONT-AIGNAN_percent', 'Exprimés', 'JADOT', 'Votants',
                         'PÉCRESSE', 'Projets de recrutement totaux_2017', 'Valeurs', 'Winner_2017']

    # Create a new DataFrame with only the selected features and target variable
    final_data_selected_features = final_merged_data[selected_features]

    # Random Forest Model
    X = final_data_selected_features.drop('Winner_2017', axis=1)
    y = final_data_selected_features['Winner_2017']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X_train, y_train)

    y_val_pred = rf_classifier.predict(X_val)
    accuracy = accuracy_score(y_val, y_val_pred)
    classification_rep = classification_report(y_val, y_val_pred)

    st.write(f"Model Accuracy: {accuracy}")
    st.write("Classification Report:")
    st.text(classification_rep)


if __name__ == "__main__":
    main()
