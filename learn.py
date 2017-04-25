
r=[1,2.0,3,5]
r.append('thing')
print(r)
a=[1,3,2]
b=a
print(b)
c=b[0:2]
print(c)
d=b[:]
print(d)
#一个意想不到的赋值结果
r=[0]*8
c=[r]*8
print(c)
c[0][0]=1
print(c)
print(c[0][0])

a='thing'
print(a) 
del a

t=(1,3,2)
print(t[1])
(a,b,c)=t
print(a,b,c)

#while loop
r=[]
n=0
last=20
while n<=last:
    r.append(str(n))
    n+=3
print(','.join(r))


#for if
r=[1,3,10,98,-2,48]
for i in r:
    if i<0:
        print('input contains negative value ',i,'!')
        break
    else:
        pass#do nothing
else:
    print('input is ok!')

def all_items_positive(r):
    for i in r:
        if i<=0:
            return True
sequences=[[1,5,6,-0.1],[0,0.01,1,2]]
for seq in sequences:
    if not all_items_positive(seq):
        print("the item is invalid!")

from math import *
print(e)
print(log(10.0))
print(exp(-1.0))
class Circle:
    def __init__(self,x,y,radius=1):
        self.x=x
        self.y=y
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
