#from typing import Sized
import numpy as np
import AlphaBlending, AlphaMasking

class SceneDescriptor:
    #Generate Scene
    def __init__(Self, layers, elements, ResolutionX, ResolutionY, AlphaTargets, MaskTargets):
        Self.Exists = 1
        Self.ScreenSizeX = ResolutionX
        Self.ScreenSizeY = ResolutionY
        NumLayers= layers
        NumElements = elements

        #Generate layers
        for i in range (layers-1):
            for place in range (elements-1):

                Self.Layer[i].PictureInfo.AlphaElement = [0]
                Self.Layer[i].PictureInfo.ApplyMask = 0
                Self.Layer[i].Picture.CLUT = 0


                Self.Layer[i].PictureInfo.Picture[place].PictureSize = [0,0]
                Self.Layer[i].Picture.Picture[place].PictureOffset = [0, 0]    
                Self.Layer[i].Picture.Picture[place].Picture = np.zeros((Self.Layer[i].PictureInfo.Picture[elements].PictureSizeY, Self.Layer[i].PictureInfo.Picture[elements].PictureSizeX, 4), dtype=np.uint8)
                Self.Layer[i].Picture.Picture[place].CLUT = np.zeros((3, 256), dtype=np.uint8)


        #3 Paralelle arrays for hver RGB-kanal for CLUT
        #Bytt alle instanser av 256 til en bitsize-input løsning
        Self.GlobalCLUT = np.zeros((3, 256), dtype=np.uint8)



        #Info om operasjoner
        Self.SceneOperations.Mask.Mask = [[],[]]
        Self.SceneOperations.Mask.Apply = False
        Self.SceneOperations.Mask.NumberOfTargets = MaskTargets
        #for i in range (Self.SceneOperations.Mask.NumberOfTargets):
        Self.SceneOperations.Mask.Target = np.zeros((layers, elements), dtype=np.uint8)
        Self.SceneOperations.Mask.StartY = 0
        Self.SceneOperations.Mask.StartX = 0

        Self.SceneOperations.GlobalForegroundAlpha = 0
        Self.SceneOperations.Alpha.Apply = False
        Self.SceneOperations.Alpha.NumberOfTargets = AlphaTargets
        #for i in range (Self.SceneOperations.Alpha.NumberOfTargets):
        Self.SceneOperations.Alpha.Target = np.zeros((layers, elements), dtype=np.uint8)
        Self.SceneOperations.Alpha.StartX = 0
        Self.SceneOperations.Alpha.StartY = 0

        Self.SceneOperations.GlobalCLUT = False
        Self.Scene.Exit = False
        #GlobalCLUT False = bruk lokale CLUT. (Standard)









