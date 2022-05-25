#from typing import Sized
import numpy as np
import AlphaBlending, AlphaMasking

class SceneDescriptor:
    #Generate Scene
    def __init__(Self, layers, elements, ResolutionX, ResolutionY):

        #Generate layers
        for i in range (layers):
            Self.Layer[i]

            for Size in range (1):
                #X, Y
                Self.Layer[i].PictureOffset[Size] = 0
            
            Self.Layer[i].PictureInfo.PictureSize = 0
            Self.Layer[i].PictureInfo.ApplyAlpya = 0
            Self.Layer[i].PictureInfo.ApplyMask = 0
            Self.Layer[i].Picture.CLUT = 0
            Self.Layer[i].Picture.Picture[elements].Picture = np.zeros((ResolutionY, ResolutionX, 4), dtype=np.uint8)
            Self.Layer[i].Picture.Picture[elements].CLUT = np.zeros((3, 256), dtype=np.uint8)


        #3 Paralelle arrays for hver RGB-kanal for CLUT
        #Bytt alle instanser av 256 til en bitsize-input løsning
        Self.GlobalCLUT = np.zeros((3, 256), dtype=np.uint8)



        #Info om operasjoner
        Self.SceneOperations.Mask = []
        Self.SceneOperations.Alpha = False
        Self.SceneOperations.GlobalCLUT = False
        #GlobalCLUT False = bruk lokale CLUT. (Standard)









