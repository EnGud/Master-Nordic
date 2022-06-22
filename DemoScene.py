
import Scene_Descriptor
import AlphaBlending
import AlphaMasking
import OperationsCounter
import Dynamic_RAM
import CLUT
from PIL import Image
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

ScreenResolutionX = MenusConstructor.ScreenResolutionX
ScreenResolutionY = MenusConstructor.ScreenResolutionY

#Setup
TestEntity = OperationsCounter.OperationsCounter(ScreenResolutionY, ScreenResolutionX)
StateMachineStatus = "Main"
OutputBuffer = np.zeros((ScreenResolutionX, 4), dtype=np.uint8)
OutputBufferLarge = np.zeros((ScreenResolutionY, ScreenResolutionX, 4), dtype=np.uint8)

RAM=Dynamic_RAM.RAM(16, TestEntity)
TestWithTime = True
#Use Scene_Descriptor to build the scene through a function


def Render(Items, CurrentY, RAM, TestEntity):
    TestEntity.FreeLine = [True]*ScreenResolutionX
    LineBufferAdress = RAM.put(np.zeros((ScreenResolutionX, 4), dtype=np.uint8), TestEntity)

    CurrentItem = Items[len(Items)-1]
    while CurrentItem.Next != None:
        TestEntity.CurrentLayer = CurrentItem.Layer
    #Start fra øverste lag, iterer nedover.
        
        RAM.StorePictureInRam(CurrentItem, CurrentY, RAM, TestEntity)
        #Sjekk om noen operasjoner skal utføres
        #om ja: Hent linjebuffer
        #utfør CLUT-operasjoner 
        #Merk av FreeLine for hvert pixel som nå er modifisert
        #utfør AlphaBlending-operasjone
        #Freeline
        #utfør AlphaMasking-operasjoner
        #Freeline

        #For hver freeline som ikke er berørt, tegn bakgrunnen
        #
        #Returner ut linja

        LineBuffer = RAM.get(LineBufferAdress, TestEntity)
        #Dersom nåværende lag er innenfor Y, gitt offset
        if ((CurrentY >= CurrentItem.PictureOffset[1]) and (CurrentY < CurrentItem.PictureOffset[1] + CurrentItem.PictureSize[1])):
                
            


            if(CurrentItem.ApplyCLUT):
                    #put_specific(self, adress, data, TestEntity):
                    #ApplyCLUT(Picture, CLUT, X_Offset, TestEntity):
                    #RAM.put_specific(LineBufferAdress, CLUT.ApplyCLUT(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.CLUT, CurrentItem.PictureOffset[0], TestEntity), TestEntity)

                    CLUTBuff = CLUT.ApplyCLUT(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.CLUT, CurrentItem.PictureOffset[0], TestEntity)
                    #Items[1].DrawOverBG = True
                    for x in range (ScreenResolutionX):
                        if TestEntity.FreeLine[x] == False:
                            LineBuffer[x] = CLUTBuff[x]



                

            if(CurrentItem.ApplyMask == True and CurrentItem.ApplyAlpha == False):
                    #ApplyMask(PictureFG, X_Offset, PictureBG, Mask, TestEntity):

                    MaskBuff = AlphaMasking.ApplyMask(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.PictureOffset[0], Items[1].Picture[CurrentY], CurrentItem.Mask[CurrentY-CurrentItem.PictureOffset[1]], TestEntity)
                    #Items[1].DrawOverBG = True
                    for x in range (ScreenResolutionX):
                        if TestEntity.FreeLine[x] == False:
                            LineBuffer[x] = MaskBuff[x]




            if(CurrentItem.ApplyAlpha):
                    #ApplyAlpha (Foreground, X_Offset, Operator, Background, TestEntity):
                if(CurrentItem.ApplyMask):
                    AlphaBuff = AlphaMasking.ApplyMask(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.PictureOffset[0], Items[1].Picture[CurrentY], CurrentItem.Mask[CurrentY-CurrentItem.PictureOffset[1]], TestEntity)
                    #Items[1].DrawOverBG = True
                    Temp = RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity)
                    
                    for x in range (len(Temp)):
                        if TestEntity.FreeLine[x+CurrentItem.PictureOffset[0]] == False:
                            Temp[x] = AlphaBuff[x + CurrentItem.PictureOffset[0]]
                    RAM.put_specific(CurrentItem.Picture_RAM_Adress, Temp, TestEntity)
                
                else:
                    AlphaBuff = AlphaBlending.ApplyAlpha(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.PictureOffset[0], "Over", Items[1].Picture[CurrentY], TestEntity)
                    #Items[1].DrawOverBG = True
                    for x in range (ScreenResolutionX):
                        if TestEntity.FreeLine[x] == False:
                            LineBuffer[x] = AlphaBuff[x]



        
               

        RAM.put_specific(LineBufferAdress, LineBuffer, TestEntity)

        CurrentItem = CurrentItem.Next

    
    #Draw background
    CurrentItem = Items[1]
    TestEntity.CurrentLayer = CurrentItem.Layer
    #Functions below could be moved to a separate file/whatever. Saves space and looks prettier. No time atm!

    RAM.StorePictureInRam(CurrentItem, CurrentY, RAM, TestEntity)

    if(CurrentItem.ApplyCLUT):

        Buff = CLUT.ApplyCLUT(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.CLUT, CurrentItem.PictureOffset[0], TestEntity)
        Temp = RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity) 
        for x in range (ScreenResolutionX):
            #Knotete INC.
            Temp[x] = Buff[x]
        RAM.put_specific(CurrentItem.Picture_RAM_Adress, Temp, TestEntity)

    

        

    for x in range(ScreenResolutionX):
        if(TestEntity.FreeLine[x] == True): 
            LineBuffer[x] = Items[1].Picture[CurrentY][x]

    

                

        
    return RAM.get(LineBufferAdress, TestEntity), TestEntity







Runs = 0 
while(1):

    #Use a state machine to control the flow of the program. Start with MainMenu, let it iterate for 3 cycles, then go to SettingsMenu. Let it run for two cycles then go to SubSettingsMenu. Let it run for two cycles then go to OrderCoffee. Let it run for three cycles then go to MainMenu. Try to implement threading on Render()
    if (StateMachineStatus == "Main"):
        Analytics.Clean(TestEntity)
        #MainMenu Build bygges ikke realtime! Bytt ut med å lagre en kopi av MainMenu i RAM eller noe.
        MainMenu = MenusConstructor.MainMenuBuild(TestEntity)
        #Render MainMeny for the length of ScreenResolutionY
        #Start timing
        TestWithTime = True
        MuskTime = time.time()
        for CurrentY in range(ScreenResolutionY):
            TestEntity.CurrentY = [CurrentY]

            #MainLoop for render
            StartTime = time.time()
            OutputBuffer, TestEntity = Render(MainMenu, CurrentY, RAM, TestEntity)
            EndTime = time.time()
            RAM.CheckEveryArrayBit(TestEntity)
            RAM.clear("All", TestEntity)
            #End MainLoop

            TestEntity.TimeTaken[CurrentY] = EndTime - StartTime
            #OutputBufferLarge is only used to visualize the picture. NOT FOR THE ACTUAL MEASUREMENTS OF LINE TIMINGS!
            OutputBufferLarge[CurrentY] = OutputBuffer
            

            #print(TestEntity.NoMask)
            Analytics.Testing(TestEntity, CurrentY)

            Analytics.Clean(TestEntity)
            #Lagre større buffer, kun for visualisering/verifisering.
        MoskTime = time.time()
        FullTime = MoskTime - MuskTime
        print(FullTime)


        #Stop timing
        
        #Calculate time taken

        
        
        #Print TestEntity into Histogram

        Analytics.histogram(TestEntity.TimeTaken)
        Analytics.Analyze(TestEntity)

        #draw OutputBufferLarge to screen

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene.bmp")
        #OutputBufferPicture.show()
        print("PrintedPicture")

        #Run MainMenu for 3 cycles
        Runs += 1
        del MainMenu
        if (Runs >= 1):
            StateMachineStatus = "SettingsMenu"
            Runs = 0
            #Hmm



    if (StateMachineStatus == "SettingsMenu"):
        Analytics.Clean(TestEntity)
        #MainMenu Build bygges ikke realtime! Bytt ut med å lagre en kopi av MainMenu i RAM eller noe.
        SettingsMenu = MenusConstructor.SettingsMenuBuild(TestEntity)
        #Render MainMeny for the length of ScreenResolutionY
        #Start timing
        TestWithTime = True
        for CurrentY in range(ScreenResolutionY):
            TestEntity.CurrentY = [CurrentY]

            #MainLoop for render
            StartTime = time.time()
            OutputBuffer, TestEntity = Render(SettingsMenu, CurrentY, RAM, TestEntity)
            EndTime = time.time()
            RAM.CheckEveryArrayBit(TestEntity)
            RAM.clear("All", TestEntity)
            #End MainLoop


            Analytics.Testing(TestEntity, CurrentY)

            Analytics.Clean(TestEntity)



            #OutputBufferLarge is only used to visualize the picture. NOT FOR THE ACTUAL MEASUREMENTS OF LINE TIMINGS!
            OutputBufferLarge[CurrentY] = OutputBuffer
            
            #Lagre større buffer, kun for visualisering/verifisering.

        #Stop timing
        
        #Calculate time taken
        
    #Print TestEntity into Histogram
    #Manuelle histogram. fuck it.

        Analytics.histogram(TestEntity.TimeTaken)
        Analytics.Analyze(TestEntity)


        #draw OutputBufferLarge to screen

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene_SettingsMenu.bmp")

        Runs += 1
        del SettingsMenu
        if (Runs >= 1):
            StateMachineStatus = "SubSettingsMenu"
            Runs = 0
            #Hmm
        

    if (StateMachineStatus == "SubSettingsMenu"):
        Analytics.Clean(TestEntity)

        #MainMenu Build bygges ikke realtime! Bytt ut med å lagre en kopi av MainMenu i RAM eller noe.
        SubSettingsMenu = MenusConstructor.SubSettingsMenuBuild(TestEntity)
        #Render MainMeny for the length of ScreenResolutionY
        #Start timing
        TestWithTime = True
        for CurrentY in range(ScreenResolutionY):
            TestEntity.CurrentY = [CurrentY]

            #MainLoop for render
            StartTime = time.time()
            OutputBuffer, TestEntity = Render(SubSettingsMenu, CurrentY, RAM, TestEntity)
            EndTime = time.time()
            RAM.CheckEveryArrayBit(TestEntity)
            RAM.clear("All", TestEntity)
            #End MainLoop

            TestEntity.TimeTaken[CurrentY] = EndTime - StartTime

            Analytics.Testing(TestEntity, CurrentY)

            Analytics.Clean(TestEntity)

            #OutputBufferLarge is only used to visualize the picture. NOT FOR THE ACTUAL MEASUREMENTS OF LINE TIMINGS!
            OutputBufferLarge[CurrentY] = OutputBuffer
            
            #Lagre større buffer, kun for visualisering/verifisering.

        #Stop timing
        
        #Calculate time taken
        
    #Print TestEntity into Histogram

        Analytics.histogram(TestEntity.TimeTaken)
        Analytics.Analyze(TestEntity)

        #draw OutputBufferLarge to screen

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene_SubSettingsMenu.bmp")

        Runs += 1
        del SubSettingsMenu
        if (Runs >= 1):
            StateMachineStatus = "Done"
            Runs = 0
            #Hmm
    
    else:
        break



#Find the Big O of an operation
""" def BigO(Operation, TimeTaken):
    #Find the average time taken for the operation
    AverageTime = sum(TimeTaken)/len(TimeTaken)
    #Find the Big O of the operation
    BigO = AverageTime/Operation
    return BigO """



