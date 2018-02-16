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


    ''' returns chosen items associated sku-number '''
    def chooseItem(self, items):
        print("Verify the item number that you were interested in automagically buying")
        itemArr = list(items.keys())
        for idx, item in enumerate(itemArr):
            print(str(idx+1) + ". " + item)
        num = input("# => ")
        verified_name = itemArr[num-1]

        print("Verify the color of the item that you were interested in automagically buying")
        colorArr = items[verified_name]['color']
        for idx, color in enumerate(colorArr):
            print(str(idx+1) + ". " + color)
        num = input("# => ")
        verified_sku = items[verified_name]['sku'][num-1]

        print verified_sku
        return verified_sku



    def getItems(self, soup, item):
        items = {} # each item will be formatted, {'name': {'sku':[vals], 'color':[vals]}}

        potential_items = soup.find_all('div', title=lambda x: x and item in x)

        ''' Since items can have the same name but different colors,
        we need to keep track of the different types of items '''
        for item in potential_items:
            productName = item.findAll(attrs={'class' : 'productName'})
            item_name = str(productName[0].contents[0].strip())

            item_sku = int(item["data-skunumber"])

            colorway = item.findAll(attrs={'class' : 'colorway'})
            item_color = str(colorway[0].contents[0].strip())

            if item_name not in items:
                items[item_name] = {'sku':[item_sku], 'color':[item_color]}
            else:
                items[item_name]['sku'].append(item_sku)
                items[item_name]['color'].append(item_color)

        return items



    def releaseCalendar(self):
        newly_released_url = "http://www.footlocker.ca/en-CA/releasecalendarca"

        print("Getting details of shoe listings")
        try:
            browser = webdriver.Firefox()
            browser.get(newly_released_url)

            html = browser.page_source
            soup = bs(html, "lxml")

            items = self.getItems(soup, 'Jordan')
            # item = self.chooseItem(items)
        except Exception, e:
            print("ERROR: " + str(e))

        browser.quit()

        return soup


    def main(self):
        # headers = requests.utils.default_headers()
        # headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})

        releases = self.releaseCalendar()


