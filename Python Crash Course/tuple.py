#IMMUTABLE LIST
dimensions = (200, 50)

print(dimensions[0]) #200

dimensions[0] = 250 # ERROR TUPLE IS IMMUTABLE

for dimension in dimensions:
  print(dimension) 
''' 
200
50
'''
