#Heather Stafford
#3/7/18
#remainder.py

from random import randint
from ggame import *

num1 = randint(10,20)
num2 = randint(1,10)

yellow = Color(0xFFFF00, 1)
black = Color(0x000000,1)

yellowCircle = CircleAsset(100, LineStyle(2,black), yellow)
blackCircle = CircleAsset(50, LineStyle(2,black),black)
yellowEdit = CircleAsset(50, LineStyle(2,yellow), yellow)

answer = float(input('What is the remainder of '+ str(num1) + '/' + str(num2) + '?'))
if answer == num1%num2:
    Sprite(yellowCircle)
    Sprite(blackCircle,(50,60))
    Sprite(yellowEdit, (50,40))
else:
    Sprite(yellowCircle)
    Sprite(blackCircle, (50,100))
    
App().run()
