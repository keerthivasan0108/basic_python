x=["karthik","keerthi","gokul"]
y=x[1:2]
print(y)  # its prints index 1 to 2 from list x
x.append("raja")
print(x)   # append a new value in list x
x.pop(3)
print(x)
z=len(x)
print(z)
a=max(x)
print(a)
b=min(x)
print(b)
t=(1,2,3,"k")
j=list(t)
print(j)
f=[12,308,"jh","h"]
h=[13,456,"fgh","ss"]
f.extend(h)
print(f)
s=[1233,24,56,56,"k","d","l"]
u=s.count(56)
print(u)
s.insert(2, 1998)
print(s)
i=s.index(24)
print(i)
s.remove(56)
print(s)
s.reverse()
print(s)
l=[12,1,3,56,43,65,0]
o=["s","d","f","a"]
l.sort()
print(l)
o.sort()
print(o)