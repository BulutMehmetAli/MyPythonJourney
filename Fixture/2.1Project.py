class DoubleRoundRobinLeague:
    def __init__(self, teams):
        self.teams = teams
        # If the number of teams is odd, add "Bye" to make it even
        if len(self.teams) % 2 != 0:
            self.teams.append("Bye")
        self.total_teams = len(self.teams)
        self.weeks = self.total_teams - 1  # Number of weeks in the first half
        self.matches = []  # All matches will be stored here

    def create_matchups(self):
        #Copy the teams
        teams = self.teams[:]
        for week in range(self.weeks):
            weekly_matches = []
            for i in range(self.total_teams // 2):
                home_team = teams[i]
                away_team = teams[-(i + 1)]
                weekly_matches.append((home_team, away_team))
            self.matches.append(weekly_matches)
            # Rotate teams using round-robin algorithm
            teams = [teams[0]] + teams[-1:] + teams[1:-1]

        second_half = []
        for weekly_matches in self.matches:
            # Reverse home and away teams for the second half of the league
            reversed_matches = [(away_team, home_team) for home_team, away_team in weekly_matches]
            second_half.append(reversed_matches)

        # Add the second half of the league to the matches
        self.matches.extend(second_half)

    def display_matches(self):
        for week, weekly_matches in enumerate(self.matches, start=1):
            print(f"Week {week}:")
            for home, away in weekly_matches:
                print(f"  {home} vs {away}")
            print()

# Usage
teams_list = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6", "Team 7"]
league = DoubleRoundRobinLeague(teams_list)
league.create_matchups()
league.display_matches()