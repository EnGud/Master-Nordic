from ctypes.wintypes import tagRECT
from Main_Test import OutputBuffer
import Scene_Descriptor
import AlphaBlending
import AlphaMasking
import OperationsCounter
from threading import Thread
from PIL import Image
import numpy as np

#Prøv å implementere enkel threading raskt. Kan dele X-array i to, og la en tråd ta hver halvdel. Anta to threads (for simpelhets skyld, samt mer realistisk for mikrokontrollere?)


TestEntity = OperationsCounter.OperationsCounter

#StateMachine = enum(Main, Settings, Subsettings)

#Build Scenes setup

#Setup. Testing purposes.
print("Custom resolution? Yes/No")
if(input()=="Yes"):
    print("Please input X resolution")
    ScreenResolutionX = input()
    print("Please input Y resolution")
    ScreenResolutionY = input()
else:
    print("Okay, No custom resolution :( Setting to standard resolution 800x600")
    ScreenResolutionX = 800
    ScreenResolutionY = 600

#layers, elements, ResolutionX, ResolutionY

#Construct Main Menu
def MainMenuBuild():
    #Sjekk om instans eksisterer ift. loops, for å slippe unødvendig rekonstruksjon.
    if ((MainMenu.Exists) != 1):
        #Setup Scene. Input #layers, #PictureElements, #ScreenX, #ScreenY
        MainMenu = Scene_Descriptor.SceneDescriptor(4, 1, ScreenResolutionX, ScreenResolutionY)
        #Insert pictures. Fugly.
        MainMenu.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        MainMenu.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")

        MainMenu.Layer[1].Picture.Picture[0].PictureSize = [200, 100]
        MainMenu.Layer[1].Picture.Picture[0].picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp")
        MainMenu.Layer[1].Picture.Picture[0].PictureOffset = [(800-200), 0]

        MainMenu.Layer[2].Picture.Picture[0].PictureSize = [100, 100]
        MainMenu.Layer[2].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp")
        MainMenu.Layer[2].Picture.Picture[0].PictureOffset = [(800-100), 300]

        MainMenu.Layer[3].Picture.Picture[0].PictureSize = [400, 200]
        MainMenu.Layer[3].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_400_200.bmp")
        MainMenu.Layer[3].Picture.Picture[0].PictureOffset = [0, 200]

        MainMenu.SceneOperations.Alpha.Apply = True
        MainMenu.SceneOperations.Alpha.Target[2,0] = 1


        #Defines
    #Draw full frame before break (and loop)

    
#Construct Settings Menu
def SettingsMenuBuild():
    return 0

#Construct Subsettings Menu
def SubSettingsMenuBuild():
    return 0

#Order some coffee
def OrderCoffeeBuild():
    return 0

#InitValues
StateMachineStatus = "Main"

#Telle antal syklyser ting tar. Gir et timing-innsyn
RunCycles = 0
Runs = 0

#Linjebufferet
LineBuffer = np.zeros((0, 800), dtype=np.uint8)

#"Simulert skjerm-buffer"
OutputBuffer = np.zeros((600, 800), dtype=np.uint8)



#MainLoop
while(1):

    

    if (StateMachineStatus == "Main"):
        #Construct MainMenu Descriptor
        MainMenuBuild()


        




        If alpha = True
        Check which alpha picture 
        apply with target 

        #Frigjør plass/ressurser. Spør om trengs
        #if (StateMachineStatus != "Main"):
        #   del MainMenu

    Runs += 1

    if (Runs >= 5):
        StateMachineStatus == "Settings"
        del MainMenuBuild.MainMenu
        Runs = 0

    


    #TestSetup for circular demo scene test




    #UserInput-driven implementation. For visualisation/testing purposes, not for analytical purposes:
    #SelectState = input()
    #if (SelectState== Main || Settings || Subsettings || OrderCoffee)
    # StateMachine = SelectState
    # Else:
    #   print("Selection not viable. Please input a state.") 



    elif (StateMachineStatus == "Settings"):
        SettingsMenuBuild()

    elif(StateMachineStatus == "SubSettings"):
        SubSettingsMenuBuild()

    elif(StateMachineStatus == "OrderCoffee"):
        OrderCoffeeBuild()



print(TestEntity)
#Lag Histogram. Hent fra Analytics.py