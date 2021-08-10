try:
    t=int(input())
    while(t):
        s=input()
        p=input()
        s=list(s)
        p=list(p)
        s.sort()
        for i in range(len(p)):
            s.remove(p[i])
        ch=ord(p[0])
        while(True):
            ch+=1            
            if(chr(ch) in s):
                break
        i=s.index(chr(ch))
        s="".join(s)
        p="".join(p)
        a=""
        a+=s[:i]
        a+=p
        a+=s[i:]
        print(a)
        t-=1
except:
    pass
