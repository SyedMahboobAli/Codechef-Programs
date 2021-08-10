t=int(input())
for x in range(t):
    n=int(input())
    for y in range(n):
        li=list(map(int,input().split()))
        distance=0
        for i in range(len(li)):
            distance=0;
            if(li==0):
                continue
            if(li==1):
                for j in range(i+1,len(li)):
                    if(li==0):
                        distance+=1
                    else:
                        
                        break
        if(distance<6):
            print("NO")
        else:
            print("YES")
