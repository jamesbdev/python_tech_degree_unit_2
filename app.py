import constants
import copy

#print(constants.TEAMS)
#print(constants.PLAYERS)

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



if __name__ == "__main__":
    print("hello world")
    clean_data(constants.PLAYERS)