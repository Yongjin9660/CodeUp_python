a = input()
a = ord(a) + 32
a = chr(a)
a = int(a,16)

i=1
while i < 16:
    print("%X*%X=%X" % (a, i, a*i))
    i+=1