# #zadanie 1
# a=b=c=[1,2,3]
# a.append(4)
# b.extend([6])
# print(a,b,c)
# print(id(a),id(b),id(c))
#
# b=[1,2,3]
# n=[1,2,3]
# m=n
# print(id(b),id(n),id(m))
# n.remove(2)
# print(b,n,m)

#zadanie 2
x="Dupa"
y=x+"!!"
print(id(x), id(y))
print(x == y)
print(x is y)

y=y[:-2]
print(id(x), id(y))
print(x == y)
print(x is y)
