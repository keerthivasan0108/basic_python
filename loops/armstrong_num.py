a = int (input("enter a number : "))
c = a
f = 0
while True :
    b = a % 10
    a = a // 10
    k = b**3
    f += k
    if a>0:
        continue
    else:
        break
if c == f:
    print("{0},is armstrong number".format(c))
else:
    print("{0} is not armstrong number".format(c))