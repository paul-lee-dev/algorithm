line = input()
status = 1
for swap_type in line:
	if swap_type == 'A' and status == 1:
		status = 2
	elif swap_type == 'A' and status == 2:
		status = 1
	elif swap_type == 'B' and status == 2:
		status = 3
	elif swap_type == 'B' and status == 3:
		status = 2
	elif swap_type == 'C' and status == 1:
		status = 3
	elif swap_type == 'C' and status == 3:
		status = 1
print(status)