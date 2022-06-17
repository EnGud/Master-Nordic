#Masks each channel given by the mask.
import numpy as np




#Masks each channel given by the mask.
def ApplyMask(PictureFG, PictureBG, Mask, CurrentY, FreeLine, OperationsCounter):
    Masking = np.asarray(Mask)
    #Create PictureOut with the same size as PictureFG.
    PictureOut = np.zeros((len(PictureFG[0]), 4), dtype=np.uint8)


    #For each X
    for i in range(len(PictureFG[CurrentY])):
        if FreeLine[i] == True:
        #For each channel
            for j in range(len(PictureFG[CurrentY][i])):
                #If the mask is not transparent
                if Masking[CurrentY][i][0] == 0:
                    #Set the channel to the background picture
                    PictureOut[i][j] = PictureBG[CurrentY][i][j]
                    OperationsCounter.ApplyNoMask += 1
                else:
                    #Set the channel to the foreground picture
                    PictureOut[i][j] = PictureFG[CurrentY][i][j]
                    OperationsCounter.ApplyMask += 1

    return PictureOut
    #, FreeLine
    

        

#Check if the picture is RGB or RGBA. Returns the number of channels.
def CheckNumbersOfChannels(Picture):
    if (len(Picture[0][0]) == 4):
        return 4
    elif (len(Picture[0][0]) == 3):
        return 3
    else:
        print("No. Just no.")


