import numpy as np

#ENKEL LØSNING FUNKER ALLTID! JA BRA HURRA!
class CLUT1D:
    def GenerateCLUT1D(Rsize, Gsize, Bsize):
        r = [R for R in range (Rsize)]
        g = [G for G in range (Gsize)]
        b = [B for B in range (Bsize)]

        CLUT1D = np.concatenate((r,g,b))
        return CLUT1D
        


#CLUT3D = Fucka atm
class CLUT3D:

    #generer en standard tom CLUT
    def GenerateCLUT(sizeR, sizeG, sizeB):
        CLUT = [[[0 for b in range (sizeR)] for g in range (sizeG)] for r in range (sizeB)]
        return CLUT

    #For å skape standard lineær CLUT-verider i en predefinert CLUT
    def CLUTStandardValues(CLUTname, sizeR, sizeG, sizeB):
        for r in range (sizeR):
            for g in range (sizeG):
                for b in range (sizeB):
                    CLUTname[r][g][b] = b
            
        

    #Funksjon for å erstatte gammel CLUT med ny, gitt samme størrelse. Eventuelt må interpolering til.
    def ImportNewCLUT(sizeR, sizeG, sizeB, newCLUT, oldCLUT):    
             for r in range (sizeR):
                for g in range (sizeG):
                    for b in range (sizeB):
                        oldCLUT[sizeR][sizeG][sizeB] = newCLUT[sizeR][sizeG][sizeB]
    
    #test-funksjon, blir ikke brukt. Fungerer feil også. hehe. :)
    def ReverseCLUT(sizeR, sizeG, sizeB, CLUTname):
        for r in range (sizeR):
                for g in range (sizeG):
                    for b in range (sizeB):
                        CLUTname[r][g][b] = (sizeR-1-r),(sizeG-1-g),(sizeB-1-b)


#Attempt 1 at CLUTApply
# def ApplyCLUT(Data, CLUT, Layers):
#     offset = np.size(CLUT)//Layers
#     for i in range (0, Layers, 3):
#             for j in range (i, np.size(Data), 3):
#                 DataOut = CLUT[Data[j+offset]]
#    return DataOut

#CLUTApply 2
def ApplyCLUT(Data, CLUT):
    Offset = 256
    x = Data.shape[0]
    y = Data.shape[1]
    DataOut = np.zeros((x, y, 3))
    for i in range(0, x):
        for j in range(0, y):
            for k in range(0, 2):
                DataOut[i][j][k] = CLUT[(Data[j][i][k])+Offset*k]
                #print(DataOut[i][j][k])
    return DataOut
    #litt forskyvd. Sjekk senere!
#


   # def CLUT7Bit():
    #Attempt

#Test

#CLUT = CLUT1D.GenerateCLUT1D(256, 256, 256)
#print(CLUT)
#CLUT = CLUT3D.GenerateCLUT(256,256,256)
#print(np.size(CLUT))
#CLUT3D.CLUTStandardValues(CLUT, 256, 256, 256)
#CLUT3D.ReverseCLUT(256,256,256, CLUT)
#print(np.size(CLUT))
#




