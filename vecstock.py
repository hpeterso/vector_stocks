#
# This is the base Stock class.
#
# translate stocks into this class to be
# used by the vector stocks program
#

import math

class VecStock:
    def __init__(self, name, symbol, start_price, current_price, change):
        self.name = name
        self.symbol = symbol
        self.start_price = start_price
        self.current_price = current_price
        self.change = change

    def start_price_string(self):
    	split = math.modf(self.start_price)
    	return "Starting price is {0:.0f} dollars and {1:.0f} cents.".format(split[1], split[0]*100)

    def current_price_string(self):
    	split = math.modf(self.current_price)
    	return "Current price is {0:.0f} dollars and {1:.0f} cents.".format(split[1], split[0]*100)

    def change_string(self):
    	split = math.modf(self.change)
    	if self.change > 0:
    		return "Up {0:.0f} dollars and {1:.0f} cents.".format(split[1], split[0]*100)
    	else:
    		return "Down {0:.0f} dollars and {1:.0f} cents.".format(abs(split[1]), abs(split[0]*100))


    def trend(self):
        return self.current_price - self.start_price


