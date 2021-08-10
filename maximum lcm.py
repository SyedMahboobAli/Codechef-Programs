def lcm(l):
    x=1
    s3={1}
    for i in range(len(l)):
        new=[]
        for j in range(2,(l[i]+1)):
            if(l[i]%j==0):
                new.append(j)
        s1=set(new)
        s3=s3.union(s1)
        
    
    for i in s3:
        x=x*i
    return(x)
    
t=int(input())
while(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    max1=1
    for i in range(1,(m+1)):
        a.append(i)
        l1=lcm(a)
        if(l1>max1):
            max1=l1
        a.pop()
    print(max1)

    t-=1
    
