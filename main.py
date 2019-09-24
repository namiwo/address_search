import requests


def main():
    # 入力
    # 1600024 ⇒ 東京都新宿区西新宿
    zipcode = "1600023"
    url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    # 計算
    # リクエストを送る⇒受け取ってパース（解析）⇒フォーマット（仮）
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
