n = input()
i = 0
a = []
win = 0
while i < n:
  a.append(raw_input())
  t = a[i]
  a[i] = a[i].replace("CD","E")
  if len(t) == len(a[i]):
    win = win + 1
  i = i + 1
print win