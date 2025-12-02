# Estimating a Model that Beats the Sports Betting Market 
# Final Project Data Analysis with Python \ University of Zürich
## Project Motivation
In a period where the stock market seems increasingly uncertain and also highly efficient, since information is immediately absorbed, it leaves little room for exploitable inefficiencies. Therefore, I am interested in exploring markets where pricing might be less perfect, and as I am highly interested in sports, I wanted to see whether it would be possible to develop a model that structurally beats the bookmakers, due to public biases, emotional sentiment, or slower information adjustment. Although many people argue that the bookmakers have implemented all available data, to make sure that there are no arbitrage opportunities, I believe that bookmakers adjust their odds based on what bets people place, and as gamblers often tend to make reckless bets, fully grounded on either current feelings or emotional sentiment, I am convinced that the bookmakers do not perfectly price the odds, such that there should be a way to develop a model that beats this market. This project aims to investigate whether a data-driven and statistically grounded model applied to data from both the Dutch and the English football league can identify these inefficiencies and make structural money out of the betting market, contrary to the common view that gamblers always lose, and bookmakers always win. Furthermore, my second hypothesis is that the betting market on the premier league is more competitive, with more companies overcutting each others' odds, due to the insane popularity of the league all over the world. Therefore, I asssume that, in general, it should be more profitable to bet on premier league matches than on Eredivisie matches from the Netherlands. 
## Project Description
### Key Questions Answered by This Project
- Are there any patterns in winning/losing probabilities for teams when leading/losing at half time, and are there differences for home vs away?
- To what extent does match statistics like shots and shots on target say anything about the likelihood of the match outcomes?
- Is there any relationship between the amount of corners per team and the probability of each team?
- To what extent does my model outperform the betting market?
- Which league is more profitable to bet on?

### Data Overview
Data imported from football-data.co.uk
Links to datasets:
```md
[DutchLeague](https://www.football-data.co.uk/netherlandsm.php)
[EnglishLeague](https://www.football-data.co.uk/englandm.php)
- Data from season 2020/2021 until 2024/2025, 5 seasons in total
- 1530 games for dutch league, 1900 games for premier league
### Main Variables
Link to list of all variables:
```md
[VariableList](https://www.football-data.co.uk/notes.txt)
Most important variables for model: FTR (Full Time Result), HomeTeam, Awayteam, 1XB odds and bet365 odds for comparison with bookmakers
### Key Technical Steps
