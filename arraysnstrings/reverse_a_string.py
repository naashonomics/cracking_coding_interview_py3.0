#Implement a function to reserse a give string
#use Collections in python
from collections import deque
def reverse_string_with_collections(string2reverse):
	dq= deque()
        dq.extendleft(string2reverse)
        return ''.join(dq) 

#Use of Silicing 
def reverse_string_with_slicing(string2reverse):
	return string2reverse[::-1]

#Use Range Operator 
def reverse_string_with_range(string2reverse):
	for i in range(len(string2reverse)-1,-1,-1):
        	yield string2reverse[i]
 
"""
Using Recurssion activation records are as created below
   reverse(hello)
 = reverse(ello) + h           # The recursive step
 = reverse(llo) + e + h
 = reverse(lo) + l + e + h
 = reverse(o) + l + l + e + h  # Base case
 = o + l + l + e + h
 = olleh
"""

def reverse_string_with_recurssion(string2reverse):
	if(len(string2reverse)<=1):
		return string2reverse
	else:
		return reverse_string_with_recurssion(string2reverse[1:]) + string2reverse[0]


#testcase
print( "Reverse a string with Collections  " +  reverse_string_with_collections("China"))
print( "Reverse a string with silicing  " +  reverse_string_with_slicing("hello"))
print( "Reverse a string with range  " +  ''.join(reverse_string_with_range("USA")))
print( "Reverse a string with Recurssion  " +  reverse_string_with_recurssion("india"))
