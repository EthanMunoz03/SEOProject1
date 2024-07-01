# WRITE YOUR CODE HERE
def swap(dict1):
  for k in dict1:
    v = dict1.pop(k)
    if (isinstance(v, (list, dict))):
      return 'Cannot swap the keys and values for this dictionary'
    dict1[v] = k
  return dict1

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : [2, 3],
    4 : 'four',
    5 : 'five'
  }

  swapped = swap(example_dict)
  print(swapped)