# Estimating a Model that Beats the Sports Betting Market 
# Final Project Data Analysis with Python \ University of Zürich

## Link to [Streamlit](https://finalprojectsimondawp.streamlit.app/)

## Project Motivation
In a period where the stock market seems increasingly uncertain and also highly efficient, since information is immediately absorbed, it leaves little room for exploitable inefficiencies. Therefore, I am interested in exploring markets where pricing might be less perfect, and as I am highly interested in sports, I wanted to see whether it would be possible to develop a model that structurally beats the bookmakers, due to public biases, emotional sentiment, or slower information adjustment. Although many people argue that the bookmakers have implemented all available data, to make sure that there are no arbitrage opportunities, I believe that bookmakers adjust their odds based on what bets people place, and as gamblers often tend to make reckless bets, fully grounded on either current feelings or emotional sentiment, I am convinced that the bookmakers do not perfectly price the odds, such that there should be a way to develop a model that beats this market. This project aims to investigate whether a data-driven and statistically grounded model applied to data from both the Dutch and the English football league can identify these inefficiencies and make structural money out of the betting market, contrary to the common view that gamblers always lose, and bookmakers always win. Furthermore, my second hypothesis is that the betting market on the premier league is more competitive, with more companies overcutting each others' odds, due to the insane popularity of the league all over the world. Therefore, I asssume that, in general, it should be more profitable to bet on premier league matches than on Eredivisie matches from the Netherlands. 
## Project Description
### Key Questions Answered by This Project
- Are there any patterns in winning/losing probabilities for teams when leading/losing at half time, and are there differences for home vs away?
    - Most teams have more success in remaining their half-time lead when playing at home than away
    - some outliers are teams that have only played in the league for one season, and only were leading at half-time once when playing away. 
    - Also for losing, a team has a higher probability to turn things around when playing at home, this could be the most important measure of home advantage, the ability to keep the lead or turn it around, supported by their fan base.
- To what extent does match statistics like shots and shots on target say anything about the likelihood of the match outcomes?
    - Looking at the Match Dominance Arena, it becomes clear that there exists quite a strong relationship between both shots and shots on targets difference and final result, although outliers always exist. 
    - Shots on Target is a stronger predictor for final result, but hard to compare, since each shot is a shot on target, but the vice versa relationship does not hold.
    - Something I assume bookmakers already incorporate in their models
- Is there any relationship between the amount of corners per team and the probability of each team?
    - Interesting to see that corners is almost no predictor at all, coefficient only 0.07 for Dutch League 
    - Away teams tend to win more often when having a significant corner deficit, while for the home team this does not hold
- To what extent does my model outperform the betting market?t
    - Straightforward model, where I assume that the strength of each team depends for 50% on the current season's form, and the other 50% on the 5-year average
    - For Dutch league, ROI = 2.21% for 1xBet, and 1.61% for Bet 365. 
    - For English League, ROI = 11.11% for 1xBet and 6.06% for Bet365
- Which league is more profitable to bet on?
    - Based on my model, Premier League is much more profitable for betting
    - In both cases, 1xBet significantly outperforms Bet365
    - Although betting is characterized by a high standard deviation, applying the law of large numbers, since you have 380 games per season, should make it quite stable to bet. 
### Data Overview
Data imported from football-data.co.uk
Links to datasets:
[DutchLeague](https://www.football-data.co.uk/netherlandsm.php)
[EnglishLeague](https://www.football-data.co.uk/englandm.php)

- Data from season 2020/2021 until 2024/2025, 5 seasons in total
- 1530 games for dutch league, 1900 games for premier league
### Main Variables
Link to list of all variables:
[VariableList](https://www.football-data.co.uk/notes.txt)

Most important variables for model: FTR (Full Time Result), HomeTeam, Awayteam, 1XB odds and bet365 odds for comparison with bookmakers
## Key Technical Steps

### Data Cleaning
- For the Premier League dataset, I had to convert the date and time variable to the same format as for the dutch league version, to be able to sort the values and compare the datasets
- Furthermore, I had to generate a new variable called "winner" by combining the hometeam/awayteam variables with the value in the full-time result column (FTR)
- For the first visualization about half-time and full-time results, I generated a new, binary variable called "HT_leader", equalling 1 for the home team if the home team goals at half time (HTHG) is larger than the away team goals (HTAG)
- I created some difference variables, for example shot difference, where I subtract the away team shots (AS) from the home team shots (HS)

### Data Analysis
- I regressed my independent variables on my dependent variable 'HomeWin'
- for my final model, I sorted games based on seaons, rather than on years, by defining a season as starting from July onwards, so if the month variable is larger or equal to 7. 
- I then computed average points per season, to demonstrate each team's seasonal performances, such that I could incorporate this in my model, where I assigned the probability of winning of being dependent equally on long-term performances and seasonal performances (both 50% weight)
- I generated variables for bookmaker probabilities, simply by dividing 1 with the bookmaker odds, since odds and probabilities are inversely related in a perfect market. 
- In the model, I implemented that I always and only bet when the model predicts higher probabilities than the bookmakers, and I found that this would have been a profitable strategy for the last 5 seasons.
### Data Visualization
- I used plotly to make the graphs, since it allows for interactive visualizations
- I used pickle to do the complicated code only in Jupyter notebook, such that I could keep my python file structured and easily to interpret for my streamlit
