t=int(input())
for i in range(t):
    n,q=list(map(int,input().split()))
    a=list(map(int,input().split()))
    c=a.copy()
    b=[]
    for j in range(q):
        x,y=list(map(int,input().split()))
        for k in range(n):
            if(a[k]==x):
                a[k]=y
        m=0
        for k in range(n-1):
            m=m+abs(a[k]-a[k+1])
        b.append(m)
    print("Case",t,":")
    for j in range(q):
        print(b[j])
    
    
