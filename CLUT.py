#Class for color lookup table with R, G and B channels
import numpy as np

def GenerateCLUT(sizeR, sizeG, sizeB):
        #Generate a color lookup table for R, G and B channels with each channel having a size of sizeR, sizeG and sizeB. Start at 0 and end at sizeR-1, sizeG-1 and sizeB-1.
        CLUT = [[[0 for b in range (sizeB)] for g in range (sizeG)] for r in range (sizeR)]
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


def ChangeCLUT(OldCLUT, NewCLUT):
        #replace OldCLUT with NewCLUT. OldCLUT and NewCLUT are 2D arrays that contain the CLUT values in R, G, B order.
        #OldCLUT and NewCLUT are of the same size.
        OutCLUT = [[[0 for b in range (len(NewCLUT[0][0]))] for g in range (len(NewCLUT[0]))] for r in range (len(NewCLUT))]

        for i in range (len(OldCLUT)):
            for j in range (len(OldCLUT[i])):
                OutCLUT[i][j] = NewCLUT[i][j]
        return OutCLUT


def ApplyCLUT(Picture, CLUT, CurrentY, TestEntity):
    #Iterate through each pixel in Picture, use the value to find the position in the CLUT and set the pixel to the value in the CLUT.
    #Picture is a 2D array that contains the pixel values in R, G, B order.
    #CLUT is a 2D array that contains the CLUT values in R, G, B order.
    #CurrentY is the current Y position in Picture.
    #PictureOut is a 2D array that contains the pixel values in R, G, B order.
    PictureOut = np.zeros((len(Picture[0]), 4), dtype=np.uint8)

    #Get the RGB values from Picture
    #Create temp as [4][255] using numpy
    Temp = np.zeros((4), dtype=np.uint8)


    for i in range(len(Picture[CurrentY])):
        Temp[0], Temp[1], Temp[2] = Picture[CurrentY][i][0], Picture[CurrentY][i][1], Picture[CurrentY][i][2]

        #[0, 0, 0, 0]
        #Use the RGB values to find the position in the CLUT. R, G, B

        Temp[0], Temp[1], Temp[2] = CLUT[0][Temp[0]], CLUT[1][Temp[1]], CLUT[2][Temp[2]]



        #Set the pixel to the value in the CLUT
        
        PictureOut[i][0], PictureOut[i][1], PictureOut[i][2] = Temp[0], Temp[1], Temp[2]
        if (len(Picture[CurrentY][i]) == 4):
            PictureOut[i][3] = Picture[CurrentY][i][3]

    return PictureOut

    