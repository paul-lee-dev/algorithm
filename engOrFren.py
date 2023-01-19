n = int(input())
t_count = 0
s_count = 0

for i in range(n):
    line = input()
    t_count = t_count + line.count('t')
    t_count = t_count + line.count('T')
    s_count = s_count + line.count('s')
    s_count = s_count + line.count('S')

if t_count <= s_count:
    print('French')
else:
    print('English')
