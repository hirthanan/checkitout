from adidas.adidas import AdidasShop
from nba.nba import NbaShop


class Shop:

    def getStore(self):
        return self.__store

    ''' returns store instance using dependency injection'''
    def pickStore(self):
        shops = {'Adidas':AdidasShop , 'NBA': NbaShop, 'Footlocker': FootlockerShop}
        store = raw_input("Which store do you want to buy from? [Adidas, NBA] \n")

        if store not in shops:
            print("Sorry, that's an invalid store, choose one from the following options")
            return self.pickStore()
        else:
            return shops[store]


    def __init__(self):
        self.__store = self.pickStore()
