#Convert a greyscale picture to RGB
def GreyScaleToRGB(Picture):
    PictureOut = [[[0, 0, 0, 0] for i in range(len(Picture[0]))] for j in range(len(Picture))]
    for i in range(len(Picture)):
        for j in range(len(Picture[i])):
            PictureOut[i][j][0] = Picture[i][j][0]
            PictureOut[i][j][1] = Picture[i][j][0]
            PictureOut[i][j][2] = Picture[i][j][0]
            PictureOut[i][j][3] = Picture[i][j][3]
    return PictureOut