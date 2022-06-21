#Create a function that combines two pictures by using the alpha blending algorithm.
import numpy as np
from PIL import Image

#Create a function that masks the current picture with a mask.
def Ref_Mask(Foreground, Offset, Background, Mask, FreeLine):

    for y in range (len(Foreground)):
        for x in range (len(Foreground[y])):
#                for c in range (len(Foreground[y][x])):
                    if Mask[y][x].all() == 0:
                        Background[y+Offset[1]][x+Offset[0]] = Background[y+Offset[1]][x+Offset[0]]
                        
                    else:
                        Background[y+Offset[1]][x+Offset[0]] = Foreground[y][x]
                        FreeLine[y+Offset[1]][x+Offset[0]] = False
    
    for y in range (len(Background)):
        for x in range (len(Background[y])):
            #((Temp[y][x][0] and Temp[y][x][1] and Temp[y][x][2])== 0) and (Nedenfor)
                if  (FreeLine[y][x] == True):
                    Background[y][x] = Background[y][x]

    return Background, FreeLine






#Create a function that applies a CLUT to the current picture.
def Ref_CLUT(Picture, CLUT, Offset):
    for y in range (len(Picture)):
        for x in range (len(Picture[y])):
                for c in range (len(Picture[y][x])):
                    Picture[y][x][c] = CLUT[c][Picture[y][x][c]]
                    
    return Picture



def Ref_Alpha(StructFG, Offset, StructBG, FreeLine):
    PictureOut = np.zeros((StructBG.Size[1], StructBG.Size[0], 4), dtype=np.uint8)
    for y in range(len(StructBG.Picture)):
        for x in range(len(StructBG.Picture[0])):
            if x - Offset[0] >= 0 and x - Offset[0] < StructFG.Size[0]:
                if y - Offset[1] >= 0 and y - Offset[1] < StructFG.Size[1]:
                 #Blend it
                 #Each channel
                    R = StructFG.Picture[y-Offset[1]][x-Offset[0]][0]*StructFG.Picture[y-Offset[1]][x-Offset[0]][3]/255 + StructBG.Picture[y][x][0]*(1-StructFG.Picture[y-Offset[1]][x-Offset[0]][3]/255)
                    B = StructFG.Picture[y-Offset[1]][x-Offset[0]][1]*StructFG.Picture[y-Offset[1]][x-Offset[0]][3]/255 + StructBG.Picture[y][x][1]*(1-StructFG.Picture[y-Offset[1]][x-Offset[0]][3]/255)
                    G = StructFG.Picture[y-Offset[1]][x-Offset[0]][2]*StructFG.Picture[y-Offset[1]][x-Offset[0]][3]/255 + StructBG.Picture[y][x][2]*(1-StructFG.Picture[y-Offset[1]][x-Offset[0]][3]/255)
                    FreeLine[y][x] = False
                    PictureOut[y][x][0], PictureOut[y][x][1], PictureOut[y][x][2], PictureOut[y][x][3]  =  R, G, B, StructFG.Picture[y-Offset[1]][x-Offset[0]][3]
                else:
                    PictureOut[y][x] = StructBG.Picture[y][x]
            else:
                PictureOut[y][x] = StructBG.Picture[y][x]

    return PictureOut, FreeLine


def PutAlpha (Picture, Alpha):
    PictureOut = np.zeros((len(Picture),len(Picture[0]), 4), dtype=np.uint8)
    for j in range (len(Picture)):
        for i in range(len(Picture[0])):
            PictureOut[j][i][0] = Picture[j][i][0]
            PictureOut[j][i][1] = Picture[j][i][1]
            PictureOut[j][i][2] = Picture[j][i][2]
            PictureOut[j][i][3] = Alpha

    return PictureOut

