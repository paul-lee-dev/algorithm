P = int(input())
B = int(input())
D = int(input())

total = (P // B) * D
total = total + (P % B)
print(total)
