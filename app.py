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
  return panthers, bandits, warriors
#display team's name
# total number of players on that team
# player's names on that team

teams = balance_teams()


def create_menu():
   print("Basketball team stats tool \n *** Menu *** \n Here are your choices: \n A) Display team stats \n B) Quit")
   first_option = input("Enter an option  ")
   # if user chooses A - display teams names
   # Ask user to pick team A, B or C
   if first_option.lower() == "a":
      #display_stats()
      print("A) Panthers \n B) Bandits \n C) Warriors")
      team_choice = input("Enter an option  ")
      teams = balance_teams()
      if team_choice.lower() == "a":
        #display stats of Panthers
        print("Panthers \n ------ Stats")
        display_stats(teams[0])
      elif team_choice.lower() == "b":
        #display stats of Bandits
        display_stats(teams[1])
      else: 
        #display stats of Warriors
        display_stats(teams[2])
      
      
   # Display team stats that the user picked
   print("Press Enter to continue")

#loops through a team and outputs the player names in a list
def showPlayerName(team):
  player_names = []
  for player in team:
    player_names.insert(0, player['name'])

  return player_names

#function to display the team stats
def display_stats(team):
   #how to show the team name?
   print(team, "stats \n ----------")
   print("Total Players: ", len(team))
   #Loop through team and display names
   print("Players on the team:")

#display_stats(constants.PLAYERS)

if __name__ == "__main__":
    clean_data(constants.PLAYERS)
    balance_teams()
    create_menu()