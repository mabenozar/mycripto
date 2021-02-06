import requests
import json


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '04438c40-b1df-4c11-ab70-4fb3e0a3b357' 
}


def getApi(selectFrom, selectTo, quantityFrom):
  try:
      response = requests.get(f'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={quantityFrom}&symbol={selectFrom}&convert={selectTo}', headers=headers)
      data = response.json()
      
      return data
  except:
      print('Fetch failed')

