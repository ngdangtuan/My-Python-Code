def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return leap

#More concisely

def is_leap(year):
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
