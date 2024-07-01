# WRITE YOUR CODE HERE
def find_key(dict, value):
  for k in dict:
    v = dict[k]
    if v == value:
      return k
  return -1

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, 'impale mat a')
  print(key)