#SLICING
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #['charles', 'martina', 'michael']
#Without a starting index, Python starts at the beginning of the list:
print(players[:4]) #['charles', 'martina', 'michael', 'florence']

print(players[2:] #['michael', 'florence', 'eli']

print(players[-3:] #['michael', 'florence', 'eli']

#[start:end:step]

#COPY
myFoods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
#NOTE: THIS DOESN'T WORK friend_foods = my_foods

			
