# We have a function that outputs "Welcome, user" as it is called. We want to make it more personalized, so redesign the given function so that it will take the given input as the name of the user and output the welcome message with it.

# Sample Input
# Tommy

# Sample Output
# Welcome, Tommy


def welcome_message():
	#redesign this function
	name = input()
	print(f'Welcome, {name}')
	

welcome_message()