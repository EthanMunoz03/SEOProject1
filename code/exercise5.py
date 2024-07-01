# WRITE YOUR CODE HERE
import json

def compare(file1, file2):
  with open(file1) as file:
    info1 = json.load(file)

  with open(file2) as file:
    info2 = json.load(file)
  
  if  info1 == info2:
    return 'The dictionaries are equal'

  elif len(info1) > len(info2):
    return 'Dictionary 1 is longer than dictionary 2'

  elif len(info1) < len(info2):
    return 'Dictionary 2 is longer than dictionary 1'

  else:
    return 'Dictionary 1 and dictionary 2 have the same length'


# test code below
if __name__ == "__main__":
  import sys
  
  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))