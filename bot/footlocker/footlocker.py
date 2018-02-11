import requests
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





    def __init__(self):
        print("FootlockerShop Initialized")