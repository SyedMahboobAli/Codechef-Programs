t=int(input())
while(t):
    s=input()
    k,x=map(int,input().split())
    count=0
    l=list(s)
    l1=[]
    l2=[]
    for i in l:
        if i not in l1:
            l1.append(i)
            l2.append(1)
        else:
            y=l1.index(i)
            l2[y]+=1
    size=len(l2)
    a=0
    for i in range(size):
        if(l2[i]==x):
            count+=1
    while(k>0):
        x+=1
        a+=1
        for i in range(size):
            if(l2[i]==x):
                count+=1
                k-=a
                if(k==0):
                    break
            
    print(count)
    t-=1
