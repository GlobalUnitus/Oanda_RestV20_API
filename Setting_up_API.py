
import pandas as pd
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
import configparser

### Account Details ###

config = configparser.ConfigParser()
config.read('../config/config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)
r = accounts.AccountDetails(accountID)

client.request(r)
print(r.response)
print(pd.Series(r.response['account']))

### Account Lists ###

r = accounts.AccountList()
client.request(r)
print(r.response)

### Account Summary ###

r = accounts.AccountSummary(accountID)
client.request(r)
print(r.response)
pd.Series(r.response['account'])

### Account Instruments ###

params = {"instruments": "EUR_USD"}
r = accounts.AccountInstruments(accountID=accountID, params=params)
client.request(r)

print(pd.DataFrame(r.response['instruments']))
