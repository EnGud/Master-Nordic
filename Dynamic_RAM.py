#This code will simulate a dynamic RAM module with a set size as init input argument.
#It will increment an attribute of the input class "TestEntity" every time each function is called.


from numpy import true_divide

#Initiate a RAM module
class RAM:
    def __init__(self, Size, TestEntityIn):
        self.Size = Size
        self.data = [None] * Size
        self.dataoccupied = [False] * Size
        self.RAMTestEntity = TestEntityIn


# A function to put data into the RAM array, and return an andress
    def put(self, data, TestEntity):
        TestEntity.RAM_put_call += 1

        #loop through dataoccupied to see if there is space left in the ram. If there is, put the data in the ram.
        for i in range(len(self.dataoccupied)):
            if self.dataoccupied[i] == False:
                self.data[i] = data
                self.dataoccupied[i] = True
                TestEntity.RAM_put += 1
                return i
        #If no place left in the ram, print error.
        print("No space left in the RAM")
        return -1

    #Put data in specific RAM adress. Similar to regular put, but no scanning needed.
    def put_specific(self, adress, data, TestEntity):
        self.data[adress] = data
        self.dataoccupied[adress] = True
        TestEntity.RAM_put += 1
        return adress


    #Function to get the data at a given adress
    def get(self, adress, TestEntity):
        TestEntity.RAM_get_call += 1

        #check if the adress is in the ram
        #If not in RAM
        if self.dataoccupied[adress] == False:
            print("Data not in the RAM")
            TestEntity.RAM_get_DataNotFound += 1
            return -1

        #If in RAM
        elif self.dataoccupied[adress] == True:
            TestEntity.RAM_get += 1
            return self.data[adress]


        #Situations not covered will give an error.
        elif (self.dataoccupied[adress] == True and self.data[adress] == None) or (self.dataoccupied[adress] == False and self.data[adress] != None):
            TestEntity.RAM_get_error += 1
            print("Fatal Error. Situation not covered by the code.")
            return -1


#Function to clear out the ram of either all data, or select data.
    def clear(self, adress, TestEntity):
        if adress == "All":
            for i in range(len(self.dataoccupied)):
                self.data[i] = None
                self.dataoccupied[i] = False
                TestEntity.RAM_clear += 1
            return 0
        else:
            self.data[adress] = None
            self.dataoccupied[adress] = False
            TestEntity.RAM_clear += 1

            #If commando "All", clear all data in the ram.
            
            return True


#Function to check how many "entities" are in the RAM
    def check(self, TestEntity):
        count = 0
        for i in range(len(self.dataoccupied)):
            if self.dataoccupied[i] == True:
                count += 1
        #print("There are", count, "data in the RAM")
        #TestEntity.RAM_check += 1
        return count


   #Function to find how many bytes are stored in RAM
    def CheckEveryArrayBit(self, TestEntity):
        DataSize = 0
        DataArray = 0
        #DataBits = 0
        for i in range(len(self.data)):
            if (self.dataoccupied[i]):
                X = len(self.data[i]) - 1
                Z = len(self.data[i][X])

                DataArray =  X * Z
            else:
                break
                
            TestEntity.RAM_Used_Bytes +=  DataArray

        #print("There are", DataSize, "databits in the RAM")
        return



#Store a Y-axis of a picture in ram
    def StorePictureInRam(self, Structure, CurrentY, RAM_Entity, TestEntity):
        #Save the current line of the active picture in the RAM.
        #
        if (CurrentY < Structure.PictureSize[1] + Structure.PictureOffset[1]) and (CurrentY >= Structure.PictureOffset[1]):
            Structure.Picture_RAM_Adress = RAM_Entity.put(Structure.Picture[CurrentY-Structure.PictureOffset[1]], TestEntity)
            Structure.PictureStoredInRam = True
        else:
            Structure.PictureStoredInRam = False

