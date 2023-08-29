import os
import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def train_and_evaluate_model(X_train, X_val, y_train, y_val):
    # Initialize the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Evaluate the model
    y_val_pred = rf_classifier.predict(X_val)
    accuracy = accuracy_score(y_val, y_val_pred)
    classification_rep = classification_report(y_val, y_val_pred)

    # Return trained model and evaluation metrics
    return rf_classifier, accuracy, classification_rep


def main():
    st.title("Prediction Model - Presidential Election")

    # Data Preprocessing
    final_data = load_preprocess_data()

    # Prepare features and labels for model training
    X = final_data.drop('Winner_2017', axis=1)
    y = final_data['Winner_2017']
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fetch saved
    if not os.path.exists('saved_models'):
        os.makedirs('saved_models')
    model_files = os.listdir('saved_models/')
    selected_model_file = st.selectbox('Select a saved model:', model_files)

    # Display details about the selected model
    if selected_model_file:
        loaded_model = joblib.load(f'saved_models/{selected_model_file}')
        st.write(f"Details for model {selected_model_file}")
        st.write(f"Number of Estimators: {loaded_model.n_estimators}")
        st.write(f"Criterion: {loaded_model.criterion}")
        st.write(f"Max Depth: {loaded_model.max_depth}")

    # Button to train and save the model
    if st.button('Train Model and Save'):
        rf_classifier, accuracy, classification_rep = train_and_evaluate_model(X_train, X_val, y_train, y_val)

        # Save the model to a file
        joblib.dump(rf_classifier, f'saved_models/random_forest_model_{accuracy}.joblib')

        # Display the model information
        st.write(f"Model Accuracy: {accuracy}")
        st.write("Classification Report:")
        st.text(classification_rep)


def load_preprocess_data():
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
    return final_data_selected_features


if __name__ == "__main__":
    main()
