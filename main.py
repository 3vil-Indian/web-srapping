import requests
from requests_html import HTMLSession
from requests_html import HTML
url = "https://www.myntra.com/shirts/louis-philippe/louis-philippe-men-classic-pure-cotton-striped-formal-shirt/20646846/buy"

response = requests.get(url)
if response.status_code == 200:
    html = HTML(html=response.text)
    print("Number of elements in html:", len(html))
    price_element = html.find('.pdp-price')
    print("Number of elements with class 'pdp-price':", len(price_element))
    if price_element:
        price = price_element[0].text
        print("Price:", price)
    else:
        print("Price element not found.")
else:
    print("Failed to get response from url")
