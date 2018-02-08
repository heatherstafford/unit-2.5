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
greenEllipse = EllipseAsset(100,50,blackOutline, green) #width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x-endpoint, y-endpoint, lineStyle
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline, red) #enpoints, outlines, fill
text = TextAsset('Heather', fill = red, style = 'italic 35pt Times') #text, other options

Sprite(redRectangle)
Sprite(blueCircle,(300,50)) #(moving it over by coordinates)
Sprite(greenEllipse, (40,200))
Sprite(blackLine, (40,100))
Sprite(redTriangle)
Sprite(text, (300,50))

App().run()
