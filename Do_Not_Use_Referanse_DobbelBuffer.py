""" #Create a main() that renders a scene, utilizing alpha blending and masking. It uses a dual buffer for output.

#Create a structure to store pictures and their properties. It should allow the pictures to be layered. 

import Scene_Descriptor
import AlphaBlending
import AlphaMasking
import OperationsCounter
import Dynamic_RAM
import CLUT
from PIL import Image
import Analytics
import numpy as np
import threading
import MenusConstructor
import Referanse_Funksjoner
import time

class PictureList:
    def __init__(Self, Layers):
        Self.list = [0]*Layers

class Picture:
    def __init__(Self, layer, ResolutionX, ResolutionY):
        Self.Exists = 1
        Self.SizeX = ResolutionX
        Self.SizeY = ResolutionY
        Self.Layer = layer
        Self.Picture = [[]]
        Self.Offset = [0, 0]
        Self.ApplyCLUT = False
        Self.CLUT = np.zeros((3, 256), dtype=np.uint8)
        Self.ApplyMask = False
        Self.Mask = [[]]
        Self.ApplyAlpha = False


ResolutionX = 800
ResolutionY = 600

#Draw whole picture to buffer
#Move to next picture
#Draw the next picture at offset into whole buffer
#Next picture, same
#Push buffer
#Switch buffer
FreeLine = [True] * ResolutionX
TargetBuffer = False
PictureOut = np.zeros((ResolutionY, ResolutionX, 4), dtype=np.uint8)
StateMachineStatus = "MainMenu"


def BuildMainMenu():

    Test1 = Picture(0, ResolutionX, ResolutionY)
    Test2 = Picture(1, 400, 200)

    Test1.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/MainMenuBackground.bmp")
    Test1.Picture = np.asarray((Test1.Picture).convert("RGBA"))

    Test2.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/BACK_400_200.bmp")
    Test2.Picture.putalpha(150)
    Test2.Picture = np.asarray(Test1.Picture)
    Test2.ApplyAlpha = False
    Test2.Offset = [200, 200]
    Test2.ApplyMask = True
    Test2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/BACK_400_200.bmp"))

    PictureArray = PictureList(2)
    PictureArray.list[0] = Test1
    PictureArray.list[1] = Test2

    return PictureArray

def Render(Structure):
    #Draw layer 1 picture
    for i in range (len(Structure.list)):

        if Structure.list[i].ApplyCLUT == True:
            PictureOut = Referanse_Funksjoner.Ref_CLUT(Structure.list[i].Picture, Structure.list[i].CLUT, Structure.list[i].Offset)

        if Structure.list[i].ApplyMask == True:
            PictureOut = Referanse_Funksjoner.Ref_Mask(Structure.list[i].Picture, Structure.list[i].Offset, Structure.list[i].Mask, FreeLine)

        if Structure.list[i].ApplyAlpha == True:
            PictureOut = Referanse_Funksjoner.Ref_Alpha(Structure.list[i].Picture, Structure.list[i].Offset, PictureOut, FreeLine)


    return PictureOut


while(1):
    
    if StateMachineStatus == "MainMenu":
        Structure = BuildMainMenu()
        PictureOut = Render(Structure)
        
    Image.save(Image.fromarray(PictureOut))

    
    if TargetBuffer == True:
        Buffer0 = PictureOut
    if TargetBuffer == False:
        Buffer1 = PictureOut
    TargetBuffer != TargetBuffer


 """