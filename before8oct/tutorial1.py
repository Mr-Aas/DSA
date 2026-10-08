from jovian.pythondsa import evaluate_test_case

tests = [
    {"input": {"cards": [45, 43, 32, 23, 43], "query": 32}, "output": 2},
    {"input": {"cards": [], "query": 32}, "output": -1},
    {"input": {"cards": [45, 43, 23, 43], "query": 32}, "output": -1},
    {"input": {"cards": [45, 65, 32, 23, 43], "query": 43}, "output": 4},
]


def locate_card(cards, query):
    position = 0  # 1. Start at 0 for Python indexing

    # 2. Check position condition *before* accessing the list to avoid IndexError
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

    return -1  # Returns -1 if the loop finishes and the card wasn't found


for test in tests:
    evaluate_test_case(locate_card, test)
# 3. Correct way to pass the arguments from your test structure
# result = locate_card(tests[0]['input']['cards'], tests[0]['input']['query'])
# print(f"Found at position: {result}")  # Output: 1

# dix = {
#     "student1":{
#         "name":"aas mohd",
#         "class":12
#     },
#     "student2":{
#         "name":"anas mohd",
#         "class":12
#     },
#     "student3":{
#         "name":"aashif mohd",
#         "class":11
#     },
# }

# print(dix["student1"]["name"],dix["student3"]["class"])
