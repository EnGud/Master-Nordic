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
                
                #Generate an empty Alpha mask.
                Self.Layer[i].PictureInfo.ApplyAlpha = False
                Self.Layer[i].PictureInfo.AlphaMask = np.zeros((Self.Layer[i].PictureInfo.Picture[elements].PictureSizeY, Self.Layer[i].PictureInfo.Picture[elements].PictureSizeX, 4), dtype=np.uint8)
                

                #Generate an empty mask.
                Self.Layer[i].PictureInfo.ApplyMask = False
                Self.Layer[i].PictureInfo.AlphaMask = np.zeros((Self.Layer[i].PictureInfo.Picture[elements].PictureSizeY, Self.Layer[i].PictureInfo.Picture[elements].PictureSizeX, 4), dtype=np.uint8)

                Self.Layer[i].PictureInfo.Picture[place].PictureSize = [0,0]
                Self.Layer[i].Picture.Picture[place].PictureOffset = [0, 0]    
                Self.Layer[i].Picture.Picture[place].Picture = np.zeros((Self.Layer[i].PictureInfo.Picture[elements].PictureSizeY, Self.Layer[i].PictureInfo.Picture[elements].PictureSizeX, 4), dtype=np.uint8)

                Self.Layer[i].Picture.Picture[place].LocalCLUT=False
                Self.Layer[i].Picture.Picture[place].CLUT = np.zeros((3, 256), dtype=np.uint8)


        #3 Paralelle arrays for hver RGB-kanal for CLUT. Global.
        Self.GlobalCLUT = np.zeros((3, 256), dtype=np.uint8)



        #Info om operasjoner
        
        #Generate an empty mask.
        Self.SceneOperations.Mask.Apply = False
        Self.SceneOperations.Mask.Mask = np.zeros((Self.ScreenSizeX, Self.ScreenSizeY, 1), dtype=np.uint8)
        
        Self.SceneOperations.Mask.MaskTargets = MaskTargets


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


        