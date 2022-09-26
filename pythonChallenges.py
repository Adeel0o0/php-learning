#Every Three Numbers

def every_three_nums(start):
  num_between = [*range(start, 101, 3)]
  return num_between

print(every_three_nums(81))


#Remove Middle

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1]
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#More Frequent Item

def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2
  
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


#Double Index

def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        newList = lst[0:index]
        newList.append(lst[index] * 2)
        newList = newList + lst[index+1:]   
        return newList
  
print(double_index([3, 8, -10, 12], 2))