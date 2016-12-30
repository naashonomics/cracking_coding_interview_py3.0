#Check unique char in string with dictionary
def hasAllUniqueCharDict(inputstring):
#using dict key value par
	chardict = {}
	for char in inputstring:     
		#check if char is in dict
 		if char in chardict:
                	 return False
        	else:
        		chardict[char]=True
        	return True

#postive testcase
test_string_true="abcdefg"
#nefative test case
test_string_false="abccdefg"

#postive test case
if hasAllUniqueCharDict(test_string_true):
	print "Test1 postive test case passed"
else:
	print "Test1 postive test case failed"

#negative test case
if hasAllUniqueCharDict(test_string_false):
        print "Test2 negative test case passed"
else:
        print "Test2 negativetest case failed"
       

    
      
