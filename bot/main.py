from shop import Shop

def main():
    shop = Shop()
    chosenStore = shop.getStore()
    chosenStore.main()


if __name__ == '__main__':
    main()
