# Jake Anderson
# CS 30
# Array Practice

# functions
school_map = [
     ["DeadEnd", "Cafeteria", "Classroom", "DeadEnd"],
     ["Classroom", "Classroom", "Classroom", "Classroom"],
     ["DeadEnd", "Entrance", "DeadEnd", "SchoolExit"],
     ["SchoolExit", "Classroom", "Classroom", "Classroom"]
 ]
row = 2 
col = 1
actions = ["walk"]
movements = ["north", "south", "east", "west"]

# defining movement function
def movement():
  global row, col
  while True:
    for movement in movements:
      print(movement)
    movement_input = input("which direction? ")
    if movement_input.lower() == "north" and row != 0 :
      row -= 1
      break
    elif movement_input.lower() == "west" and col != 0 :
      col -= 1
      break
    elif movement_input.lower() == "south" and row != 3 :
      row += 1
      break
    elif movement_input.lower() == "east" and col != 3 :
      col += 1
      break
    else:
      print("that's not valid!")
    
  
# tile functions
while True:
  current_location = school_map[row][col]
  if current_location == "Classroom":
    print("you are in a classroom")
  elif current_location == "Entrance":
    print("you are at the entrance of campbell")
  elif current_location == "DeadEnd":
    print("there is nothing here")
  elif current_location == "Cafeteria":
    print("you are in the cafeteria, and eat some food")
  elif current_location == "SchoolExit":
    print("congrats, you escaped campbell!")
  else:
    print("Somthing went wrong!")

  # action function
  action_input = input("what do you do? ")
  if action_input.lower() == "walk":
    print("you can go:")
    movement()

