# Write your solution here

# my approach
# loop through 0 - n -> create a list of 0-9, 11-19, can  all 10*n -> convert the n into string, split and add to list, then loop through that list and convert each element in list to int, now we have a list having indivisual digit -> fro two digit number that lies outside the list, add "ty" to first digit then dash and name for last digit (looping through 0-9 list would work because they all range between 0-9)


def dict_of_numbers():

  dict_ = {}

  single_digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
  ]

  teens = [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
  ] 

  tens = [
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
  ]

  for num in range(0,100):

    if num < 10:
      dict_[num] = single_digits[num]
    elif 11 <= num <= 19:
      dict_[num] = teens[num-11]
    elif num % 10 == 0:
      dict_[num] = tens[num//10 - 1]
    else:
      dict_[num] = tens[num//10-1] + "-" + single_digits[num%10]

  return dict_



if __name__ == "__main__":
  numbers = dict_of_numbers()
  print(numbers[2])
  print(numbers[11])
  print(numbers[45])
  print(numbers[99])
  print(numbers[20])
  print(numbers[0])
    
