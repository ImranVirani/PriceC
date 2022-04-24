#!/usr/bin/python

from pycoingecko import CoinGeckoAPI
import sys

cg = CoinGeckoAPI()

price = cg.get_price(str(sys.argv[0]), str(sys.argv[1]))

print("The price of " + str(sys.argv[0]), "in ", str(sys.argv[1]), "is ", str(price))
