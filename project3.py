import random

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3 
MAX_OPERAND = 12 

def generate_problem():
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)

  expr = str(left) + " " + right + " " + str(right)
  print()
  return expr

generate_problem