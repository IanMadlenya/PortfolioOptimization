#
# Copyright (c) 2016 Yatpang Cheung. All rights reserved.
#

# represents an instance of random portfolio stimulation
class randPortfolio(object):

    # initializes with portfolio tickers, weights, sharpe ratio, and overall std
    def __init__ (self, tickerList, portWeights, portSharpeR, portStd):
    	self.tickers = tickerList
        self.weights = portWeights
        self.sharpeRatio = portSharpeR
        self.standardDev = portStd

    # overloaded output
    def __str__ (self):
    	output = "Stimulated Portfolio-- "+"Sharpe Ratio: "+format(self.sharpeRatio, '.2f')
    	output = output + " | Annualized Standard Deviation: "+format(self.standardDev, '.2f')+"% | Weights-- "
    	for i in range(len(self.tickers)):
    		output = output + self.tickers[i] + ": " + format((self.weights[i])*100, '.2f')+"% "
    	return output
