from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus, 
            prices = {'A': 50,
                    'B': 30,
                    'C': 20,
                    'D': 15,
                    'E': 40,
                    'F': 10,
                    'G': 20,
                    'H': 10,
                    'I': 35,
                    'J': 60,
                    'K': 70,
                    'L': 90,
                    'M': 15,
                    'N': 40,
                    'O': 10,
                    'P': 50,
                    'Q': 30,
                    'R': 50,
                    'S': 20,
                    'T': 20,
                    'U': 40,
                    'V': 50,
                    'W': 20,
                    'X': 17,
                    'Y': 20,
                    'Z': 21},
            specials = {'A': [(3, 130), (5, 200)],
                        'B': (2, 45),
                        'H': [(5, 45), (10, 80)],
                        'K': (2, 120),
                        'P': (5, 200),
                        'Q': (3, 80),
                        'V': [(2, 90), (3, 130)]},
            specials_combo = [(2, 'E', 1, 'B'), 
                              (2, 'F', 1, 'F'),
                              (3, 'N', 1, 'M'),
                              (3, 'R', 1, 'Q'),
                              (3, 'U', 1, 'U')],
            group_offers = [(3, ['S', 'T', 'X', 'Y', 'Z'], 45)]):

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
        if item1 in sku_count_dict:
            if item1 == free_item:
                if sku_count_dict[item1] >= q_item1 + free_q:
                    num_combo = sku_count_dict[item1] // (q_item1 + free_q)
                    sku_count_dict[item1] -= num_combo * free_q
            else:
                if item1 in sku_count_dict and free_item in sku_count_dict:
                    num_combo = sku_count_dict[item1] // q_item1
                    free_items = min(num_combo * free_q, sku_count_dict[free_item])
                    sku_count_dict[free_item] = max(0, sku_count_dict[free_item] - free_items)

    total = 0
    for qt, item_group, offer_price in group_offers:
        group_counts = {item: sku_count_dict.get(item, 0) for item in item_group}
        total_group_items = sum(group_counts.values())
        
        num_offers = total_group_items // qt
        
        if num_offers > 0:
            remaining_items = total_group_items % qt

            remove_items = num_offers * qt

            sorted_items = sorted([(item, cnt) for item, cnt in group_counts.items()], key=lambda x: prices[x[0]], reverse=True)

            for item, cnt in sorted_items:
                if remove_items > 0 and item in sku_count_dict:
                    used = min(cnt, remove_items)
                    sku_count_dict[item] -= used
                    remove_items -= used
        
        total += num_offers * offer_price

    for k, v in sku_count_dict.items():
        if v <= 0:
            continue

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
            
            total += best_price

        elif k in specials:
            q, p = specials[k]

            num_deals = v // q
            remaining = v % q

            total += (num_deals * p) + (remaining * prices[k])
        else:
            total += v * prices[k]

    return int(total)



