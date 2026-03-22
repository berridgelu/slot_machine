##
# slot_machine.py
# Slot machine simulator

import random

# Constant variables are set
PAYLINE_COST = 20
ROWS = 3
COLUMNS = 5
SYMBOLS = ["❤", "❤", "⭐", "⭐", "🍒", "🍒", "🍎", "🍎", "$", "↑"]

def force_int(min_int, max_int):
    """
    Forces the user to enter an integer
    """
    
    while True:
        try:
            variable = int(input("> ")) 
        except ValueError:
            print("Please enter a valid number")
            continue

        if variable < min_int or variable > max_int:
            print(f"Please enter an option between {min_int} - {max_int}")
        else:
            break

    return variable

def menu():
    """
    Prints options given at the start of the program
    """

    print("""
Press 1 for the pay table
Press 2 for paylines
Press 3 to spin
""")

def pay_table():
    """
    Prints pay table
    """
    
    print("""
Pay table:
5 of a kind - 10,000 credits
4 of a kind - 1,000 credits
3 of a kind - 100 credits
'$' or '↑' win triple credit!
""")

def pay_lines():
    """
    Prints paylines
    """

    print("""Paylines:

* * * * * - 1
* * * * * - 2
* * * * * - 3
-------------
*       * - 4  
  *   *  
    *
-------------
    *
  *   *
*       * - 5

Paylines are counted from left to right
'↑' is a wild card
Each payline costs 20 credits
The winning payline is the one that earns the most money
""") 

def create_slot_machine(rows, columns):
    """
    Creates the slot_machine display
    """

    slot_machine = []

    for i in range(rows):
        slot_machine.append([])
        for j in range(columns):
            slot_machine[i].append(random.choice(SYMBOLS))

    return slot_machine

def display_slot_machine(slot_machine):
    """
    Displays the slot machine
    """

    print("""spinning...
""")
    
    for row in slot_machine:
        print("\t".join(row))

def create_paylines(slot_machine):
    """
    Creates the existing paylines
    """

    paylines = []

    for row in slot_machine:
        paylines.append(row)

    paylines.append([slot_machine[0][0], slot_machine[1][1], slot_machine[2][2], slot_machine[1][3], slot_machine[0][4]])
    paylines.append([slot_machine[2][0], slot_machine[1][1], slot_machine[0][2], slot_machine[1][3], slot_machine[2][4]])

    return paylines

    
# Slot Machine Simulation
print("SLOT MACHINE SIMULATOR")

# Prompt user to play or recieve further game information until they give a valid response
while True:
    # Loops starting information until user initiates game
    while True:
        # Prints menu
        menu()

        # Forces the user to choose an option from the menu
        option = force_int(1, 3)
            
        if option == 1:
            pay_table()

        elif option == 2:
            pay_lines()

        else:
            break

# Counter to control if the loop repeats
repeat = True

# Keeps track of credits
credits = 1000

while repeat == True:
    print(f"Credits: {credits}")
    
    # Asks user for amount of paylines they will bet on until they enter a valid response
    paylines_num = force_int(1, 5)

    # Create the slot machine
    slot_machine = create_slot_machine(ROWS, COLUMNS)

    # Display the slot machine
    display_slot_machine(slot_machine)

    # Creates the list of paylines
    paylines = create_paylines(slot_machine)
        
   # A list to keep track of the winning paylines
    winning = []
    
    # Checks winning conditions
    for i in range(COLUMNS):
        # Creates multiplier for symbol specific bonuses
        multiplier = 1

        # Consec  is a counter that checks for consecutive symbols in a payline
        consec = 0

        for j in range(COLUMNS):
            # Multiplier increases for rarer symbols
            if paylines[i][0] == "↑" or paylines[i][0] == "$":
                multiplier = 3
            if paylines[i][j] == paylines[i][0] or paylines[i][j] == "↑":
                consec += 1
            else:
                break
            
        if consec >= 3:
            winning.append(10**(consec-1)*multiplier)

        else:
            winning.append(0)

    # Tells the user how much they have won
    if max(winning[:paylines_num]) == 0:
        print("You have won nothing")

    else:
        # Find out how on which lines the win occurs
        winning_lines = []
        for i in range(paylines_num):
            if winning[:paylines_num][i] == max(winning[:paylines_num]):
                winning_lines.append(i+1)       
        print(f"You have won {max(winning[:paylines_num])} credits for line(s): {', '.join(winning_lines)}")
            
    
    # Ask user if they want to play again until they enter a valid response
    while True:
        # Asks user if they want to spin again
        if credits < 20:
            print("Game over. You no longer have enough credits to spin")
            repeat = False
            break

        else:
            choice = int(input("""
Press 1 to spin again
Press 2 to finish
> """))
        
            # Checks users choice            
            if choice == 1:
                break
            
            elif choice == 2:
                repeat = False
                break
                
            else:
                print("Please enter a valid response")
        
