import sys
try:
    t=int(input())
    while(t):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        l1=[]
        min1=sys.maxsize*2+1
        pos=-1
        for i in l:
            if(k%i==0):
                l1.append(i)
                if(min1>k//i):
                    min1=(k//i)
                    pos=i
        if(len(l)==0):
            print(-1)
        if(len(l1)==0):
            print(-1)
        else:
            print(pos)
        t-=1
except:
    pass
