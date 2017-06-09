#INSERT
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) #['ducati', 'honda', 'yamaha', 'suzuki']


#REMOVE USING DEL
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles) #['honda', 'suzuki']


#REMOVE USING POP
motorcycles = ['honda', 'yamaha', 'suzuki']
poppedMotorcycle = motorcycles.pop()
print(motorcycles) #['honda', 'yamaha']
print(poppedMotorcycle) #suzuki
#Popping Items from any Position in List
firstOwned = motorcycles.pop(0)
print(firstOwned) #honda


#REMOVE USING REMOVE
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
tooExpensive = 'ducati' #store the value 'ducati' to reuse
motorcycles.remove(tooExpensive)
print(motorcycles) #['honda', 'yamaha', 'suzuki']
print("A" + tooExpensive.title() + " is too expensive for me.") #A Ducati is too expensive for me.


#CLEAR ( Equivalent to del a[:] )
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.clear()
print(motorcycles) #[]




# SORT A LIST
#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']
#Sorting a List Temporarily with the sorted() Function
print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars, reverse=True)) #['toyota', 'subaru', 'bmw', 'audi']


#REVERSE A LIST
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars) #['subaru', 'toyota', 'audi', 'bmw']
#== print(list(reversed(cars)))


#EXTEND A LIST
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.extend(['lamborghini', 'chevrolet'])
print(cars) #['bmw', 'audi', 'toyota', 'subaru', 'lamborghini', 'chevrolet']
      

#INDEX
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars.index('audi')) #1      


#COUNT
cars = ['bmw', 'audi', 'toyota', 'subaru', 'bmw']
print(cars.count('bmw')) #2

# USING RANGE MIN MAX SUM
#generate a series of numbers
for value in range(1,5):
  print(value)
''' 
result:
1
2
3
4 
'''
# range(0,n) == range(n)
                                       ########################################################
#Using range() to Make a List of Numbers (using the list() function)
evenNumbers = list(range(2,11,2))
print(evenNumbers) #[2, 4, 6, 8, 10]
#range(start,end,step)

#More:
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#more concisely
print([value**2 for value in range(1,11)])
#or 
squares = [value**2 for value in range(1,11)]
print(squares)
                                     ########################################################
#find the minimum, maximum, and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits) #0
max(digits) #9
sum(digits) #45


# SLICE AND COPY A LIST
#SLICING
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #['charles', 'martina', 'michael']
#Without a starting index, Python starts at the beginning of the list:
print(players[:4]) #['charles', 'martina', 'michael', 'florence']

print(players[2:] #['michael', 'florence', 'eli']

print(players[-3:] #['michael', 'florence', 'eli']
#[start:end:step]

      
#COPY
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
#NOTE: THIS DOESN'T WORK friend_foods = my_foods    
#ANOTHER WAY      
friend_foods = my_foods.copy()

      
# LIST COMPREHENSIONS
      
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]) #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#it’s equivalent to
combs = []
for x in [1,2,3]:
      for y in [3,1,4]:
            if x != y:
                  combs.append((x, y))

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem] #[1, 2, 3, 4, 5, 6, 7, 8, 9]

from math import pi
[str(round(pi, i)) for i in range(1, 6)] #3.1', '3.14', '3.142', '3.1416', '3.14159']
