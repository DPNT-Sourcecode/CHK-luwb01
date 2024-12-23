from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus, 
             prices = {'A': 50,
                            'B': 30,
                            'C': 20,
                            'D': 15},
            specials = {'A': (3, 130),
                        'B': (2, 45)}):

    skus_list = [sku for sku in skus]

    sku_count_dict = dict(Counter(skus_list))