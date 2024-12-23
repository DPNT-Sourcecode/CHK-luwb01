from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus, 
             prices = {'A': 50,
                        'B': 30,
                        'C': 20,
                        'D': 15,
                        'E': 40,
                        'F': 10},
            specials = {'A': [(3, 130), (5, 200)],
                        'B': (2, 45)},
            specials_combo = [(2, 'E', 1, 'B'), (2, 'F', 1, 'F')]):

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

    for (q_item1, item1, free_q, free_item) in specials_combo:
        if item1 in sku_count_dict and free_item in sku_count_dict:
            num_combo = sku_count_dict[item1] // q_item1
            free_items = min(num_combo * free_q, sku_count_dict[free_item])
            sku_count_dict[free_item] = max(0, sku_count_dict[free_item] - free_items)

    sum = 0
    for k, v in sku_count_dict.items():
        if k in specials and isinstance(specials[k], list):
            best_price = float('inf')
            remaining = v

            deals = specials[k]

            biggest_deal = max(deal[0] for deal in deals)

            for first_deal_cnt in range(v // biggest_deal + 1):
                curr_price = 0
                remaining = v - (first_deal_cnt * deals[-1][0])
                curr_price += first_deal_cnt * deals[-1][1]

                for q, p in deals[:-1]:
                    deal_cnt = remaining // q
                    remaining = remaining % q
                    curr_price += deal_cnt * p

                curr_price += remaining * prices[k]
                best_price = min(best_price, curr_price)
            
            sum += best_price

        elif k in specials:
            q, p = specials[k]

            num_deals = v // q
            remaining = v % q

            sum += (num_deals * p) + (remaining * prices[k])
        else:
            sum += v * prices[k]

    return int(sum)


