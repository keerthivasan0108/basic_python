a= {"name": "keerthi", "age": 17, "class": "first"}
print(a["name"])
a["age"]=18
print(a)
a["school"]="govt"
print(a)
del a["name"]
print(a)
a.clear()
print(a)
f=a.copy()
print(f)
a.update({"swiggie":"pizza"})
print(a)
s=a.get("swiggie")
print(s)
w= {"name": "keerthi", "age": 17, "class": "first"}
w.items()
print(w)
e=w.values()
print(e)