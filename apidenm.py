import requests


rsp1=requests.get("https://imdb-api.com/en/API/SearchMovie/k_s526x1tl/godfather")
snc1=rsp1.json()
print(snc1['results'][0]['id'])

rsp=requests.get("https://imdb-api.com/en/API/FullCast/k_s526x1tl/"+ snc1['results'][0]['id'])


snc=rsp.json()
print(snc)
print(snc['directors']['items'][0]['name'])


