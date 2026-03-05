import random

# Slot Machine Simulation
print("SLOT MACHINE SIMULATOR")

# Prompt user to play or recieve further game information until they give a valid response
while True:
    # Give user options for the pay table, paylines and to play
    try:
        instructions = int(input(f"""
Press 1 for the pay table
Press 2 for paylines
Press 3 to spin
> """))

    except ValueError:
        print("Please enter a valid response")
        continue
        
    if instructions == 1:
        # Print pay table
        print("""
Pay table:
5 of a kind - 10,000 credits
4 of a kind - 1,000 credits
3 of a kind - 100 credits
'$' or '↑' win triple credit!
""")

    elif instructions == 2:
        # Print paylines
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
The winning payline is the one that earns the most money""") 

    elif instructions == 3:
        break

    else:
        print("Please enter a valid number")

# Create symbol list where 
symbols = ["❤", "❤", "⭐", "⭐", "🍒", "🍒", "🍎", "🍎", "$", "↑"]

# Counter to control if the loop repeats
repeat = True

# Create constants called rows and columns
ROWS = 3
COLUMNS = 5

# Create constant which represents the cost of each line
PAYLINE_COST = 20

# Keeps track of credits
credits = 1000

while repeat == True:
    print(f"Credits: {credits}")
    # Asks user for amount of paylines they will bet on until they enter a valid response
    while True:
        try:
            paylines_num = int(input("""
Enter amount of paylines you will bet on (1-5)
> """))

        except ValueError:
            print("Please enter a valid number")
            continue

        # Checks if the user has enough credits
        if paylines_num * PAYLINE_COST > credits:
            print(f"""
Sorry, your bet exceeds your credits balance of {credits}
You may bet on up to {(credits - (credits % 20))/20} lines
Please enter a valid number""")

        elif paylines_num > 0 and paylines_num < 6:
            credits -= paylines_num*PAYLINE_COST
            break

        else:
            print("Please enter a valid number")

    print("spinning...")
    print("")

    # Create slot machine in the form of a list
    slot_machine = []

    # Create 3 rows and 5 columns with one random symbol on each row
    # Print out each row
    for a in range(ROWS):
        slot_machine.append([])
        for b in range(COLUMNS):
            slot_machine[a].append(random.choice(symbols))
        print("\t".join(slot_machine[a]))
        print('')

    # Creates 2d payline list
    paylines = []

    # Adds paylines 1-3 by looping through slot_machine
    for row in slot_machine:
        paylines.append(row)
        
    # Manually creates paylines 4-5
    paylines.append([slot_machine[0][0], slot_machine[1][1], slot_machine[2][2], slot_machine[1][3], slot_machine[0][4]])
    paylines.append([slot_machine[2][0], slot_machine[1][1], slot_machine[0][2], slot_machine[1][3], slot_machine[2][4]])

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
        
