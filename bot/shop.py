from adidas.adidas import AdidasShop
from nba.nba import NbaShop
from footlocker.footlocker import FootlockerShop


class Shop:

    def getStore(self):
        return self.__store

    ''' returns store instance using dependency injection'''
    def pickStore(self):
        shops = {'Adidas':AdidasShop , 'NBA': NbaShop, 'Footlocker': FootlockerShop}
        store = input("Which store do you want to buy from? [Footlocker, Adidas, NBA] \n")

        if store not in shops:
            print("Sorry, that's an invalid store, choose one from the following options")
            return self.pickStore()
        else:
            store = shops[store]

            # create instance of store
            return store()


    def __init__(self):
        self.__store = self.pickStore()
