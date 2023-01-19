burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger == 1:
	total = 461
elif burger == 2:
	total = 431
elif burger == 3:
	total = 420
else:
	total = 0

if side == 1:
	total = total + 100
elif side == 2:
	total = total + 57
elif side == 3:
	total = total + 70

if drink == 1:
	total = total + 130
elif drink == 2:
	total = total + 160
elif drink == 3:
	total = total + 118

if dessert == 1:
	total = total + 167
elif dessert == 2:
	total = total + 266
elif dessert == 3:
	total = total + 75
print('Your total Calorie count is ' + str(total) + '.')
