#Class for color lookup table with R, G and B channels
import numpy as np


def GenerateCLUT(sizeR, sizeG, sizeB):
        #Generate a color lookup table for R, G and B channels with each channel having a size of sizeR, sizeG and sizeB. Start at 0 and end at sizeR-1, sizeG-1 and sizeB-1. The array is 2D.
    CLUTR = np.zeros((1, sizeR), dtype=np.uint8)
    CLUTG = np.zeros((1, sizeG), dtype=np.uint8)
    CLUTB = np.zeros((1, sizeB), dtype=np.uint8)
    #Merge CLUTR, CLUTG and CLUTB into a single 2D array called CLUT
    CLUT = np.concatenate((CLUTR, CLUTG, CLUTB), axis=0)
    return CLUT



def GenerateTestCLUT(sizeR, sizeG, sizeB):
    #Generate a color lookup table for R, G and B channels with each channel having a size of sizeR, sizeG and sizeB. Start at sizeR-1, sizeG-1 and sizeB-1 and end at 0.
    #Only similar CLUT values atm
    CLUT = np.zeros((3, sizeR), dtype=np.uint8)
    #Generate the CLUT as 2D arrays in R, G, B order.
    for i in range(sizeR):
        CLUT[0][i] = sizeR - i
        CLUT[1][i] = sizeG - i
        CLUT[2][i] = sizeB - i
    return CLUT


def ChangeCLUT(OldCLUT, NewCLUT, TestEntity):
        #replace OldCLUT with NewCLUT. OldCLUT and NewCLUT are 2D arrays that contain the CLUT values in R, G, B order.
        #OldCLUT and NewCLUT are of the same size.
        OutCLUT = [[[0 for b in range (len(NewCLUT[0][0]))] for g in range (len(NewCLUT[0]))] for r in range (len(NewCLUT))]

        for i in range (len(OldCLUT)):
            for CurrentX in range (len(OldCLUT[i])):
                OutCLUT[i][CurrentX] = NewCLUT[i][CurrentX]
        TestEntity.ChangeCLUT += 1
        return OutCLUT

#CurrentY er midlertidig til RAM er oppe
def ApplyCLUT(Picture, CLUT, X_Offset, TestEntity):
    #Iterate through each pixel in Picture, use the value to find the position in the CLUT and set the pixel to the value in the CLUT.
    #Picture is a 2D array that contains the pixel values in R, G, B order.
    #CLUT is a 2D array that contains the CLUT values in R, G, B order.
    #CurrentY is the current Y position in Picture.
    #PictureOut is a 2D array that contains the pixel values in R, G, B order.
    PictureOut = np.zeros((800, 4), dtype=np.uint8)

    #Get the RGB values from Picture
    #Create temp as [4][255] using numpy
    #Temp = np.zeros((4), dtype=np.uint8)


    for CurrentX in range(len(Picture)):
        if TestEntity.FreeLine[CurrentX+X_Offset]:

                #[0, 0, 0, 0]
                #Use the RGB values to find the position in the CLUT. R, G, B

            #Temp[0], Temp[1], Temp[2] = CLUT[0][Picture[CurrentX][0]], CLUT[1][Picture[CurrentX][1]], CLUT[2][Picture[CurrentX][2]]



                #Set the pixel to the value in the CLUT
                
            PictureOut[CurrentX+X_Offset][0], PictureOut[CurrentX+X_Offset][1], PictureOut[CurrentX+X_Offset][2] = CLUT[0][Picture[CurrentX][0]], CLUT[1][Picture[CurrentX][1]], CLUT[2][Picture[CurrentX][2]]
            if (len(Picture[CurrentX]) == 4):
                PictureOut[CurrentX+X_Offset][3] = Picture[CurrentX+X_Offset][3]
            
            if TestEntity.CurrentLayer != 0:
                TestEntity.FreeLine[CurrentX + X_Offset] = False
            TestEntity.CLUT_Pixel_Applied += 1





    TestEntity.CLUT_Applied += 1

    return PictureOut

    