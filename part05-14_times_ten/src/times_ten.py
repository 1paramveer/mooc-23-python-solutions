# Write your solution here

def times_ten(start_index: int, end_index: int):
  dict_ = {}
  for i in range(start_index,end_index+1):
    dict_[i] = i*10
  return dict_
