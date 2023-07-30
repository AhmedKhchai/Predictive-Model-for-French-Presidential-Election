import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Load the data
df = pd.read_csv('datasets/security-historic-dataset.csv', encoding='latin1')

# Checking unique values in 'Zone_geographique' column:
print(df['Zone_geographique'].value_counts())
# France métropolitaine    4034
# France                   1704
# 69-Rhône                  206
# 71-Saône-et-Loire         203
# 70-Haute-Saône            203
#                          ...
# 12-Aveyron                196
# 11-Aude                   196
# 10-Aube                   196
# 09-Ariège                 196
# 11-Île-de-France           98

# Checking unique values in 'Periodicite' column:
print(df['Periodicite'].value_counts())
# Annuelle         21276
# Mensuelle         3568
# Trimestrielle      812

# Checking unique values in 'Unite_de_compte' column:
print(df['Unite_de_compte'].value_counts())
# Victimes                       9022
# Infractions                    7471
# Véhicules                      5367
# Mis en cause                   3257
# Ménages victimes                185
# Atteintes                       174
# victimes                         60
# Personnes de 14 ans ou plus      45
# Procédure                        30
# Victime                          30
# Checking unique values in 'Indicateur' column:
print(df['Indicateur'].value_counts())
# Vols et tentatives de vols liés aux véhicules                       5549
# Violences physiques                                                 4748
# Vols et tentatives de vols avec violence                            3643
# Infractions à la législation sur les stupéfiants                    3078
# Cambriolages et tentatives                                          1916
# Violences sexuelles                                                 1896
# Vols et tentatives de vols sans violence                            1847
# Destructions et dégradations volontaires                            1798
# Escroqueries et autres infractions assimilées                        349
# Atteintes envers les animaux domestiques                             180
# Homicides                                                            127
# Traite et exploitation des êtres humains                              90
# Actes de vandalisme                                                   60
# Atteintes à l'environnement                                           54
# Violences conjugales                                                  48
# Outrages sexistes                                                     46
# Sentiment d'insécurité                                                45
# Outrages et violences contre dépositaires de l'autorité publique      44
# Atteintes à la probité                                                36
# Vols sans effraction de résidences principales                        30
# Atteintes anti LGBT+                                                  21
# Atteintes à caractère raciste, xénophobe ou antireligieux             21
# Injures                                                               15
# Menaces                                                               15

# TODO (DATA CLEANING):
# - Convert the 'Unite temps' column to a more readable format.
# - Create a new column called 'Year' that contains the year of the 'Unite temps' column.
# - Create a new column called 'Month' that contains the month of the 'Unite temps' column.
# - Correct the 'Zone_geographique' column values to remove the numbers and the '-' at the beginning of the string.
# - Correct the 'Unite_de_compte' column values by making them all lowercase and making all values containing 'victime' to 'victime'.
# TODO (EDA VISUALISATIONS):
# - Using streamlit, create a visualisation that shows the number of crimes committed in each geographical area.
# - Using streamlit, create a visualisation that shows the Indicateur column as a pie chart per the selected geographical area.
# - Using streamlit, create a visualisation that shows the number of crimes committed per year and per month for the selected geographical area.


# Create a more readable format for 'Unite temps' column
# df['Unite temps'] = pd.to_datetime(df['Unite temps'])


def main():
    st.title("Historic Security Data Analysis")

    # User selection for geographical area
    geo_area = st.selectbox(
        "Select a Geographical Area", options=df['Zone_geographique'].unique()
    )

    # Subset of data for the selected geographical area
    df_geo = df[df['Zone_geographique'] == geo_area]



if __name__ == "__main__":
    main()
