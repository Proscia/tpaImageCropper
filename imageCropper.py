from wand.image import Image
import os

for filename in os.listdir('Images'):
    image = Image(filename ='Images/' + filename)
    image.crop(left=1, top=50,bottom=-87, right=-4)
    image.crop(width=512, height=512, gravity='center')
    image.save(filename ='CroppedImages/' + filename)