from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus, 
             prices = {'A': 50,
                        'B': 30,
                        'C': 20,
                        'D': 15,
                        'E': 40},
            specials = {'A': (3, 130),
                        'B': (2, 45)}):

    if skus == '':
        return 0

    if any(c.islower() for c in skus):
        return -1

    if not isinstance(skus, str) or not skus.isalpha():
        return -1
    
    for c in set(skus):
        if c not in set(prices.keys()):
            return -1

    skus_list = [sku for sku in skus]

    sku_count_dict = dict(Counter(skus_list))

    sum = 0
    for k, v in sku_count_dict.items():
        if k in specials:
            num_specials = v // specials[k][0]
            remainder = v % specials[k][0]
            sum += (num_specials * specials[k][1]) + (remainder * prices[k])
        else:
            sum += v * prices[k]

    return int(sum)

