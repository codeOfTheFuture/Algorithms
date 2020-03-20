#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  moves = ['rock', 'paper', 'scissors']
  result = []

  def helper(arr, move):
    for i in range(0, len(moves)):
      arr.append(moves[i])
      if move == n:
        result.append(arr.copy())
      else:
        helper(arr, move + 1)
      arr.pop()

  helper([], 1)

  return result
print(rock_paper_scissors(5))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')

    # total amount of permutations grow by 3 ^ n

    # ['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors']
    # ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors']
    # ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']


    # ['rock', 'rock', 'rock'],       ['rock', 'rock', 'paper'],            ['rock', 'rock', 'scissors']
    # ['rock', 'paper', 'rock'],      ['rock', 'paper', 'paper'],           ['rock', 'paper', 'scissors']
    # ['rock', 'scissors', 'rock'],    ['rock', 'scissors', 'paper'],      ['rock', 'scissors', 'scissors']
    # ['paper', 'rock', 'rock'],       ['paper', 'rock', 'paper'],          ['paper', 'rock', 'scissors']
    # ['paper', 'paper', 'rock'],      ['paper', 'paper', 'paper'],          ['paper', 'paper', 'scissors']
    # ['paper', 'scissors', 'rock'],    ['paper', 'scissors', 'paper'],      ['paper', 'scissors', 'scissors']
    # ['scissors', 'rock', 'rock'],     ['scissors', 'rock', 'paper'],       ['scissors', 'rock', 'scissors']
    # ['scissors', 'paper', 'rock'],    ['scissors', 'paper', 'paper'],      ['scissors', 'paper', 'scissors']
    # ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']


  #  [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

  # [['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'], ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'], ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'], ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'], ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper', 'paper', 'scissors'], ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'], ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'], ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']]

  # If n is 1
  # 3 total permutations
  # 1 rock 1 paper 1 scissors
  # 
  # If n is 2
  # 9 total permutations
       # 1 rock  1 paper      1 scissors 3 times
  # Then 3 rocks 3 papers and 3 scissors 1 time
  # 
  # If n is 3
  # 27 total permutations
       # 1 rock  1 paper      1 scissors 9 times
  # Then 3 rocks 3 papers and 3 scissors 3 times
  # Then 9 rocks 9 papers and 9 scissors 1 times
  # If n is 4
  # 81 total permutations
       # 1 rock  1 paper      1 scissors 27 times
  # Then 3 rocks 3 papers and 3 scissors 9 times
  # Then 9 rocks 9 papers and 9 scissors 3 times
  # Then 27 rocks 27 papers and 27 scissors 1 times

  #     rock paper scissors
  # rock + rock rock + paper rock + scissors

  # rock 