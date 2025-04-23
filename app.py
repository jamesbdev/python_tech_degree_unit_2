import constants
import copy


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
      dictionary['guardians'] = dictionary['guardians'].split('and')
    #return the new list
    return players_copy

# balance teams function
# adds equal amount of players to the 3 teams
# creates a variable for each team
def balance_teams():
  num_players_teams = int(len(constants.PLAYERS) / len(constants.TEAMS))
  
  full_team = clean_data(constants.PLAYERS)
  experienced_players = []
  unexperienced_players = []

  for player in full_team:
     if player['experience'] == True:
        experienced_players.append(player)
     else:
        unexperienced_players.append(player)
  
  # divide experienced players equally in the three teams

  panthers = [experienced_players[i] for i in range(0, 3 )]
  bandits = [experienced_players[i] for i in range(3, 6)]
  warriors = [experienced_players[i] for i in range(6, 9)]
  
  # add unexperienced players evenly between the three teams
  for player in unexperienced_players:
     if len(panthers) < num_players_teams:
        panthers.append(player)
     elif len(bandits) < num_players_teams:
        bandits.append(player)
     else:
        warriors.append(player)
  # add functionality to balance teams taking into account experience
  return panthers, bandits, warriors


teams = balance_teams()

# Set a variable to track if user wants to quit
#player_quit = False

# function that creates the menu
def create_menu():
   has_exited = False
   print("BASKETBALL TEAM STATS TOOL \n \n ******* Menu ******** \n \n Here are your choices: \n \n 1) Display team stats \n 2) Quit \n")
   first_option = input("Enter an option  ")
   # if user chooses 1 - display teams names
   # Ask user to pick team 1, 2 or 3
   if first_option == "1":
      #display_stats()
      print("1) Panthers \n2) Bandits \n3) Warriors")
      team_choice = input("Enter an option  ")
      teams = balance_teams()
      if team_choice == "1":
        #display stats of Panthers
        print("Team: Panthers Stats \n-----------")
        display_stats(teams[0])
      elif team_choice == "2":
        #display stats of Bandits
        print("Team: Bandits Stats \n----------")
        display_stats(teams[1])
      elif team_choice == "3": 
        #display stats of Warriors
        print("Team: Warriors stats \n----------")
        display_stats(teams[2])
      else:
        print("Sorry please choose an option between 1, 2 and 3")
   elif first_option == "2":
      print("user has quit")
      return True

   print("Press Enter to continue")
   return False
 

#helper function to store players names in a list
def showPlayerName(team):
  player_names = []
  for player in team:
    player_names.insert(0, player['name'])

  return player_names

#helper function to display the team stats
def display_stats(team):
   num_of_players = len(team)
   num_of_experienced_players = 0
   num_of_inexperienced_players = 0
   average_height = round(calculate_avg_height(team), 2)

   for player in team:
      if player['experience'] == True:
         num_of_experienced_players += 1
      else:
         num_of_inexperienced_players += 1
            
   print("Total Players: ", num_of_players)
   #Loop through team and display names
   print("total inexperienced players", num_of_inexperienced_players)
   print("total experienced players", num_of_experienced_players)
   print(f"The average player's height is {average_height} inches \n")

   print("Players on the team: ")
   # get list of names 
   player_names = showPlayerName(team)
   # loop through list of names to output each player's name
   for i in range(num_of_players -1 ):
      print(player_names[i], end = ", ")
   print(player_names[num_of_players -1])
   print("\n")
   guardians = []
   flattened_list = []
   print("Guardians:")
   for player in team: 
      guardians.append(player['guardians'])
   for guardian in guardians:
     flattened_list.extend(guardian)
   
   #Remove white space from guardian flattened list
   stripped_list = [item.strip() for item in flattened_list]

   # Join the list in a comma separated string
   guardians_string = ', '.join(stripped_list)
   print(guardians_string)

 
def display_guardians(team):
   guardians = []
   for player in team:
      guardians.append(player['guardians'])
   print(guardians) 

#helper function to calculate the average player height
def calculate_avg_height(team):
   # get players height
   heights = []
   for player in team:
      heights.append(player['height'])
   player_avg_height = sum(heights) / len(heights)
   return player_avg_height
   # make average calculation 
   # return average height
   


if __name__ == "__main__":
    clean_data(constants.PLAYERS)
    balance_teams()
    player_quit = False    
    while not player_quit:
     player_quit = create_menu()
    
   
    
    