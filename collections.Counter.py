

#Question Link- https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
  
#Answer

from collections import Counter
X= int(input())
n= list(map(int,input().split()))
profit=0
dict1=dict(Counter(n))
y=int(input())
for i in range(y):
    a,b=map(int,input().split())
    if dict1.get(a)==None:
        continue
    if dict1.get(a)>0:
        dict1[a]-=1
        profit+=b

print(profit)
  
