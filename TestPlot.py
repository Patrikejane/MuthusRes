__author__ = 'sunimal.malkakulage'

resultsByMethods2D = [[] for x in range (24)]

actualResult=[]

#Reading File with actual similarity values
with open('testNamesPlot.csv','rb') as f_open:
    for line in f_open:
        twoNames = line.rstrip('\n\r').split(',')
        actualResult.append(int(twoNames[0]))

#Reading 24 Method results and divid method vise
with open('MyResult.csv','rb') as f_open:
    for line in f_open:
        LineByMethodResults = []
        twoNames = line.rstrip('\n\r').split(',')[4:]
        print("list with Time : ",twoNames)
        for i in range (0,len(twoNames),2):
            LineByMethodResults.append(twoNames[i])
            print("list with method results : ",LineByMethodResults)
        print(LineByMethodResults)
        for i in range(24):
            for j in range(24):
                if i == j:
                    resultsByMethods2D[i].append(LineByMethodResults[j])


print("--------------------------------------------------------------------")
print(actualResult)
print(resultsByMethods2D)

for i in resultsByMethods2D:
    print(i)

