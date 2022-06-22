import Scene_Descriptor
import AlphaBlending
import numpy as np
from PIL import Image
import CLUT

#Setup
ScreenResolutionX = 800
ScreenResolutionY = 600


#Build Info for MainMenu
#Tips: always include mask for text. Match the mask with a blackout of the text.
def MainMenuBuild(TestEntity):
    #Use Scene_Descriptor to build the scene through a function
    MainMenuBG = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)

    MainMenuBG.Exists = 1    
    #MainMenu1.Layer = 0
    

    #set background to screen resolution
    #Save picture and CLUT in the class
    MainMenuBG.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/MainMenuBackground.bmp")
    MainMenuBG.Picture = np.asarray(MainMenuBG.Picture.convert('RGBA'))
    MainMenuBG.PictureSize = [ScreenResolutionX, ScreenResolutionY]
    MainMenuBG.ApplyCLUT = False
    MainMenuBG.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)
    #MainMenuBG.DrawOverBG = False
    
    #Background within defined screensize?
    if ((MainMenuBG.PictureSize[1] <= ScreenResolutionY) and (MainMenuBG.PictureSize[0]) <= ScreenResolutionX):
        pass
    else:
        print("Error! Picture is not the same size as the screen resolution. The background needs to fit the screen.")
        exit()
    
    #Construct layer 1
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
    

    #Construct layer 2
    MainMenu2 = Scene_Descriptor.SceneDescriptor(2, 100, 100)
    MainMenu2.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp")
    MainMenu2.Picture = MainMenu2.Picture.convert('RGBA')
    MainMenu2.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu2.Picture), 255)
    MainMenu2.PictureSize = [100, 100]


    MainMenu2.ApplyMask = True
    MainMenu2.PictureOffset = [700, 300]
    MainMenu2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp"))

    

    #Construct layer 3
    MainMenu3 = Scene_Descriptor.SceneDescriptor(3, 300, 100)
    MainMenu3.PictureSize = [300, 100]

    MainMenu3.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp")
    MainMenu3.Picture = MainMenu3.Picture.convert('RGBA')
    MainMenu3.Picture = AlphaBlending.PutAlpha(np.asarray(MainMenu3.Picture), 120)
    
    MainMenu3.PictureOffset = [0, 200]
    MainMenu3.ApplyAlpha = True
    MainMenu3.Picture = AlphaBlending.PutAlpha(MainMenu3.Picture, 120)

    #MainMenu3.ApplyCLUT = True
    #MainMenu3.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)
    #End-entity
    MainMenuEnd = Scene_Descriptor.Empty

    #Create scene array
    MainMenu = Scene_Descriptor.SceneItems
    MainMenu.Array = [MainMenuBG, MainMenu1, MainMenu2, MainMenu3]

    #Create a linked list
    MainMenu3.Next = MainMenu2
    MainMenu2.Next = MainMenu1
    MainMenu1.Next = MainMenuEnd
    #MainMenuBG.Next = MainMenuEnd
    MainMenuEnd.Next = None

    TestEntity.ScenesConstructed += 1
    return MainMenu, MainMenuBG, MainMenu1, MainMenu2, MainMenu3



#The following scene constructions should need no more explanation.



MainMenuBG = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)

#Construct Settings Menu
#Tips: always include mask for text. Match the mask with a blackout of the text.
def SettingsMenuBuild(TestEntity):
    SettingsMenuBuild = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)
    
    SettingsMenuBuild.Exists = 1

    #set background to screen resolution
    SettingsMenuBuild.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/SettingsBackground.bmp")
    SettingsMenuBuild.Picture = np.asarray(SettingsMenuBuild.Picture.convert('RGBA'))
    SettingsMenuBuild.PictureSize = [ScreenResolutionX, ScreenResolutionY]
    SettingsMenuBuild.ApplyCLUT = False
    SettingsMenuBuild.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)



    if ((SettingsMenuBuild.PictureSize[1] <= ScreenResolutionY) and (SettingsMenuBuild.PictureSize[0]) <= ScreenResolutionX):
        pass
    else:
        print("Error! Picture is not the same size as the screen resolution. The background needs to fit the screen.")
        exit()
    
    #Buffer Picture 1
    SettingsMenuBuild1 = Scene_Descriptor.SceneDescriptor(1, 400, 200)
    SettingsMenuBuild1.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Sub-Settings_400_200.bmp")
    SettingsMenuBuild1.Picture = SettingsMenuBuild1.Picture.convert('RGBA')
    SettingsMenuBuild1.Picture = AlphaBlending.PutAlpha(np.asarray(SettingsMenuBuild1.Picture), 200)
    SettingsMenuBuild1.PictureOffset = [0, 100]
    SettingsMenuBuild1.ApplyCLUT = False
    SettingsMenuBuild1.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)


    #MainMenu1.ApplyCLUT = True
    SettingsMenuBuild1.ApplyMask = True
    SettingsMenuBuild1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Sub-Settings_400_200.bmp"))
    

    #Buffer Picture 2
    SettingsMenuBuild2 = Scene_Descriptor.SceneDescriptor(2, 200, 100)
    SettingsMenuBuild2.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Temperatur_200_100.bmp")
    SettingsMenuBuild2.Picture = SettingsMenuBuild2.Picture.convert('RGBA')
    SettingsMenuBuild2.Picture = AlphaBlending.PutAlpha(np.asarray(SettingsMenuBuild2.Picture), 200)
    SettingsMenuBuild2.ApplyMask = True
    SettingsMenuBuild2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Temperatur_200_100.bmp"))

    SettingsMenuBuild2.ApplyAlpha = True
    
    SettingsMenuBuild2.PictureOffset = [300, 500]


    #Buffer Picture 3
    SettingsMenuBuild3 = Scene_Descriptor.SceneDescriptor(3, 300, 100)
    SettingsMenuBuild3.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp")
    SettingsMenuBuild3.Picture = SettingsMenuBuild3.Picture.convert('RGBA')
    SettingsMenuBuild3.Picture = AlphaBlending.PutAlpha(np.asarray(SettingsMenuBuild3.Picture), 50)
    SettingsMenuBuild3.PictureOffset = [500, 500]

    SettingsMenuBuild3.ApplyMask = True
    SettingsMenuBuild3.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp"))

    #Buffer Picture 4
    SettingsMenuBuild4 = Scene_Descriptor.SceneDescriptor(4, 200, 100)
    SettingsMenuBuild4.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Tilbake_200_100.bmp")
    SettingsMenuBuild4.Picture = SettingsMenuBuild4.Picture.convert('RGBA')
    SettingsMenuBuild4.Picture = AlphaBlending.PutAlpha(np.asarray(SettingsMenuBuild4.Picture), 0)
    SettingsMenuBuild4.PictureOffset = [500, 100]

    SettingsMenuBuild4.ApplyMask = True
    SettingsMenuBuild4.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Tilbake_200_100.bmp"))

    SettingsMenuBuildEnd = Scene_Descriptor.Empty

    SettingsMenu = Scene_Descriptor.SceneItems
    SettingsMenu.Array = [SettingsMenuBuild, SettingsMenuBuild1, SettingsMenuBuild2, SettingsMenuBuild3, SettingsMenuBuild4]

    #Create a linked list
    SettingsMenuBuild4.Next = SettingsMenuBuild3
    SettingsMenuBuild3.Next = SettingsMenuBuild2
    SettingsMenuBuild2.Next = SettingsMenuBuild1
    SettingsMenuBuild1.Next = SettingsMenuBuildEnd
    #SettingsMenuBuild.Next = SettingsMenuBuildEnd
    SettingsMenuBuildEnd.Next = None

    TestEntity.ScenesConstructed += 1

    SettingsMenu = Scene_Descriptor.SceneItems
    SettingsMenu.Array = [SettingsMenuBuild, SettingsMenuBuild1, SettingsMenuBuild2, SettingsMenuBuild3, SettingsMenuBuild4]
    
    return SettingsMenu, SettingsMenuBuild, SettingsMenuBuild1, SettingsMenuBuild2, SettingsMenuBuild3, SettingsMenuBuild4










#Construct Subsettings Menu
def SubSettingsMenuBuild(TestEntity):

    SubSettingsMenuBuild = Scene_Descriptor.SceneDescriptor(0, ScreenResolutionX, ScreenResolutionY)

    SubSettingsMenuBuild.Exists = 1
    #SubSettingsMenu.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp")
    SubSettingsMenuBuild.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/SubSettingsBackground.bmp")
    SubSettingsMenuBuild.Picture = np.asarray(SubSettingsMenuBuild.Picture.convert('RGBA'))
    SubSettingsMenuBuild.PictureSize = [ScreenResolutionX, ScreenResolutionY]

    SubSettingsMenuBuild.ApplyCLUT = True
    SubSettingsMenuBuild.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)


    SubSettingsMenuBuild1 = Scene_Descriptor.SceneDescriptor(1, 800, 600)
    SubSettingsMenuBuild1.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/MainMenuBackground.bmp")
    SubSettingsMenuBuild1.Picture = SubSettingsMenuBuild1.Picture.convert('RGBA')
    SubSettingsMenuBuild1.Picture = AlphaBlending.PutAlpha(np.asarray(SubSettingsMenuBuild1.Picture), 200)

    SubSettingsMenuBuild1.ApplyMask = True
    SubSettingsMenuBuild1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Stjerne.bmp"))

    SubSettingsMenuBuild2 = Scene_Descriptor.SceneDescriptor(2, 800, 600)
    SubSettingsMenuBuild2.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/NothingToSeeHere_800_600.bmp")
    SubSettingsMenuBuild2.Picture = SubSettingsMenuBuild2.Picture.convert('RGBA')
    SubSettingsMenuBuild2.Picture = AlphaBlending.PutAlpha(np.asarray(SubSettingsMenuBuild2.Picture), 200)

    SubSettingsMenuBuild2.ApplyMask = True
    SubSettingsMenuBuild2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/NothingToSeeHere_800_600.bmp"))



    SubSettingsMenuBuild3 = Scene_Descriptor.SceneDescriptor(3, 400, 200)
    SubSettingsMenuBuild3.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/BACK_400_200.bmp")
    SubSettingsMenuBuild3.Picture = SubSettingsMenuBuild3.Picture.convert('RGBA')
    SubSettingsMenuBuild3.Picture = AlphaBlending.PutAlpha(np.asarray(SubSettingsMenuBuild3.Picture), 200)

    SubSettingsMenuBuild3.PictureOffset = [int(ScreenResolutionX/2 - 200), int(ScreenResolutionY/2 - 100)]
    SubSettingsMenuBuild3.ApplyMask = True
    SubSettingsMenuBuild3.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/BACK_400_200.bmp"))

    SettingsMenu = Scene_Descriptor.SceneItems
    SettingsMenu.Array = [SubSettingsMenuBuild, SubSettingsMenuBuild1, SubSettingsMenuBuild2, SubSettingsMenuBuild3]


    SubSettingsMenuBuildEnd = Scene_Descriptor.Empty
    #Create a linked list
    SubSettingsMenuBuild3.Next = SubSettingsMenuBuild2
    SubSettingsMenuBuild2.Next = SubSettingsMenuBuild1
    SubSettingsMenuBuild1.Next = SubSettingsMenuBuildEnd
    #SettingsMenuBuild.Next = SettingsMenuBuildEnd
    SubSettingsMenuBuildEnd.Next = None

    TestEntity.ScenesConstructed += 1

    SubSettingsMenu = Scene_Descriptor.SceneItems
    SubSettingsMenu.Array = [SubSettingsMenuBuild, SubSettingsMenuBuild1, SubSettingsMenuBuild2, SubSettingsMenuBuild3]
    
    return SubSettingsMenu, SubSettingsMenuBuild, SubSettingsMenuBuild1, SubSettingsMenuBuild2, SubSettingsMenuBuild3


