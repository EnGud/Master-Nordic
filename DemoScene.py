import Scene_Descriptor
import AlphaBlending
import AlphaMasking
import OperationsCounter
import Dynamic_RAM
from PIL import Image
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
TestEntity = OperationsCounter.OperationsCounter()
StateMachineStatus = "Main"
FreeLine = [True]*ScreenResolutionX


def MainMenuBuild():
    #Todo: Error if picture is larger than screen for every layer/picture.

    MainMenu = Scene_Descriptor.SceneDescriptor(2, 3, ScreenResolutionX, ScreenResolutionY, False, False)
    MainMenu.Exists = 1    

    #set background to screen resolution
    MainMenu.Layer[0].Picture.Picture[0].PictureSize = [ScreenResolutionX, ScreenResolutionY]
    #Check if Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp") is the same size as the screen resolution
    if(len(MainMenu.Layer[0].Picture.Picture[0].Picture) == ScreenResolutionX and len(MainMenu.Layer[0].Picture.Picture[0].Picture[0]) == ScreenResolutionY):
        MainMenu.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")
    else:
        print("Error! Picture is not the same size as the screen resolution. The background needs to fit the screen.")
    
    MainMenu.Layer[1].Picture.Picture[0].picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp")
    MainMenu.Layer[1].Picture.Picture[0].PictureSize = [200, 100]
    MainMenu.Layer[1].Picture.Picture[0].PictureOffset = [(800-200), 0]
        
    MainMenu.Layer[1].Picture.Picture[1].PictureSize = [100, 100]
    MainMenu.Layer[1].Picture.Picture[1].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp")
    MainMenu.Layer[1].Picture.Picture[1].PictureOffset = [(800-100), 300]
    
    MainMenu.Layer[1].Picture.Picture[2].PictureSize = [400, 200]
    MainMenu.Layer[1].Picture.Picture[2].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_400_200.bmp")
    MainMenu.Layer[1].Picture.Picture[2].PictureOffset = [0, 200]





















def Render(Structure, CurrentY):
    #This function will draw one Y-axis of the scene
    #it will start with the highest i and lowest j in MainMenu.Layer[i].Picture.Picture[j].Picture. j will increment until the end of the layer, then i will increment and j will reset to 0
    #it will then draw the next layer and repeat
    #The picture is stored in MainMenu.Layer[i].Picture.Picture[j].Picture. It has the format of [ResolutionY, ResolutionX, [R, G, B, A]]
    #it will create an array that checks if the current X position is occupied.
    #It will iterate over the X-axis bitwise.
    #If the current X position is occupied, it will not draw the current picture.
    #If the current X position is not occupied, it will draw the current picture.
    #It will then move to the next X-position.
    #It will repeat until it reaches the end of the X-axis.
    #It will then return the array of drawn X-positions.
    #It will attempt to use threading.

    for i in range (Structure.NumLayers, 0, -1):
        for j in range(0, Structure.NumElements, 1):
            #Checks if picture/data is present
            if(Structure.Layer[i].Picture.Picture[j].Picture):

                #Check if Alpha should be applied between picture and picture below
                if(Structure.Layer[i].PictureInfo.ApplyAlpha):
                    AlphaBlending.AlphaOperations.AlphaAlpha(Structure.Layer[i].Picture.Picture[j].Picture, 'over', Structure.Layer[i-1].Picture.Picture[0].Picture, Structure.Layer[i].Picture.Picture[j].Picture[0][0][3], TestEntity)
                    
                
                
                   






    



"""     for y in range (Structure.ScreenSizeY):
    
    FreeLine = [0]*Structure.ScreenSizeX

    for i in range (Structure.NumLayers, 0, -1):
        for j in range(0, Structure.NumElements, 1):

            ##Check if data/picture present. Else, skip.
            if(Structure.Layer[i].Picture.Picture[j].Picture != None):
                #Check if picture present on current Y line. Else, skip to next picture/layer
                if(y >= Structure.Layer[i].Picture.Picture[j].PictureOffset[1] and y < Structure.Layer[i].Picture.Picture[j].PictureOffset[1]+Structure.Layer[i].Picture.Picture[j].PictureSize[1]):

        
    
    
    
    
    return 0 """



while(1):
    #Use a state machine to control the flow of the program. Start with MainMenu, let it iterate for 3 cycles, then go to SettingsMenu. Let it run for two cycles then go to SubSettingsMenu. Let it run for two cycles then go to OrderCoffee. Let it run for three cycles then go to MainMenu. Try to implement threading on Render()
    if (StateMachineStatus == "Main"):
        #Render MainMeny for the length of ScreenResolutionY
        for i in range(0, ScreenResolutionY, 1):
            Render(MainMenuBuild, i)




        #Run MainMenu for 3 cycles
        Runs = Runs + 1
        if (Runs == 3):
            StateMachineStatus = "SettingsMenu"
            Runs = 0

    elif (StateMachineStatus == "SettingsMenu"):
        #Run SettingsMenu for 2 cycles
        Render(SettingsMenuBuild)
        Runs = Runs + 1
        if (Runs == 2):
            StateMachineStatus = "SubSettingsMenu"
            Runs = 0

    elif (StateMachineStatus == "SubSettingsMenu"):
        #Run SubSettingsMenu for 2 cycles
        Render(SubSettingsMenuBuild)
        Runs = Runs + 1
        if (Runs == 2):
            StateMachineStatus = "OrderCoffee"
            Runs = 0

    elif (StateMachineStatus == "OrderCoffee"):
        #Run OrderCoffee for 3 cycles
        Render(OrderCoffeeBuild)
        Runs = Runs + 1
        if (Runs == 3):
            StateMachineStatus = "Done"
            Runs = 0

    else:
        print("Error: StateMachineStatus not recognized.")
        break



print(TestEntity)
#Lag Histogram. Hent fra Analytics.py?
Result = Analytics.Histogram(TestEntity)
Analytics.PlotHistogram(Result)
