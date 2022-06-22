import AlphaBlending
import AlphaMasking
import OperationsCounter
import Dynamic_RAM
import CLUT
from PIL import Image
import Analytics
import numpy as np
import MenusConstructor

import time

#If you want to input custom values. Testing grounds.
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

#Get screen sizes
ScreenResolutionX = MenusConstructor.ScreenResolutionX
ScreenResolutionY = MenusConstructor.ScreenResolutionY

#Setup
TestEntity = OperationsCounter.OperationsCounter(ScreenResolutionY, ScreenResolutionX)
StateMachineStatus = "Main"
OutputBuffer = np.zeros((ScreenResolutionX, 4), dtype=np.uint8)
OutputBufferLarge = np.zeros((ScreenResolutionY, ScreenResolutionX, 4), dtype=np.uint8)

#Create RAM
RAM=Dynamic_RAM.RAM(16, TestEntity)
TestWithTime = True



#Main render function, where the drawing magic happens.
def Render(Items, CurrentY, RAM, TestEntity):
    TestEntity.FreeLine = [True]*ScreenResolutionX
    #Create a linebuffer for shared use. Will always get position 0.
    LineBufferAdress = RAM.put(np.zeros((ScreenResolutionX, 4), dtype=np.uint8), TestEntity)

    CurrentItem = Items[len(Items)-1]
    #Start at top layer. Iterate downwards towards background.
    while CurrentItem.Next != None:
        TestEntity.CurrentLayer = CurrentItem.Layer

        
        RAM.StorePictureInRam(CurrentItem, CurrentY, RAM, TestEntity)

        LineBuffer = RAM.get(LineBufferAdress, TestEntity)
        #If current layer is within current y, proceed to do operations
        if ((CurrentY >= CurrentItem.PictureOffset[1]) and (CurrentY < CurrentItem.PictureOffset[1] + CurrentItem.PictureSize[1])):
                
            


            if(CurrentItem.ApplyCLUT):
                    CLUTBuff = CLUT.ApplyCLUT(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.CLUT, CurrentItem.PictureOffset[0], TestEntity)
                    
                    # fill buffer with used pixels
                    for x in range (ScreenResolutionX):
                        if TestEntity.FreeLine[x] == False:
                            LineBuffer[x] = CLUTBuff[x]



                

            if(CurrentItem.ApplyMask == True and CurrentItem.ApplyAlpha == False):


                    MaskBuff = AlphaMasking.ApplyMask(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.PictureOffset[0], Items[1].Picture[CurrentY], CurrentItem.Mask[CurrentY-CurrentItem.PictureOffset[1]], TestEntity)
                    
                    # fill buffer with used pixels
                    for x in range (ScreenResolutionX):
                        if TestEntity.FreeLine[x] == False:
                            LineBuffer[x] = MaskBuff[x]




            if(CurrentItem.ApplyAlpha):
                    
                    #workaround to use both alpha and mask
                if(CurrentItem.ApplyMask):
                    AlphaBuff = AlphaMasking.ApplyMask(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.PictureOffset[0], Items[1].Picture[CurrentY], CurrentItem.Mask[CurrentY-CurrentItem.PictureOffset[1]], TestEntity)

                    Temp = RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity)
                    
                    for x in range (len(Temp)):
                        if TestEntity.FreeLine[x+CurrentItem.PictureOffset[0]] == False:
                            Temp[x] = AlphaBuff[x + CurrentItem.PictureOffset[0]]
                    RAM.put_specific(CurrentItem.Picture_RAM_Adress, Temp, TestEntity)
                
                #real alpha part
                else:
                    AlphaBuff = AlphaBlending.ApplyAlpha(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.PictureOffset[0], "Over", Items[1].Picture[CurrentY], TestEntity)

                    for x in range (ScreenResolutionX):
                        if TestEntity.FreeLine[x] == False:
                            LineBuffer[x] = AlphaBuff[x]



        
               
        #Store in ram
        RAM.put_specific(LineBufferAdress, LineBuffer, TestEntity)
        
        #Move to next layer
        CurrentItem = CurrentItem.Next

    
    #Draw background when at end of array
    CurrentItem = Items[1]
    TestEntity.CurrentLayer = CurrentItem.Layer


    RAM.StorePictureInRam(CurrentItem, CurrentY, RAM, TestEntity)
    #Possibly apply CLUT if requested
    if(CurrentItem.ApplyCLUT):

        Buff = CLUT.ApplyCLUT(RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity), CurrentItem.CLUT, CurrentItem.PictureOffset[0], TestEntity)
        Temp = RAM.get(CurrentItem.Picture_RAM_Adress, TestEntity) 
        for x in range (ScreenResolutionX):
            #Knotete INC.
            Temp[x] = Buff[x]
        RAM.put_specific(CurrentItem.Picture_RAM_Adress, Temp, TestEntity)

    

        
    #Fill rest of unmodified pixels with background
    for x in range(ScreenResolutionX):
        if(TestEntity.FreeLine[x] == True): 
            LineBuffer[x] = Items[1].Picture[CurrentY][x]

    

                

        
    return RAM.get(LineBufferAdress, TestEntity), TestEntity







Runs = 0 
while(1):

    
    #Construct the main scene if statemachine requests it
    if (StateMachineStatus == "Main"):
        
        #Clean testing
        Analytics.Clean(TestEntity)

        #Construct the MainMenu Scene Descriptor list
        MainMenu = MenusConstructor.MainMenuBuild(TestEntity)

        #Start timing
        TestWithTime = True
        #Total time
        MuskTime = time.time()
        for CurrentY in range(ScreenResolutionY):
            TestEntity.CurrentY = [CurrentY]

            #MainLoop for render
            #Line-time
            StartTime = time.time()
            #Start render
            OutputBuffer, TestEntity = Render(MainMenu, CurrentY, RAM, TestEntity)
            EndTime = time.time()

            RAM.CheckEveryArrayBit(TestEntity)
            #Cleanup
            RAM.clear("All", TestEntity)
            #End MainLoop
            #Save time
            TestEntity.TimeTaken[CurrentY] = EndTime - StartTime
            #OutputBufferLarge is only used to visualize the whole picture at the end. NOT FOR THE ACTUAL MEASUREMENTS OF LINE TIMINGS!
            OutputBufferLarge[CurrentY] = OutputBuffer
            

            #More analytics
            Analytics.Testing(TestEntity, CurrentY)
            Analytics.Clean(TestEntity)
            
        MoskTime = time.time()
        FullTime = MoskTime - MuskTime
        print(FullTime)



        #Print TestEntity into Histograms
        Analytics.histogram(TestEntity.TimeTaken)
        Analytics.Analyze(TestEntity)

        #draw OutputBufferLarge to screen, and save it locally
        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene.bmp")
        #OutputBufferPicture.show()
        print("PrintedPicture")

        #Run MainMenu for x cycles
        Runs += 1
        del MainMenu
        if (Runs >= 1):
            StateMachineStatus = "SettingsMenu"
            Runs = 0
            #Hmm


        #Acts the same way as MainMenu when ran. No comments neccesary.
    if (StateMachineStatus == "SettingsMenu"):
        Analytics.Clean(TestEntity)
        
        SettingsMenu = MenusConstructor.SettingsMenuBuild(TestEntity)
        
        TestWithTime = True
        for CurrentY in range(ScreenResolutionY):
            TestEntity.CurrentY = [CurrentY]


            StartTime = time.time()
            OutputBuffer, TestEntity = Render(SettingsMenu, CurrentY, RAM, TestEntity)
            EndTime = time.time()
            RAM.CheckEveryArrayBit(TestEntity)
            RAM.clear("All", TestEntity)


            Analytics.Testing(TestEntity, CurrentY)
            Analytics.Clean(TestEntity)


            OutputBufferLarge[CurrentY] = OutputBuffer



        Analytics.histogram(TestEntity.TimeTaken)
        Analytics.Analyze(TestEntity)

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_DemoScene_SettingsMenu.bmp")

        Runs += 1
        del SettingsMenu
        if (Runs >= 1):
            StateMachineStatus = "SubSettingsMenu"
            Runs = 0
            #Hmm
        
        #No comments needed
    if (StateMachineStatus == "SubSettingsMenu"):
        Analytics.Clean(TestEntity)


        SubSettingsMenu = MenusConstructor.SubSettingsMenuBuild(TestEntity)

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

            OutputBufferLarge[CurrentY] = OutputBuffer
            

        Analytics.histogram(TestEntity.TimeTaken)
        Analytics.Analyze(TestEntity)


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


