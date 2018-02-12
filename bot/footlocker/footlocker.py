from selenium import webdriver
from bs4 import BeautifulSoup as bs

class FootlockerShop:

    '''URL only needs a sku number for product of interest
       which can be retrieved from html markup on footlockers newly released calendar'''
    def genUrl(self, sku):
        url = "http://www.footlocker.ca/en-CA/product/sku:" + str(sku)
        return url

    def checkout(self, sku):
        print("sku = " + str(sku))



    def main(self):
        newly_released_url = "http://www.footlocker.ca/en-CA/releasecalendarca"
        # headers = requests.utils.default_headers()
        # headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})

        browser = webdriver.Firefox()

        browser.get(newly_released_url)

        html = browser.page_source

        soup = bs(html, "lxml")

        print soup

        # req = requests.get(newly_released_url, headers=headers)

        # req_data = req.text
        # print req_data

        return





    def __init__(self):
        print("FootlockerShop Initialized")
        print("While running")