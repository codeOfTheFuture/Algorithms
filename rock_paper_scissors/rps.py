#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

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