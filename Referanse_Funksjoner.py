#Create a function that combines two pictures by using the alpha blending algorithm.
import numpy as np
from PIL import Image


#Create a function that masks the current picture with a mask. Similar to model Mask
def Ref_Mask(Foreground, Offset, Background, Mask, FreeLine, RAM, TestEntity):
    #Store in RAM
    ForegroundAdress = RAM.put(Foreground, TestEntity)
    BackgroundAdress = RAM.put(Background, TestEntity)
    #For Iterate over the whole picture
    for y in range (len(Foreground)):
        for x in range (len(Foreground[y])):
#                for c in range (len(Foreground[y][x])):
                    #If maskbit empty, do nothing
                    if Mask[y][x].all() == 0:
                        pass
                    #if maskbit set, mask out picture
                    else:
                        Temp1 = RAM.get(ForegroundAdress, TestEntity)
                        Temp2 = RAM.get(BackgroundAdress, TestEntity)
                        Temp2[y+Offset[1]][x+Offset[0]] = Temp1[y][x]
                        RAM.put_specific(BackgroundAdress, Temp2, TestEntity)
                        RAM.put_specific(ForegroundAdress, Temp1, TestEntity)
                        FreeLine[y+Offset[1]][x+Offset[0]] = False
    
    return RAM.get(BackgroundAdress, TestEntity), FreeLine






#Create a function that applies a CLUT to the current picture. Similar to model CLUT
def Ref_CLUT(Picture, CLUT, Offset, RAM, TestEntity):
    #Store in RAM
    PicAdress = RAM.put(Picture, TestEntity)
    CLUTAdress = RAM.put(CLUT, TestEntity)
    #For whole picture
    for y in range (len(Picture)):
        for x in range (len(Picture[y])):
            #For every channel
                for c in range (len(Picture[y][x])-1):
                    TempPic = RAM.get(PicAdress, TestEntity)
                    TempCLUT = RAM.get(CLUTAdress, TestEntity)
                    #Change colour to accompanied new CLUT value
                    Picture[y][x][c] = CLUT[c][Picture[y][x][c]]
                    RAM.put_specific(PicAdress, Picture, TestEntity)
                    
    return RAM.get(PicAdress, TestEntity)


#Function to apply alpha to a picture. Similar to model Alpha
def Ref_Alpha(StructFG, Offset, StructBG, FreeLine, RAM, TestEntity):
    PictureOut = np.zeros((StructBG.Size[1], StructBG.Size[0], 4), dtype=np.uint8)
    #Store in RAM
    ForegroundAdress = RAM.put(StructFG.Picture, TestEntity)
    BackgroundAdress = RAM.put(StructBG.Picture, TestEntity)
    PictureOutAdress = RAM.put(PictureOut, TestEntity)
    for y in range(len(StructBG.Picture)):
        for x in range(len(StructBG.Picture[0])):
            if x - Offset[0] >= 0 and x - Offset[0] < StructFG.Size[0]:
                if y - Offset[1] >= 0 and y - Offset[1] < StructFG.Size[1]:
                    #If fully transparent
                    if StructFG.Picture[y-Offset[1]][x-Offset[0]][3] == 0:
                        TempFG = RAM.get(ForegroundAdress, TestEntity)
                        TempOut = RAM.get(PictureOutAdress, TestEntity)
                        TempOut[x + Offset[0]] = TempFG[y][x]
                        RAM.put_specific(PictureOutAdress, TempOut, TestEntity)
                        RAM.put_specific(ForegroundAdress, TempFG, TestEntity)
                        TestEntity.AlphaPassed += 1
                    #Blend it
                    #Each channel
                    #Fg*Alpha + Bg*(1-Alpha)
                    else:
                        TempFG = RAM.get(ForegroundAdress, TestEntity)
                        TempBG = RAM.get(BackgroundAdress, TestEntity)
                        TempOut = RAM.get(PictureOutAdress, TestEntity)
                        R = TempFG[y-Offset[1]][x-Offset[0]][0]*TempFG[y-Offset[1]][x-Offset[0]][3]/255 + TempBG[y][x][0]*(1-TempFG[y-Offset[1]][x-Offset[0]][3]/255)
                        TestEntity.ApplyAlphaR += 1
                        B = TempFG[y-Offset[1]][x-Offset[0]][1]*TempFG[y-Offset[1]][x-Offset[0]][3]/255 + TempBG[y][x][1]*(1-TempFG[y-Offset[1]][x-Offset[0]][3]/255)
                        TestEntity.ApplyAlphaG += 1
                        G = TempFG[y-Offset[1]][x-Offset[0]][2]*TempFG[y-Offset[1]][x-Offset[0]][3]/255 + TempBG[y][x][2]*(1-TempFG[y-Offset[1]][x-Offset[0]][3]/255)
                        TestEntity.ApplyAlphaB += 1
                        FreeLine[y][x] = False
                        TempOut[y][x][0], TempOut[y][x][1], TempOut[y][x][2], TempOut[y][x][3]  =  R, G, B, TempFG[y-Offset[1]][x-Offset[0]][3]
                        RAM.put_specific(PictureOutAdress, TempOut, TestEntity)
                else:
                    TempBG = RAM.get(BackgroundAdress, TestEntity)
                    TempOut = RAM.get(PictureOutAdress, TestEntity)
                    TempOut[y][x] = TempBG[y][x]
                    RAM.put_specific(PictureOutAdress, TempOut, TestEntity)
            else:
                TempBG = RAM.get(BackgroundAdress, TestEntity)
                TempOut = RAM.get(PictureOutAdress, TestEntity)
                TempOut[y][x] = TempBG[y][x]
                RAM.put_specific(PictureOutAdress, TempOut, TestEntity)

        TestEntity.AlphaBlend += 1
    return RAM.get(PictureOutAdress, TestEntity), FreeLine


#Fills any free pixels with background
def Ref_Fill(Picture, Background, FreeLine, RAM, TestEntity):
    PicAdress = RAM.put(Picture, TestEntity)
    BackgroundAdress = RAM.put(Background, TestEntity)
    for y in range(len(Background)):
        for x in range(len(Background[0])):
            if FreeLine[y][x] == True:
                RAM.get(PicAdress, TestEntity)
                RAM.get(BackgroundAdress, TestEntity)
                Picture[y][x] = Background[y][x]
    return Picture