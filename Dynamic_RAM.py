#This code will simulate a dynamic RAM module with a set size as init input argument.
#It will increment an attribute of the input class "TestEntity" every time each function is called.
import ctypes
from numpy import true_divide


class RAM:
    def __init__(self, Size):
        self.Size = Size
        self.data = [None] * Size
        self.dataoccupied = [False] * Size


# it will contain a function to put data into the ram, and return the adress of the data such that the same data can be collected later given the adress.
    def put(self, data, TestEntity):
        TestEntity.RAM_put += 1


        #loop through dataoccupied to see if there is space left in the ram. If there is, put the data in the ram.
        for i in range(len(self.dataoccupied)):
            if self.dataoccupied[i] == False:
                self.data[i] = data
                self.dataoccupied[i] = True
                TestEntity.RAM.put += 1
                return i
        #If no place left in the ram, print error.
        print("No space left in the RAM")
        return -1





# it will contain a function to get data from ram by a given adress.
    def get(self, adress, TestEntity):
        TestEntity.RAM.get.get += 1

        #check if the adress is in the ram
        #If not in RAM
        if self.data[adress] == None or self.dataoccupied[adress] == False:
            print("Data not in the RAM")
            TestEntity.RAM.get.DataNotFound += 1
            return -1

        #If in RAM
        elif self.data[adress] != None and self.dataoccupied[adress] == True:
            TestEntity.RAM.get.DataFound += 1
            return self.data[adress]


        #Situations not covered will give an error.
        elif (self.dataoccupied[adress] == True and self.data[adress] == None) or (self.dataoccupied[adress] == False and self.data[adress] != None):
            TestEntity.RAM.get_error += 1
            print("Fatal Error. Situation not covered by the code.")
            return -1

#It will contain a function to clear out the data and dataoccupied arrays to make them empty in a given adress
    def clear(self, adress, TestEntity):
        self.data[adress] = None
        self.dataoccupied[adress] = False
        TestEntity.RAM.clear += 1
        return True


#it will contain a function to check how much of the ram is used
#and how much is free.
    def check(self, TestEntity):
        count = 0
        for i in range(len(self.dataoccupied)):
            if self.dataoccupied[i] == True:
                count += 1
        print("There are", count, "data in the RAM")
        TestEntity.RAM.check += 1
        return count
    


