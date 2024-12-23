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

    if not isinstance(skus, str) or not skus.isalpha():
        return -1
    
    if set(skus) != set(prices.keys()):
        return -1
    
    skus = skus.upper()

    skus_list = [sku for sku in skus]

    sku_count_dict = dict(Counter(skus_list))

    sum = 0
    for k, v in sku_count_dict.items():
        if k in specials:
            if v % specials[k][0] == 0:
                sum += (v / specials[k][0]) * specials[k][1]
            else:
                sum += prices[k]
        else:
            sum += prices[k]

    return int(sum)
