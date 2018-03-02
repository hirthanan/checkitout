# requests library used to create api requests
import requests

# selenium webdriver used to retrieve dynamic data from page source
from selenium import webdriver

# beatifulsoup used to parse html
from bs4 import BeautifulSoup as bs


class FootlockerShop:

    def __init__(self):
        print("FootlockerShop Initialized")
        print("While running")
        self.browser = None
        self.shoeSize = None


    '''URL only needs a sku number for product of interest
       which can be retrieved from html markup on footlockers newly released calendar'''
    def genUrl(self, sku, model):
        url = "http://www.footlocker.ca/en-CA/product/model:" + str(model) + "/sku:" + str(sku);
        return url

    ''' Using regex, finds the requestKey in html '''
    def getRequestKey(self, soup):
        keys = soup.find_all("input",attrs={"id": "requestKey"})

        # check if keys list is empty
        if keys:
            reqKey = keys[0]["value"]
        else:
            '''

            THIS IS WHERE THE TIMELY REQUESTS TO PREORDER ITEMS WILL BE MADE

            '''
            raise Exception('The item you have chosen has not been released yet! Try again later.')

        return reqKey

    ''' returns chosen items associated properties '''
    def getItem(self, items):
        print("Verify the item number that you were interested in automagically checking")
        itemArr = list(items.keys())
        for idx, item in enumerate(itemArr):
            print(str(idx+1) + ". " + item)
        num = input("# => ")
        verified_name = itemArr[num-1]

        print("Verify the color of the item that you were interested in automagically checking")
        colorArr = items[verified_name]['color']
        for idx, color in enumerate(colorArr):
            print(str(idx+1) + ". " + color)
        num = input("# => ")
        print("What is your Shoe Size? (i.e 09.0)")
        self.shoeSize = input("# => ")
        verified_sku = items[verified_name]['sku'][num-1]
        verified_model = items[verified_name]['model_num'][num-1]

        props = {'sku':verified_sku, 'model_num':verified_model}

        return props



    def getReleaseItems(self, soup, item):
        items = {} # each item will be formatted, {'name': {'sku':[vals], 'color':[vals]}}

        potential_items = soup.find_all('div', title=lambda x: x and item in x)

        ''' Since items can have the same name but different colors,
        we need to keep track of the different types of items '''
        for item in potential_items:
            productName = item.findAll(attrs={'class' : 'productName'})
            item_name = str(productName[0].contents[0].strip())

            item_sku = str(item["data-skunumber"])
            item_model = str(item["data-modelnumber"])

            colorway = item.findAll(attrs={'class' : 'colorway'})
            item_color = str(colorway[0].contents[0].strip())

            if item_name not in items:
                items[item_name] = {'sku':[item_sku], 'color':[item_color], 'model_num':[item_model]}
            else:
                items[item_name]['sku'].append(item_sku)
                items[item_name]['color'].append(item_color)
                items[item_name]['model_num'].append(item_model)

        return items

    ''' given web url, return page source html '''
    def soupify(self, url):
        self.browser.get(url)
        html = self.browser.page_source
        soup = bs(html, 'lxml')

        return soup


    ''' Looks through release calendar of all items and
    finds the exact SKU (id) number of your inputted item '''
    def releaseCalendar(self):
        newly_released_url = "http://www.footlocker.ca/en-CA/releasecalendarca"

        print("Getting details of shoe listings")
        soup = self.soupify(newly_released_url)

        items = self.getReleaseItems(soup, 'Jordan')
        item = self.getItem(items)

        return item

    def addCart(self, item):
        addToCartUrl = 'http://www.footlocker.ca/catalog/miniAddToCart.cfm?secure=0&'
        sku = item['sku']
        model = item['model_num']
        productUrl = self.genUrl(sku, model)

        soup = self.soupify(productUrl)
        requestKey = self.getRequestKey(soup)

        headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Host': 'www.footlocker.ca',
                    'Referer': productUrl,
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'http://www.footlocker.ca'
                }

        payload = {
            'coreMetricsCategory': 'blank',
            'fulfillmentType': 'SHIP_FROM_STORE',
            'inlineAddToCart': '0,1',
            'qty': '1',
            'requestKey': requestKey,
            'size': '06.5',
            'sku': sku,
            'storeCostOfGoods': '0.00',
            'storeNumber': '00000',
            'the_model_nbr': model
        }

        cookie = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}

        # payload = {
        #     'coreMetricsCategory': 'blank',
        #     'fulfillmentType': 'SHIP_TO_HOME',
        #     'inlineAddToCart': '0,1',
        #     'qty': '1',
        #     'rdo_deliveryMethod': 'shiptohome',
        #     'requestKey': requestKey,
        #     'size': '06.5',
        #     'sku': sku,
        #     'storeCostOfGoods': '0.00',
        #     'storeNumber': '00000',
        #     'the_model_nbr': model
        # }

        # headers = {
        #     'Accept': '*/*',
        #     'Origin': 'http://www.footlocker.ca',
        #     'X-Requested-With': 'XMLHttpRequest',
        #     'Referer': productUrl,
        #     'Accept-Encoding': 'gzip, deflate',
        # }

        session = requests.Session()

        res = session.post(addToCartUrl, headers=headers, data=payload)

        print "status_code " + str(res.status_code)
        print "payload " + str(payload)
        print "headers " + str(headers)

        print res.text
        if res.status_code == 200:
            return True
        return False


    def main(self):

        try:
            self.browser = webdriver.Firefox()

            item = self.releaseCalendar()
            success = self.addCart(item)

            if success:
                print ("Successfully added your item to your Cart")
            else:
                print ("Failed to add your item to your Cart")

        except Exception, e:
            print("ERROR: " + str(e))

        # self.browser.quit()




