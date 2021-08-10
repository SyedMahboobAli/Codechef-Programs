# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:41:50 2019

@author: HOME
"""
digits=input()
digits=list(digits)
#digits=list(map(int,input().split(" ")))
a=0
b=0
for i in range(0,len(digits)):
   if(digits[i]=='0'):
       a=a+1
   else:
       b=b+1
if(a==1 or b==1):
    print('YES')
else:
    print("NO")