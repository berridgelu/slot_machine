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
ORIGINAL_BALANCE = 1000
SYMBOLS = ["❤", "❤", "⭐", "⭐", "🍒", "🍒", "🍎", "🍎", "$", "↑"]

def force_int(min_int, max_int):
    """
    Forces the user to enter an integer
    """
    
    while True:
        try:
            choice = float(input("> ")) 
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if choice < min_int or choice > max_int or choice % 1 != 0:
            print(f"Please enter a whole number between {min_int} - {max_int}")
        else:
            break

    return int(choice)

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
The winning payline is the one that earns the most 
""") 

def create_slot_machine():
    """
    Creates the slot_machine display
    """

    slot_machine = []

    
    
    for i in range(ROWS):
        slot_machine.append([])
        for j in range(COLUMNS):
            slot_machine[i].append(random.choice(SYMBOLS))

    print("""spinning...
""")
        
    return slot_machine

def display_slot_machine(slot_machine):
    """
    Displays the slot machine
    """
    
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

def determine_multiplier(first_symbol):
    """
    Checks to see what the multiplier is 
    """

    if first_symbol == "↑" or first_symbol == "$":
        multiplier = 3
    else:
        multiplier = 1

    return multiplier

def calc_payline_credits(consec, multiplier):
    """
    Adds the amount of credits each payline wins to a list
    """

    if consec >= CONSEC_IN_WINNING_PAYLINE:
        paylines_credits = 10**(consec-1)*multiplier
    else:
        paylines_credits = 0

    return paylines_credits

def winning_paylines(credits_list):
    """
    Finds the winning paylines and credit value
    """
    winning_paylines = []

    for i in range(len(credits_list)):
        if credits_list[i] == max(credits_list):
            winning_paylines.append(str(i+1))
            
    return winning_paylines

def total_winnings(balance):
    """
    Calculates and prints the total amount of credits a user has earnt
    """

    total_winnings = balance - ORIGINAL_BALANCE

    if total_winnings < 0:
        print(f"You lost {0 - total_winnings} credits")
    elif total_winnings == 0:
        print(f"You earnt nothing")
    elif total_winnings > 0:
        print(f"You earnt {total_winnings} credits")

# Main program
if __name__ == "__main__":
    print("SLOT MACHINE SIMULATOR")

    # Prompts user to ask for instructions or initiate game
    while True:
        menu()
        
        option = force_int(1, 3)
        
        if option == 1:
            pay_table()
        elif option == 2:
            pay_lines()
        elif option == 3:
            break

    # Keeps track of credits
    balance = ORIGINAL_BALANCE

    while True:
        print(f"Credits: {balance}")
        
        # Asks user for amount of paylines they will bet on until they enter a valid response
        print("""
Chosen number of paylines:""")
        amount_paylines = force_int(1, 5)

        # Changes balance
        balance -= 20*amount_paylines

        # Creates and displays slot machine
        slot_machine = create_slot_machine()
        display_slot_machine(slot_machine)

        # Creates a list of all paylines
        paylines = create_paylines(slot_machine)

        # Creates a list of payline credits
        payline_credits = []
        
        # Creates list of the amount of credits each payline wins
        for i in range(PAYLINES):
            multiplier = determine_multiplier(paylines[i][0])
            consec = 1
            for j in range(SYMBOLS_IN_PAYLINES):
                if paylines[i][0] == paylines[i][j]:
                    consec += 1
                else:
                    break
                
            payline_credits.append(calc_payline_credits(consec, multiplier))

        # Creates a list of the amount of credits each payline the user has bet on wins
        user_payline_credits = payline_credits[:amount_paylines]

            
        # Tells the user how much they have won
        if max(user_payline_credits) == 0:
            print("""You won nothing""")
        else:
            winning_paylines = winning_paylines(user_payline_credits)
            print(f"You have won {max(user_payline_credits)} credits for line(s): {', '.join(winning_paylines)}")
            balance += max(user_payline_credits)

        # Tells user what they could have won
        if max(user_payline_credits) < max(payline_credits):
            possible_winning_paylines = winning_paylines(payline_credits)
            print(f"You could have won {max(payline_credits)} credits for line(s): {', '.join(possible_winning_paylines)}")
        else:
            print("This was the best possible outcome")


        # Checks if the user will play again
        if balance < 20:
            print("Game over. You no longer have enough credits to spin")
            break

        else:
            print("""
Press 1 to spin again
Press 2 to finish""")
            choice = force_int(1, 2)
        if choice == 2:
            repeat = False
            break

    # Tells user total wins
    total_winnings(balance)
    print("Thank you for using my slot machine simulation")

    
