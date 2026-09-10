import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")


# Q1. Count total matches in 2008
matches_2008 = len(matches[matches['season'] == 2008])
print("1. Total matches in 2008:", matches_2008)

# Q2. Cities with max and min matches
city_counts = matches['city'].value_counts()
print("2. Max matches city:", city_counts.idxmax())
print("   Min matches city:", city_counts.idxmin())

# Q3. Total count of matches city-wise
print("3. Matches city-wise:\n", city_counts)

# Q4. Tally toss decisions taken by each team
toss_tally = matches.groupby(['toss_winner', 'toss_decision']).size().unstack(fill_value=0)
print("4. Toss decisions tally:\n", toss_tally)

# Q5. Count total normal and tied matches
results = matches['result'].value_counts()
print("5. Normal and tied matches:\n", results[['normal', 'tie']])

# Q6. Teams where result was a tie
tied_matches = matches[matches['result'] == 'tie']
tied_teams = set(tied_matches['team1']).union(set(tied_matches['team2']))
print("6. Teams in tied matches:", list(tied_teams))

# Q7. Team which won by highest and lowest number of runs
max_run_idx = matches['win_by_runs'].idxmax()
highest_team = matches.loc[max_run_idx, 'winner']

run_wins = matches[matches['win_by_runs'] > 0]
min_run_val = run_wins['win_by_runs'].min()
lowest_teams = run_wins[run_wins['win_by_runs'] == min_run_val]['winner'].unique()

print("7. Highest run win team:", highest_team)
print("   Lowest run win team:", list(lowest_teams))

# Q8. Mean, median, std of win_by_runs
runs_list = matches['win_by_runs']
print("8. Mean win by runs:", round(np.mean(runs_list), 2))
print("   Median win by runs:", np.median(runs_list))
print("   Std dev of win by runs:", round(np.std(runs_list), 2))

# Q9. Venue where team won by highest and lowest runs
highest_venue = matches.loc[max_run_idx, 'venue']
lowest_venues = run_wins[run_wins['win_by_runs'] == min_run_val]['venue'].unique()
print("9. Highest run win venue:", highest_venue)
print("   Lowest run win venue:", list(lowest_venues))

# Q10. Players who won Player of the Match more than 3 times
pom_counts = matches['player_of_match'].value_counts()
print("10. Players with > 3 POTM awards:\n", pom_counts[pom_counts > 3])

# Q11. Find all deliveries where batsman scored a six
sixes = deliveries[deliveries['batsman_runs'] == 6]
print("11. Total sixes scored:", len(sixes))

# Q12. Compute average runs scored in matches across all venues
match_totals = deliveries.groupby('match_id')['total_runs'].sum().reset_index()
merged_venues = match_totals.merge(matches[['id', 'venue']], left_on='match_id', right_on='id')
avg_venue_runs = merged_venues.groupby('venue')['total_runs'].mean()
print("12. Average runs per match venue-wise:\n", avg_venue_runs)

# Q13. Umpires who umpired maximum number of times
all_umpires = pd.concat([matches['umpire1'], matches['umpire2']]).dropna()
print("13. Most frequent umpire:", all_umpires.value_counts().idxmax())

# Q14. Total number of matches played in each season
season_matches = matches['season'].value_counts().sort_index()
print("14. Matches played per season:\n", season_matches)

# Q15. Total runs scored in each season
merged_seasons = deliveries.merge(matches[['id', 'season']], left_on='match_id', right_on='id')
season_runs = merged_seasons.groupby('season')['total_runs'].sum()
print("15. Total runs scored per season:\n", season_runs)

# Q16. Total runs scored by each batsman (Top 10)
top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().nlargest(10)
print("16. Top 10 batsmen by runs:\n", top_batsmen)

# Q17. Total wickets taken by each bowler (Top 10)
wicket_kinds = ['caught', 'bowled', 'lbw', 'stumped', 'caught and bowled', 'hit wicket']
wickets = deliveries[deliveries['dismissal_kind'].isin(wicket_kinds)]
top_bowlers = wickets.groupby('bowler').size().nlargest(10)
print("17. Top 10 wicket takers:\n", top_bowlers)

# Q18. Compute batting averages (Top 10, min 500 runs)
total_runs = deliveries.groupby('batsman')['batsman_runs'].sum()
total_outs = deliveries[deliveries['player_dismissed'].notnull()]['player_dismissed'].value_counts()
runs_500 = total_runs[total_runs >= 500]
bat_avg = runs_500 / total_outs
top_averages = bat_avg.nlargest(10)
print("18. Top 10 batting averages:\n", top_averages.round(2))

# Q19. Visualize toss decisions across all seasons
toss_season_df = matches.groupby(['season', 'toss_decision']).size().unstack()
toss_season_df.plot(kind='bar')
plt.title('19. Toss Decisions Across Seasons')
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()

# Q20. Visualize Total Matches vs Winning Matches vs Win Rate
played_count = matches['team1'].value_counts().add(matches['team2'].value_counts(), fill_value=0)
wins_count = matches['winner'].value_counts()
team_stats = pd.DataFrame({'Total': played_count, 'Wins': wins_count}).fillna(0)
team_stats['Win Rate'] = (team_stats['Wins'] / team_stats['Total']) * 100

fig, ax1 = plt.subplots()
team_stats[['Total', 'Wins']].plot(kind='bar', ax=ax1)
ax2 = ax1.twinx()
ax2.plot(team_stats.index, team_stats['Win Rate'], color='red', marker='o')
plt.title('20. Matches vs Wins vs Win Rate')
plt.show()

# Q21. Distribution of teams who won matches
winner_dist = matches['winner'].value_counts()
winner_dist.plot(kind='pie', autopct='%1.1f%%')
plt.title('21. Winning Teams Distribution')
plt.ylabel('')
plt.show()

# Q22. Visualize toss outcomes of all teams
toss_outcomes_df = matches.groupby(['toss_winner', 'toss_decision']).size().unstack()
toss_outcomes_df.plot(kind='bar', stacked=True)
plt.title('22. Toss Outcomes by Team')
plt.xlabel('Team')
plt.ylabel('Count')
plt.show()

# Q23. Visualize top 5 teams with most wins across seasons
top_5_winners = matches['winner'].value_counts().head(5)
top_5_winners.plot(kind='bar')
plt.title('23. Top 5 Teams with Most Wins')
plt.xlabel('Team')
plt.ylabel('Wins')
plt.show()