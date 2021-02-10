import robin_stocks
from PersonalInfo.MyInfo import usr, pwd

def getHistList(ticker='LABP', interval='5minute', span='week'):
    login = robin_stocks.login(usr, pwd)

    list_prices = robin_stocks.stocks.get_stock_historicals(ticker, interval, span)

    return list_prices

def meanClosePrice(ticker='LABP', interval='5minute', span='week'):
    list_prices = getHistList(ticker, interval, span)
    total = 0
    #calculate overall average
    for i in list_prices:
        total += float(i['close_price'])

    Mean = total / len(list_prices)
    #Mean = average(Values);
    return Mean

def meanOpenPrice(ticker='LABP', interval='5minute', span='week'):
    list_prices = getHistList(ticker, interval, span)
    total = 0
    #calculate overall average
    for i in list_prices:
        total += float(i['open_price'])

    Mean = total / len(list_prices)
    #Mean = average(Values);
    return Mean

def findRatesOfChange(ticker='LABP', interval='5minute', span='week'):
    list_prices = getHistList(ticker, interval, span)
    change_list = []
    for i in list_prices:
        change = float(i['open_price']) - float(i['close_price'])
        change_list.append(change)
    return change_list

list_of_tickers = ['LABP','OGI','TSLA','GPRO', 'DOGE']

print(meanClosePrice())
print(meanOpenPrice())

for ticker in list_of_tickers:
    print(getHistList(ticker))
    print(f"{ticker} open {meanOpenPrice(ticker)}")
    print(f"{ticker} close {meanClosePrice(ticker)}")
    print(f"{ticker} rates {findRatesOfChange(ticker)}")

