#Heather Stafford
#2/7/18
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x000FF,1)
black = Color(0x000000,1) 

blackOutline = LineStyle(2,black)

redRectangle = RectangleAsset(200,100,blackOutline, red) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill

Sprite(redRectangle)
Sprite(blueCircle,(300,5))

App().run()

