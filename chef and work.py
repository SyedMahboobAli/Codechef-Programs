t=int(input())
for _ in range(1,t+1):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    c=0
    s=0
    for i in range(len(a)):
        if(s+a[i]<k):
            s+=a[i]
        elif(a[i]<k):
            c+=1
            s=a[i]
    if(s>0):
        c+=1
    if(c>0):
        print(c)
    else:
        print(-1)
