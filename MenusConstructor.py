import Scene_Descriptor
import AlphaBlending
import AlphaMasking
import OperationsCounter
import numpy as np
from PIL import Image
import CLUT

#Setup




ScreenResolutionX = 800
ScreenResolutionY = 600

#Use Scene_Descriptor to build the scene through a function



def MainMenuBuild():
    #Todo: Error if picture is larger than screen for every layer/picture.

    MainMenuBG = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)

    MainMenuBG.Exists = 1    
    #MainMenu1.Layer = 0
    

    #set background to screen resolution
    #Check if Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp") is the same size as the screen resolution
    #MainMenuBG.Picture = AlphaBlending.PutAlpha(np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Grassfield.bmp")), 120)
    MainMenuBG.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Grassfield.bmp")
    MainMenuBG.Picture = np.asarray(MainMenuBG.Picture.convert('RGBA'))
    MainMenuBG.PictureSize = [ScreenResolutionX, ScreenResolutionY]


    if ((MainMenuBG.PictureSize[1] <= ScreenResolutionY) and (MainMenuBG.PictureSize[0]) <= ScreenResolutionX):
        pass
    else:
        print("Error! Picture is not the same size as the screen resolution. The background needs to fit the screen.")
        exit()
    

    MainMenu1 = Scene_Descriptor.SceneDescriptor(1, 200, 100)
    MainMenu1.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp")
    MainMenu1.Picture = MainMenu1.Picture.convert('RGBA')
    MainMenu1.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu1.Picture), 200)
    MainMenu1.PictureSize = [200, 100]
    MainMenu1.PictureOffset = [600, 0]
    MainMenu1.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)


    #MainMenu1.ApplyCLUT = True
    MainMenu1.ApplyMask = True
    MainMenu1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp"))
    


    MainMenu2 = Scene_Descriptor.SceneDescriptor(2, 100, 100)
    MainMenu2.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp")
    MainMenu2.Picture = MainMenu2.Picture.convert('RGBA')
    MainMenu2.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu2.Picture), 255)
    MainMenu2.PictureSize = [100, 100]


    MainMenu2.ApplyMask = True
    MainMenu2.PictureOffset = [700, 300]
    MainMenu2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp"))

    

    
    MainMenu3 = Scene_Descriptor.SceneDescriptor(3, 300, 100)
    MainMenu3.PictureSize = [300, 100]

    #Paint.net er retarded.
    MainMenu3.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp")
    MainMenu3.Picture = MainMenu3.Picture.convert('RGBA')
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






MainMenuBG = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)

#Construct Settings Menu
def SettingsMenuBuild():
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
    MainMenu2.PictureOffset = [700, 0]
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

    return MainMenu

    #while structure.Next != None:
    #Render the operations
    #Go to next item in linked list



        


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

def PushItToTheLimitJPG():
    return 0
