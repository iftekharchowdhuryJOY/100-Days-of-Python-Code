class Store:

    def __init__(self, name):
        # global variable

        self.name = name
        self.items = []



    def add_item(self, name, price):

        item_dict = {'name': name, 'price': price}
        print(item_dict)
        self.items.append(item_dict)
        return self.items

    def stock_price(self):

        total = 0
        for item in self.items:
            total = total +item['price']
            return total
        return sum([item['price'] for item in self.items])



store = Store("joy")
print(store.stock_price())
print(store.add_item("rice", 100))

