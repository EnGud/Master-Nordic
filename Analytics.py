import matplotlib.pyplot as plt

class Analytics:

    #input structure contains multiple attributes. Create induvidual histograms for each attribute. 
    def histogram(self, input_structure):
        #create a histogram for each attribute
        for i in range(len(input_structure)):
            #create a histogram for each attribute
            Histogram = [0]*256
            for j in range(len(input_structure[i])):
                Histogram[input_structure[i][j]] += 1
            self.PlotHistogram(Histogram)
        return Histogram
  
  



    def PlotHistogram(Histogram):
        plt.bar(range(256), Histogram)
        plt.show()
