n,q=map(int,input().split())
l=list(map(int,input().split()))
l1=[0]
for i in range(1,len(l)):
    f=0
    for j in range(0,i):
        if(l[j]>l[i]):
            l1.append(1)
            f=1
            break
    if(f==0):
        l1.append(0)

while(q):
    
    l,r=map(int,input().split())
    l=l-1
    r=r-1
    sum1=0
    for i in range(l,r+1):
        sum1+=l1[i]
    print(sum1)
    
    q-=1
    
