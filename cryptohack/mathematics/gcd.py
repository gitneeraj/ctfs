#!/usr/bin/env python3

# Python code to demonstrate naive 
# method to compute gcd ( recursion ) 
  
def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 
  
a = 26513
b= 32321
  
# prints 12 
print (f"The gcd of {a} and {b} is : ",end="") 
print (hcfnaive(a,b)) 