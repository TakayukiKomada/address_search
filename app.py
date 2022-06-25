from socket import if_nameindex, if_nametoindex
import requests

postal_code = "0287111"

response = requests.get(
    f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
)

dic = response.json()
dic2 = dic['results'][0]
pref_name = dic2['address1']
city_name = dic2['address2']
town_name = dic2['address3']
city = pref_name+city_name+town_name
print(city)
