# Exercise 1
import math

c = 50
h = 30
d_list = input("input numbers for d comma separated: ").split(",")
output=[]
for d in d_list:
    q = math.sqrt(2*c*float(d)/h)
    output.append(q)
print(*output, sep=",")
    