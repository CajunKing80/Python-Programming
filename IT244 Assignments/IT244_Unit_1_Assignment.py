#Unit 1 Program 2

#define the variables for the 8 hours sleep group
x1 = 5
x2 = 7
x3 = 5
x4 = 3
x5 = 5
x6 = 3
x7 = 3
x8 = 9
#define the variables for the 4 hours sleep group
y1 = 8
y2 = 1
y3 = 4
y4 = 6
y5 = 6
y6 = 4
y7 = 1
y8 = 2

#x and y variables
countOfX = 8
countOfY = 8

#average of x set
mx = ((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) / countOfX)
#average of y set
my = ((y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8) / countOfY)

#sx2
sx2 = ((x1-mx)**2/(countOfX-1)) + ((x2-mx)**2/(countOfX-1)) + ((x3-mx)**2/(countOfX-1)) + ((x4-mx)**2/(countOfX-1)) + ((x5-mx)**2/(countOfX-1)) + ((x6-mx)**2/(countOfX-1)) + ((x7-mx)**2/(countOfX-1)) + ((x8-mx)**2/(countOfX-1))
#sy2
sy2 = ((y1-my)**2/(countOfY-1)) + ((y2-my)**2/(countOfY-1)) + ((y3-my)**2/(countOfY-1)) + ((y4-my)**2/(countOfY-1)) + ((y5-my)**2/(countOfY-1)) + ((y6-my)**2/(countOfY-1)) + ((y7-my)**2/(countOfY-1)) + ((y8-my)**2/(countOfY-1))

#t-test formula
ttest = (mx-my)/((sx2/countOfX + sy2/countOfY))**(1/2)
print ("t = " , ttest)
