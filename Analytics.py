import matplotlib.pyplot as plt

from AlphaBlending import ApplyAlpha



    #input structure contains multiple attributes which are arrays.. Create induvidual histograms for each attribute. 
def histogram(input_structure):
        #create a histogram for each attribute
        Histogram = [0]*600
        for i in range(input_structure.Length):
            #create a histogram for each attribute
            Histogram[i] = input_structure.ApplyAlpha
            PlotHistogram(Histogram)
        return Histogram



""" 
def histogram(input):
    Histogram = [0 for i in range(256)]
    for i in range(len(input)):
        for j in range(len(input[i])):
            Histogram[input[i][j]] += 1
    return Histogram
    
   """
    
  

  

def PlotHistogram(Histogram):
        plt.bar(range(600), Histogram)
        plt.show()
        #Save the histogram
        #plt.savefig("F:/Google Drive/Skule/Elsys 5. år/Nordic Master/Billeder/Histogram/Test_Histogram.bmp")
