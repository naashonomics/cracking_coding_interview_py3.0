#Implement a function to reserse a give string


def reverse_string_with_slicing(string2reverse):
	return string2reverse[::-1]

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
print( "Reverse a string with silicing  " +  reverse_string_with_slicing("hello"))
print( "Reverse a string with Recurssion  " +  reverse_string_with_recurssion("india"))
