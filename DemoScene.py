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
if(input()==("Yes" or "yes")):
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
    #if ((MainMenu.Exists) != 1):
    
        #Setup Scene. Input #layers, #PictureElements, #ScreenX, #ScreenY
        MainMenu = Scene_Descriptor.SceneDescriptor(2, 3, ScreenResolutionX, ScreenResolutionY)
        MainMenu.Exists = 1
        #Insert pictures. Fugly.
        MainMenu.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        MainMenu.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")

        #Istedenfor å manuelt legge inn størelse, kan np.size(element) brukes direkte i class?
        MainMenu.Layer[1].Picture.Picture[0].PictureSize = [200, 100]
        MainMenu.Layer[1].Picture.Picture[0].picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp")
        MainMenu.Layer[1].Picture.Picture[0].PictureOffset = [(800-200), 0]

        MainMenu.Layer[1].Picture.Picture[1].PictureSize = [100, 100]
        MainMenu.Layer[1].Picture.Picture[1].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp")
        MainMenu.Layer[1].Picture.Picture[1].PictureOffset = [(800-100), 300]

        MainMenu.Layer[1].Picture.Picture[2].PictureSize = [400, 200]
        MainMenu.Layer[1].Picture.Picture[2].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_400_200.bmp")
        MainMenu.Layer[1].Picture.Picture[2].PictureOffset = [0, 200]

        MainMenu.SceneOperations.Alpha.Apply = True
        MainMenu.SceneOperations.Alpha.Target[1,2] = True




    
#Construct Settings Menu
def SettingsMenuBuild():
    if ((SettingsMenu.Exists) != 1):
        #Setup Scene. Input #layers, #PictureElements, #ScreenX, #ScreenY
        SettingsMenu = Scene_Descriptor.SceneDescriptor(3, 2, ScreenResolutionX, ScreenResolutionY)
        SettingsMenu.Exists = 1
        #Insert pictures. Fugly.
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
    if ((SubSettingsMenu.Exists) != 1):
        SubSettingsMenu = Scene_Descriptor.SceneDescriptor(3, 2, ScreenResolutionX, ScreenResolutionY)
        SubSettingsMenu.Exists = 1

        SubSettingsMenu.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        SubSettingsMenu.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp")



#Order some coffee
def OrderCoffeeBuild():
    if ((OrderCoffee.Exists) != 1):

        OrderCoffee = Scene_Descriptor.SceneDescriptor(2, 1, ScreenResolutionX, ScreenResolutionY)
        OrderCoffee.Exists = 1

        OrderCoffee.Layer[0].Picture.Picture[0].PictureSize = [800, 600]
        OrderCoffee.Layer[0].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")

        OrderCoffee.Layer[1].Picture.Picture[0].PictureSize = [400, 300]
        OrderCoffee.Layer[1].Picture.Picture[0].Picture = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_Traktes_400_300.bmp")
        OrderCoffee.Layer[1].Picture.Picture[0].PictureOffset = [0, 600]

        OrderCoffee.SceneOperations.Mask = Image.Open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Masking Example.bmp")
        OrderCoffee.SceneOperations.MaskApply = True
        OrderCoffee.SceneOperations.Target[1][0] = True


#def Run(Menu)
#General Purpose run for any given structure, by any given operations
#Ikke pri akkurat nå.


def Render(Structure):

    for i in range (Structure.NumLayers, 0, -1):
        for j in range(Structure.NumElements, 0, -1):

            #Check if data/picture present. Else, skip.
            if (Structure.Layer[i].Picture.Picture[j].Picture):
                if (Structure.SceneOperations.Alpha.Apply):
                    

                if(Structure.SceneOperation.Mask.Apply):
                    return 0

                #Rendre lag




    
    #Eksempel:
    #Får inn MainMenu
    #finn høyeste lag
    #Hent start/slutt-posisjon høyeste lag
    #gjør eventuelle operasjoner som mask/alpha
    #Lagre høyeste lag i buffer
    #Gå ned til neste lag
    #Dersom underlag innenfor lag over, ikke lagre/utfør operasjon


    


    #Scan over hele linja, rendre øverste lag. Lagre grensene. Deretter hopp ned ett lag, og rendre gjenstående. fortsett til nederste lag er rendra.


def RunAlpha(structure):
    #Apply alpha på øverste lag, og nedover. Må hente ut AlphaTargets.
    return 0
    






def RunMask(structure):
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



#Scan over hele linja, rendre bunn til topp

#MainLoop
while(1):

    


    if (StateMachineStatus == "Main"):
        #Construct MainMenu Descriptor
        if (not(MainMenu)):
            MainMenu = MainMenuBuild()
        



        




        #If alpha = True
        #Check which alpha picture 
        #apply with target 

        #Frigjør plass/ressurser. Spør om trengs
        #if (StateMachineStatus != "Main"):
        #   del MainMenu

        Runs += 1

        if (Runs >= 5):
            #Kunne brukt enum
            StateMachineStatus == "Settings"
            del MainMenu
            Runs = 0



    elif (StateMachineStatus == "Settings"):
        if (not(Settings)):
            Settings = SettingsMenuBuild()


    elif (StateMachineStatus == "SubSettings"):
        if (not(SubSettings)):
            SubSettings = SubSettingsMenuBuild()
    

    elif (StateMachineStatus == "OrderCoffee"):
        if (not(OrderCoffee)):
            OrderCoffee = OrderCoffeeBuild()
    


    #TestSetup for circular demo scene test




    #UserInput-driven implementation. For visualisation/testing purposes, not for analytical purposes:
    #SelectState = input()
    #if (SelectState== Main || Settings || Subsettings || OrderCoffee)
    # StateMachine = SelectState
    # Else:
    #   print("Selection not viable. Please input a state.") 




print(TestEntity)
#Lag Histogram. Hent fra Analytics.py?









#def GenericBuilder (Layers, PicturesPerLayer, XRes, YRex)
#   GenericClass = Scene_Descriptor.SceneDescriptor(Layers, PicturesPerLayer, ScreenResolutionX, ScreenResolutionY)
#
#
#
#
#
#
#
#



Image.frombuffer