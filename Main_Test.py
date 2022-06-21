
import Scene_Descriptor, AlphaBlending, AlphaMasking, OperationsCounter, Dynamic_RAM, Analytics, CLUT, Scene_Descriptor

from PIL import Image
import numpy as np
import threading
import Analytics
#Limitation: Every picture needs an alpha


TestEntity = OperationsCounter.OperationsCounter(600, 800)
TestEntity.Length = 600 
# Manual fix
#Bærbar
#BufferedPicture1 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")
#BufferedPicture2 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp")
#BufferedPicture3 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Alternativ.bmp")
#BufferedPicture4 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")
#BufferedMask = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")

#Stasjonær
BufferedPicture1 = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/MainMenuBackground.bmp").convert("RGBA"))
BufferedPicture2 = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/SettingsBackground.bmp").convert("RGBA"))
BufferedPicture3 = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/SubSettingsBackground.bmp").convert("RGBA"))
#BUFFER EQUALS SAVED ON FLASH/DISK/WHATEVER


#Generate Outputbuffer Array with the same y length as AlphaedPicture


BufferedMask = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp"))
BufferedMask1 = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Stjerne.bmp")

TestEntity.FreeLine = [True]*800

Histogram = [0]*600

AlphaTest = False
if AlphaTest == True:
    AlphaedPictureOut = np.zeros((600, 800, 4), dtype=np.uint8)

    AlphaedPicture = AlphaBlending.check_alpha(BufferedPicture1, TestEntity)
    input()

    for CurrentY in range (len(BufferedPicture1)):
        
        Picture = AlphaedPicture[CurrentY]
        PictureBG = BufferedPicture2[CurrentY]
        #
        print(CurrentY)
        
        AlphaedPictureOut[CurrentY] = AlphaBlending.ApplyAlpha(Picture, 0, "Over", PictureBG, TestEntity)
        #Histogram[i] = TestEntity.ApplyAlpha
        #TestEntity.ApplyAlpha = 0

    
        


    AlphaedPictureOut = np.asarray(AlphaedPictureOut)
    AlphaedPictureOut = Image.fromarray(AlphaedPictureOut)
    AlphaedPictureOut.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_AlphaBlending.bmp")
    Analytics.PlotHistogram(Histogram)
    AlphaedPictureOut.show()



MaskTest = False
if MaskTest == True:
    MaskedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)

    for CurrentY in range (len(BufferedPicture1)):
        LineMask = BufferedMask[CurrentY]
        LineBuff1 = BufferedPicture1[CurrentY]
        LineBuff2 = BufferedPicture2[CurrentY]

        print(CurrentY)
        MaskedPicture[CurrentY] = AlphaMasking.ApplyMask(LineBuff1, 0, LineBuff2, LineMask, TestEntity)
        #Histogram[i] = TestEntity.ApplyMask
        #TestEntity.ApplyMask = 0
    
    MaskedPicture = np.asarray(MaskedPicture)
    MaskedPicture = Image.fromarray(MaskedPicture)
    MaskedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking.bmp")
    Analytics.PlotHistogram(Histogram)
    MaskedPicture.show()



#CLUT stands for Color Look Up Table

CLUTTest = False
if CLUTTest == True:
    TestCLUT = CLUT.GenerateTestCLUT(256, 256, 256)

    CLUTedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)


    #apply a CLUT on a picture by changing the colour value to the corresponding color value of the CLUT
    for CurrentY in range (len(BufferedPicture1)):
        print(CurrentY)
        CLUTedPicture[CurrentY] = CLUT.ApplyCLUT(BufferedPicture1[CurrentY], TestCLUT, 0, TestEntity)

    CLUTedPicture = np.asarray(CLUTedPicture)
    CLUTedPicture = Image.fromarray(CLUTedPicture)
    CLUTedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_CLUT.bmp")



Both = False
if Both == True:
    AlphaedPictureOut = np.zeros((600, 800, 4), dtype=np.uint8)
    MaskedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)
    AlphaedPicture = AlphaBlending.check_alpha(BufferedPicture1, TestEntity)
    input()

    for CurrentY in range (len(BufferedPicture1)):
        
        Picture = AlphaedPicture[CurrentY]
        PictureBG = BufferedPicture2[CurrentY]
        #
        print(CurrentY)
        
        AlphaedPictureOut[CurrentY] = AlphaBlending.ApplyAlpha(Picture, 0, "Over", PictureBG, TestEntity)
        #Histogram[i] = TestEntity.ApplyAlpha
        #TestEntity.ApplyAlpha = 0
  

    for CurrentY in range (len(BufferedPicture1)):
        LineMask = BufferedMask[CurrentY]
        LineBuff1 = BufferedPicture3[CurrentY]
        LineBuff2 = AlphaedPictureOut[CurrentY]

        print(CurrentY)
        MaskedPicture[CurrentY] = AlphaMasking.ApplyMask(LineBuff1, 0, LineBuff2, LineMask, TestEntity)
        #Histogram[i] = TestEntity.ApplyMask
        #TestEntity.ApplyMask = 0
    
    MaskedPicture = np.asarray(MaskedPicture)
    MaskedPicture = Image.fromarray(MaskedPicture)
    MaskedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking_And_Alpha.bmp")
    Analytics.PlotHistogram(Histogram)
    MaskedPicture.show()


All = True
if All == True:

    TestCLUT = CLUT.GenerateTestCLUT(256, 256, 256)
    CLUTedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)


    #apply a CLUT on a picture by changing the colour value to the corresponding color value of the CLUT
    for CurrentY in range (len(BufferedPicture1)):
        print(CurrentY)
        CLUTedPicture[CurrentY] = CLUT.ApplyCLUT(BufferedPicture1[CurrentY], TestCLUT, 0, TestEntity)

    AlphaedPictureOut = np.zeros((600, 800, 4), dtype=np.uint8)
    MaskedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)
    AlphaedPicture = AlphaBlending.check_alpha(CLUTedPicture, TestEntity)
    input()

    for CurrentY in range (len(BufferedPicture1)):
        
        Picture = AlphaedPicture[CurrentY]
        PictureBG = BufferedPicture2[CurrentY]
        #
        print(CurrentY)
        
        AlphaedPictureOut[CurrentY] = AlphaBlending.ApplyAlpha(Picture, 0, "Over", PictureBG, TestEntity)
        #Histogram[i] = TestEntity.ApplyAlpha
        #TestEntity.ApplyAlpha = 0
  

    for CurrentY in range (len(BufferedPicture1)):
        LineMask = BufferedMask[CurrentY]
        LineBuff1 = BufferedPicture3[CurrentY]
        LineBuff2 = AlphaedPictureOut[CurrentY]

        print(CurrentY)
        MaskedPicture[CurrentY] = AlphaMasking.ApplyMask(LineBuff1, 0, LineBuff2, LineMask, TestEntity)
        #Histogram[i] = TestEntity.ApplyMask
        #TestEntity.ApplyMask = 0
    
    MaskedPicture = np.asarray(MaskedPicture)
    MaskedPicture = Image.fromarray(MaskedPicture)
    MaskedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking_And_Alpha_And_CLUT.bmp")
    Analytics.PlotHistogram(Histogram)
    MaskedPicture.show()
