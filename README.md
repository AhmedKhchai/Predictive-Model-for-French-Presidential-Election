# Predictive Model for French Presidential Election

## Project Overview

This project aims to create a predictive model for the French presidential elections. Using the historical data from the 2017 election as well as data on employment and security, the model will be trained to predict the outcome of the 2022 elections.

The datasets for the model will be sourced per each French department to capture more localized influences on the election outcomes. Data from the five years preceding the election years will be used to understand trends and patterns that could impact the elections.

## [Data Sources](docs/Datasets.md)

1. **Election Data**: Historical data from the 2017 French Presidential Election organized by departement and constituencies (circonscriptions) as well as a twin dataset but from the 2022 French Presidential Election.
2. **Employment Data**: The annual "Besoins en Main-d'Œuvre" (BMO) survey data for the years 2015-2022. This dataset contains information about recruitment needs based on industry sector and employment basin for approximately 1.9 million French establishments organized per each French department. 
3. **Security Data**: Data from the Service statistique ministériel de la sécurité intérieure (SSMSI) for the years 2011-2022. This dataset includes several statistical indicators related to crimes, offenses, violation rates, and public sentiment towards security, this dataset is also organized per each French department.

## [Methodology](docs/Strategy.md)

1. **Data Collection & Preprocessing**: Collect the data from the sources mentioned above and perform necessary cleaning and preprocessing steps. This would include dealing with missing values, handling outliers, feature encoding, etc.

2. **Exploratory Data Analysis**: Analyze the datasets to understand the distribution, correlation and potential influence of the variables on the election outcomes.

3. **Model Building & Training**: Use machine learning algorithms to build a predictive model. This model will be trained on the 2017 datasets.

4. **Model Validation & Tuning**: Validate the performance of the model using appropriate metrics. Perform hyperparameter tuning if necessary.

5. **Prediction & Evaluation**: Use the trained model to predict the 2022 election results based on the 2022 datasets. Evaluate the performance of the model.

## Goals

The goal of the project is to build a predictive model that can accurately predict the outcome of the French presidential election based on the relevant employment and security factors. The model's performance will be assessed based on its accuracy in predicting the 2022 election results. This can potentially provide valuable insights into the interplay between local employment and security situations and their influence on election outcomes.
