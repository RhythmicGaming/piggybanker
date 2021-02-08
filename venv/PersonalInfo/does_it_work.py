#must be run once to verify login and create a personal app id
#this will trigger 2 factor at least the first time, more if enabled on your account
import robin_stocks
from BasePersonalInfo.MyInfo import usr, pwd

login = robin_stocks.login(usr, pwd)
my_stocks = robin_stocks.build_holdings()
for key,value in my_stocks.items():
     print(key,value)
