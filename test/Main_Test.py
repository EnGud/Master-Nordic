
import Scene_Descriptor, AlphaBlending, AlphaMasking, OperationsCounter, Dynamic_RAM, Analytics, Bits_Per_Pixel, CLUT, Scene_Descriptor

from PIL import Image
import numpy as np
import threading
import Analytics
#Limitation: Every picture needs an alpha


TestEntity = OperationsCounter.OperationsCounter(600)
TestEntity.Length = 600 
# Manual fix
#Bærbar
#BufferedPicture1 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")
#BufferedPicture2 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp")
#BufferedPicture3 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Alternativ.bmp")
#BufferedPicture4 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")
#BufferedMask = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")

#Stasjonær
BufferedPicture1 = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp"))
BufferedPicture2 = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp"))
BufferedPicture3 = np.asarray(Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Alternativ.bmp"))

#Generate Outputbuffer Array with the same y length as AlphaedPicture


BufferedMask = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")
BufferedMask1 = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Stjerne.bmp")

FreeLine = [True]*800

Histogram = [0]*600

#Tests

#Blending test
AlphaTest = False
if AlphaTest == True:
    AlphaedPicture = AlphaBlending.check_alpha(BufferedPicture1, TestEntity)
    
    for i in range (len(AlphaedPicture)):
        print(i)
        AlphaedPicture[i], FreeLine = AlphaBlending.ApplyAlpha(AlphaedPicture, [0, 0], "Over", BufferedPicture2, i, FreeLine, TestEntity)
        Histogram[i] = TestEntity.ApplyAlpha
        TestEntity.ApplyAlpha = 0


    AlphaedPicture = np.asarray(AlphaedPicture)
    AlphaedPicture = Image.fromarray(AlphaedPicture)
    AlphaedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_AlphaBlending.bmp")
    Analytics.PlotHistogram(Histogram)
    AlphaedPicture.show()


MaskTest = True
if MaskTest == True:
    MaskedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)

    for i in range (len(BufferedPicture1)):
        print(i)
        MaskedPicture[i] = AlphaMasking.ApplyMask(BufferedPicture1, BufferedPicture2, BufferedMask, i, TestEntity)
        Histogram[i] = TestEntity.ApplyMask
        TestEntity.ApplyMask = 0
    
    MaskedPicture = np.asarray(MaskedPicture)
    MaskedPicture = Image.fromarray(MaskedPicture)
    MaskedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking.bmp")
    Analytics.PlotHistogram(Histogram)
    MaskedPicture.show()


Both = False
if Both == True:
    AlphaedPicture = AlphaBlending.check_alpha(BufferedPicture1, TestEntity)
    MaskedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)
    BufferedPicture3 = AlphaBlending.check_alpha(BufferedPicture3, TestEntity)

    for i in range (len(AlphaedPicture)):
        print(i)
        AlphaedPicture[i] = AlphaBlending.ApplyAlpha(AlphaedPicture, [0, 0], "Over", BufferedPicture2, i, FreeLine, TestEntity)
        MaskedPicture[i] = AlphaMasking.ApplyMask(AlphaedPicture, BufferedPicture3, BufferedMask, i, TestEntity)

    MaskedPicture = np.asarray(MaskedPicture)
    MaskedPicture = Image.fromarray(MaskedPicture)
    MaskedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking_And_Blending.bmp")
    
#CLUT stands for Color Look Up Table
CLUTTest = False
if CLUTTest == True:
    TestCLUT = CLUT.GenerateTestCLUT(256, 256, 256)
    CLUTedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)
    #apply a CLUT on a picture by changing the colour value to the corresponding color value of the CLUT
    for i in range (len(BufferedPicture1)):
        print(i)
        CLUTedPicture[i] = CLUT.ApplyCLUT(BufferedPicture1, TestCLUT, i, TestEntity)

    CLUTedPicture = np.asarray(CLUTedPicture)
    CLUTedPicture = Image.fromarray(CLUTedPicture)
    CLUTedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_CLUT.bmp")

All = False
if All == True:
    TestCLUT = CLUT.GenerateTestCLUT(256, 256, 256)
    CLUTedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)

    for i in range (len(BufferedPicture1)):
        print(i)
        CLUTedPicture[i] = CLUT.ApplyCLUT(BufferedPicture1, TestCLUT, i, TestEntity)
        

    AlphaedPicture = AlphaBlending.check_alpha(CLUTedPicture, TestEntity)
    
    MaskedPicture = np.zeros((BufferedPicture1.shape[0], BufferedPicture1.shape[1], 4), dtype=np.uint8)
    BufferedPicture3 = AlphaBlending.check_alpha(BufferedPicture3, TestEntity)



    for i in range (len(CLUTedPicture)):
        print(i)
        AlphaedPicture[i] = AlphaBlending.ApplyAlpha(AlphaedPicture, "Over", BufferedPicture2, i, TestEntity)
        MaskedPicture[i] = AlphaMasking.ApplyMask(AlphaedPicture, BufferedPicture3, BufferedMask, i, TestEntity)

    MaskedPicture = np.asarray(MaskedPicture)
    MaskedPicture = Image.fromarray(MaskedPicture)
    MaskedPicture.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking_And_Blending_And_CLUT.bmp")
