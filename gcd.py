#! -*-coding : utf-8 -*-
#! /usr/env/bin python

def gcd(a,b):
    t = b
    b = a % b
	
    if b == 0:
            
	return t
        print t
    else:
	return gcd(t,b)
        print gcd(t,b)





a=int(raw_input("a : "))
b=int(raw_input("b : "))


		
