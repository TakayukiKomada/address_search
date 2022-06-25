import requests

response = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111')
print(response)
print(response.text)