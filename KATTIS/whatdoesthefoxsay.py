n = input()
i = 0
while i < n:
  r = raw_input().split()
  a = []
  l = raw_input()
  while l != "what does the fox say?":
    l = l.split()
    a.append(l[len(l) - 1])
    l = raw_input()
  k = 0
  pok = ""
  while k < len(r):
    if r[k] not in a:
      pok = pok + " " + r[k]
    k = k + 1
  print pok
  i = i + 1