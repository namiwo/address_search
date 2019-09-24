import requests


def main():
    # 入力
    zipcode = input("郵便番号を入力してください > ")
    url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

    # 計算
    response = requests.get(url)

    address = response.json()["results"][0]
    都道府県 = address["address1"]
    市区町村 = address["address2"]
    町域 = address["address3"]

    result = f"{都道府県}{市区町村}{町域}"

    # 出力

    print(result)


if __name__ == '__main__':
    main()
