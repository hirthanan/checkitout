from shop import Shop

def main():
    s = Shop()
    chosenStore = s.getStore()

    chosenStore.main()


if __name__ == '__main__':
    main()
