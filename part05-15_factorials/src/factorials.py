# Write your solution here

def factorials(n: int):
  fact_ = {}
  for i in range(1,n+1):
    temp = 1
    for j in range(1,i+1):
      temp *= j
    fact_[i] = temp
  return fact_
