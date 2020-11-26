import requests
from bs4 import BeautifulSoup as bs

class AdidasShop:

    def generateUrl(self):

        #7   Sample Adidas Shoe URL: http://www.adidas.ca/en/mens-eqt-cushion-adv-shoes/AC8774_590.html?forceSelSize=AC8774_590
        #8.5 Sample Adidas Shoe URL: http://www.adidas.ca/en/mens-eqt-cushion-adv-shoes/AC8774_620.html?forceSelSize=AC8774_620
        #12  Sample Adidas Shoe URL: http://www.adidas.ca/en/mens-eqt-cushion-adv-shoes/AC8774_690.html?forceSelSize=AC8774_690
        #7   Sample Adidas Shoe URL: http://www.adidas.ca/en/mens-eqt-cushion-adv-shoes/CQ2374_590.html?forceSelSize=CQ2374_590
        #7   Sample Adidas Shoe URL: http://www.adidas.ca/en/mens-eqt-support-ultra-primeknit-king-push-shoes/DB0181_590.html?forceSelSize=DB0181_590

        baseUrl = "http://www.adidas.ca/en/"
        shoe_type = input("What is the model of the shoe you are purchasing?")
        shoe_size = eval(input("What is the size?"))


    def main():
        print("done")

    def __init__(self):
        print("AdidasShop initialized")


