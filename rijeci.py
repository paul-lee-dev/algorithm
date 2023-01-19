n = int(input())
A_num = 1
B_num = 0

for i in range(n):
    tmp = A_num
    A_num = B_num
    B_num = B_num + tmp

print(A_num, B_num)
