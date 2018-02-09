#Heather Stafford
#2/9/18
#name.py

from ggame import *

name = input('Enter your name: ')
colorCode = input('Enter an RGB color code: ')

color = Color(colorCode,1)
black = Color(0x000000,1)

colorOutline = LineStyle(2,color)

colorRectangle = RectangleAsset(1000,2000, colorOutline, color)
text = TextAsset(name, fill = black, style = 'italic 30pt Times')

Sprite(colorRectangle)

App().run()
