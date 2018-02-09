#Heather Stafford
#2/8/18
#house.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
blue = Color(0x0000FF,1)

blackOutline = LineStyle(2,black)

redRectangle = RectangleAsset(200,100, blackOutline, red)
blackTriangle = PolygonAsset([(0,300),(120,180),(240,300)],blackOutline, black)
blackRectangle = RectangleAsset(20,50, blackOutline, black)
blueRectangle = RectangleAsset(50,25, blackOutline, blue)

Sprite(redRectangle,(300,200))
Sprite(blackTriangle,(279,80))
Sprite(blackRectangle,(385,250))
Sprite(blueRectangle,(317, 250))

App().run()
