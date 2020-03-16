#!/usr/bin/python

import sys

# [1 0 0 0 0 0 0 0 0 0]

def making_change(amount, denominations, cache=None):
  if not cache:
    cache = [0 for i in range(0, amount + 1)]
    cache[0] = 1

  if amount == 0 or amount == 1:
    return 1

  if len(denominations) and amount >= denominations[0]:
    coin = denominations[0]
    for higher_amount in range(coin, amount + 1):
      result = higher_amount - coin

      if cache[result]:
        cache[higher_amount] += cache[result]
      
    making_change(amount, denominations[1:], cache)

    # print(denominations[1:])

    # print(cache)
    return cache[amount]

  else:
    # print(f'cache result {cache[amount]}')
    return




# amount = 10
# denominations = [1, 5, 10, 25, 50]
# print(making_change(amount, denominations))

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")