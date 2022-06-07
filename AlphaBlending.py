from ast import Return
from math import fabs
from multiprocessing.dummy import Array
from tkinter import Image
from turtle import clear
import PIL
from PIL import Image
import numpy as np
import OperationsCounter
#import lvgl as lv


#def UserImageOpen()
#Number of pictures Input()
#Loop through numbers, taking input picture location as new input()


#R2, G2, B2, A2 = Image.split(BufferedPicture2)

class AlphaOperations:


    def AlphaFormula(Operator, Fg, A, Bg):
        if(Operator == "Over"):
            Out = Fg*A+(1-A)*Bg
            return Out

        #Andre operatører, TBA
        elif(Operator == "Xor"):
            exit
        elif(Operator == "Top"):
            exit
        elif(Operator == "And"):
            exit
        elif(Operator == "Xor"):
            exit
        elif(Operator == "Xor"):
            exit
        else:
            exit


    #If different format or illeglible/missing alpha
    def CheckAlpha(Picture):
    #If Picture != RGBA
        Height, Width, Channels = np.asarray(Picture).shape
        if Channels != 4:
            print("Image #X has no Alpha Channel. Please input desired transparency:")
            while (Channels != 4 or (UserAlpha > 255 or UserAlpha < 0)):
                NumberPlease = input()
                if (NumberPlease.isdigit()):
                    UserAlpha = int(input())
                    if UserAlpha > 255 or UserAlpha < 0:
                        print("Alpha must be between 0 and 255")
                    elif UserAlpha <= 255 or UserAlpha >= 0:
                        break
                else:
                    print("Please input a number")


            
            Picture.putalpha(UserAlpha)
            #BufferedPicture2.save("test.bmp", "BMP")
        OperationsCounter.CheckAlpha =+ 1


    #Input foreground, background
    def ApplyAlpha(PictureFG, PictureBG, CurrentY, operatorIn, OperationsCounter):
        #Setups local variables etc.
        FGSize = PictureFG.size 
        BGSize = PictureBG.size 
        FG_X_Size, FG_Y_Size, BG_X_Size, BG_Y_Size = (FGSize[0]-1), (FGSize[1]-1), (BGSize[0]-1), (BGSize[1]-1)

  #      BitDepthRed, BitDepthGreen, BitDepthBlue


        ArrayedForeground = np.asarray(PictureFG)
        #LineForeground = ArrayedForeground[CurrentY]
        ArrayedBackground = np.asarray(PictureBG)
        #LineBackground = ArrayedBackground[CurrentY]

        Output = np.zeros((1, BG_X_Size, 4), dtype=np.uint8)
 

        #Flagging-system
        RIsReady = False
        GIsReady = False
        BIsReady = False

        #count
        OperationsCounter.ApplyAlphaInit =+ 1
        #Iterate over each pixel, each channel, applying the alpha
        #Bedre å hente ut arrayene til 1D array, istedenfor søk hver iterasjon? 

        #ApplyAlpha for hver kanal, R G B.

        #RED
        for i in range (FG_X_Size):
            LocalFgR = ArrayedForeground[CurrentY][i][0]
            LocalA = ArrayedForeground[CurrentY][i][3]/255
            LocalBgR = ArrayedBackground[CurrentY][i][0]
            
            Output[0][i][0] = int(AlphaOperations.AlphaFormula(operatorIn, LocalFgR, LocalA, LocalBgR))

            OperationsCounter.ApplyAlphaR =+ 1
            if (i is (FG_X_Size-1)):
                RIsReady = True

        
        #GREEN
        for i in range (FG_X_Size):
            LocalFgG = ArrayedForeground[CurrentY][i][1]
            LocalA = float(ArrayedForeground[CurrentY][i][3])/255
            LocalBgG = ArrayedBackground[CurrentY][i][1]
            
            Output[0][i][1] = AlphaOperations.AlphaFormula(operatorIn, LocalFgG, LocalA, LocalBgG)


            OperationsCounter.ApplyAlphaG =+ 1
            if (i is (FG_X_Size-1)):
                GIsReady = True

        #BLUE
        for i in range (FG_X_Size):
            LocalFgB = ArrayedForeground[CurrentY][i][2]
            LocalA = float(ArrayedForeground[CurrentY][i][3])/255
            LocalBgB = ArrayedBackground[CurrentY][i][2]
            
            Output[0][i][2] = AlphaOperations.AlphaFormula(operatorIn, LocalFgB, LocalA, LocalBgB)

            OperationsCounter.ApplyAlphaB =+ 1
            if (i is (FG_X_Size-1)):
                BIsReady = True


        return Output


        #Dersom 1D array, bytt til
        #for i in range (Offset, (xlength+Offset)):
        #        BlueArray[i] = int((ArrayedForeground[y][i][2] * ArrayedForeground[y][i][3]/255) + (ArrayedBackground[y][i][2] * (1.0 - float(ArrayedForeground[y][i][3])/255)));
        
    

        #if (RIsReady and GIsReady and BIsReady):

            #for i in range (xlength):
            #    OutResult[i][0] = RedArray[i]
           # for i in range (xlength):
           #     OutResult[i][1] = GreenArray[i]
           # for i in range (xlength):    
           #     OutResult[i][2] = BlueArray[i]

            #Update flags
           # RIsReady = False
           # GIsReady = False
           # BIsReady = False
            



        OperationsCounter.ApplyAlpha =+ 1

        return OutResult



    


#Leftover Code Backup


#           RedArray[i] = int((ArrayedForeground[ylength][i][3]* ArrayedForeground[ylength][i][3]/255) + (ArrayedBackground[ylength][i][0] * (1.0 - float(ArrayedForeground[ylength][i][3])/255)));
#           GreenArray[i] = int((ArrayedForeground[ylength][i][1] * ArrayedForeground[ylength][i][3]/255) + (ArrayedBackground[ylength][i][1] * (1.0 - float(ArrayedForeground[ylength][i][3])/255)));
#           BlueArray[i] = int((ArrayedForeground[ylength][i][2] * ArrayedForeground[ylength][i][3]/255) + (ArrayedBackground[ylength][i][2] * (1.0 - float(ArrayedForeground[ylength][i][3])/255)));
           


#        def __iter__(self, Picture1, Picture2, ycoordinate):
 #       #Picture1 foreground, Picture2 background
  #          self.ArrayedForeground = np.asarray(Picture1)
   #         self.ArrayedBackground = np.asarray(Picture2)
#
 #           
  #          #Convert to between 0.0 and 1.0 as array
   #         #R, G, B = R/255, G/255, B/255
#
 #           OperationsCounter.ApplyAlphaInit =+ 1
  #          return self
   # 
    #    def __next__(self):
     #       
      #      
       #     for i in range (Offset, (Offset + xlength)):
        #        #Iterer over hver R, G, B, over hver pixel. Begrensning til en linje kommer når funksjonen funker ;)))))))
#
#
 #               outputRed = (Picture1[3][1][i]/255 * Picture1[3][4][i]/255) + (Picture2[3][1][i]/255 * (1.0 - float(Picture1[3][4][i])/255));
  #              outputGreen = (Picture1[3][2][i]/255 * Picture1[3][4][i]/255) + (Picture2[3][2][i]/255 * (1.0 - float(Picture1[3][4][i]))/255);
   #             outputBlue = (Picture1[3][3][i]/255 * Picture1[3][4][i]/255) + (Picture2[3][3][i]/255 * (1.0 - float(Picture1[3][4][i]))/255);



            #if size > max
            #   raise StopIteration
           # OperationsCounter.ApplyAlpha =+ 1




    #Main Loop
    #CheckAlpha(BufferedPicture2)
    #ApplyAlpha()
   # Test = np.asarray(BufferedPicture2)
   # print(Test.shape)









    #Testsinsgss
    #print(np.asarray(BufferedPicture2))

#    BufferedPicture1 = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/800x600_Wallpaper_Blue_Sky.jpg")
#    BufferedPicture1.putalpha(250)
#    print(BufferedPicture1.mode)
#    BufferedPicture1.save("Test.bmp")