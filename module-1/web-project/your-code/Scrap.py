import requests
import pandas as pd
import json
from pandas.io.json import json_normalize 

ciudad ='Madrid'
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&APPID=30c0b644a0a2950cbb356c1cb2747f01'


response = requests.get(url)
results = response.json()
weather_keys = results.keys()

normalized_data = json_normalize(results)
normalized_data.to_csv('pepe.csv', sep=",")
df = pd.read_csv('pepe.csv')

print(df.head)
# df = pd.DataFrame(results['weather'])
# df.head(10)





