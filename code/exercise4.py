# WRITE YOUR CODE HERE
def is_nested(d):
  for k in d:
    v = d[k]
    if isinstance(v, (list, tuple, dict)):
      return True
  
  return False

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : [4, 5]
  }

  print(is_nested(example_dict))