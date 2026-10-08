tests = [
    {"input": {"cards": [45, 43, 32, 23, 43], "query": 32}, "output": 2},
    {"input": {"cards": [], "query": 32}, "output": -1},
    {"input": {"cards": [45, 43, 23, 43], "query": 32}, "output": -1},
    {"input": {"cards": [45, 65, 32, 23, 43], "query": 43}, "output": 4},
]


def locate_card(cards, query):
    # 1. Pair each card with its original index: [(45, 0), (43, 1), (32, 2), ...]
    indexed_cards = [(card, index) for index, card in enumerate(cards)]
    
    # 2. Sort the pairs by value (Python sorts by the first element of each tuple)
    indexed_cards.sort(key=lambda x: x[0])
    
    # 3. Binary Search on the sorted pairs
    low, high = 0, len(indexed_cards) - 1
    
    while low <= high:
        mid = (low + high) // 2
        card_value, original_index = indexed_cards[mid]
        
        if card_value == query:
            return original_index  # Return the original index, not mid!
        elif card_value < query:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# print(5.4//2)
for  test in tests:
    print(locate_card(test['input']['cards'],test['input']['query']))
    # print(locate_card(test[]))