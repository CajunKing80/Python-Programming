# You are given a program with two inputs: one as password and the second one as password repeat. Complete and call the given function to output "Correct" if password and repeat are equal, and output "Wrong", if they are not.

# Sample Input
# nfs1598
# nfs1598

# Sample Output
# Correct


password = input()
repeat = input()

def validate(text1, text2):
	#your code goes here
	if password == repeat:
		print('Correct')
	else:
		print('Wrong')
		
validate(password, repeat)