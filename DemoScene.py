from asyncio.base_futures import _FINISHED
import Scene_Descriptor
import AlphaBlending
import AlphaMasking
import OperationsCounter
import Dynamic_RAM
import CLUT
from PIL import Image
import Misc_Operations
import Analytics
import numpy as np
import threading
import MenusConstructor

import time


""" print("Custom resolution? Yes/No")
if(input()==("Yes" or "yes")):
    print("Please input X resolution")
    ScreenResolutionX = input()
    print("Please input Y resolution")
    ScreenResolutionY = input()
else:
    print("Okay, No custom resolution :( Setting to standard resolution 800x600")
    ScreenResolutionX = 800
    ScreenResolutionY = 600 """

ScreenResolutionX = 800
ScreenResolutionY = 600

#Setup
TestEntity = OperationsCounter.OperationsCounter(ScreenResolutionY)
StateMachineStatus = "Main"
OutputBuffer = np.zeros((ScreenResolutionX, 4), dtype=np.uint8)
OutputBufferLarge = np.zeros((ScreenResolutionY, ScreenResolutionX, 4), dtype=np.uint8)

RAM=Dynamic_RAM.RAM(32, TestEntity)

#Use Scene_Descriptor to build the scene through a function


def Render(Items, CurrentY, RAM):
    FreeLine = [True]*ScreenResolutionX
    #MainMenu
    #.Items

    DrawnCurrentLine = False

    #VI STARTER MED EN TOM X-ARRAY MED STØRRELSE SKJERMEN
    PictureOut = np.zeros((800, 4), dtype=np.uint8)

    #Traverse linked list
    CurrentItem = Items[len(Items)-1]
    while CurrentItem.Next != None:
        #Pointer
        Structure = CurrentItem

        Dynamic_RAM.StorePicInRam(CurrentItem, CurrentY, RAM, TestEntity)
        #print(CurrentItem.Picture_RAM_Adress)
        #RAM.check(TestEntity)
        #RAM.CheckEveryArrayBit(TestEntity)


        
        
        #

        #Hvis CurrentY er innenfor nåværendes bilde-lag
        if ((CurrentY >= Structure.PictureOffset[1]) and (CurrentY < Structure.PictureOffset[1] + Structure.PictureSize[1])): 
            #Dynamic_RAM.StorePicInRam(CurrentItem, CurrentY, RAM, TestEntity)
            #RAM.check(TestEntity)
            #RAM.CheckEveryArrayBit(TestEntity)
            #Sjekk om CLUT skal utføres
            if(Structure.ApplyCLUT):
                #Utfør CLUT
                #ApplyCLUT(Picture, CLUT, FreeLine, TestEntity):
                #RAM.get(PictureAdress, TestEntity)
                PictureOut, FreeLine = CLUT.ApplyCLUT(Structure.Picture[CurrentY-Structure.PictureOffset[1]], Structure.CLUT, Structure.PictureOffset[0], FreeLine, TestEntity)
                #RAM.put(Picture, TestEntity)

            if(Structure.ApplyMask):
            #            #Generate MaskedPicture as empty image with size of picture
            #ApplyMask(PictureFG, X_Offset, PictureBG, Mask, FreeLine, TestEntity):
            #Mask must match PictureFG.
                PictureOut, FreeLine = AlphaMasking.ApplyMask(Structure.Picture[(CurrentY-Structure.PictureOffset[1])], Structure.PictureOffset[0], Items[1].Picture[CurrentY], Structure.Mask[CurrentY-Structure.PictureOffset[1]], FreeLine, OperationsCounter)
            #    Structure.Picture[CurrentY] = AlphaMasking.ApplyMask(Structure.Picture, Items.Array[0].Picture, Structure.PictureInfo.Mask , CurrentY, TestEntity)

            #Sjekk om Alpha Blending skal utføres
            if(Structure.ApplyAlpha):
                #Utfør Alpha Blending
                #ApplyAlpha (Foreground, X_Offset, Operator, Background, FreeLine, TestEntity):
                #Picture = RAM.get(Structure.Picture_RAM_Adress, TestEntity)
                #RAM Eksempel
                #PictureOut = AlphaBlending.ApplyAlpha(RAM.get(Structure.Picture_RAM_Adress, TestEntity), "over", Items[0].Picture_RAM_Adress, FreeLine, TestEntity)
                #Dynamic_RAM.StorePicInRam(Items[0].Picture, CurrentY, RAM, TestEntity)
                PictureOut, FreeLine = AlphaBlending.ApplyAlpha(Structure.Picture[(CurrentY-Structure.PictureOffset[1])], Structure.PictureOffset[0], "Over", Items[1].Picture[CurrentY], FreeLine, TestEntity)
                #Structure.Picture_RAM_Adress = RAM.put(Picture_RAM_Adress, TestEntity)

            


        #Apply Background to every FreeLine bit
        for x in range(ScreenResolutionX):
            if(FreeLine[x] == True):
                PictureOut[x] = Items[1].Picture[CurrentY][x]


        RAM.clear(CurrentItem.Picture_RAM_Adress, TestEntity)
        #RAM.check(TestEntity)
        #RAM.CheckEveryArrayBit(TestEntity)
        #FreeLine = FreeLine and PictureOut
        CurrentItem = CurrentItem.Next

    
    return PictureOut

        


Runs = 0 
while(1):

    #Use a state machine to control the flow of the program. Start with MainMenu, let it iterate for 3 cycles, then go to SettingsMenu. Let it run for two cycles then go to SubSettingsMenu. Let it run for two cycles then go to OrderCoffee. Let it run for three cycles then go to MainMenu. Try to implement threading on Render()
    if (StateMachineStatus == "Main"):
        #MainMenu Build bygges ikke realtime! Bytt ut med å lagre en kopi av MainMenu i RAM eller noe.
        MainMenu = MenusConstructor.MainMenuBuild()
        #Render MainMeny for the length of ScreenResolutionY
        #Start timing
        StartTime = time.time()
        for CurrentY in range(ScreenResolutionY):
            OutputBuffer = Render(MainMenu, CurrentY, RAM)
            #OutputBufferLarge is only used to visualize the picture. NOT FOR THE ACTUAL MEASUREMENTS OF LINE TIMINGS!
            OutputBufferLarge[CurrentY] = OutputBuffer
            print(CurrentY)
            #Lagre større buffer, kun for visualisering/verifisering.
        #Stop timing
        EndTime = time.time()


        #draw OutputBufferLarge to screen

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene.bmp")
        #OutputBufferPicture.show()
        print("PrintedPicture")
        NewPictureReady = False


        #Run MainMenu for 3 cycles
        Runs += 1
        del MainMenu
        if (Runs >= 2):
            StateMachineStatus = "SettingsMenu"
            Runs = 0
            #Hmm
        
    
    else:
        break