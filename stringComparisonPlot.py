__author__ = 'sunimal.malkakulage'

import matplotlib.pyplot as plt
import numpy as np


def sensitivity(tp, fp, tn, fn):
    sensitivity = (float(tp) / (tp + fn)) * 100
    return sensitivity


def precision(tp, fp, tn, fn):
    precision = (float(tp) / (tp + fp)) * 100
    return precision


def accuracy(tp, fp, tn, fn):
    accuracy = (float(tp + tn) / (tp + fp + tn + fn)) * 100
    return accuracy

while True:
    print(" ")
    changeList = input("Enter 0 -- 23 string comparision methods : \n")

    if changeList < 24:

        resultsByMethods2D = [[] for x in range(24)]
        actualResult = []

        # Reading File with actual similarity values
        with open('TEST_DATA.csv', 'rb') as f_open:
            for line in f_open:
                twoNames = line.rstrip('\n\r').split(',')
                actualResult.append(int(twoNames[2]))

        # Reading 24 Method results and divid method vise
        with open('MyResult.csv', 'rb') as f_open:
            for line in f_open:
                LineByMethodResults = []
                twoNames = [float(x) for x in line.rstrip('\n\r').split(',')[4:]]
                # print("list with Time : ",twoNames)
                for i in range(0, len(twoNames), 2):
                    LineByMethodResults.append(twoNames[i])
                    # print("list with method results : ",LineByMethodResults)
                # print(LineByMethodResults)
                for i in range(24):
                    for j in range(24):
                        if i == j:
                            resultsByMethods2D[i].append(LineByMethodResults[j])

        # print(resultsByMethods2D)
        # print(len(resultsByMethods2D))

        print("-----------------------Threshold vs accuracy-------------------------")

        resultsByMethodsthrehold2D = []
        for j in np.arange(0, 1.1, 0.1):
            # print(j)
            arrSet = []
            for i in range(len(resultsByMethods2D)):
                arrRounded = []
                for x in range(len(resultsByMethods2D[i])):
                    # print("x :",x,resultsByMethods2D[i][x])

                    if (resultsByMethods2D[i][x] >= j):
                        arrRounded.insert(x, 1)
                    else:
                        arrRounded.insert(x, 0)
                # print("arrRounded : ",arrRounded)
                arrSet.append(arrRounded)
            # print(arrSet)
            resultsByMethodsthrehold2D.append(arrSet)

        # print(len(resultsByMethodsthrehold2D))
        # print(actualResult)
        # print("--------------------")

        percisionList = []
        sensitivityList = []
        threshold = 0.0
        for i in resultsByMethodsthrehold2D:
            tp = 0
            fp = 0
            tn = 0
            fn = 0

            for j in range(len(i[changeList])):
                if (actualResult[j] == 1) and (i[changeList][j] == 1):
                    tp += 1
                elif (actualResult[j] == 0) and (i[changeList][j] == 1):
                    fp += 1

                elif (actualResult[j] == 0) and (i[changeList][j] == 0):
                    tn += 1

                elif (actualResult[j] == 1) and (i[changeList][j] == 0):
                    fn += 1
            if (tp + fp) != 0:
                percisionList.append(precision(tp, fp, tn, fn))
            else:
                percisionList.append(0.0)
            if (tp + fn) != 0:
                sensitivityList.append(sensitivity(tp, fp, tn, fn))
            else:
                sensitivityList.append(0.0)
            if (tp + fp + tn + fn) != 0:
                print("threshold : " + str(threshold) + " accuracy : " + str(accuracy(tp, fp, tn, fn)))

            threshold += 0.1

        print("\n")

        x = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        y = np.array(percisionList)
        b = np.array(sensitivityList)

        # ---------------- Ploting ----------------------------------
        # plotting the points
        plt.plot(x, y, 'r*')
        plt.plot(x, b, 'b+')

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('graph! method ' + str(changeList))

        # function to show the plot
        plt.show()

    if changeList == 24:
        break
