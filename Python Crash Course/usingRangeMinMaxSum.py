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
