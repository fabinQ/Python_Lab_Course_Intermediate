import time
import sys
start = time.time()
class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions= promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(products):
            self.current_product = 0
            raise StopIteration ("Iteration is stop.")

        item_to_return = "{} - {} - {}".format(self.products[self.current_product], self.promotions[self.current_promotion], self.customers[self.current_customer])
        self.current_customer += 1
        return item_to_return

    def __iter__(self):
        return self


products = ["Product {}".format(i) for i in range(1, 5)]
# print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 10)]
# print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 20)]
# print(customers)

combinations = Combinations(products, promotions, customers)

print('****')
# print(combinations)
for c in combinations:
    print(c)
    pass

    # here an analysis will be done - currently, just nothing happens :)

print('****')
# time.sleep(1)

print('****')
stop = time.time()
print("Fast and furious - {} sec".format(stop-start))
print('RAM - {}KB'.format(sys.getsizeof(combinations)/100))