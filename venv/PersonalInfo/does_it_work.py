#must be run once to verify login and create a personal app id
#this will trigger 2 factor at least the first time, more if enabled on your account
import robin_stocks
from PersonalInfo.MyInfo import usr, pwd

#login with your creds
login = robin_stocks.login(usr, pwd)
#dictionary of owned shares
my_stocks = robin_stocks.build_holdings()
for key,value in my_stocks.items():
     print(key,value)
#list of price info every 5m for a span='week'
list_prices = robin_stocks.stocks.get_stock_historicals('LABP',interval='5minute')
robin_stocks.stocks.get_latest_price('')
#setup for dictionary of change
change_dict = {}
counter = 0
for price in list_prices:
    counter += 1
    print(counter, price['open_price'], price['close_price'])
    print(price)
    change_dict.update({counter: (float(price['open_price']) - float(price['close_price'])) / float(price['open_price'])})
#rate of change per hour of LABP in a dictionary
print(change_dict)


