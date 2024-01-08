import matplotlib.pyplot as plt
from scipy import stats


# Example usage:
team1 = [190, 195, 200, 210, 193]  # Heights of players from team 1
team2 = [185, 190, 195, 198, 189]  # Heights of players from team 2
team3 = [200, 205, 210, 215, 202]  # Heights of players from team 3


F, p = stats.f_oneway(team1, team2, team2)

print("F-value: ", F)
print("p-value: ", p)

# Visualization
plt.boxplot([team1, team2, team3], labels=["Team 1", "Team 2", "Team 3"])
plt.title("Heights of Basketball Players from Three Teams")
plt.ylabel("Height (cm)")
plt.show()
