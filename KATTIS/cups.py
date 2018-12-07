k = input()
i = 0
a = []
b = {}
while i < k:
    u = raw_input().split()
    if u[0][0] >= "a" and u[0][0] <= "z":
        b[int(u[1])] = u[0]
        a.append(int(u[1]))
    else:
        r = int(u[0]) / 2
        b[r] = u[1]
        a.append(r)
    i = i + 1
a.sort()
l = 0
while l < len(a):
    print b[a[l]]
    l = l + 1