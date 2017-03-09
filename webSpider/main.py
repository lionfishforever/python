import requests

r = requests.get('http://ddragon.leagueoflegends.com/cdn/5.14.1/data/zh_CN/champion/Gangplank.json')

test = 'dd'+r.url
print(test)