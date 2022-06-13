
#Convert a x bit RGB picture to a y bit RGB picture
def ConvertBPP(Picture, X_bits, Y_bits):
    #If the picture is already y bits, return the picture
    if X_bits == Y_bits:
        return Picture
    #If the picture is x bits, convert it to y bits
    elif X_bits > Y_bits:
        #Create a new picture with the correct number of bits
        PictureOut = [[[0, 0, 0, 0] for i in range(int(len(Picture[0])*Y_bits/X_bits))] for j in range(int(len(Picture)*Y_bits/X_bits))]
        #For each pixel in the picture, convert it to the correct number of bits
        for i in range(len(Picture)):
            for j in range(len(Picture[i])):
                #If the picture is x bits, convert it to y bits
                if X_bits > Y_bits:
                    #Convert the pixel to the correct number of bits
                    PictureOut[i][j] = [Picture[i][j][0]*(Y_bits/X_bits), Picture[i][j][1]*(Y_bits/X_bits), Picture[i][j][2]*(Y_bits/X_bits), Picture[i][j][3]]
                #If the picture is y bits, convert it to x bits
                elif X_bits < Y_bits:
                    #Convert the pixel to the correct number of bits
                    PictureOut[i][j] = [Picture[i][j][0]/(Y_bits/X_bits), Picture[i][j][1]/(Y_bits/X_bits), Picture[i][j][2]/(Y_bits/X_bits), Picture[i][j][3]]
        return PictureOut
    #If the picture is x bits, convert it to y bits
    elif X_bits < Y_bits:
        #Create a new picture with the correct number of bits
        PictureOut = [[[0, 0, 0, 0] for i in range(int(len(Picture[0])*X_bits/Y_bits))] for j in range(int(len(Picture)*X_bits/Y_bits))]