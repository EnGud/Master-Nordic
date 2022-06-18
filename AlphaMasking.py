#Masks each channel given by the mask.
import numpy as np




#Masks each channel given by the mask.
def ApplyMask(PictureFG, X_Offset, PictureBG, Mask, FreeLine, TestEntity):
    
    #Create PictureOut with the same size as PictureFG.
    PictureOut = np.zeros((len(PictureBG), 4), dtype=np.uint8)


    #For each X
    for i in range(len(PictureFG)):
        if FreeLine[i+X_Offset] == True:
        #For each channel
                #If the mask is not transparent
                if Mask[i] == 0:
                    #Set the channel to the background picture
                    pass
                    #PictureOut[i+X_Offset] = PictureBG[i+X_Offset]
                    #TestEntity.NoMask += 1
                else:
                    #Set the channel to the foreground picture
                    PictureOut[i+X_Offset] = PictureFG[i]
                    FreeLine[i+X_Offset] = False
                    #TestEntity.ApplyMask += 1

    return PictureOut, FreeLine
    #, FreeLine
    

        

#Check if the picture is RGB or RGBA. Returns the number of channels.
def CheckNumbersOfChannels(Picture):
    if (len(Picture[0][0]) == 4):
        return 4
    elif (len(Picture[0][0]) == 3):
        return 3
    else:
        print("No. Just no.")


