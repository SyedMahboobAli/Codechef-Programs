# cook your dish here
t=int(input())
while(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            x=a[i]&a[j]
            if(x==a[i]):
                count+=1
    print(count)
    t-=1
