#A test class with attributes that measures times a function has been used.

#Length is the y-length of the screen.

class OperationsCounter():
    def __init__(self, Length):
            self.Length = Length
        #Alpha
            self.CurrTime = [0]*Length
        #Redundant v
            self.CheckAlpha = [0]*Length

            self.ApplyAlphaInit = 0*Length

            self.ApplyAlpha = 0*Length
            self.ApplyAlphaWithGammaCorrection = 0*Length
            
            #If induvidual channel (different BPP) used later. Not currently used.
            self.ApplyAlphaR = 0*Length
            self.ApplyAlphaG = 0*Length
            self.ApplyAlphaB = 0*Length
            
            self.ApplyAlphaOperation = 0*Length

            self.ApplyMask = 0*Length
            self.ApplyNoMask = 0*Length

            self.ModifyCLUT = 0*Length
            self.ApplyCLUT = 0*Length

            self.RAM_get = 0*Length
            self.RAM_put = 0*Length
            self.RAM_clear = 0*Length
            self.RAM_get_error = 0*Length
            self.RAM_get_DataFound = 0*Length
            self.RAM_get_DataNotFound = 0*Length
            self.RAM_get_get = 0*Length

