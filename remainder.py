#Heather Stafford
#3/7/18
#remainder.py

from random import randint
from ggame import *

num1 = randint(1,10)
num2 = randint(1,10)

yellow = Color(0xFFFF00)
yellowCircle = CircleAsset(100, LineStyle(2,black), yellow)

answer = int(input('What is '+ str(num1) + '/' + str(num2) + '?'))
if answer == num1%num2:
    sprite(yellowCircle)
else:
    sprite(yellowCirlce)
    
