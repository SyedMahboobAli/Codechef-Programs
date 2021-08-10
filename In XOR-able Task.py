t=int(input())
while(t):
    n,q=map(int,input().split())
    l1=list(map(int,input().split()))
    for i in range(q-1):
        l,r=map(int,input().split())
        count=0
        for k in range(l-1,r):
            for m in range(k+1,r):
                x=l1[k]^l1[m]
                if(l1[l-1]<=x and x<=l1[r-1]):
                    count+=1
        print(count)
t-=1
