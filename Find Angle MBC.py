#Question Link: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
    
#Ans-

import math

a = int(input())

b = int(input())

print(round(math.degrees(math.atan(a/b))),chr(176), sep='')
    
