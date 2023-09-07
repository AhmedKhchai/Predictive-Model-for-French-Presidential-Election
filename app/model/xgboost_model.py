import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import numpy as np
import joblib

# Load the datasets
df_training = pd.read_csv('datasets/final_merged_data_3_years.csv', encoding='latin1')
df_prediction = pd.read_csv('datasets/prediction-samples-2017-3.csv', encoding='latin1')

# Features and target variable
features = ['Département', 'Votants', 'Blancs', 'Exprimés', 'employment_3', 'employment_2', 'employment_1', 'security']
target_winner = ['Winner_2017']

# Extract features and target from the training data
X = df_training[features]
y = df_training[target_winner]

# Label encode the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y.values.ravel())

# Preprocessing setup
numeric_features = ['Votants', 'Blancs', 'Exprimés', 'employment_3', 'employment_2', 'employment_1', 'security']
categorical_features = ['Département']
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Apply preprocessing
X_preprocessed = preprocessor.fit_transform(X)

# Initialize the XGBoost classifier
xgb_classifier = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')

# Hyperparameter tuning using Grid Search
param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5, 7],
    'min_child_weight': [1, 3, 5],
    'reg_alpha': [0.5, 1],
    'reg_lambda': [1, 1.5]
}

grid_search = GridSearchCV(xgb_classifier, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_preprocessed, y_encoded)

# Get the best parameters and best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print(f"Best Parameters: {best_params}")
print(f"Best Score: {best_score}")

# Use the best estimator for predictions
best_xgb_classifier = grid_search.best_estimator_
cv_scores = cross_val_score(best_xgb_classifier, X_preprocessed, y_encoded, cv=5)

print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Score: {np.mean(cv_scores)}")

# Save the best model and label encoder
joblib.dump(best_xgb_classifier, "best_xgb_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(preprocessor, "preprocessor.pkl")
joblib.dump(best_params, "best_params.pkl")
joblib.dump(best_score, "best_score.pkl")
joblib.dump(cv_scores, "cv_scores.pkl")
joblib.dump(np.mean(cv_scores), "mean_cv_score.pkl")


def predict_winner(df_prediction, features, preprocessor, model, label_encoder):
    # Prepare the prediction dataset
    X_predict = df_prediction[features]
    X_predict_preprocessed = preprocessor.transform(X_predict)

    # Make predictions on the prediction dataset
    y_predict_winner = model.predict(X_predict_preprocessed)

    # Decode the label encoded predictions
    y_predict_winner_decoded = label_encoder.inverse_transform(y_predict_winner)

    return y_predict_winner_decoded


# Example usage of the predict_winner function
predicted_winners = predict_winner(df_prediction, features, preprocessor, best_xgb_classifier, label_encoder)
print("Predicted Winners for Each Department:")
print(predicted_winners)
