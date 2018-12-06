s3 = raw_input()
j = 0
while s3[j] != " ":
    j = j + 1
s1 = float(s3[:j])
s2 = float(s3[j + 1:])
r = (s1 / 3.14) ** 0.5
po = (2 * s1) / r
if s2 > po:
    print "Diablo is happy!"
else:
    print "Need more materials!"

