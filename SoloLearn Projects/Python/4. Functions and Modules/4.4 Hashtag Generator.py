# We are creating our own social network application and need to have a hashtag generator program.
# Complete the program to output the input text starting with the hashtag (#).
# Also, if the user entered several words, the program should delete the spaces between them.

# Sample Input
# code sleep eat repeat

# Sample Output
# #codesleepeatrepeat

# Hint
# You can use the replace() function to replace the spaces (" ") with empty strings (""). See how it works:


s = input()

def hashtagGen(text):
	#your code goes here

    s1 = s.replace(" ","#")
	# s1 = s.replace(s,f'#{s}')
    return s1
    
print(hashtagGen(s))