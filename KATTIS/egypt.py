k = raw_input()
while k != "0 0 0":
    k = k.split(" ")
    k[0] = int(k[0])
    k[1] = int(k[1])
    k[2] = int(k[2])
    k.sort()
    if ((k[0] **2) + (k[1]**2)) == (k[2]**2):
        print "right"
    else:
        print "wrong"
    k = raw_input()