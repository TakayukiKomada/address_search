import requests

postal_code = "0287111"

response = requests.get(
    f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
)

dic = response.json()
pref_name = dic['results'][0]['address1']
city_name = dic['results'][0]['address2']
town_name = dic['results'][0]['address3']
print(pref_name+city_name+town_name)
