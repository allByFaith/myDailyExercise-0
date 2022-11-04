def concatenate(**kwargs):
  result = ""
  # Iterating over the Python kwargs dictionary
  for arg in kwargs.values():
    result += arg + ' '
  print (result)

concatenate(a="Real", b="Python", c="Is", d="Great", e="[1,2,3,4, 'example']")