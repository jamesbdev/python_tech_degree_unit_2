import constants
import copy


teams = constants.TEAMS 
players = constants.PLAYERS


#function to clean the Players data
def clean_data(list):
    # make a copy of the data 
    players_copy = copy.deepcopy(list)

    for dictionary in players_copy:
      # change height to integer
      dictionary['height'] = int(dictionary["height"].replace(" inches", ""))
      # change experience to boolean
      if dictionary['experience'] == 'YES':
         dictionary['experience'] = True
      else:
         dictionary['experience'] = False
    #return the new list
    return players_copy

#balance teams function
# adds equal amount of players to the 3 teams
# creates a variable for each team
def balance_teams():
  num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
  full_team = clean_data(constants.PLAYERS)
  panthers = [full_team[i] for i in range(6)]
  bandits = [full_team[i] for i in range(6, 12)]
  warriors = [full_team[i] for i in range(12, 18)]
  

if __name__ == "__main__":
    clean_data(constants.PLAYERS)
    balance_teams()