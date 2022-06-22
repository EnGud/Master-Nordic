#Masks each channel given by the mask.
import numpy as np




#Masks each channel given by the mask.
def ApplyMask(PictureFG, X_Offset, PictureBG, Mask, TestEntity):
    #White (>0) means draw, black (0) means remove
    #Create PictureOut with the same size as PictureFG.
    PictureOut = np.zeros((len(PictureBG), 4), dtype=np.uint8)


    #For each X
    for i in range(len(PictureFG)):
        if TestEntity.FreeLine[i+X_Offset] == True:
        #For each channel
                #If the mask is not transparent
                if Mask[i].all() == 0:
                    #Set the channel to the background picture
                    PictureOut[i+X_Offset] = PictureBG[i+X_Offset]
                    TestEntity.NoMask += 1
                    pass
                    
                    
                else:
                    #Set the channel to the foreground picture
                    PictureOut[i+X_Offset] = PictureFG[i]
                    if TestEntity.CurrentLayer != 0:
                        TestEntity.FreeLine[i+X_Offset] = False
                    TestEntity.ApplyMask += 1

    return PictureOut
    #, TestEntity.FreeLine
    

        

#Check if the picture is RGB or RGBA. Returns the number of channels. Not used.
def CheckNumbersOfChannels(Picture):
    if (len(Picture[0][0]) == 4):
        return 4
    elif (len(Picture[0][0]) == 3):
        return 3
    else:
        print("No. Just no.")
