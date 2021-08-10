t=int(input())
while(t):
    n=int(input())
    str1=input()
    str2=""
    d=dict()
    for i in range(n):
        if(str1[i] in d):
            d[str1[i]]+=1
        else:
            d[str1[i]]=1
    for i in range(n):
        if(d[str1[i]]%2==0):
            continue
        else:
            str2+=str1[i]
    if(str2==""):
        print("YES")
    else:
        print("NO")
    t-=1
