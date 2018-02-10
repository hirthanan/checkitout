
class Shop:

    def pickStore(self):
        shops = {'Nike', 'Adidas', 'NBA'}
        store = raw_input("Which store do you want to buy from? [Nike, Adidas, NBA] \n")

        if store not in shops:
            print("Sorry, that's an invalid store, choose one from the following options")
            return self.pickStore()
        else:
            return store


    def __init__(self):
        self.store = self.pickStore()
