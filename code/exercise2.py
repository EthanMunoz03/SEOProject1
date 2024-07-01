# WRITE YOUR CODE HERE
def move_to_bottom(dict, key):
  dict2 = dict.copy()
  if key in dict:
    val = dict2[key]
    print(val)
    del dict2[key]
    dict2[key] = val
    return dict2
  else:
    return 'The key is not in the dictionary'

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 4)
  print(example_dict)