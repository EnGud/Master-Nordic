import matplotlib.pyplot as plt




#Input is a class which contain multiple attributes which are arrays. Create a histogram for each attribute, iterating over the arrays.
def histogram(input_structure, Length):
        #create a histogram for each attribute
        Histogram = [0]*Length
        for i in range(len(input_structure)):
            #create a histogram for each attribute
            Histogram[i] = input_structure[i]
            
        PlotHistogram(Histogram, Length)
        return Histogram


#Input a class. The class contains multiple atributes. Create a histogram for each attribute.

    
  

  
#Function to plot the histogram
def PlotHistogram(Histogram, Length):
        plt.bar(range(Length), Histogram)
        plt.show()
        #Save the histogram
        #plt.savefig("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Histogram/Test_Histogram.bmp")

#Save every iteration-value into array
def Testing(TestEntity, CurrentY):


    TestEntity.ApplyAlpha_Pixel_Array[CurrentY] = TestEntity.ApplyAlpha_Pixel
    TestEntity.ApplyMask_Pixel_Array[CurrentY] = TestEntity.ApplyMask
    TestEntity.CLUT_Pixel_Array[CurrentY] = TestEntity.CLUT_Pixel_Applied
    TestEntity.RAM_put_Array[CurrentY] = TestEntity.RAM_put
    TestEntity.RAM_get_Array[CurrentY] = TestEntity.RAM_get
    TestEntity.RAM_Used_Bytes_Array[CurrentY] = TestEntity.RAM_Used_Bytes

#Erase every valye
def Clean(TestEntity):
    TestEntity.ApplyAlpha_Pixel = 0
    TestEntity.ApplyMask = 0
    TestEntity.CLUT_Pixel_Applied = 0
    TestEntity.RAM_put = 0
    TestEntity.RAM_get = 0
    TestEntity.RAM_Used = 0
    TestEntity.RAM_Used_Bytes = 0

#Analyze by printing histogram of each array
def Analyze(TestEntity):
    histogram(TestEntity.ApplyAlpha_Pixel_Array)
    histogram(TestEntity.ApplyMask_Pixel_Array)
    histogram(TestEntity.CLUT_Pixel_Array)
    histogram(TestEntity.RAM_put_Array)
    histogram(TestEntity.RAM_get_Array)
    histogram(TestEntity.RAM_Used_Bytes_Array)