import random
import time
import sys

def game():

    # the coordinates of the tanks are stored in this list
    tanks_coordinates = []
    tanks_coordinates_x = []
    tanks_coordinates_y = []

    # the coordinates of the tanks are generated here. each x and y coordinate go in the list 'tank'. the list 'tank' is added to the larger list of the coordinates
    for i in range(0, 5):
        tank = []

        random.seed()
        tank_x = random.randint(1, 10)

        random.seed()
        tank_y = random.randint(1, 10)
        tank.append(tank_x)
        tank.append(tank_y)
        tanks_coordinates_x.append(tank)

        if tank_y == 1:
            tank = [] 
            tank.append(tank_x)
            tank.append(tank_y + 1)       
            tanks_coordinates_x.append(tank)
        
        elif tank_y == 10:
            tank = []
            tank.append(tank_x)
            tank.append(tank_y - 1)
            tanks_coordinates_x.append(tank)
        
        else:
            tank = []
            tank.append(tank_x)
            tank.append(tank_y + 1) 
            tanks_coordinates_x.append(tank)
    
    for j in range(0, 5):
        if tank is tanks_coordinates_x:
            tanks_coordinates_y.pop(tank)

        tank = []

        random.seed()
        tank_x = random.randint(1, 10)
        random.seed()
        tank_y = random.randint(1, 10)

        tank.append(tank_x)
        tank.append(tank_y)
        tanks_coordinates_y.append(tank)

        if tank_x == 1:
            tank = [] 
            tank.append(tank_x + 1)   
            tank.append(tank_y)    
            tanks_coordinates_y.append(tank)
        
        elif tank_y == 10:
            tank = []
            tank.append(tank_x - 1)
            tank.append(tank_y)
            tanks_coordinates_y.append(tank)
        
        else:
            tank = []
            tank.append(tank_x - 1)
            tank.append(tank_y) 
            tanks_coordinates_y.append(tank)

    tanks_coordinates = tanks_coordinates_x + tanks_coordinates_y

    print("There are", len(tanks_coordinates) + 1, "tanks!")
    print("Tanks are sent out to the battlefield in pairs and will be next to each other!\nDestroy the tanks and save the day!")
    #print(tanks_coordinates)

    # creation of the game board
    x_axis_graphical = ["  ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "]
    
    y10 = ["10", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y9 = ["9 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y8 = ["8 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y7 = ["7 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y6 = ["6 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y5 = ["5 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y4 = ["4 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y3 = ["3 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y2 = ["2 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    y1 = ["1 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    
    # game board being displayed
    print()
    print(*x_axis_graphical)
    print(*y1)
    print(*y2)
    print(*y3)
    print(*y4)
    print(*y5)
    print(*y6)
    print(*y7)
    print(*y8)
    print(*y9)
    print(*y10)
    
    #tanks_coordinates = list(set(tanks_coordinates))
    print(*tanks_coordinates)

    a = 0
    while a <= 35:
        # when a user guesses the coordinates correct, the coordinate is removed. the player wins if all the tanks are removed
        if len(tanks_coordinates) == 0:
            print("All Tanks Destroyed! The Day is Won!")
            print("Well Done Officer!")
            break
        else:
            # this list stores the tank coordinates provided by the user
            user_tank = []

            # the user provides the x and y coordinates of the tanks
            print()
            print()
            
            user_x = int(input("Input X coordinate: "))
            user_tank.append(user_x)
            
            user_y = int(input("Input Y coordinate: "))
            user_tank.append(user_y)
            #print(user_tank)

            # this segment of the code checks whether the tanks are in the coordinates provided by the user
            # if the tank is in the coordinates, the coordinate is removed. else, the game continues
            if user_tank in tanks_coordinates:
                print("That was a HIT!")

                if user_y == 1:
                    y1[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 2:
                    y2[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 3:
                    y3[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 4:
                    y4[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 5:
                    y5[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 6:
                    y6[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 7:
                    y7[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 8:
                    y8[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 9:
                    y9[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 10:
                    y10[user_x] = "[X]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)

                tanks_coordinates.remove(user_tank)

            else:
                print("That was a MISS!")
                if user_y == 1:
                    y1[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 2:
                    y2[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 3:
                    y3[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 4:
                    y4[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 5:
                    y5[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 6:
                    y6[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 7:
                    y7[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 8:
                    y8[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 9:
                    y9[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)
                if user_y == 10:
                    y10[user_x] = "[O]"
                    print(*x_axis_graphical)
                    print(*y1)
                    print(*y2)
                    print(*y3)
                    print(*y4)
                    print(*y5)
                    print(*y6)
                    print(*y7)
                    print(*y8)
                    print(*y9)
                    print(*y10)


        a = a + 1
    print("You've used all your bombers! The Nazi Fleet is ascending!\nThe Blitzkrieg is happening!")
    print("Game Over.")
    print()
    print("The tanks were at the locations", *tanks_coordinates_x, tanks_coordinates_y)

def opening():
    print("""
 __      __                   ________                                  
/  \    /  \_____  _______   /  _____/ _____     _____    ____    ______
\   \/\/   /\__  \ \_  __ \ /   \  ___ \__  \   /     \  / __ \  /  ___/
 \        /  / __ \_|  | \/ \    \_\  \ / __ \_|  Y Y  \ \  ___/  \___ \ 
  \__/\  /  (____  /|__|     \______  /(____  /|__|_|  /  \___ > /____  >
       \/        \/                 \/      \/       \/      \/      \/ 
    """)

    print("An rsh production ©rsh 2021")

    print()
    print()

    line_1 = "Emergency officer! The Nazis have unleashed the blitzkrieg! We need to locate and bomb the tanks!"
    line_2 = "The locations of the tanks are unknown. Use your tactics and locate the tanks."
    line_3 = "You have only 35 bomber planes!"
    line_4 = "Tanks are sent out to the battlefield in pairs and will be next to each other!"
    line_5 = "Destroy the tanks and save the day!"

    for char in line_1:
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print()

    for char in line_2:
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print()

    for char in line_3:
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print()

    for char in line_4:
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print()

    for char in line_5:
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print()

    print()
    print()

opening()
game()
