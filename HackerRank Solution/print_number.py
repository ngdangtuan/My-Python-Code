def print_numbers():
	print(*range(1, int(input())+1), sep='')
print_numbers()

#Another solution
n = int(input())
def print_numbers(n):
    numbers = list(range(1, n+1))
    return ''.join(str(i) for i in numbers)
print(print_numbers(n)
