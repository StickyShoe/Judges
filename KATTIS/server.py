h = raw_input().split()
m = int(h[0])
t = int(h[1])
j = raw_input().split()
i = 0
su = 0
while su <= t and i < m:
    su = su + int(j[i])
    i = i + 1
if i == m:
  if su <= t:
    print i
  elif su > t:
    print i -1
else:
    print i - 1 