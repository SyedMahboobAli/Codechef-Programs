try:
    t=int(input())
    while(t):
        f=1
        n=int(input())
        l1=list(map(int,input().split()))
        l2=[]
        for i in range(n):
            x=l1[i]
            if(x in l2):
                f=0
                break
            else:
                l2.append(x)
            for j in range(i+1,n):
                x=x|l1[j]
                if(x in l2):
                    f=0
                    break
                else:
                    l2.append(x)
            if(f==0):
                break
        if(f==1):
            print("YES")
        else:
            print("NO")
        t-=1
except:
    pass
