#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']
#Sorting a List Temporarily with the sorted() Function
print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars, reverse=True)) #['toyota', 'subaru', 'bmw', 'audi']
