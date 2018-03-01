import re
from selenium import webdriver
from bs4 import BeautifulSoup as bs


class FootlockerShop:

    def __init__(self):
        print("FootlockerShop Initialized")
        print("While running")
        self.request_key = None
        self.browser = None


    '''URL only needs a sku number for product of interest
       which can be retrieved from html markup on footlockers newly released calendar'''
    def genUrl(self, sku):
        url = "http://www.footlocker.ca/en-CA/product/sku:" + str(sku)
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

    ''' returns chosen items associated sku-number '''
    def getSku(self, items):
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

        return verified_sku



    def getReleaseItems(self, soup, item):
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
        sku = self.getSku(items)

        return sku

    def addCart(self, sku):
        addToCartUrl = 'http://www.footlocker.ca/catalog/addToCart'
        productUrl = self.genUrl(sku)

        soup = self.soupify(productUrl)
        requestKey = self.getRequestKey(soup)

        print requestKey


        # headers = requests.utils.default_headers()
        # headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})

        # payload = {
        #     "Host": "www.mywbsite.fr",
        #     "Connection": "keep-alive",
        #     "Content-Length": 129,
        #     "Origin": "https://www.mywbsite.fr",
        #     "X-Requested-With": "XMLHttpRequest",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        #     "Content-Type": "application/json",
        #     "Accept": "*/*",
        #     "Referer": "https://www.mywbsite.fr/data/mult.aspx",
        #     "Accept-Encoding": "gzip,deflate,sdch",
        #     "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
        #     "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        #     "Cookie": "ASP.NET_SessionId=j1r1b2a2v2w245; GSFV=FirstVisit=; GSRef=https://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CHgQFjAA&url=https://www.mywbsite.fr/&ei=FZq_T4abNcak0QWZ0vnWCg&usg=AFQjCNHq90dwj5RiEfr1Pw; HelpRotatorCookie=HelpLayerWasSeen=0; NSC_GSPOUGS!TTM=ffffffff09f4f58455e445a4a423660; GS=Site=frfr; __utma=1.219229010.1337956889.1337956889.1337958824.2; __utmb=1.1.10.1337958824; __utmc=1; __utmz=1.1337956889.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
        # }




    def main(self):

        try:
            self.browser = webdriver.Firefox()

            itemSku = self.releaseCalendar()
            success = self.addCart(itemSku)

            if success:
                print ("Successfully added your item to your Cart")
            else:
                print ("Failed to add your item to your Cart")

        except Exception, e:
            print("ERROR: " + str(e))

        self.browser.quit()




