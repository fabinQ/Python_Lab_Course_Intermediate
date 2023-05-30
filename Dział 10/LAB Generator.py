def Combinations (products, promotions, customers):
        # print(products,promotions,customers)
        for prod in products:
            # print(prod)
            for prom in promotions:
                # print(prom)
                for cust in customers:
                    # print(cust)
                    # item_to_return = "{} - {} -{}".format(products[prod],
                    #                                       promotions[prom],
                    #                                       customers[cust])
                    item_to_return = "{} - {} -{}".format(prod, prom, cust)
                    yield item_to_return




products = ["Product {}".format(i) for i in range(1, 4)]
# products = [range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
# promotions = [range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
# customers = [range(1, 5)]
combinations = Combinations(products, promotions, customers)

for c in combinations:
    print(c)

# while True:
#     try:
#         print(next(combinations))
#     except StopIteration:
#         print('stop')
#         break
#     except Exception:
#         print('error')
#         break
