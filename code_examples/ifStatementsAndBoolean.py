#Checking for Equality
car = 'bmw'
car == 'bmw' #True
car == 'sudi' #False

#Ignoring Case When Checking for Equality
car = 'Audi'
car == 'audi' #False
car.lower() = 'audi' #True

#Checking for Inequality
requestedTopping = 'mushrooms'
if requestedTopping != 'anchovies': #True
    print("Hold the anchovies!") #Hold the anchovies!
    
#Numerical Comparisons:
age = 18
age == 18 #True
age != 18 #False
age < 21 #True
age <= 21 #True
age > 21 #False
age >= 21 #False

#Using and to Check Multiple Conditions (To check whether two conditions are both True simultaneously)
age0 = 22
age1 = 18
age0 >= 21 and age1 >= 21 #False 

#Using or to Check Multiple Conditions
age0 = 22
age1 = 18
age0 >= 21 or age1 >= 21 #True
#It passes when either or both of the individual tests pass. An or expression
fails only when both individual tests fail.

#Checking Whether a Value Is in a List
requestedToppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requestedToppings #True
'pepperoni' in requested_toppings #False

#Checking Whether a Value Is Not in a List
bannedUsers = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in bannedUsers:
    print(user.title() + ",you can post a response if you wish.") 
    #Marie, you can post a response if you wish.



