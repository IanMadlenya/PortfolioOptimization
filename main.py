#
# Copyright (c) 2016 Yatpang Cheung. All rights reserved.
#

# imports
import numpy
from optimization import optimize

if __name__ == '__main__':

	# tickers of interest in portfolio
    portList = ['WFC', 'DAL', 'FB', 'NVDA', 'TSLA']
    optimize(portList)

