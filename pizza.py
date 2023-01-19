width = int(input())
cheese = int(input())

if (width == 3) and (cheese >= 95):
    M = 'absolutely'
elif (width == 1) and (cheese <= 50):
    M = 'fairly'
else:
    M = 'very'

print('C.C. is ' + M + ' satisfied with her pizza.')
