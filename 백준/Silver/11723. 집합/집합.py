import sys
input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
S = 0

for _ in range(M):
    cmd = input().strip().split()

    if cmd[0] == "add":
        S |= (1 << int(cmd[1]))
    elif cmd[0] == "remove":
        S &= ~(1 << int(cmd[1]))
    elif cmd[0] == "check":
        write('1\n' if S & (1 << int(cmd[1])) else '0\n')
    elif cmd[0] == "toggle":
        S ^= (1 << int(cmd[1]))
    elif cmd[0] == "all":
        S = (1 << 21) - 1
    elif cmd[0] == "empty":
        S = 0