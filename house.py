#Heather Stafford
#2/8/18
#house.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1) 

blackOutline = LineStyle(2,black)

redRectangle = RectangleAsset(200,100, blackOutline, red)

Sprite(redRectangle,(300,200))

