#SCENE DESCRIPTOR


import numpy as np


class SceneItems:
    def __init__(self, Items, Size):
        self.Items = []*Items
        self.NumberOfItems = Size
        self.Picture = []
    
    




class SceneDescriptor:
    #Generate Scene
    def __init__(Self, layer, ResolutionX, ResolutionY, AlphaTargets, MaskTargets):
        Self.Exists = 1
        Self.SizeX = ResolutionX
        Self.SizeY = ResolutionY
        Self.Layer = layer
        Self.Picture = [[]]
        Self.GlobalCLUT = np.zeros((3, 256), dtype=np.uint8)

        Self.Next = None
        Self.Previous = None

    class PictureInfo:
        def __init__(Self):
            Self.ApplyAlpha = False
            Self.ApplyTargetAlpha = False
            Self.ApplyAlphaTarget = 0

            Self.ApplyTargetMask = False
            Self.ApplyMaskTarget = 0
            Self.ApplyMask = False
            Self.Mask = [[]]

            Self.LocalCLUT=False
            Self.CLUT = np.zeros((3, 256), dtype=np.uint8)

            #X, Y
            Self.PictureSize = [0, 0]
            Self.PictureOffset = [0, 0]    


        


        #3 Paralelle arrays for hver RGB-kanal for CLUT. Global.
        



        #Info om operasjoner
        
        #Generate an empty mask.
    class SceneOperations:
        def __init__(Self):
            Self.MaskApply = False
            Self.Mask = [[]]
            
            #Self.MaskTargets = MaskTargets


            #for i in range (Self.SceneOperations.Mask.NumberOfTargets):
            #Self.SceneOperations.Mask.Target = np.zeros((layers, elements), dtype=np.uint8)
            Self.MaskStart = [0, 0]


            Self.GlobalForegroundAlpha = 0
            Self.GlobalAlphaApply = False
            #Self.Alpha.NumberOfTargets = AlphaTargets
            #for i in range (Self.SceneOperations.Alpha.NumberOfTargets):
            #Self.SceneOperations.Alpha.Target = np.zeros((layers, elements), dtype=np.uint8)
            #Self.SceneOperations.Alpha.StartX = 0
            #Self.SceneOperations.Alpha.StartY = 0

            Self.GlobalCLUT = False
            Self.Exit = False
            #GlobalCLUT False = bruk lokale CLUT. (Standard)