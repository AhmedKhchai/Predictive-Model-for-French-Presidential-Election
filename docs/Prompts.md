## Project Description

Based on the historical data of the 2017 presidential French election we would like to create a prediction model that would be trained on the 2017 election data as well a few other datasets concerning employment and security. The datasets need to be per each French department. The goal is to predict the outcome of the 2022 based on the employment and security datasets of 2022 
**Tasks**:
	Help find adequate (elections-employment-security) datasets for the 2017 and 2022
	Plan step to build and train my model based on the 2017 datasets and compare the output to the 2022 datasets  

## EDA

Lets run EDA on the The election dataset of the French Presidential Elections of 2017. The dataset presents a granular view of the voting behaviour across different regions in France, and it includes information about the total number of registered voters, the voter turnout, the number of abstentions, and the votes received by each candidate. It can be used to study the spatial distribution of votes, understand regional political preferences, and analyse voting trends over the two election years.
	**Task:**
		You should give me an overall plan, then we can go through step-by-step. In each step you should write some code and I will run it in the terminal then report back to you the results.

### Column Descriptions

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



