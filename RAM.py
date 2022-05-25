import numpy as np
from PIL import Image

class RAMClass:


    #enkel instansiering av RAM-arrayet
    def CreateRAM(RAM_SIZE, Type):
        if (Type == "B"):
            RAM_SIZE_b = RAM_SIZE
            RAM = [0 for i in range(RAM_SIZE_b)]
            return RAM
        elif (Type == "KB"):
            RAM = [0 for i in range(RAM_SIZE* 1024)]
            return RAM
        

    #Funksjon for å skalere opp RAM i sektorer, hvor man henter ut et offset for hver sektor
    def ram_allocate_sectors(Sections, RAMSize):
        
        SectionSize = (len(RAMSize)//Sections)
        #Offset=[(SectionSize*n) for n in range(Sections)]
        #return Offset
        return SectionSize


    #Setter startpunkt av dataen til rett sektor, og skriver derifra
    def ram_put_data(Layer, Offset, Data, RAMIn):
        LayerOffset = (Layer*Offset)
        DataLen = np.size(Data)
        FlatArray = Data.reshape(-1)
        #Shameless testing
        #print(DataLen)
        #print(Offset)
        if DataLen <= Offset:
            for i in range (0, DataLen-3, 3):
                for n in range (0, 3):
                    RAMIn[LayerOffset + i + n] = FlatArray[i + n]   
        
        else:
            print("Data does not fit inside sector. Reduce data size or increase sector size.")

        return DataLen  
        

    def ram_put_clut(DataEnd, Layer, Offset, CLUT, RAMIn):
        DataLen = np.size(CLUT)
        CLUTOffset = (Layer * Offset) + (DataEnd+1)
        if DataLen <= ((Layer+1)*Offset - CLUTOffset):
            for i in range (DataLen):
                RAMIn[CLUTOffset + i] = CLUT[i]   

    
        else:
            print("CLUT does not fit inside sector. Reduce data/clut size or increase sector size.")

    #Henter ut all data 
    def ram_get_data(Layer, Offset, DataLen, RAMIn, y, x):
        DataOut =[0 for i in range(DataLen)]
        LayerOffset = (Layer*Offset)
        for i in range (0, DataLen-3, 3):
            #DataOut[i] = RAMIn[(Offset*Layer) + DataLen + i]
            for n in range (0, 3):
                DataOut [i + n] = RAMIn[LayerOffset + i + n]

        DataOut = np.array(DataOut)
        DataOut = DataOut.reshape(y, x, 3)
        return DataOut
    #Gjør motsatt av put
    


    def ram_get_clut(Layer, Offset, DataLen, RAMIn, DataEnd):
        CLUTOut = [0 for i in range(DataLen)]
        CLUTOffset = (Layer * Offset) + (DataEnd+1)
        for i in range (DataLen):
            CLUTOut[i] = RAMIn[CLUTOffset +i]

        return CLUTOut
        

    # def ram_clear_section(section):
    #     Size=(section.__sizeof__)
    #     RamUsage -=Size
    #     #clear section

    # def ram_clear(NumOfLayers):
    #     for i in range (NumOfLayers):
    #         RAM[i] = 0


#Test


directory = "F:\\Google Drive\\Skule\\Elsys 5. år\\Prosjekt Nordic\\Prosjekt kodefiler\\test.jpg"

PictureIn = np.array(Image.open(directory))
#print(PictureIn)
#RAM = 24
RAM = RAMClass.CreateRAM(4096, "KB")
SectionSize = RAMClass.ram_allocate_sectors(2, RAM)
#print(SectionSize)
#print(len(RAM))
DataEnd = RAMClass.ram_put_data(0, SectionSize, PictureIn, RAM)
#RAMClass.ram_put_clut(DataEnd, 0, SectionSize, CLUT, RAM)
#print(Test)

#Out = RAMClass.ram_get_data(0, SectionSize, DataLen, RAM)
#OutCLUT = RAMClass.ram_get_clut(Layer, Offset, DataLen, RAMIn, DataEnd)