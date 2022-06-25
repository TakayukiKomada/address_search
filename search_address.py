import requests


def search_address(postal_code):
    response = requests.get(
        f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
    )

    dic = response.json()  # パース

    pref_name = dic["results"][0]["address1"]
    city_name = dic["results"][0]["address2"]
    town_name = dic["results"][0]["address3"]

    address = f"{pref_name}{city_name}{town_name}"
    return address


def main():
    postal_code = "0287111"
    address = search_address(postal_code)
    assert "岩手県  八幡平市  大更" == address
