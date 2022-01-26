import statistics;
import plotly.graph_objects as go;
import plotly.figure_factory as ff;
import pandas as pd;
import random;


data = pd.read_csv("medium_data.csv")
dataList = data["reading_time"].tolist()

population = statistics.mean(dataList)

def RandomSet(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0,len(dataList)-1)
        value = dataList[randomIndex]
        dataset.append(value)
    randomMean = statistics.mean(dataset)
    return randomMean

def showfig(meanList):
    figData = meanList
    samplingMean = statistics.mean(meanList)
    sd = statistics.stdev(meanList)

    std_1_start,std_1_end = samplingMean - sd,samplingMean + sd
    std_2_start,std_2_end = samplingMean - (2*sd),samplingMean + (2*sd)
    std_3_start,std_3_end = samplingMean - (3*sd),samplingMean + (3*sd)
    sampleMean = statistics.mean(dataList)
    ztest = (sampleMean - samplingMean)/ sd
    print(ztest)

meanlist = []
for i in range(0,100):
    m = RandomSet(30)
    meanlist.append(m)
    
showfig(meanlist)