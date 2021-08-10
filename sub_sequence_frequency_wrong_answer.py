t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    l11=[]
    for i in range(len(l)):
        b=[l[i],0]
        l11.append(b)
    print(l11)
    for i in range(len(l)):
        for j in range(i+1,len(l)+1):
            l1=l[i:j]
            print(l1)
            l2=[]
            for k in range(len(l1)):
                x=l1.count(l1[k])
                l2.append([l1[k],x])
            l2.sort(key=lambda x:x[1])
            print(l2)
            l3=[]
            m1=l2[-1][1]
            for k in range(len(l2)):
                if(l2[k][1]==m1):
                    l3.append([l2[k][0],m1])
            l3.sort()
            print(l3)
            for k in range(len(l11)):
                if(l11[k][0]==l3[0][0]):
                    l11[k][1]+=1
                    l11[k][1]%=1000000007
                    break
            print(l11)
    for i in range(len(l11)):
        print(l11[i][1],end=' ')
    t-=1
