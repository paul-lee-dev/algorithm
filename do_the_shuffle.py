btn = 0
line = 'ABCDE'

while btn != 4:
    btn = int(input())
    num = int(input())
    if btn == 1:
        for i in range(num):
            line = line[1:] + line[0]
    if btn == 2:
        for i in range(num):
            line = line[-1] + line[:4]
    if btn == 3:
        for i in range(num):
            line = line[1] + line[0] + line[2:]

output = ''
for song in line:
    output = output + song + ' '

print(output[:-1])
