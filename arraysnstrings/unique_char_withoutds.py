#Check unique char in string without use of data structure
def hasAllUniqueChar(inputstring):
	for char1 in inputstring:
        	found_count=0
		for char2 in inputstring:
                	if char1==char2:
				found_count=found_count+1
			if found_count>1:
				return False
			return True	     
		       
#postive testcase
test_string_true="abcdefg"
#nefative test case
test_string_false="abccdefg"

#postive test case
if hasAllUniqueChar(test_string_true):
	print "Test1 postive test case passed"
else:
	print "Test1 postive test case failed"

#negative test case
if hasAllUniqueChar(test_string_false):
        print "Test2 negative test case passed"
else:
        print "Test2 negativetest case failed"
       

    
      
