from collections import Counter


def make_sells(shoe_sizes, customers):
    payments = 0

    for size, value in customers:
        if size in shoe_sizes.keys():
            shoe_sizes[size] -= 1
            payments += value

            shoe_sizes.pop(size) if shoe_sizes[size] == 0 else None

    return payments


if __name__ == "__main__":
    n_shoes = int(input())
    available_shoe_sizes = Counter([int(x) for x in input().split(" ")])
    n_customers = int(input())
    customers = []
    for _ in range(n_customers):
        size, value = [int(x) for x in input().split(" ")]
        customers.append((size, value))

    print(make_sells(available_shoe_sizes, customers))

"""
TODO: input
10                      # number of items
2 3 4 5 6 8 7 6 5 18    # items 'models'
6                       # number of 'buyers'
6 55
6 45
6 55
4 40
18 60
10 50                   # 'model', 'cost' per buyer

TODO: input             # sum of buyers value input that matches with available models quantities
200
"""
