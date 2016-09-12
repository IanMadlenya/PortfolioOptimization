#
# Copyright (c) 2016 Yatpang Cheung. All rights reserved.
#

# imports
import numpy
import random
import downloadData
import randPortfolio

# stimulations per ticker
stimPerTicker = 10000

# optimize a set of tickers
def optimize(tickerList):

    tickerReturnList = downloadData.getData(tickerList)

    # if any ticker has less than a year of trading data
    if len(tickerList) is not len(tickerReturnList):
        return

    print "Start of optimization."

    # calculate covariance matrix, individual variances, and avg returns 
    covMatrix = calcCovMatrix(tickerReturnList)
    varList = calcVariance(tickerReturnList)
    returnList = calcReturns(tickerReturnList)

    trialNum = 1
    numPositions = len(tickerList)

    maxSharpeRatio = float('-inf')
    minStd = float('inf')

    # keep track of highest sharpe and lowest std
    bestSharpe = None
    globalMinVar = None

    while trialNum <= (stimPerTicker * numPositions):
        portVar = 0
        portRet = 0

        # generate list of random weights
        weights = randWeights(numPositions)

        # calculate overall portfolio variance and return given the random weights
        for x in range(numPositions):
            for y in range(numPositions):
                if x is not y:
                    portVar += (weights[x] * weights[y] * covMatrix[x][y])
            portVar += (weights[x]*weights[x]*varList[x])
            portRet += (weights[x]*returnList[x])

        # calculate annualized sharpe ratio
        sharpeRatio = portRet/numpy.sqrt(portVar)*252/numpy.sqrt(252)

        # calculate annualized portfolio standard deviation
        std = numpy.sqrt(portVar)*numpy.sqrt(252)*100

        # store the instance in an object so its easier to track
        randPort = randPortfolio.randPortfolio(tickerList, weights, sharpeRatio, std)

        # can write out to a file for further analyzing
        # or store in a list and use convex hull
        print randPort

        # keeping track of highest sharpe and lowest std
        if(sharpeRatio > maxSharpeRatio):
            maxSharpeRatio = sharpeRatio
            bestSharpe = randPort
        if(std<minStd):
            minStd = std
            globalMinVar = randPort

        trialNum += 1

    print "End of optimization process.\n"
    print "Allocation with highest Sharpe Ratio:"
    print bestSharpe
    print "Global minimum variance allocation:"
    print globalMinVar

# generate list of random weights for the tickers
def randWeights(numPositions):
    weights = []

    for i in range(numPositions):
        weights.append(random.uniform(0, 1))

    total = sum(weights)
    for i in range(numPositions):
        weights[i] = weights[i]/total

    return weights

# calculate average daily return for each ticker
def calcReturns(tickerReturnList):

    returnList = []
    for aReturnList in tickerReturnList:
        returnList.append(sum(aReturnList)/len(aReturnList))
    return returnList

# calculate average daily return for each ticker
def calcVariance(tickerReturnList):
    varList = []
    for returnList in tickerReturnList:
        variance = numpy.var(returnList)
        varList.append(variance)
    return varList

# build the covariance matrix
def calcCovMatrix(tickerReturnList):

    covMatrix = []
    for x in tickerReturnList:
        xCovList = []
        for y in tickerReturnList:
            covVal = numpy.cov(x, y)[0][1]
            xCovList.append(covVal)
        covMatrix.append(xCovList)

    return covMatrix
