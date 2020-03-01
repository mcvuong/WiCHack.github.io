import requests
import json

# get category level of info
api_token = "c455d00cb0f64e238a5282d75921f27e"
api_url_base = "https://api.wegmans.io"

url = "https://api.wegmans.io/products/categories?api-version=2018-10-18&Subscription-Key=c455d00cb0f64e238a5282d75921f27e"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data = payload)
json_data = json.loads(response.text)

categories_hrefs = []
for k, v in json_data.items():
    for j in v:
        if 'id' in j:
            categories_hrefs.append((j["_links"][0]['href']))
print(categories_hrefs)


# get bakery level of info
for i in categories_hrefs:
    url = api_url_base + i + "&Subscription-key=" + api_token
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    json_data = json.loads(response.text)

    bakery_level = []
    for i in json_data["categories"]:
        bakery_level.append(i["_links"][0]["href"])
    
    # get bakery-bread level of info
    for i in bakery_level:
        url = api_url_base + i + "&Subscription-key=" + api_token
        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)
        json_data = json.loads(response.text)

        # get sku and information on each item
        bakery_bread_level_sku = []
        bakery_bread_level_info = []
        for i in json_data["products"]:
            bakery_bread_level_sku.append(i["sku"])
            bakery_bread_level_info.append([i["name"], api_url_base + i["_links"][0]["href"]+ "&Subscription-key=" + api_token])

        # get price of each item based on unique SKU
        # for i in bakery_bread_level_info:
        #     print(i)

        # for i in bakery_bread_level_sku:
        #     url = api_url_base + "/products/" + str(i) + "/prices/68?api-version=2018-10-18&subscription-key=" + api_token
        #     payload = {}
        #     headers= {}
        #     response = requests.request("GET", url, headers=headers, data = payload)
        #     json_data = json.loads(response.text)

        #     print(json_data)
