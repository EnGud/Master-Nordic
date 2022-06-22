#A test class with attributes that measures times a function has been used.

#Length is the y-length of the screen.

#Just a lot of values for reading different values
class OperationsCounter():
    def __init__(self, Length, Width):

        FreeLine = [True]*Width
        self.Length = Length

        self.CurrentLayer = 0

        self.ScenesConstructed = 0
        self.TimeTaken =[0]*Length
        #Alpha
        #Redundant v

        #Alpha
        self.AlphaPassed = 0
        
        self.ApplyAlpha_Pixel = 0
        self.ApplyAlpha_Pixel_Array = [0]*Length
        self.ApplyAlphaR = 0
        self.ApplyAlphaG = 0
        self.ApplyAlphaB = 0

        self.AlphaBlend = 0

        #Mask
        self.NoMask = 0
        self.ApplyMask = 0
        self.ApplyMask_Pixel_Array = [0]*Length

        #CLUT
        self.ChangeCLUT = 0
        self.CLUT_Applied = 0
        self.CLUT_Pixel_Applied = 0
        self.CLUT_Pixel_Array = [0]*Length
        self.CLUT_Pixel_Skipped = 0

        #RAM
        self.RAM_put_call = 0
        self.RAM_put = 0
        self.RAM_put_Array = [0]*Length
        
        self.RAM_get_call = 0
        self.RAM_get = 0
        self.RAM_get_Array = [0]*Length

        self.RAM_get_DataNotFound = 0
        self.RAM_get_error = 0
        self.RAM_clear = 0
        self.RAM_Used_Cumulative = 0
        self.RAM_Used_Bits_Cumulative = 0

        self.RAM_Used = 0
        self.RAM_Used_Array = [0]*Length
        self.RAM_Used_Bytes = 0
        self.RAM_Used_Bytes_Array = [0]*Length

        #self.list =

    """  @property
    def NoMask(self):
        return self._NoMask
    @NoMask.setter
    def NoMask(self, value):
        self._NoMask = value
        print("value: ")
        print(self._NoMask) """
    
