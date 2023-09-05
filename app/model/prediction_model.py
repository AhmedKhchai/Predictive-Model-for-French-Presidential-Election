import os
import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier


def train_and_evaluate_model(X_train, X_val, y_train, y_val):
    # Initialize the Random Forest Classifier
    mlp_classifier = MLPClassifier(random_state=1, max_iter=100)

    # Define the parameter grid
    param_grid = {
        'hidden_layer_sizes': [(16, 8, 4), (32, 16, 8), (64, 32, 16)],
        'alpha': [1e-4, 1e-3, 1e-2],
        'learning_rate_init': [0.001, 0.01, 0.1]
    }

    # Create a GridSearchCV object
    grid_search = GridSearchCV(estimator=mlp_classifier, param_grid=param_grid,
                               cv=3, n_jobs=-1, verbose=2, scoring='accuracy')

    # Fit the Grid Search to the data
    grid_search.fit(X_train, y_train)

    # Get the best parameters and create a new classifier with them
    best_params = grid_search.best_params_
    best_mlp_classifier = MLPClassifier(random_state=42, max_iter=100, **best_params)
    best_mlp_classifier.fit(X_train, y_train)

    # Evaluate the model
    y_val_pred = best_mlp_classifier.predict(X_val)
    accuracy = accuracy_score(y_val, y_val_pred)
    classification_rep = classification_report(y_val, y_val_pred)
    confusion_mat = confusion_matrix(y_val, y_val_pred)

    # Return trained model and evaluation metrics
    return best_mlp_classifier, accuracy, classification_rep, confusion_mat


def main():
    st.title("Prediction Model - Presidential Election")

    st.markdown("""
        ## Why Random Forest Model?
        We chose the Random Forest model for several reasons:
        1. **Ensemble Method**: Random Forest is an ensemble of Decision Trees, generally trained via the bagging method.
        2. **Handle Missing Values**: It can handle missing values and still gives a good accuracy.
        3. **High Accuracy**: Random Forest algorithms maintain high accuracy even for large datasets.

        ## Data Merging and Preprocessing
        1. **Standardization**: The department names across all datasets have been standardized to uppercase.
        2. **Filtering**: Employment and security data have been filtered for the year 2017.
        3. **Aggregation**: Security data has been aggregated by department.
        4. **Merging**: Finally, the datasets have been merged based on the department names.
        5. **Missing Value Treatment**: Missing values have been replaced with the mean value of each feature.

        ## Model Output Explanation
        1. **Accuracy**: The percentage of correct predictions out of all predictions.
        2. **Classification Report**: Provides key metrics in classification problem, such as precision, recall, f1-score, etc.
        """)
    # Data Preprocessing
    final_data = load_preprocess_data()

    # Prepare features and labels for model training
    X = final_data.drop('Winner_2017', axis=1)
    y = final_data['Winner_2017']
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fetch saved models
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

    # Train and Save the model
    if st.button('Train Model and Save'):
        mlp_classifier, accuracy, classification_rep, confusion_mat = train_and_evaluate_model(X_train, X_val, y_train, y_val)

        # Save the model to a file
        joblib.dump(mlp_classifier, f'saved_models/random_forest_model_{accuracy}.joblib')

        # Display the model information
        st.write(f"Model Accuracy: {accuracy}")
        st.write("Classification Report:")
        st.text(classification_rep)
        st.write(f"Confusion Matrix: {confusion_mat}")
        st.success(f"Model saved to saved_models/random_forest_model_{accuracy}.joblib")

# Load and preprocess data
def load_preprocess_data():
    # Load datasets
    election_data_2017 = pd.read_csv('datasets/election-dataset-2017-cleaned.csv')
    employment_data = pd.read_csv('datasets/Employment dataset/merged-employment-dataset.csv')
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
