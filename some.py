def front_back(str):
  first = str[0]
  middle = str[1:-1]
  last = [-1]
  return last + middle + first
  
front_back("hello")