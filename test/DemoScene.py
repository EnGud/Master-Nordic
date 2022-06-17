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
FreeLine = [True]*ScreenResolutionX
TempLine = [0]*ScreenResolutionX
OutputBuffer = np.zeros((ScreenResolutionX, 4), dtype=np.uint8)
OutputBufferLarge = np.zeros((ScreenResolutionY, ScreenResolutionX, 4), dtype=np.uint8)


RAM=Dynamic_RAM.RAM


#Build the scenes. Manual.
def ResetFreeLine():
    FreeLine = [True]*ScreenResolutionX


def MainMenuBuild():
    #Todo: Error if picture is larger than screen for every layer/picture.

    MainMenuBG = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY, False, False)
    MainMenuBG.Exists = 1    

    #set background to screen resolution
    #Check if Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp") is the same size as the screen resolution
    MainMenuBG.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp"))
    MainMenuBG.PictureInfo.PictureSize = [len(MainMenuBG.Picture), len(MainMenuBG.Picture[0])]
    if ((MainMenuBG.PictureInfo.PictureSize[0] <= ScreenResolutionY) and (MainMenuBG.PictureInfo.PictureSize[1]) <= ScreenResolutionX):
        pass
    else:
        print("Error! Picture is not the same size as the screen resolution. The background needs to fit the screen.")
        exit()
    
    MainMenu1 = Scene_Descriptor.SceneDescriptor(1, ScreenResolutionX, ScreenResolutionY, False, False)
    MainMenu1.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp"))
    MainMenu1.PictureInfo.PictureSize = [200, 100]
    MainMenu1.PictureInfo.PictureOffset = [(800-200), 0]
    
    MainMenu2 = Scene_Descriptor.SceneDescriptor(2, ScreenResolutionX, ScreenResolutionY, False, False)
    MainMenu2.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp"))
    MainMenu2.PictureInfo.PictureSize = [100, 100]
    MainMenu2.PictureInfo.PictureOffset = [(800-100), 300]
    
    
    MainMenu3 = Scene_Descriptor.SceneDescriptor(3, ScreenResolutionX, ScreenResolutionY, False, False)
    MainMenu3.PictureInfo.PictureSize = [300, 100]
    MainMenu3.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp"))
    MainMenu3.PictureInfo.PictureOffset = [0, 200]

    MainMenu3.PictureInfo.LocalCLUT = False
    MainMenu3.PictureInfo.ApplyAlpha = False
    MainMenu3.PictureInfo.ApplyMask = False
    MainMenu3.PictureInfo.ApplyTargetAlpha = False
    MainMenu3.PictureInfo.ApplyTargetMask = False

    MainMenu = Scene_Descriptor.SceneItems
    MainMenu.Array = [MainMenuBG, MainMenu1, MainMenu2, MainMenu3]

    #Create a linked list
    MainMenu3.Next = MainMenu2
    MainMenu2.Next = MainMenu1
    MainMenu1.Next = MainMenuBG

    return MainMenu

    #while structure.Next != None:
    #Render the operations
    #Go to next item in linked list







#Construct Settings Menu
def SettingsMenuBuild():
    #if ((SettingsMenu.Exists) != 1):
        #Setup Scene. Input #layers, #PictureElements, #ScreenX, #ScreenY
        SettingsMenu = Scene_Descriptor.SceneDescriptor(3, 2, ScreenResolutionX, ScreenResolutionY, False, False)
        SettingsMenu.Exists = 1
        #Insert pictures and data. Fugly.
        SettingsMenu.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        SettingsMenu.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")


        SettingsMenu.Layer[1].Picture.Picture[0].PictureSize = [200, 100]
        SettingsMenu.Layer[1].Picture.Picture[0].picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Temperatur_200_100.bmp")
        SettingsMenu.Layer[1].Picture.Picture[0].PictureOffset = [(800-200), 200]

        SettingsMenu.Layer[1].Picture.Picture[1].PictureSize = [200, 100]
        SettingsMenu.Layer[1].Picture.Picture[1].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Hjelp_200_100.bmp")
        SettingsMenu.Layer[1].Picture.Picture[1].PictureOffset = [(800-100), 500]

        SettingsMenu.Layer[2].Picture.Picture[0].PictureSize = [400, 200]
        SettingsMenu.Layer[2].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Tilbake_200_100.bmp")
        SettingsMenu.Layer[2].Picture.Picture[0].PictureOffset = [0, 600]
        



        


#Construct Subsettings Menu
def SubSettingsMenuBuild():
    #if ((SubSettingsMenu.Exists) != 1):
        SubSettingsMenu = Scene_Descriptor.SceneDescriptor(3, 2, ScreenResolutionX, ScreenResolutionY, False, False)
        SubSettingsMenu.Exists = 1

        SubSettingsMenu.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        SubSettingsMenu.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp")



#Order some coffee
def OrderCoffeeBuild():
   # if ((OrderCoffee.Exists) != 1):

        OrderCoffee = Scene_Descriptor.SceneDescriptor(2, 1, ScreenResolutionX, ScreenResolutionY, False, False)
        OrderCoffee.Exists = 1

        OrderCoffee.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        OrderCoffee.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")

        OrderCoffee.Layer[1].Picture.Picture[0].PictureSize = [400, 300]
        OrderCoffee.Layer[1].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_Traktes_400_300.bmp")
        OrderCoffee.Layer[1].Picture.Picture[0].PictureOffset = [0, 600]

        OrderCoffee.SceneOperations.Mask = Image.Open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Masking Example.bmp")
        OrderCoffee.SceneOperations.MaskApply = True
        OrderCoffee.SceneOperations.Target[1][0] = True





def Render(Items, CurrentY, FreeLine):
    #MainMenu
    #.Items
    DrawnCurrentLine = False
    PictureOut = np.zeros((800, 4), dtype=np.uint8)



    # MainMenu.Array = [MainMenuBG, MainMenu1, MainMenu2, MainMenu3]#
    #Traverse the linked list of SceneDescription
    for i in range (len(Items.Array)-1, 0, -1):
        #Current Object
        Structure = Items.Array[i]


        #Sjekk om bildet ligger innenfor CurrentY, og skal rendres. Hvis ikke, skipp linjen. Hopper til neste item på samme X-linje.

        #check if CurrentY is larger or equal than the picture offset, but smaller than the picture size plus the offset (Check if CurrentY is within the picture)
        
        if ((CurrentY >= Structure.PictureInfo.PictureOffset[1]) and (CurrentY <= Structure.PictureInfo.PictureOffset[1] + Structure.PictureInfo.PictureSize[1])): 
        #if Jepp
            Picture = np.zeros((Structure.PictureInfo.PictureSize[0], 4), dtype=np.uint8)
            PictureModified = False




            if(Structure.PictureInfo.LocalCLUT):
                        #Generate CLUTPicture as empty image with size of picture
                        #ApplyCLUT(Picture, CLUT, CurrentY, OperationsCounter):
                Structure.Picture[CurrentY] = CLUT.ApplyCLUT(Structure.Picture, Structure.PictureInfo.CLUT, CurrentY, FreeLine, TestEntity)
                PictureModified = True
                


            if(Structure.PictureInfo.ApplyAlpha):
                        #Generate AlphaedPicture as empty image with size of picture
                        #ApplyAlpha(Foreground, Operator, Background, currentY, TestEntity): 
                        #Standard blender med bakgrunn. Om overlappende med annen, bruk ApplyTargetAlpha
                Structure.Picture[CurrentY] = AlphaBlending.AlphaAlpha(Structure.Picture, 'over', Items.Array[0].Picture, CurrentY, FreeLine, TestEntity)
                PictureModified = True

            if(Structure.PictureInfo.ApplyTargetAlpha):
                    #Generate AlphaedPicture as empty image with size of picture
                    #ApplyAlpha(Foreground, Operator, Background, currentY, TestEntity): 
                    #Bruk bare om to bilder overlapper.
                Structure.Picture[CurrentY] = AlphaBlending.AlphaAlpha(Structure.Picture, 'over', Items.Array[Structure.PictureInfo.ApplyAlphaTarget].Picture, CurrentY, FreeLine, TestEntity)
                PictureModified = True


            if(Structure.PictureInfo.ApplyMask):
                        #Generate MaskedPicture as empty image with size of picture
                        #ApplyMask(PictureFG, PictureBG, Mask, CurrentY, OperationsCounter):
                Structure.Picture[CurrentY] = AlphaMasking.ApplyMask(Structure.Picture, Items.Array[0].Picture, Structure.PictureInfo.Mask , CurrentY, TestEntity)
                PictureModified = True

            if(Structure.PictureInfo.ApplyTargetMask):
                Structure.Picture[CurrentY] = AlphaMasking.ApplyMask(Structure.Picture, Items.Array[Structure.PictureInfo.ApplyMaskTarget].Picture, Structure.PictureInfo.Mask , CurrentY, TestEntity)
                PictureModified = True

                
            #Use Freeline to "and" the current picture with FreeLine

            #Merk av gjeldende piksler som er brukt.
            for x in range (Structure.PictureInfo.PictureSize[0]):
                FreeLine[x] = FreeLine[x] and Structure.Picture[CurrentY][x]
                PictureOut[x + Structure.PictureInfo.PictureOffset[0]] = Structure.Picture[CurrentY][x]
        
    

           

            
            


    return PictureOut, FreeLine
    





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
        
        MainMenu = MainMenuBuild()
        #Render MainMeny for the length of ScreenResolutionY
        for i in range(ScreenResolutionY):
            OutputBuffer, FreeLine = Render(MainMenu, i, FreeLine)

            #Lagre større buffer, kun for visualisering/verifisering.

            #broadcast an array from a set size into a bigger array




            OutputBufferLarge[i] = OutputBuffer

            if (i == ScreenResolutionY-1):
                NewPictureReady = True

        
        #draw OutputBufferLarge to screen

        OutputBufferPicture = Image.fromarray(OutputBufferLarge)
        OutputBufferPicture.show()
        NewPictureReady = False
        ResetFreeLine()


        #Run MainMenu for 3 cycles
        Runs = Runs + 1
        if (Runs == 3):
            StateMachineStatus = "SettingsMenu"
            Runs = 0
            #Hmm
            del MainMenu

        



    elif (StateMachineStatus == "SettingsMenu"):
        #Run SettingsMenu for 2 cycles
        Render(SettingsMenuBuild)
        Runs = Runs + 1

        OutputBufferLarge[i] = OutputBuffer
        ResetFreeLine()
        if (Runs == 2):
            StateMachineStatus = "SubSettingsMenu"
            Runs = 0




    elif (StateMachineStatus == "SubSettingsMenu"):
        #Run SubSettingsMenu for 2 cycles
        Render(SubSettingsMenuBuild)
        Runs = Runs + 1

        OutputBufferLarge[i] = OutputBuffer
        ResetFreeLine()
        if (Runs == 2):
            StateMachineStatus = "OrderCoffee"
            Runs = 0




    elif (StateMachineStatus == "OrderCoffee"):
        #Run OrderCoffee for 3 cycles
        Render(OrderCoffeeBuild)
        Runs = Runs + 1

        OutputBufferLarge[i] = OutputBuffer
        ResetFreeLine()
        if (Runs == 3):
            StateMachineStatus = "PrintResult"
            Runs = 0

    elif (StateMachineStatus == "PrintResult"):
        #Print every attribute of TestEntity


        StateMachineStatus = "Done"

    elif (StateMachineStatus == "Done"):
        #Print "Done"
        print("Done")
        break

    else:
        print("Error: StateMachineStatus not recognized.")
        break



print(TestEntity)
#Lag Histogram. Hent fra Analytics.py?
Result = Analytics.Histogram(TestEntity)
Analytics.PlotHistogram(Result)




#Experimental af

""" #Measure the CPU bandwidth usage of the system
def BandwidthMeasure():
    #This function will measure the CPU bandwidth usage of the system
    #It will return the CPU bandwidth usage in bytes/second
    #It will attempt to use threading.

    #Get the current time
    CurrentTime = time.time()
    #Get the current CPU usage
    CurrentUsage = psutil.cpu_percent()
    #Get the current CPU bandwidth usage
    CurrentBandwidth = psutil.net_io_counters().bytes_sent
    #Calculate the CPU bandwidth usage
    BandwidthUsage = (CurrentBandwidth - PreviousBandwidth) / (CurrentTime - PreviousTime)
    #Set the previous time and previous bandwidth to the current time and current bandwidth
    PreviousTime = CurrentTime
    PreviousBandwidth = CurrentBandwidth
    #Return the CPU bandwidth usage
    return BandwidthUsage

 """