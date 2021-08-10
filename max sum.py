t=int(input())
while(t):
    a,b=map(int,input().split())
    a1=a//10
    a2=a%10
    b1=b//10
    b2=b%10
    sum1=a+b
    n1=(b2*10)+a2
    n2=(b1*10)+a1
    sum2=n1+n2
    n3=(a1*10)+b2
    n4=(b1*10)+a2
    sum3=n3+n4
    n5=(b1*10)+a2
    n6=(a1*10)+b2
    sum4=n5+n6
    n7=(a1*10)+b1
    n8=(a2*10)+b2
    sum5=n7+n8
    l=[sum1,sum2,sum3,sum4,sum5]
    m=max(l)
    print(m)
    
    t-=1
    
