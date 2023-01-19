password = input()
lower_num = 0
upper_num = 0
digit_num = 0
pl = len(password)

for type in password:
	if type.islower():
		lower_num = lower_num + 1
	elif type.isupper():
		upper_num = upper_num + 1
	else:
		digit_num = digit_num + 1

if (lower_num >= 3) and (upper_num >= 2) and (digit_num >= 1) and (pl <= 12) and (pl >= 8):
	print('Valid')
else:
	print('Invalid')		