#Every Three Numbers

def every_three_nums(start):
  num_between = [*range(start, 101, 3)]
  return num_between

print(every_three_nums(81))


#Remove Middle

def remove_middle(lst, start, end):
  lst_start = lst[:start] 
  lst_end = lst[end+1:]
  return_list = lst_start + lst_end
  return return_list
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))