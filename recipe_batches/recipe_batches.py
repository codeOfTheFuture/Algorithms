#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  total_batch = None

  for i in recipe:
    if i not in ingredients:
      return 0
    else:
      if ingredients[i] < recipe[i]:
        total_batch = 0
      elif ingredients[i] == recipe[i]:
        total_batch = 1
      else:
        batches = ingredients[i] // recipe[i]
        if not total_batch:
          total_batch = batches
        else:
          if batches < total_batch:
            total_batch = batches
  return total_batch    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))