seq = input()
n = len(seq)
c_dur = 0
a_mol = 0

if seq[0] in 'CFG':
    c_dur = 1
elif seq[0] in 'ADE':
    a_mol = 1

for i in range(1, n):
    if seq[i-1] == '|':
        if seq[i] in 'CFG':
            c_dur = c_dur + 1
        elif seq[i] in 'ADE':
            a_mol = a_mol + 1

if c_dur > a_mol:
    print('C-dur')
elif c_dur < a_mol:
    print('A-mol')
else:
    if seq[-1] in 'CFG':
        print('C-dur')
    elif seq[-1] in 'ADE':
        print('A-mol')
