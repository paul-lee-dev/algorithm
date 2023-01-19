line = input()
happy = line.count(':-)')
sad = line.count(':-(')

if sad == happy == 0:
	print('none')
elif sad == happy:
	print('unsure')
elif sad > happy:
	print('sad')
else:
	print('happy')