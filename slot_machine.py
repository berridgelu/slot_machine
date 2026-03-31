##
# slot_machine.py
# Slot machine simulator

import random
import gambling

# Constant variables are set
MENU = ["Pay table", "Paylines", "Spin"]
PAYLINE_COST = 20
ROWS = 3
COLUMNS = 5
PAYLINES = 5
SYMBOLS_IN_PAYLINES = 5
CONSEC_IN_WINNING_PAYLINE = 3
ORIGINAL_BALANCE = 1000
SYMBOLS = ["❤", "❤", "⭐", "⭐", "🍒", "🍒", "🍎", "🍎", "$", "↑"]

def displays_choices(choices):
    """
    Forces the user to choose a choice from a list
    """
    
    print("Choose an option:")

    # Prints numbered options
    for i in range(list_size):
        print(f"{i+1}: choices[i]")

def force_int(max_value):
    """
    Forces user to enter an integer within a certain range
    """
    
    while True:
        try:
            choice = float(input("> ")) # Retrieves input
        except ValueError:
            print("Please enter a valid option") # Displays error message if the input is invalid
            continue

        # Checks if the users number is within the range and a whole number
        if choice < 1 or choice > max_value or choice % 1 != 0:
            print(f"Please enter a valid option") # Dsiplays error message
        else:
            choice = int(choice) # Makes float into an integer
            break

    return choice

def pay_table():
    """
    Prints pay table
    """

    # Prints pay table
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

    # Prints paylines
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

    # Creates slot machine list
    slot_machine = []
    
    for i in range(ROWS):
        slot_machine.append([]) # Creates new sub-list in multidimensional slot machine list
        for j in range(COLUMNS):
            slot_machine[i].append(random.choice(SYMBOLS)) # Appends a random symbol

    print("""spinning...
""")
        
    return slot_machine

def display_slot_machine(slot_machine):
    """
    Displays the slot machine
    """

    # Prints 2-d slot machine list
    for row in slot_machine:
        print("\t".join(row))

def create_paylines(slot_machine):
    """
    Creates the existing paylines after a spin
    """

    # Creates a list of all existing paylines
    paylines = []

    # Appends rows 1-3 of the slot machine
    for row in slot_machine:
        paylines.append(row)

    # Appends row 4 of the slot machine
    paylines.append([slot_machine[0][0], slot_machine[1][1],
                     slot_machine[2][2], slot_machine[1][3],
                     slot_machine[0][4]])
    # Appends row 5 of the slot machine
    paylines.append([slot_machine[2][0], slot_machine[1][1],
                     slot_machine[0][2], slot_machine[1][3],
                     slot_machine[2][4]])

    return paylines

def determine_multiplier(first_symbol):
    """
    Checks to see what the multiplier is 
    """

    # Checks for rare symbols to increase multiplier
    if first_symbol == "↑" or first_symbol == "$":
        multiplier = 3
    else:
        multiplier = 1

    return multiplier

def calc_payline_credits(consec, multiplier):
    """
    Calculates the amount of credits a payline earns
    """

    # Checks if there are more than 3 consecutive symbols
    if consec >= CONSEC_IN_WINNING_PAYLINE:
        # Calculates the amount of credits a payline earns
        paylines_credits = 10**(consec-1)*multiplier
    else:
        paylines_credits = 0

    return paylines_credits

def winning_paylines(credits_list):
    """
    Finds the winning paylines postitions
    """

    # Find the positions of the winning paylines in a list of credits
    winning_paylines = []

    # Checks if a value is equal to the maximum amount of credits earned
    for i in range(len(credits_list)):
        if credits_list[i] == max(credits_list):
            winning_paylines.append(str(i+1)) # String for simplicity printing out
            
    return winning_paylines

def total_winnings(balance):
    """
    Calculates and prints the total amount of credits a user has earnt
    """

    # Calculates the total winnings at the end of game
    total_winnings = balance - ORIGINAL_BALANCE

    # Tells user how much they have won
    if total_winnings < 0:
        print(f"You lost {0 - total_winnings} credits")
    elif total_winnings == 0:
        print(f"You won 0 credits")
    elif total_winnings > 0:
        print(f"You won {total_winnings} credits")

# Main program
if __name__ == "__main__":
    print("SLOT MACHINE SIMULATOR")

    # Prompts user to ask for instructions or initiate game
    while True:
        display_options(MENU) # Displays menu
        option = force_int(len(MENU)) # Forces user to enter valid option
        
        if option == 1:
            pay_table() # Prints pay table
        elif option == 2:
            pay_lines() # Prints paylines
        elif option == 3:
            break # Spin

    # Sets balance to initial balance
    balance = ORIGINAL_BALANCE
    print(f"Balance: {balance}")

    while True:        
        #
        print("""
Chosen number of paylines:""")
        amount_paylines = force_int(PAYLINES) # Forces the user to enter amount of paylines

        cost = 20*amount_paylines # Calculates cost
        print(f"Cost: {cost}")
        balance -= 20*amount_paylines # Changes balance
        print(f"Balance: {balance}")

        # Creates and displays slot machine
        slot_machine = create_slot_machine()
        display_slot_machine(slot_machine)
        
        paylines = create_paylines(slot_machine) # Creates a list of all paylines
        payline_credits = [] # Creates a list of credits each payline earns
        
        # Adds the amount of credits each payline earns to list
        for i in range(PAYLINES):
            multiplier = determine_multiplier(paylines[i][0]) # Determines multiplier
            consec = 1 # Consecutive starts off as 1
            for j in range(SYMBOLS_IN_PAYLINES): # Checks each payline in a row
                if paylines[i][0] == paylines[i][j] or paylines[i][0] == "↑": # Checks if there are consecutive symbols
                    consec += 1
                else:
                    break
                
            payline_credits.append(calc_payline_credits(consec, multiplier)) # Appends the amount of credits a payline earns
        user_payline_credits = payline_credits[:amount_paylines] # Creates a select list of credits specific to the user

            
        # Tells the user how much they have won
        if max(user_payline_credits) == 0:
            print("""You won nothing""")
            win = False
        else:
            winning_paylines = winning_paylines(user_payline_credits)
            print(f"You have won {max(user_payline_credits)} credits for line(s): {', '.join(winning_paylines)}")
            balance += max(user_payline_credits)
            win = True

        # Tells user what they could have won
        if max(user_payline_credits) < max(payline_credits):
            possible_winning_paylines = winning_paylines(payline_credits)
            print(f"You could have won {max(payline_credits)} credits for line(s): {', '.join(possible_winning_paylines)}")

        # Checks if the user would like to gamble their winnings
        if win == True:
            print("""
1. Gamble your winnings
2. Keep current winnings""")

            option = force_int(1, 2)

        # Code for gambling
        if option == 1:
            print("""
1. Rules
2. Gamble""")
            while True:
                option = force_int(1, 2)

                # Displays rules or continues to gambling
                if option == 1:
                    gambling.gamble_rules()
                elif option == 2:
                    break

            # User chooses between color and suit
            print("""
1. Color
2. Suit""")
            option = force_int(1, 2)

            # User chooses between colors
            if option == 1:
                print("""
1. Red
2. Black""")
                option = force_int(1, 2)
            # User choose between suits
            if option == 2:
                print("""
1. Hearts
2. Diamonds
3. Clubs
4. Spades""")
                option = force_int(1, 4)

                

            card() # Draw the card
            print_card # Print the card
 
        print(f"Balance: {balance}") # Print balance

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

    # Tells user total winnings
    total_winnings(balance)
    print("Thank you for using my slot machine simulation")

    
