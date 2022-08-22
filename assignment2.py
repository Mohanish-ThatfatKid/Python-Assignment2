import keyword
from datetime import datetime
# Question 1 This is the Single line comment
print("\"Learning Python\"") 


#Question 2
"""This is 
Multiline 
Comment"""
var1 = "Mohanish"
var2 = 27
var3 = 69.99
var4 = True

print(var1)
print(var2)
print(var3)
print(var4)

#Question 3

num1 = 300
varbool = True
varString = "MySirG"
varFloat = 5.46
varComp = 3+4j

print(type(num1))
print(type(varbool))
print(type(varString))
print(type(varFloat))
print(type(varComp))

# Question 4
a = 10
b = 10

print(id(a))
print(id(b))

# Question 5
m = 10
n = 3+4j
o = "Mohanish"
p = True

print("Value: ",m,"|","Type: ",type(m), "|", "ID:", id(m))
print("Value: ",n,"|","Type: ",type(n), "|", "ID:", id(n))
print("Value: ",o,"|","Type: ",type(o), "|", "ID:", id(o))
print("Value: ",p,"|","Type: ",type(p), "|", "ID:", id(p))


# question 6
print(keyword.kwlist)

# Question 9
"""True, False, None are keyword That can be used as data"""

#Question 10
d1 = datetime.today();
dt = d1.strftime("%d-%m-%Y and %I:%M %p")
print(dt)
