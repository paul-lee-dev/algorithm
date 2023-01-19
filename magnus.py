line = input()
flag0 = 0
flag1 = 0
flag2 = 0
total = 0

for c in line:
	flag3 = 0
	if c == 'H':
		flag0 = 1
	if c == 'O' and flag0 == 1:
		flag1 = 1
	if c == 'N' and flag1 == 1:
		flag2 = 1
	if c == 'I' and flag2 == 1 and flag3 == 0:
		flag3 == 1		
		total = total + 1
		flag0 = 0
		flag1 = 0
		flag2 = 0
print(total)