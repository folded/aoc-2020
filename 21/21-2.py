import sys
import re
import collections
import functools
import operator

def Intersection(sets):
  return functools.reduce(operator.__and__, sets)

class AllergenMap:
  def __init__(self):
    self.all_ingredients = collections.Counter()
    self.all_allergens = set()
    self.allergen_ingredients = collections.defaultdict(list)
    self.allergen_map = {}

  def AddItem(self, ingredients, allergens):
    self.all_ingredients.update(ingredients)
    self.all_allergens.update(allergens)
    for allergen in allergens:
      self.allergen_ingredients[allergen].append(ingredients)

  def Assign(self, allergen, ingredient):
    am = AllergenMap()
    am.all_ingredients = self.all_ingredients.copy()
    am.all_ingredients.pop(ingredient)
    am.all_allergens = self.all_allergens - {allergen}
    am.allergen_ingredients = {
      a: [ i - {ingredient} for i in il ]
      for a, il in self.allergen_ingredients.items()
      if a != allergen
    }
    am.allergen_map = self.allergen_map.copy()
    am.allergen_map[allergen] = ingredient
    return am

  def PossibleAssignments(self):
    return {
      allergen: Intersection(ingredient_lists)
      for allergen, ingredient_lists in self.allergen_ingredients.items()
    }

  def Solve(self):
    possible_assignments = sorted(self.PossibleAssignments().items(), key = lambda x: len(x[1]))
    if not len(possible_assignments):
      yield self
    else:
      allergen, ingredients = possible_assignments[0]
      for ingredient in ingredients:
        yield from self.Assign(allergen, ingredient).Solve()

allergen_map = AllergenMap()
for line in sys.stdin:
  m = re.match(r'(.*) \(contains (.*)\)', line)
  ingredients = set(m.group(1).split())
  allergens = set(m.group(2).split(', '))
  allergen_map.AddItem(ingredients, allergens)

solutions = list(allergen_map.Solve())
assert len(solutions) == 1
solution = solutions[0]
print(','.join([ x[1] for x in sorted(solution.allergen_map.items()) ]))
