# The university gives students discounts on tuition fees depending on their performance:
# 90-100 => 50%
# 80-89 => 30%
# 70-79 => 10%
# 0-69 => 0%
# Write a program that will take the scores from the first and second semesters, then calculate the average score, and output the discount, depending on the score.

# Sample Input
# 67
# 83

# Sample Output
# 10

# Explanation
# Average of 67 and 83 is 75, which is in range of 70 to 79 and gets a 10% discount. Do not include the % symbol in the output. 

score1 = int(input())
score2 = int(input())
#your code goes here

def tuition():

    semester_avg = (score1 + score2) // 2

    if(semester_avg >= 90 and semester_avg <= 100):
        print('50')
    elif (semester_avg >= 80 and semester_avg <= 89):
        print('30')
    elif (semester_avg >= 70 and semester_avg <= 79):
        print('10')   
    elif (semester_avg >= 0 and semester_avg <= 69):
        print('0')  

tuition()  