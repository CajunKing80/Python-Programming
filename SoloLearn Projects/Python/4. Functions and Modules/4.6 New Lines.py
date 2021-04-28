
# You are given the following list:
# names = ["John", "Oscar", "Jacob"] 
# PY
# Complete the program to create a file where you write the names from the list, each on a new line, and separately output them.

# Output
# John
# Oscar
# Jacob 


names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
#write down the names into the file
file.write("John \n" "Oscar \n" "Jacob")

file.close()

file= open("names.txt", "r")
#output the content of file in console
print(file.read())

file.close()