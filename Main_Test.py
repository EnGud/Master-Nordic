from turtle import delay
import AlphaBlending, AlphaMasking
from PIL import Image
import numpy as np

#Bilde =[0]*600
Bilde = np.zeros((800, 600, 3), dtype=np.uint8)
BildeMask = np.zeros((800, 600, 3), dtype=np.uint8)
TestAlphaBlending = AlphaBlending


#Init sizes

# Manual fix
#Bærbar
#BufferedPicture1 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")
#BufferedPicture2 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp")
#BufferedPicture3 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Alternativ.bmp")
#BufferedPicture4 = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")
#BufferedMask = Image.open("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")

#Stasjonær
BufferedPicture1 = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Lykke.bmp")
BufferedPicture2 = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Overlegg.bmp")

BufferedMask = Image.open("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Graas.bmp")

#print(np.asarray(BufferedPicture1).shape)

OutputBuffer = np.zeros((600, 799, 4), dtype=np.uint8)
OutputBufferMask = np.zeros((600, 799, 4), dtype=np.uint8)

#print(BufferedPicture2)

#Legg inn alpha på foreground manuelt:
TestAlphaBlending.AlphaOperations.CheckAlpha(BufferedPicture1)
#samme, men for BG:
TestAlphaBlending.AlphaOperations.CheckAlpha(BufferedPicture2)


for CurrentY in range (600):
    Bilde = TestAlphaBlending.AlphaOperations.ApplyAlpha(BufferedPicture1, BufferedPicture2, CurrentY, 'Over')
    OutputBuffer[CurrentY] = Bilde

print(OutputBuffer.shape)

#print(Bilde)

Test = Image.fromarray(OutputBuffer)
#Bærbar
#Test.save("C:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test.bmp")
#Stasjonær
Test.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test.bmp")

for CurrentY in range (600):
    BildeMask = AlphaMasking.MaskingOperations.MaskAllChannels(BufferedPicture1, BufferedPicture2, BufferedMask, CurrentY)
    OutputBuffer[CurrentY] = Bilde

TestMask = Image.fromarray(OutputBuffer)
TestMask.save("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Test_Masking.bmp")

print("Done!")