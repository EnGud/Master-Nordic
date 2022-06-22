#SCENE DESCRIPTOR
import numpy as np

class Empty():
    def __init__(self):

        self.Next = None


def BuildScene(PictureFG, PictureBG, OperationsCounter):

    return 0


#Array of scenes, for layering purposes
class SceneItems:
    def __init__(self, Items, Size):
        self.Items = []*Items
        self.NumberOfItems = Size
        self.Picture = []
    
#Class for wrapping scene around picture
class SceneDescriptor:
    #Generate Scene
    def __init__(Self, layer, ResolutionX, ResolutionY):
        Self.Exists = 1
        Self.SizeX = ResolutionX
        Self.SizeY = ResolutionY
        Self.Layer = layer
        Self.DrawOverBG = True

        Self.Picture = [[]]
        Self.PictureSize = [ResolutionX, ResolutionY]
        Self.PictureStoredInRam = False
        Self.Picture_RAM_Adress = 0

        Self.Next = None
        Self.Previous = None

   # class PictureInfo:
        #def __init__(Self):
        #Additional scene operations info
        Self.PictureOffset = [0, 0]    


        Self.ApplyAlpha = False
        Self.ApplyTargetAlpha = False
        Self.ApplyAlphaTarget = 0

        Self.ApplyTargetMask = False
        Self.ApplyMaskTarget = 0
        Self.ApplyMask = False
        Self.Mask = [[]]


        Self.ApplyCLUT=False
        Self.CLUT = np.zeros((3, 256), dtype=np.uint8)
        Self.GlobalCLUT=False
        Self.GlobalCLUT = np.zeros((3, 256), dtype=np.uint8)

            #X, Y


        
