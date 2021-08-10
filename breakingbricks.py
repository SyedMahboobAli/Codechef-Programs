try:
    n=int(input())
    for i in range(n):
        s,w1,w2,w3=list(map(int,input().split()))
        if(w1+w2+w3<=s):
            print(1)
        elif(w1+w2<=s):
            print(2)
        elif(w2+w3<=s):
            print(2)
        elif(w1+w2>s and w2+w3<=s):
            print(2)
        elif(w2+w3>s and w1+w2<=s):
            print(2)
        else:
            print(3)
except:
    pass
