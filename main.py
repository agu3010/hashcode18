lines = [line.rstrip('\n') for line in open('a_example.in')]
print lines
info = lines.pop(0).split()

R = int(info[0])
C = int(info[1])
F = int(info[2])
N = int(info[3])
B = int(info[4])
T = int(info[5])


print R
print C
print F
print N
print B
print T
