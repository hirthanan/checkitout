from selenium import webdriver
from bs4 import BeautifulSoup as bs

class FootlockerShop:

    def __init__(self):
        print("FootlockerShop Initialized")
        print("While running")


    '''URL only needs a sku number for product of interest
       which can be retrieved from html markup on footlockers newly released calendar'''
    def genUrl(self, sku):
        url = "http://www.footlocker.ca/en-CA/product/sku:" + str(sku)
        return url


    def checkout(self, sku):
        print("sku = " + str(sku))


    def getItem(self, soup, item):
        items = {}
        potential_items = soup.find_all('div', title=lambda x: x and item in x)
        for item in potential_items:
            print(item)
        # print potential_items


    def releaseCalendar(self):
        newly_released_url = "http://www.footlocker.ca/en-CA/releasecalendarca"

        print("Getting details of shoe listings")
        try:
            browser = webdriver.Firefox()
            browser.get(newly_released_url)

            html = browser.page_source
            soup = bs(html, "lxml")

            self.getItem(soup, 'Jordan Retro 1 High', "ASdas")
        except Exception, e:
            print("ERROR: " + str(e))

        browser.quit()


        # Clean up bs4 html markup data
        # print soup.prettify()


        return soup


    def main(self):
        # headers = requests.utils.default_headers()
        # headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})

        releases = self.releaseCalendar()


