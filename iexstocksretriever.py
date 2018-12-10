#!/usr/bin/env python3

from iexfinance.stocks import Stock
from vecstock import VecStock

def pretty_print(quote):
	print('\n' + str(quote['symbol']) + " " + str(quote['companyName'])
		+ '\n\tLatest Time: ' + str(quote['latestTime'])
		+ '\n\tOpen Price: ' + str(quote['open'])
		+ '\n\tCurrent Price: ' + str(quote['latestPrice'])
		+ '\n\tHigh: ' + str(quote['high'])
		+ '\n\tLow: ' + str(quote['low'])
		+ '\n\tPrimary Exchange: ' + str(quote['primaryExchange'])
		+ '\n\tSector: ' + str(quote['sector'])
		+ '\n\tCalculation Price: ' + str(quote['calculationPrice'])
		+ '\n\tOpen Time: ' + str(quote['openTime'])
		+ '\n\tClose: ' + str(quote['close'])
		+ '\n\tClose Time: ' + str(quote['closeTime'])
		+ '\n\tLatest Source: ' + str(quote['latestSource'])
		+ '\n\tLatest Update: ' + str(quote['latestUpdate'])
		+ '\n\tLatest Volume: ' + str(quote['latestVolume'])
		+ '\n\tiex Real Time Price: ' + str(quote['iexRealtimePrice'])
		+ '\n\tiex Real Time Size: ' + str(quote['iexRealtimeSize'])
		+ '\n\tiex Last Updated: ' + str(quote['iexLastUpdated'])
		+ '\n\tDelayed Price: ' + str(quote['delayedPrice'])
		+ '\n\tDelayed Price Time: ' + str(quote['delayedPriceTime'])
		+ '\n\tExtended Price: ' + str(quote['extendedPrice'])
		+ '\n\tExtended Change: ' + str(quote['extendedChange'])
		+ '\n\tExtended Change Percent: ' + str(quote['extendedChangePercent'])
		+ '\n\tExtended Price time: ' + str(quote['extendedPriceTime'])
		+ '\n\tPrevious Close: ' + str(quote['previousClose'])
		+ '\n\tChange: ' + str(quote['change'])
		+ '\n\tChange Percent: ' + str(quote['changePercent'])
		+ '\n\tiex Market Percent: ' + str(quote['iexMarketPercent'])
		+ '\n\tiex Volume: ' + str(quote['iexVolume'])
		+ '\n\tAverage Total Volume: ' + str(quote['avgTotalVolume'])
		+ '\n\tiex Bid Price: ' + str(quote['iexBidPrice'])
		+ '\n\tiex Bid Size: ' + str(quote['iexBidSize'])
		+ '\n\tiex Ask Price: ' + str(quote['iexAskPrice'])
		+ '\n\tiex Ask Size: ' + str(quote['iexAskSize'])
		+ '\n\tMarket Cap: ' + str(quote['marketCap'])
		+ '\n\tPE Ration: ' + str(quote['peRatio'])
		+ '\n\t52 Week Hight: ' + str(quote['week52High'])
		+ '\n\t52 Week Low: ' + str(quote['week52Low'])
		+ '\n\tYear To Date Change: ' + str(quote['ytdChange']))

def getStocks(stock_list):
	print('Fetching stocks: ' + str(stock_list))
	
	stocks = Stock(stock_list)
	vec_stocks = list()

	for quote in stocks.get_quote().items():
		quote_data = quote[1]
		pretty_print(quote_data)
		vec_stocks.append(VecStock(name=quote_data.get('companyName'),
			symbol=quote_data.get('symbol'), 
			start_price=quote_data.get('open'),
			current_price=quote_data.get('latestPrice'),
			change=quote_data.get('change')))

	return vec_stocks
