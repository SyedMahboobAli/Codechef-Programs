try:
    t=int(input())
    while(t):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        if(k==1):
            sum1=0
            l1=[]
            for i in range(len(l)):
                if(l[i] not in l1):
                    l1.append(l[i])
                else:
                    sum1+=1
                    l1=[l[i]]
            if(len(l1)!=0):
                sum1+=1
                l1=[]
            print(sum1)
        else:
            sum1=0
            l1=[]
            for i in range(len(l)):
                if(l[i] not in l1):
                    l1.append(l[i])
                else:
                    sum1+=k
                    l1=[]
                    l1.append(l[i])
            if(len(l1)!=0):
                sum1+=k
                l1=[]
            sum2=k
            l1=[]
            s=set(l)
            for i in s:
                l1.append([i,l.count(i)])
            for i in range(len(l1)):
                if(l1[i][1]>1):
                    sum2+=l1[i][1]
            if(sum2>sum1):
                print(sum1)
            else:
                print(sum2)
        t-=1
except:
    pass

            
