from PIL import Image
import numpy as np

#import C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_400_200.bmp and print the shape of the image.

Bilde = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")
print(Bilde.size)
