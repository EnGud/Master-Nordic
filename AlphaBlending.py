#Alpha Compositing

import numpy as np

#Alpha Compositing is the process of combining two images with a transparency mask


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
def ApplyAlpha(Foreground, Operator, Background, currentY, TestEntity):
        #0 = transparent, 255 = opaque
        #Create PictureOut as an output buffer
        PictureOut = np.zeros((len(Foreground[currentY]), 4), dtype=np.uint8)


        #For each pixel in the picture, apply the alpha value
        if (Operator == ("Over" or "over")):
            for CurrentX in range (len(Foreground[0])):
                
                if Foreground[currentY][CurrentX][3] == 0:
                    PictureOut[CurrentX] = Foreground[currentY][CurrentX]
                    #TestEntity.AlphaPassed += 1
                else:
                        
                    #map the foreground alpha value to a range of 0 to 1. This is done to avoid floating point errors.
                    #wtf skjer her? bugga bajs
                    Alpha = np.asarray(Foreground[currentY][CurrentX][3])
                    AlphaOut = Alpha
                    Alpha = Alpha/255
                   
                    
                    #TestEntity.ApplyAlpha += 1



                    
                    Red = AlphaFormula(Foreground[currentY][CurrentX][0], Background[currentY][CurrentX][0], Alpha)
                    Green = AlphaFormula(Foreground[currentY][CurrentX][1], Background[currentY][CurrentX][1], Alpha)
                    Blue = AlphaFormula(Foreground[currentY][CurrentX][2], Background[currentY][CurrentX][2], Alpha)
                    #Combine Red, Green and Blue into PictureOut
                    PictureOut[CurrentX] = [Red, Green, Blue, AlphaOut]

            return PictureOut

        #Ubrukte funksjoner nedenfor.
        if (Operator == "in"):
            #not used
            pass
        if (Operator == "out"):
            #not used
            pass
        if (Operator == "atop"):
            #not used
            pass
        if (Operator == "xor"):
            #not used
            pass


    #Ikke testa. ikke viktig atm. drit i hele funksjonen. :)
def ApplyGammaCorrection(self, Foreground, Background, currentY, Gamma, TestEntity):
                #StackOverflow'd-ish & Veldig Wikipedia'd.
        
        #Buffer
        PictureOut = np.zeros((len(Foreground[currentY]), 4), dtype=np.uint8)
        #For each pixel in the picture, apply the alpha value and gamma correction
        for i in range(len(Foreground)):
            for j in range(len(Foreground[i])):
                #Apply the alpha value
                #feil
                Alpha = Foreground[currentY][i][3]
                PictureOut[i][j][3] = Foreground[i][j][3]*Alpha
                #Apply the gamma correction
                PictureOut[i][j][0] = Foreground[i][j][0]**Gamma
                PictureOut[i][j][1] = Foreground[i][j][1]**Gamma
                PictureOut[i][j][2] = Foreground[i][j][2]**Gamma
        return PictureOut
    #Mattematisk formel for gamma-korreksjon:
    #Co = ((Ca**(1/gamma)*Aa + Cb**(1/gamma)*Ab*(1-Aa))/Ao)**(gamma)


#