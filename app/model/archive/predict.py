import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
from xgboost_model import XGBRegressor, XGBClassifier
import joblib
import numpy as np


def main():
    print("French Presidential Election Prediction Model")
    print("=" * 50)

    # Load training dataset
    df = pd.read_csv("datasets/final_merged_data_for_training_cleaned.csv", encoding='latin1')

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

    # Regression Model for Percentages using XGBoost
    regression_model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', MultiOutputRegressor(XGBRegressor()))
    ])
    X_train, X_test, y_train_percentages, y_test_percentages = train_test_split(X, y_percentages, test_size=0.2,
                                                                                random_state=42)
    regression_model.fit(X_train, y_train_percentages)

    # Classification Model for Winner using XGBoost
    classification_model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', XGBClassifier())
    ])
    X_train, X_test, y_train_winner, y_test_winner = train_test_split(X, y_winner, test_size=0.2, random_state=42)
    classification_model.fit(X_train, y_train_winner.values.ravel())

    # Hyperparameter Tuning for XGBoost (Simplified for demonstration)
    param_grid = {
        'classifier__n_estimators': [50, 100],
        'classifier__learning_rate': [0.01, 0.1],
        'classifier__max_depth': [3, 5]
    }
    grid_search = GridSearchCV(estimator=classification_model, param_grid=param_grid,
                               cv=3, n_jobs=-1, verbose=2, scoring='accuracy')
    grid_search.fit(X_train, y_train_winner.values.ravel())
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    print(f"Best Parameters: {best_params}")
    print(f"Best Score: {best_score}")

    # Use the best estimator for further predictions and evaluations
    classification_model = grid_search.best_estimator_

    # Evaluate Models
    y_pred_percentages = regression_model.predict(X_test)
    mse = mean_squared_error(y_test_percentages, y_pred_percentages)
    rmse = np.sqrt(mse)
    print(f"Regression Model RMSE: {rmse}")

    y_pred_winner = classification_model.predict(X_test)
    accuracy = accuracy_score(y_test_winner, y_pred_winner)
    print(f"Classification Model Accuracy: {accuracy}")

    # Save Models
    save_directory = "saved_models"
    regression_model_path = "regression_model_xgboost.pkl"
    classification_model_path = "classification_model_xgboost.pkl"
    joblib.dump(regression_model, regression_model_path)
    joblib.dump(classification_model, classification_model_path)
    print("Models saved successfully!")

    # Load prediction dataset
    df_predict = pd.read_csv("datasets/prediction-samples-2017-2.csv", encoding='latin1')

    # Prepare new data
    X_predict = df_predict[features]

    # Make Predictions using saved models
    y_predict_percentages = regression_model.predict(X_predict)
    y_predict_winner = classification_model.predict(X_predict)

    # Display Predictions
    print("Predicted Percentages for Each Candidate:")
    print(y_predict_percentages)

    print("Predicted Winners for Each Department:")
    print(y_predict_winner)


if __name__ == "__main__":
    main()
