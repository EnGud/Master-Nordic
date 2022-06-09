import numpy as np
import OperationsCounter
import PIL
from PIL import Image

class MaskingOperations:


    def MaskAllChannels(PictureFG, PictureBG, Mask, CurrentY, OperationsCounter):
        FGSize = PictureFG.size
        X_Size = (FGSize[0]-1)
        Output = np.zeros((1, X_Size, 4))
        #Channels = np.asarray(PictureBG).shape
        #if Channels[2] != 4: 
       #     Picture.putalpha(255)
        #     OutputBG = np.zeros((1, X_Size, 4))


        ArrayedForeground = np.asarray(PictureFG)
        ArrayedBackground = np.asarray(PictureBG)
        ArrayedMask = np.asarray(Mask)


        for i in range (X_Size):
            Hm, Hmm, Hmmm = ArrayedMask[CurrentY][i][0], ArrayedMask[CurrentY][i][1], ArrayedMask[CurrentY][i][2]
            if (Hm and Hmm and Hmmm):
                Output[0][i][0] = ArrayedForeground[CurrentY][i][0]
                Output[0][i][1] = ArrayedForeground[CurrentY][i][1]
                Output[0][i][2] = ArrayedForeground[CurrentY][i][2]
                OperationsCounter.ApplyNoMask =+1
                return Output

            else:
                Output[0][i][0] = ArrayedBackground[CurrentY][i][0]
                Output[0][i][1] = ArrayedBackground[CurrentY][i][1]
                Output[0][i][2] = ArrayedBackground[CurrentY][i][2]
                OperationsCounter.ApplyMask =+1
                return Output










#Last inn maskingfilter
#Last inn bakgrunnsbilde
#last inn forgrunnsbilde

#Compare background to maskingfilter on current x line, given y co-ordinate 
#create output picture variable
#If black, apply background picture

#if white, apply foreground picture pixel over background
#loop until end of line

#return masked picture