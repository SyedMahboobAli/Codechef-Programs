import math
n=int(input("Enter the number of components:"))
cost=int(input("Enter the total amount available:"))
r=[]
c=[]
u=[]
s={(1,0)}
x=0
for i in range(n):
    c.append(int(input("Enter cost:")))
    r.append(float(input("Enter reliability:")))
    x+=c[i]
for i in range(n):
    y=(cost-x)/c[i]
    y=y+1
    u.append(math.floor(y))
    print(u[i])
