###############################################################################
# Title: Campbell RPG      
# Class: CS 30
# Date: March 22, 2023
# Coders Name: Jake Anderson
# Version: 002   
###############################################################################
'''
Current Assignment: Create a text-based RPG

An RPG set within Campbell
'''
#------------------------------------------------------------------------------
#----Imports and Global Variables----------------------------------------------
import sys
import random
#-----Functions----------------------------------------------------------------
tile = ["Entrance", "Classroom", "Cafeteria", "DeadEnd", "SchoolExit"]
tiles = {
    tile[0] : {"description" : "you are at the entrance"},
    tile[1] : {"description" : "you are in a classroom"},
    tile[2] : {"description" : "you are in the cafeteria"},
    tile[3] : {"description" : "there is nothing here"},
    tile[4] : {"description" : "you found the exit! congrats!"}  
}

school_map = [
  [tile[3], tile[2], tile[1], tile[3]],
  [tile[1], tile[1], tile[1], tile[1]],
  [tile[3], tile[0], tile[3], tile[4]],
  [tile[4], tile[1], tile[1], tile[1]]
]

item = ["Pencil", "Textbook", "Calculator", "Binder", "Phone"]

items = {
  item[0] : {"description": "a pencil you can write with"},
  item[1] : {"description": "a textbook full of knowledge"},
  item[2] : {"description": "a calculator for math"},
  item[3] : {"description": "a binder to put things in"},
  item[4] : {"description": "a phone that you can use"}
  
         }

row = 2 

col = 1

actions = ["walk"]

movements = ["north", "south", "east", "west"]

inventory = []

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
    
  
#----Tile Functions----------------------------------------------------------------------
while True:
  current_location = school_map[row][col]
  if current_location == tile[1]:
    print("you are in a classroom")
    print("you can search this room!")
  elif current_location == tile[0]:
    print("you are at the entrance of campbell")
  elif current_location == tile[3]:
    print("there is nothing here")
  elif current_location == tile[2]:
    print("you are in the cafeteria, and eat some food")
  elif current_location == tile[4]:
    print("congrats, you escaped campbell!")
    sys.exit
  else:
    print("you can't do that!")

#----Action Functions----------------------------------------------------------------------
  action_input = input("what do you do? ")
  if action_input.lower() == "walk":
    print("you can go:")
    movement()
  elif action_input.lower() == "inventory":
    print("you currently have:")
    for item in inventory:
      print(f"{item}")
  elif action_input.lower() == "search":
    if current_location == tile[1]:
        item_chance = random.randint(0,4)
        if item_chance == 0:
          print("you found a pencil!")
          inventory.append(item[0])
        elif item_chance == 1:
          print("you found a textbook!")
          inventory.append(item[1])
        elif item_chance == 2:
          print("you found a calculator!")
          inventory.append(item[2])
        elif item_chance == 3:
          print("you found a binder!")
          inventory.append(item[3])
        elif item_chance == 4:
          print("you found a phone!")
          inventory.append(item[4])
    elif current_location != tile[1]:
      print("you can't do that!")