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



print("Custom resolution? Yes/No")
if(input()==("Yes" or "yes")):
    print("Please input X resolution")
    ScreenResolutionX = input()
    print("Please input Y resolution")
    ScreenResolutionY = input()
else:
    print("Okay, No custom resolution :( Setting to standard resolution 800x600")
    ScreenResolutionX = 800
    ScreenResolutionY = 600

#Setup
TestEntity = OperationsCounter.OperationsCounter(ScreenResolutionY)
StateMachineStatus = "Main"
OutputBuffer = np.zeros((ScreenResolutionX, 4), dtype=np.uint8)
OutputBufferLarge = np.zeros((ScreenResolutionY, ScreenResolutionX, 4), dtype=np.uint8)

RAM=Dynamic_RAM.RAM(32, TestEntity)

#Use Scene_Descriptor to build the scene through a function

def MainMenuBuild():
    #Todo: Error if picture is larger than screen for every layer/picture.

    MainMenuBG = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)

    MainMenuBG.Exists = 1    
    #MainMenu1.Layer = 0
    

    #set background to screen resolution
    #Check if Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp") is the same size as the screen resolution
    MainMenuBG.Picture = AlphaBlending.PutAlpha(np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")), 120)
    MainMenuBG.PictureSize = [ScreenResolutionX, ScreenResolutionY]


    if ((MainMenuBG.PictureSize[1] <= ScreenResolutionY) and (MainMenuBG.PictureSize[0]) <= ScreenResolutionX):
        pass
    else:
        print("Error! Picture is not the same size as the screen resolution. The background needs to fit the screen.")
        exit()
    

    MainMenu1 = Scene_Descriptor.SceneDescriptor(1, 200, 100)
    MainMenu1.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp")
    MainMenu1.Picture = MainMenu1.Picture.convert('RGB')
    MainMenu1.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu1.Picture), 200)
    MainMenu1.PictureSize = [200, 100]
    MainMenu1.PictureOffset = [600, 0]
    MainMenu1.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)


    #MainMenu1.ApplyCLUT = True
    MainMenu1.ApplyMask = True
    MainMenu1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp"))
    


    MainMenu2 = Scene_Descriptor.SceneDescriptor(2, 100, 100)
    MainMenu2.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp")
    MainMenu2.Picture = MainMenu2.Picture.convert('RGB')
    MainMenu2.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu2.Picture), 255)
    MainMenu2.PictureSize = [100, 100]


    MainMenu2.ApplyMask = True
    MainMenu2.PictureOffset = [700, 300]
    MainMenu2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp"))

    

    
    MainMenu3 = Scene_Descriptor.SceneDescriptor(3, 300, 100)
    MainMenu3.PictureSize = [300, 100]

    #Paint.net er retarded.
    MainMenu3.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp")
    MainMenu3.Picture = MainMenu3.Picture.convert('RGB')
    MainMenu3.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu3.Picture), 120)

    MainMenu3.PictureOffset = [0, 200]
    MainMenu3.ApplyAlpha = True
    MainMenu3.Picture = AlphaBlending.PutAlpha(MainMenu3.Picture, 120)


    MainMenuEnd = Scene_Descriptor.Empty


    MainMenu = Scene_Descriptor.SceneItems
    MainMenu.Array = [MainMenuBG, MainMenu1, MainMenu2, MainMenu3]

    #Create a linked list
    MainMenu3.Next = MainMenu2
    MainMenu2.Next = MainMenu1
    MainMenu1.Next = MainMenuBG
    MainMenuBG.Next = MainMenuEnd
    MainMenuEnd.Next = None

    return MainMenu, MainMenuBG, MainMenu1, MainMenu2, MainMenu3

    #while structure.Next != None:
    #Render the operations
    #Go to next item in linked list


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

            if(Structure.ApplyMask):
            #            #Generate MaskedPicture as empty image with size of picture
            #ApplyMask(PictureFG, X_Offset, PictureBG, Mask, FreeLine, TestEntity):
            #Mask must match PictureFG.
                PictureOut, FreeLine = AlphaMasking.ApplyMask(Structure.Picture[(CurrentY-Structure.PictureOffset[1])], Structure.PictureOffset[0], Items[1].Picture[CurrentY], Structure.Mask[CurrentY-Structure.PictureOffset[1]], FreeLine, OperationsCounter)
            #    Structure.Picture[CurrentY] = AlphaMasking.ApplyMask(Structure.Picture, Items.Array[0].Picture, Structure.PictureInfo.Mask , CurrentY, TestEntity)


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

        

        


    #START PÅ ØVERSTE LAG
    #UTFØR OPERASJONER (GITT OFFSET)
    #PLASSER BILDET KORREKT PÅ SKJERM
    #MERK AV FREELINES STATUS
    #GÅ TILNÆRESTE LAG
    #UTFØR OPERASJONER, MEN KUN DER FREELINER ER SANN
    #FORTSETT TIL NEDERSTE LAG
    #DIMADA DEMADA
    #RETURNER LINJA




    #Eksempel med RAM
    
    #        if(Structure.LocalCLUT):
    #            RAM.get(Adress, TestEntity)
    #            Structure.Picture[CurrentY] = CLUT.ApplyCLUT(Structure.Picture, Structure.CLUT, CurrentY, FreeLine, TestEntity)
    #            PictureModified = True
    #            PictureAdress = RAM.put(Picture, TestEntity)


    #Ved exit:
    #RAM.clear(Adress, TestEntity)
                


    


#PutInRAM



Runs = 0 
while(1):

    #Use a state machine to control the flow of the program. Start with MainMenu, let it iterate for 3 cycles, then go to SettingsMenu. Let it run for two cycles then go to SubSettingsMenu. Let it run for two cycles then go to OrderCoffee. Let it run for three cycles then go to MainMenu. Try to implement threading on Render()
    if (StateMachineStatus == "Main"):
        #MainMenu Build bygges ikke realtime! Bytt ut med å lagre en kopi av MainMenu i RAM eller noe.
        MainMenu = MainMenuBuild()
        #Render MainMeny for the length of ScreenResolutionY
        for CurrentY in range(ScreenResolutionY):
            OutputBuffer = Render(MainMenu, CurrentY, RAM)
            OutputBufferLarge[CurrentY] = OutputBuffer
            print(CurrentY)
            #Lagre større buffer, kun for visualisering/verifisering.

            #broadcast an array from a set size into a bigger array




            

            if (CurrentY == ScreenResolutionY-1):
                NewPictureReady = True

        
        #draw OutputBufferLarge to screen

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene.bmp")
        #OutputBufferPicture.show()
        print("PrintedPicture")
        NewPictureReady = False


        #Run MainMenu for 3 cycles
        Runs += 1
        if (Runs >= 3):
            StateMachineStatus = "SettingsMenu"
            Runs = 0
            #Hmm
            del MainMenu
    
    else:
        break