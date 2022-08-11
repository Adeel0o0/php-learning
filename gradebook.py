last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ['physics', 'calculus', 'poetry', 'history']

grades = [98, 97, 85, 88]

# combine subjects and grades
gradebook = [
  ['physics', 98],
  ['calculus', 97],
  ['poetry', 85],
  ['history', 88]
]

print(gradebook)

#add CS and visual arts 
gradebook.append(['computer science', 100])

gradebook.append(['visual arts', 93])

#modifying the gradebook

gradebook[5][1] = 98

#change numeric value to pass/fail option

gradebook[2].remove(85)
gradebook[2].append("Pass")

# combine gradebooks

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)