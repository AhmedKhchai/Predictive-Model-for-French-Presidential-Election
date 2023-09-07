import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib

from app.model.xgboost_model import predict_winner


def main():
    st.title("Predictive Model for French Presidential Election")

    st.write("## Model Description")
    st.write("""
    This model uses XGBoost, a machine learning algorithm, to predict the winner of the French Presidential Election in different departments.
    """)

    st.write("## Why XGBoost over Random Forest?")
    st.write("""
    Initially, a Random Forest model was considered for this prediction task. However, despite hyperparameter tuning, the highest accuracy achieved was around 50%. 
    XGBoost not only performs well in terms of speed but also has built-in capabilities for handling imbalanced datasets.
    After tuning, XGBoost provided a more accurate model, making it the algorithm of choice for this application.
    """)

    st.write("## Model Performance Indicators")

    # Best Parameters
    st.write("### Best Parameters")
    best_params = {'learning_rate': 0.01, 'max_depth': 5, 'min_child_weight': 3, 'n_estimators': 100, 'reg_alpha': 0.5,
                   'reg_lambda': 1}
    st.json(best_params)

    # Best Score
    st.write("### Best Score")
    best_score = 0.551948051948052
    st.write(f"{best_score:.4f}")
    fig1 = go.Figure(go.Indicator(
        mode="gauge",
        value=best_score,
        title={'text': "Best Score"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [None, 1]}}
    ))
    st.plotly_chart(fig1)

    # Cross-Validation Scores
    st.write("### Cross-Validation Scores")
    cv_scores = [0.54545455, 0.5, 0.57142857, 0.52380952, 0.61904762]
    fig2 = px.bar(x=list(range(1, len(cv_scores) + 1)), y=cv_scores, labels={'x': 'Fold', 'y': 'Score'})
    st.plotly_chart(fig2)

    # Mean CV Score
    st.write("### Mean CV Score")
    mean_cv_score = 0.551948051948052
    st.write(f"{mean_cv_score:.4f}")

    # Add mean to the bar chart
    fig2.add_shape(
        go.layout.Shape(type='line', x0=0, x1=len(cv_scores), y0=mean_cv_score, y1=mean_cv_score,
                        line=dict(color='Red')),
    )
    st.plotly_chart(fig2)

    #TODO: Add a justification to why the model's performance is not that good and how it can be improved

    if st.button("Predict"):
        # Load the model and label encoder
        model = joblib.load("best_xgb_model.pkl")
        label_encoder = joblib.load("label_encoder.pkl")
        preprocessor = joblib.load("preprocessor.pkl")

        # Load the prediction dataset
        df_prediction = pd.read_csv('datasets/prediction-samples-2017-3.csv', encoding='latin1')

        features = ['Département', 'Votants', 'Blancs', 'Exprimés', 'employment_3', 'employment_2', 'employment_1',
                    'security']

        # Call the prediction function from xgboost_model.py
        predicted_winners = predict_winner(df_prediction, features, preprocessor, model, label_encoder)

        # Create a DataFrame for predicted winners
        df_results = pd.DataFrame(predicted_winners, columns=["Predicted Winner"])

        # Plot predicted winners
        winner_counts = df_results["Predicted Winner"].value_counts().reset_index()
        winner_counts.columns = ["Candidate", "Count"]

        fig_winner = px.bar(winner_counts, x='Candidate', y='Count', color='Candidate', title='Predicted Winners',
                            text='Count')
        fig_winner.update_traces(texttemplate='%{text}', textposition='outside')
        st.plotly_chart(fig_winner)


if __name__ == "__main__":
    main()
