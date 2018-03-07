#Heather Stafford
#3/7/18
#remainder.py

from random import randint
from ggame import *

num1 = randint(10,20)
num2 = randint(1,10)

yellow = Color(0xFFFF00, 1)
yellowCircle = CircleAsset(100, LineStyle(2,black), yellow)

answer = float(input('What is the remainder of '+ str(num1) + '/' + str(num2) + '?'))
if answer == num1%num2:
    Sprite(yellowCircle)
else:
    Sprite(yellowCircle)
    
App().run()
