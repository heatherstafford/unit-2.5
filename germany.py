#Heather Stafford
#2/9/18
#germany.py

from ggame import *

black = Color(0x000000,1)
red = Color(0xFF0000,1)
yellow = Color(0xFFE55C,1)

blackOutline = LineStyle(2,black)
redOutline = LineStyle(2,red)
yellowOutline = LineStyle(2,yellow)

blackRectangle = RectangleAsset(500,100, blackOutline, black)
redRectangle = RectangleAsset(500,100, redOutline, red)
yellowRectangle = RectangleAsset(500,100, yellowOutline, yellow)

Sprite(blackRectangle)
Sprite(redRectangle,(0,100))
Sprite(yellowRectangle,(0,200))

App().run()
