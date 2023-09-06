import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
import joblib


def main():
    st.title("Simplified French Presidential Election Prediction Model")

    # Load the training data from a hard-coded path
    df = pd.read_csv("datasets/final_merged_data_for_training_cleaned.csv", encoding='latin1')
    st.write(df.head())

    # Prepare data for training
    features = ['Département', 'Votants', 'Blancs', 'Exprimés', 'employment', 'security']
    target_percentages = [
        'ARTHAUD_percent', 'ROUSSEL_percent', 'MACRON_percent',
        'LASSALLE_percent', 'LE PEN_percent', 'ZEMMOUR_percent',
        'MÉLENCHON_percent', 'HIDALGO_percent', 'JADOT_percent',
        'PÉCRESSE_percent', 'POUTOU_percent', 'DUPONT-AIGNAN_percent'
    ]
    target_winner = ['Winner_2017']
    X = df[features]
    y_percentages = df[target_percentages]
    y_winner = df[target_winner]

    # Preprocessing setup
    numeric_features = ['Votants', 'Blancs', 'Exprimés', 'employment', 'security']
    categorical_features = ['Département']
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ]
    )

    # Regression Model for Percentages
    regression_model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42)))
    ])
    X_train, X_test, y_train_percentages, y_test_percentages = train_test_split(X, y_percentages, test_size=0.2,
                                                                                random_state=42)
    regression_model.fit(X_train, y_train_percentages)

    # Classification Model for Winner
    classification_model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    X_train, X_test, y_train_winner, y_test_winner = train_test_split(X, y_winner, test_size=0.2, random_state=42)
    classification_model.fit(X_train, y_train_winner.values.ravel())

    # Save Models
    save_directory = "saved_models"
    regression_model_path = "saved_models/regression_model.pkl"
    classification_model_path = "saved_models/classification_model.pkl"
    joblib.dump(regression_model, regression_model_path)
    joblib.dump(classification_model, classification_model_path)
    st.success("Models saved successfully!")

    # Load Models for Prediction
    loaded_regression_model = joblib.load(regression_model_path)
    loaded_classification_model = joblib.load(classification_model_path)

    # Load the prediction data from a hard-coded path
    df_predict = pd.read_csv("datasets/prediction-samples-2017-2.csv", encoding='latin1')
    st.write(df_predict.head())

    X_predict = df_predict[features]
    X_predict_preprocessed = preprocessor.transform(X_predict)

    # Make Predictions using saved models
    y_predict_percentages = loaded_regression_model.predict(X_predict_preprocessed)
    y_predict_winner = loaded_classification_model.predict(X_predict_preprocessed)

    # Display Predictions
    st.write("Predicted Percentages for Each Candidate:")
    st.write(y_predict_percentages)
    st.write("Predicted Winners for Each Department:")
    st.write(y_predict_winner)


if __name__ == "__main__":
    main()
