#Every Three Numbers

def every_three_nums(start):
  num_between = [*range(start, 101, 3)]
  return num_between

print(every_three_nums(81))


#Remove Middle

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1]
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))