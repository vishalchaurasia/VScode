a=("a","b","c","d","e")
b=(2.432, False,[1,2,3])
c=(1,1,0,0,1)
print(a)
print(b)
print(c)

d=tuple([3.1,2.342,10])
e=tuple("afshjk")
print(d)
print(e)
print(d[2])

f=(1,2,3,4,5,6,7,8,9,10)
print(f[:8])
print(f[2:7])
print(f[2:])

g=("gkp","deos","bsb","vskp","ndls","anvt")
for i in g:
    print(i)

count=0
while count<len(g):
    print(g[count])
    count+=1
