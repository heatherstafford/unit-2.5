#Heather Stafford
#3/7/18
#remainder.py

from random import randint

num1 = randint(1,10)
num2 = randint(1,10)

answer = int(input('What is '+ str(num1) + '/' + str(num2) + '?'))
if answer == num1%num2:
    
