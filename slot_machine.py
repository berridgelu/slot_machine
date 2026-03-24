##
# slot_machine.py
# Slot machine simulator

import random

# Constant variables are set
PAYLINE_COST = 20
ROWS = 3
COLUMNS = 5
PAYLINES = 5
SYMBOLS_IN_PAYLINES = 5
CONSEC_IN_WINNING_PAYLINE = 3
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
    Creates the existing paylines after a spin
    """

    paylines = []

    for row in slot_machine:
        paylines.append(row)

    paylines.append([slot_machine[0][0], slot_machine[1][1], slot_machine[2][2], slot_machine[1][3], slot_machine[0][4]])
    paylines.append([slot_machine[2][0], slot_machine[1][1], slot_machine[0][2], slot_machine[1][3], slot_machine[2][4]])

    return paylines

def user_paylines(paylines, amount_paylines):
    """
    Retrieves the user's chosen paylines from the list of winning paylines
    """

    user_paylines = paylines[: amount_paylines]

    return user_paylines

def determine_multiplier(first_symbol):
    """
    Checks to see what the multiplier is 
    """

    if first_symbol == "↑" or first_symbol == "$":
        multiplier = 3
    else:
        multiplier = 1

    return multiplier

def consec_counter(first_symbol, evaluated_symbol):
    """
    Counts consecutive symbols in a payline
    """

    consec = 1

    while True:
        if first_symbol == evaluated_symbol or evaluated_symbol == "↑":
            consec += 1
        else:
            break

    return consec

def add_payline_credits(consec, multiplier):
    """
    Adds the amount of credits a payline wins to a list
    """

    paylines_credits = []

    if consec >= CONSEC_IN_WINNING_PAYLINE:
        paylines_credits.append(10**(consec-1)*multiplier)

    else:
        paylines_credits.append(0)

    return paylines_credits

def find_winning_paylines_num(credits_list):
    """
    Finds the winning paylines and credit value
    """
    winning_paylines_num = []

    for i in range(len(credits_list)):
        if credits_list[i] == max(credits_list):
            winning_paylines_num.append(i+1)
            
    return winning_paylines_num

# Main program
if __name__ == "__main__":
    print("SLOT MACHINE SIMULATOR")

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

    # Keeps track of credits
    balance = 1000

    while True:
        print(f"Credits: {credits}")
        
        # Asks user for amount of paylines they will bet on until they enter a valid response
        amount_paylines = force_int(1, 5)

        # Create the slot machine
        slot_machine = create_slot_machine(ROWS, COLUMNS)

        # Display the slot machine
        display_slot_machine(slot_machine)

        # Creates the list of paylines
        paylines = create_paylines(slot_machine)
            
       # A list to keep track of the winning paylines
        user_paylines = user_paylines(paylines, amount_paylines)
        
        # Checks winning conditions
        for i in range(PAYLINES):
            for j in range(SYMBOLS_IN_PAYLINES):
                
                # Determines multiplier for payline
                multiplier = determine_multiplier(paylines[i][0])
                
                # Determines amount of consecutive symbols in payline
                consec = consec_counter(paylines[i][0], paylines[i][j])
                
            payline_credits = add_payline_credits(consec, multiplier)

        user_payline_credits = payline_credits[:paylines_num]
            
        # Tells the user how much they have won
        if max(user_payline_credits) == 0:
            print("""You won nothing""")
        else:
            winning_paylines = find_winning_paylines_num(user_payline_credits)
            print(f"You have won {max(user_payline_credits)} credits for line(s): {', '.join(winning_paylines)}")
            balance += max(user_payline_credits)

        if max(user_payline_credits) < max():
            possible_winning_paylines = find_winning_paylines_num(payline_credits)
            print(f"You could have won {max(payline_credits)} credits for line(s): {', '.join(possible_winning_paylines)}")

        else:
            print("This was the best possible outcome")

        if credits < 20:
            print("Game over. You no longer have enough credits to spin")
            break

        else:
            print("""
    Press 1 to spin again
    Press 2 to finish
    > """)
            choice = force_int(1, 2)
                
        if choice == 2:
            repeat = False
            break

        

