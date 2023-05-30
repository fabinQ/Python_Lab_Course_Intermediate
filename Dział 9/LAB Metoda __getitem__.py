class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        print('products ', len(self.products))
        print('promotions', len(self.promotions))
        print('customers', len(self.customers))
        print('*'*10)


    def __getitem__(self, item):
        if item >= (len(self.products) * len(self.promotions) * len(self.customers)):
            raise StopIteration()
        else:
            pos_products = item//(len(self.promotions) * len(self.customers))
            item = item%(len(self.promotions) * len(self.customers))

            pos_promotions = item//len(self.customers)
            item = item%len(self.customers)

            pos_customers = item

        item_to_return = "Products {} - Promotions {} - Customers {}".format(pos_products, pos_promotions, pos_customers)

        return item_to_return


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)
b=0
for i in combinations:
    print(b,' :', i)
    b+=1


it = iter(combinations)
for i in combinations:
    print(next(it))