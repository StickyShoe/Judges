n = input()
c = 1
d = 0
i = 0
while i < n:
    u = d
    d = d + c
    c = u
    i = i + 1
print str(c) + " " + str(d)