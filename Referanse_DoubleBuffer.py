#Create a main() that renders a scene, utilizing alpha blending and masking. It uses a dual buffer for output.

#Create a structure to store pictures and their properties. It should allow the pictures to be layered. 

import numpy as np
import AlphaBlending
import AlphaMasking
import OperationsCounter
import CLUT

class PictureList:
    def __init__(self, Picture, Layer):
        #the picture will contain the data of the picture, the layer number, and a "pictureInfo" that contains resolution, alpha, masking, CLUT, etc.
        self.Picture = Picture
        self.Layer = Layer

        self.PictureInfo.ResolutionX = len(Picture[0])
        self.PictureInfo.ResolutionY = len(Picture)
        self.PictureInfo.ApplyAlpha = False
        self.PictureInfo.ApplyMasking = False
        self.PictureInfo.ApplyCLUT = False
        #Info about target picture to alpha and mask

NumberOfPictures = 3
FirstBuffer = np.zeros((800, 600, 4), dtype=np.uint8)
SecondBuffer = np.zeros((800, 600, 4), dtype=np.uint8)


#Draw whole picture to buffer
#Move to next picture
#Draw the next picture at offset into whole buffer
#Next picture, same
#Push buffer
#Switch buffer
def DrawPicturesToScreen(NumberOfPictures, X, Y):
    #Get the first picture
    for I in range (NumberOfPictures):
    Picture = PictureList.Picture
    Layer = PictureList.Layer


    #Apply Alpha if self.PictureInfo.ApplyAlpha == True
    #Apply Masking if self.PictureInfo.ApplyMasking == True
    #Apply CLUT if self.PictureInfo.ApplyCLUT == True
    #ApplyAlpha(Foreground, Operator, Background, currentY, TestEntity):

    for CurrentY in range (len(Picture)):

        Picturebuff = AlphaBlending.ApplyAlpha(PictureOver, 'over', PictureUnder, CurrentY, TestEntity)
        return Picturebuff
        



    #Draw the picture to the buffer


        for i in range (len(Picture)):
            for j in range (len(Picture[0])):
                FirstBuffer[i+Y][j+X] = Picture[i][j]

    #Move to the next picture





    #Draw the next picture at offset into the buffer



    #Next picture, same

    #Push buffer


    #Switch buffer

