from webbrowser import Opera
import Scene_Descriptor
import OperationsCounter
import Dynamic_RAM
import CLUT
from PIL import Image
import Analytics
import numpy as np
import Referanse_Funksjoner

import time

class PictureList:
    def __init__(Self, Layers):
        Self.list = [0]*Layers

class Picture:
    def __init__(Self, layer, ResolutionX, ResolutionY):
        Self.Exists = 1
        Self.Size = [ResolutionX, ResolutionY]
        Self.Layer = layer
        Self.Picture = [[]]
        Self.Offset = [0, 0]
        Self.ApplyCLUT = False
        Self.CLUT = np.zeros((3, 256), dtype=np.uint8)
        Self.ApplyMask = False
        Self.Mask = [[]]
        Self.ApplyAlpha = False



ScreenResolutionX = 800
ScreenResolutionY = 600


TargetBuffer = False
TestEntity = OperationsCounter.OperationsCounter(ScreenResolutionX, ScreenResolutionY)
StateMachineStatus = "SubSettingsMenus"
RAM = Dynamic_RAM.RAM(16, TestEntity)

#Main Menu
MainMenuBG = Picture(0, ScreenResolutionX, ScreenResolutionY)
MainMenu1 = Picture(1, 200, 100)
MainMenu2 = Picture(2, 100, 100)
MainMenu3 = Picture(3, 300, 100)

MainMenuBG.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/MainMenuBackground.bmp").convert("RGBA"))
MainMenu1.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp").convert("RGBA"))
MainMenu2.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp").convert("RGBA"))
MainMenu3.Picture = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp").convert("RGBA")
MainMenu3.Picture.putalpha(128)
MainMenu3.Picture = np.asarray(MainMenu3.Picture)

MainMenu1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Innstillinger_200_100.bmp"))
MainMenu2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Kaffe_100_100.bmp"))

MainMenu1.Offset = [600, 0]
MainMenu2.Offset = [700, 300]
MainMenu3.Offset = [0, 200]


#Settings
SettingsMenuBG = Picture(0, ScreenResolutionX, ScreenResolutionY)
SettingsMenu1 = Picture(1, 400, 200)
SettingsMenu2 = Picture(2, 200, 100)
SettingsMenu3 = Picture(3, 300, 100)
SettingsMenu4 = Picture(4, 200, 100)

SettingsMenuBG.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/SettingsBackground.bmp").convert("RGBA"))
SettingsMenu1.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Sub-Settings_400_200.bmp").convert("RGBA"))
SettingsMenu2.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Temperatur_200_100.bmp").convert("RGBA"))
SettingsMenu3.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp").convert("RGBA"))
SettingsMenu4.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Tilbake_200_100.bmp").convert("RGBA"))

SettingsMenu1.Offset = [0, 100]
SettingsMenu2.Offset = [300, 500]
SettingsMenu3.Offset = [500, 500] 
SettingsMenu4.Offset = [500, 100]

SettingsMenu1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Sub-Settings_400_200.bmp"))
SettingsMenu2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Temperatur_200_100.bmp"))
SettingsMenu3.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Brukerguide_300_100.bmp"))
SettingsMenu4.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/Tilbake_200_100.bmp"))


#SubSettings
SubSettingsMenuBG = Picture(0, ScreenResolutionX, ScreenResolutionY)
SubSettingsMenu1 = Picture(1, 800, 600)
SubSettingsMenu2 = Picture(2, 800, 600)
SubSettingsMenu3 = Picture(3, 400, 200)

SubSettingsMenuBG.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/SubSettingsBackground.bmp").convert("RGBA"))
SubSettingsMenu1.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/MainMenuBackground.bmp").convert("RGBA"))
SubSettingsMenu2.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/NothingToSeeHere_800_600.bmp").convert("RGBA"))
SubSettingsMenu3.Picture = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/BACK_400_200.bmp").convert("RGBA"))

SubSettingsMenuBG.CLUT = CLUT.GenerateTestCLUT(256, 256, 256)
SubSettingsMenu1.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Stjerne.bmp"))
SubSettingsMenu2.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/NothingToSeeHere_800_600.bmp"))
SubSettingsMenu3.Mask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Egne/BACK_400_200.bmp"))

SubSettingsMenuBG.Offset = [0,0]
SubSettingsMenu1.Offset = [0,0]
SubSettingsMenu2.Offset = [0,0]
SubSettingsMenu3.Offset = [int(ScreenResolutionX/2 - 200), int(ScreenResolutionY/2 - 100)]


while(1):

    
    if StateMachineStatus == "MainMenu":
        FreeLine=np.full((ScreenResolutionY, ScreenResolutionX), True)
        
        #foreground = foreground.resize(background.size)
        StartTime = time.time()
        Out, FreeLine = Referanse_Funksjoner.Ref_Alpha(MainMenu3, MainMenu3.Offset, MainMenuBG, FreeLine, RAM, TestEntity)
        #Test = Image.fromarray(Out)
        #Test.show()
        Out1, FreeLine = Referanse_Funksjoner.Ref_Mask(MainMenu1.Picture, MainMenu1.Offset, Out, MainMenu1.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out2, FreeLine = Referanse_Funksjoner.Ref_Mask(MainMenu2.Picture, MainMenu2.Offset, Out1, MainMenu2.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out3 = Referanse_Funksjoner.Ref_Fill(Out2, MainMenuBG.Picture, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)

        EndTime = time.time()
        #print the time

        print (EndTime - StartTime)

        Out3 = Image.fromarray(Out3)
        Out3.show()

        #Not important, but shows how Shadow buffers switch on a software level.
        if TargetBuffer == True:
            Buffer0 = Out3
        if TargetBuffer == False:
            Buffer1 = Out3
        TargetBuffer != TargetBuffer
        break
    
    if StateMachineStatus == "SettingsMenu":
        FreeLine=np.full((ScreenResolutionY, ScreenResolutionX), True)

        StartTime = time.time()
        Out, FreeLine = Referanse_Funksjoner.Ref_Mask(SettingsMenu1.Picture, SettingsMenu1.Offset, SettingsMenuBG.Picture, SettingsMenu1.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out1, FreeLine = Referanse_Funksjoner.Ref_Mask(SettingsMenu2.Picture, SettingsMenu2.Offset, Out, SettingsMenu2.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out2, FreeLine = Referanse_Funksjoner.Ref_Mask(SettingsMenu3.Picture, SettingsMenu3.Offset, Out1, SettingsMenu3.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out3, FreeLine = Referanse_Funksjoner.Ref_Mask(SettingsMenu4.Picture, SettingsMenu4.Offset, Out2, SettingsMenu4.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        EndTime = time.time()
        print (EndTime - StartTime)

        Out3 = Image.fromarray(Out3)
        Out3.show()

    if StateMachineStatus == "SubSettingsMenus":
        FreeLine=np.full((ScreenResolutionY, ScreenResolutionX), True)

        StartTime = time.time()

        Out = Referanse_Funksjoner.Ref_CLUT(SubSettingsMenuBG.Picture, SubSettingsMenuBG.CLUT, [0,0], RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out1, FreeLine = Referanse_Funksjoner.Ref_Mask(SubSettingsMenu1.Picture, SubSettingsMenu1.Offset, Out, SubSettingsMenu1.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)    
        Out2, FreeLine = Referanse_Funksjoner.Ref_Mask(SubSettingsMenu2.Picture, SubSettingsMenu2.Offset, Out1, SubSettingsMenu2.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        Out3, FreeLine = Referanse_Funksjoner.Ref_Mask(SubSettingsMenu3.Picture, SubSettingsMenu3.Offset, Out2, SubSettingsMenu3.Mask, FreeLine, RAM, TestEntity)
        RAM.clear("All", TestEntity)
        #Out3 = Referanse_Funksjoner.Ref_Fill(Out2, MainMenuBG.Picture, FreeLine, RAM, TestEntity)


        EndTime = time.time()
        print (EndTime - StartTime)

        Out3 = Image.fromarray(Out3)
        Out3.show()


    

#if StateMachineStatus == "SettingsMenu":





#if StateMachineStatus == "SubSettingsMenu":





















