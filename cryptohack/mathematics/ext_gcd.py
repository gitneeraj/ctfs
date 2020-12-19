#!/usr/bin/env python3

# p = 26513
# q = 32321

# p * u + q * v = gcd(p,q)

# 26513 * u + 32321 * v = 1
# 26513 * u = 1 - 32321 * v

# Python program to demonstrate working of extended  
# Euclidean Algorithm  
     
# function for extended Euclidean Algorithm  
def gcdExtended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 
      
  
# Driver code 
p, q = 26513,32321
g, x, y = gcdExtended(p, q)  
print("gcd(", p , "," , q, ") = ", g)  
print(x, y)