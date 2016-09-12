#
# Copyright (c) 2016 Yatpang Cheung. All rights reserved.
#

# imports
import requests

# requests the data for some categories of stock universe
def getData(tickerList):

    tickerReturnList = []

    yahooFinance = 'http://ichart.finance.yahoo.com/table.csv?s='

    for ticker in tickerList:

        print "Requesting historical data for "+ticker
        req = requests.get(yahooFinance+ticker)
        content = req.content

        returnList = []
        priceList = []

        parsedContent = content.split('\n')

        # at least one year of trading data
        if len(parsedContent) > 252:

            # create price list
            for line in parsedContent[1:252]:
                lineList = line.split(',')
                if len(lineList) == 7:
                    adjustedClose = float(lineList[6])
                    priceList.append(adjustedClose)  

            # for the price list, convert to daily return list
            for i in range(len(priceList)-1):
                dayReturn = priceList[i]/priceList[i+1]-1
                returnList.append(dayReturn)

            tickerReturnList.append(returnList)
            
        else:
            print ticker + " has less than a year of trading data. Process end."
            return tickerReturnList

    return tickerReturnList

