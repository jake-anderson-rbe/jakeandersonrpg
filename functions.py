movements = ["north", "south", "east", "west"]
#----Movement Function----------------------------------------------------------------------
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