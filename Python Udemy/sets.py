a = {"apple", "banana", "cherry","apple"}
print(a)

b={1,3,4,5,6,67,8}
for i in b:
    print(i)

print(12 in b)
print(1 in b)

c={"star trek","star wars","halo"}
c.add("mass effect")
print(c)
c.remove("mass effect")
print(c)

d={1,3,4,5,8}
e={6,7,8,9}
f=d.union(e)
print(f)
g=d.intersection(e)
print(g)