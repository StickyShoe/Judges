import math
n = raw_input()
while n != "0 0 0":
    n = n.split()
    a = math.pi * float(n[0]) * float(n[0])
    l = 0
    k = 4 * (float(n[2])/float(n[1]))
    a1 = k * float(n[0]) * float(n[0])
    t = str(a)
    if len(t) > 11:
        t = t[:12]
        if int(t[-1]) >= 5:
            a = t[:10] + str(int(t[-2]) + 1)
        else:
            a = t[:10] + str(int(t[-2]))
    o = int(a1)
    t = str(a1)
    if len(t) > 11:
        t = t[:12]
        if int(t[-1]) >= 5:
            a1 = t[:10] + str(int(t[-2]) + 1)
        else:
            a1 = t[:10] + str(int(t[-2]))
    if a1 == o:
        a1= o
    print a, a1
    n = raw_input()