#Alpha Compositing

import numpy as np

#Alpha Compositing is the process of combining two images with a transparency mask
PictureOut = np.zeros((800, 4), dtype=np.uint8)

#Function that checks if a picture contains alpha.
def check_alpha(picture, TestEntity):     
        #If it does not, allow the user to input a custom alpha. If it is not within bounds (0, 255), return an error and ask again.
        if (len(picture[0][0]) == 3):
            while True:
                alpha = input("Enter alpha value: ")
                if alpha.isdigit():
                    alpha = int(alpha)
                    if alpha >= 0 and alpha <= 255:
                        break
                    else:
                        print("Invalid alpha value")
                else:
                    print("Invalid alpha value")
            
            
            #put the alpha value into thepicture
            PictureOut = [[[0, 0, 0, 0] for i in range(len(picture[0]))] for j in range(len(picture))]

            for i in range(len(picture)):
                for j in range(len(picture[i])):
                    PictureOut[i][j][0] = picture[i][j][0]
                    PictureOut[i][j][1] = picture[i][j][1]
                    PictureOut[i][j][2] = picture[i][j][2]
                    PictureOut[i][j][3] = alpha
            print("Alpha value set.")
            return PictureOut
        else:
            print("Alpha already present")
            #ask user if want to input new alpha
            print("Do you want to input a new alpha value? Y/N")
            if (input() == "y" or "Y" or "yes" or "Yes"):
                while True:
                    alpha = input("Enter alpha value: ")
                    if alpha.isdigit():
                        alpha = int(alpha)
                        if alpha >= 0 and alpha <= 255:
                            break
                        else:
                            print("Invalid alpha value")
                    else:
                        print("Invalid alpha value")

                for i in range (len(picture)):
                    for j in range (len(picture[i])):
                        picture[i][j][3] = alpha
                return picture
                
            
            
            else:
                print("ok, no alpha value set.")
                
            return picture




#Formula for simple "Over" operator.
def AlphaFormula(Fg, Bg, Alpha):
        #Out = Fg*A+Bg*(1-A)
        return Fg*Alpha + Bg*(1-Alpha)

#Create a function that blends two pictures together, using foregrounds alpha as "mask".
def ApplyAlpha (Foreground, X_Offset, Operator, Background, FreeLine, TestEntity):
    #The input Foreground is a picture of x length with a x offset relative to background. Background is a picture of another length.
    #The output is a picture of the same length as the background, but with the foreground applied.
    if (Operator == ("Over" or "over")):
        PictureOut = np.zeros((len(Background), 4), dtype=np.uint8)
        for CurrentX in range(len(Foreground)):
            

            #If the current pixel is free
            if FreeLine[CurrentX + X_Offset] == True:

                if Foreground[CurrentX][3] == 0:
                    PictureOut[CurrentX + X_Offset] = Foreground[CurrentX]
                    TestEntity.AlphaPassed += 1

                else:
                            
                        #map the foreground alpha value to a range of 0 to 1. This is done to avoid floating point errors.
                        #wtf skjer her? bugga bajs
                    Alpha = np.asarray(Foreground[CurrentX][3])
                    AlphaOut = Alpha
                    Alpha = Alpha/255
                    
                        
                    TestEntity.ApplyAlpha += 1



                        
                    Red = AlphaFormula(Foreground[CurrentX][0], Background[CurrentX+X_Offset][0], Alpha)
                    TestEntity.ApplyAlphaR += 1
                    Green = AlphaFormula(Foreground[CurrentX][1], Background[CurrentX+X_Offset][1], Alpha)
                    TestEntity.ApplyAlphaG += 1
                    Blue = AlphaFormula(Foreground[CurrentX][2], Background[CurrentX+X_Offset][2], Alpha)
                    TestEntity.ApplyAlphaB += 1
                        #Combine Red, Green and Blue into PictureOut
                    PictureOut[CurrentX+X_Offset][0] = Red
                    PictureOut[CurrentX+X_Offset][1] = Green
                    PictureOut[CurrentX+X_Offset][2] = Blue
                    PictureOut[CurrentX+X_Offset][3] = AlphaOut
                        #PictureOut[CurrentX] = [Red, Green, Blue, AlphaOut]

                FreeLine[CurrentX + X_Offset] = False

        return PictureOut, FreeLine


#Put alpha value into the input picture, which is in format (800, 4). The input also contains the alpha value to put in
def PutAlpha (Picture, Alpha):
    PictureOut = np.zeros((len(Picture),len(Picture[0]), 4), dtype=np.uint8)
    for j in range (len(Picture)):
        for i in range(len(Picture[0])):
            PictureOut[j][i][0] = Picture[j][i][0]
            PictureOut[j][i][1] = Picture[j][i][1]
            PictureOut[j][i][2] = Picture[j][i][2]
            PictureOut[j][i][3] = Alpha

    return PictureOut