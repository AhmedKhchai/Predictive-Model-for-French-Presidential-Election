# Datasets

## Elections:

The election dataset is a comprehensive collection of voting statistics for the French Presidential Elections of 2017 and 2022. Each row corresponds to a voting district, represented by a unique combination of the department and the electoral district number.

## Column Descriptions

1. **CodeCirco**: Unique code of the electoral district.
2. **Département**: Name of the French department.
3. **NumeroCirco**: Electoral district number.
4. **Circonscription**: Name of the electoral district.
5. **Inscrits**: Number of registered voters.
6. **Abstentions**: Number of people who abstained from voting.
7. **Abstentions_ins**: Ratio of abstentions to registered voters.
8. **Votants**: Number of voters.
9. **Votants_ins**: Ratio of voters to registered voters.
10. **Blancs**: Number of blank votes.
11. **Blancs_ins**: Ratio of blank votes to registered voters.
12. **Blancs_vot**: Ratio of blank votes to voters.
13. **Nuls**: Number of null votes.
14. **Nuls_ins**: Ratio of null votes to registered voters.
15. **Nuls_vot**: Ratio of null votes to voters.
16. **Exprimés**: Number of expressed votes.
17. **Exprimés_ins**: Ratio of expressed votes to registered voters.
18. **Exprimés_vot**: Ratio of expressed votes to voters.
19. **Candidate Names (ARTHAUD, ROUSSEL, MACRON, etc.)**: Number of votes received by each candidate.
20. **Candidate.ins (ARTHAUD.ins, ROUSSEL.ins, MACRON.ins, etc.)**: Ratio of votes received by each candidate to the number of registered voters.
21. **Candidate.exp (ARTHAUD.exp, ROUSSEL.exp, MACRON.exp, etc.)**: Ratio of votes received by each candidate to the number of expressed votes.

The dataset presents a granular view of the voting behaviour across different regions in France, and it includes information about the total number of registered voters, the voter turnout, the number of abstentions, and the votes received by each candidate. It can be used to study the spatial distribution of votes, understand regional political preferences, and analyse voting trends over the two election years.

## Security: 

#### Dataset Description

This dataset is derived from the chronology series base of the Ministerial Statistical Service of Internal Security (Service statistique ministériel de la sécurité intérieure - SSMSI). It encompasses a wide array of indicators pertinent to the areas of security and crime, ranging from minor offenses to severe criminal activities, as well as sentiments of insecurity among the population. The data is recorded at national and departmental levels across various time periods (monthly, quarterly, yearly). 

The indicators are diverse, encapsulating categories such as acts of vandalism, environmental offenses, offenses characterized by racism, xenophobia or anti-religious sentiments, anti-LGBT+ offenses, offenses against domestic animals, burglaries and attempts, voluntary destruction and degradation, fraud and related offenses, homicides, drug law offenses, insults, threats, violence against public authorities, sexist offenses, feelings of insecurity, human trafficking and exploitation, domestic violence, physical violence, sexual violence, thefts and attempts with violence, vehicle-related thefts and attempts, thefts and attempts without violence, and home invasions without break-ins.

Each indicator, in addition to its values, provides information about its source, periodicity, unit of account, and definition. This includes a link to a publication associated with it, directly downloadable from the SSMSI website.

#### Column Descriptions:

1. `Valeurs`: The count or frequency of the specific indicator during the given time period.
2. `Unite temps`: The time period for the data entry, provided in a Year-Month (YYYYMM) format.
3. `Indicateur`: The specific security-related indicator or category being tracked.
4. `Source`: The data source.
5. `SourceGraphique`: The graphical representation of the data source.
6. `Sous_indicateur`: A specific subcategory within the main indicator.
7. `Nomenclature`: The system or standard used for classifying the data.
8. `Declinaison`: Further classification of the data.
9. `Statistique`: The type of statistic being represented (in this case, a count or number).
10. `Zone_geographique`: The geographic area for which the data is relevant, for example, a specific department or metropolitan France as a whole.
11. `Champ`: The field of application for the data.
12. `Periodicite`: The frequency with which the data is recorded (monthly, quarterly, annually).
13. `Unite_de_compte`: The unit of measurement used for the data (e.g., individual incidents, vehicles, etc.)
14. `Correction`: Specifies whether the data series is raw or has been adjusted or corrected in any way.
15. `Description`: A detailed explanation of the indicator and its relevance. This often includes additional context or links to further resources.






## Employment:
*Source:* https://www.data.gouv.fr/fr/datasets/enquete-besoins-en-main-doeuvre-bmo/#/resources

#### Dataset Description:

The annual "Besoins en Main-d'Œuvre" (BMO) survey, or "Workforce Needs" survey, conducted by Pôle emploi is a vital tool for understanding the job market. The survey is sent to approximately 1.9 million establishments each year to gather information about their recruitment needs based on industry sector and employment basin. 

The data obtained from this survey serves to anticipate recruitment difficulties, improve the orientation of job seekers towards training or professions that meet the needs of the job market, and to inform job seekers about the evolution of their job market and promising professions.

Column Descriptions:

1. `annee`: The year the data was collected.
2. `code métier BMO`: The BMO occupation code.
3. `nom_metier BMO`: The name of the occupation according to the BMO classification.
4. `Famille_metier`: The code for the occupation's family or category.
5. `Libellé de famille de métier`: The name of the occupation's family or category.
6. `REG`: The INSEE code for the region.
7. `NOM_REG`: The name of the region.
8. `Dept`: The department number.
9. `NomDept`: The name of the department.
10. `BE21`: The code for the employment basin.
11. `NOMBE21`: The name of the employment basin.
12. `met`: The number of recruitment projects.
13. `xmet`: The number of recruitment projects considered difficult.
14. `smet`: The number of seasonal recruitment projects.

The dataset you're proposing to use covers each year from 2015 to 2022 and provides a comprehensive overview of recruitment needs and challenges across different sectors and regions in France. This should be a valuable addition to your predictive model.