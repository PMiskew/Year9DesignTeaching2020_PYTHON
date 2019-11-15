import math 

a = "word 1"
b = "word 2"
c = 99
print(a + b)
print(a,b) 
print(a + " " + b)
#print(a + c) #ERROR
#Fix 1
print(a + str(c)) #Cast to string
print(a,c)

print(str(math.pow(3,5))+" cm\u00B2")
print("\u00B3")