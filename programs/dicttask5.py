teams = {
          "TeamA": [
              {"name": "Alice", "role": "Batsman"},
              {"name": "Bob", "role": "Bowler"}
          ],
          "TeamB": [
              {"name": "Charlie", "role": "Allrounder"},
              {"name": "Dave", "role": "Wicketkeeper"}
          ]
      }

for team,playerinfo in teams.items():
    print(team)
    print("------------------")
    for data in playerinfo:
        print(data['name'])
    print()