"""This program simulates a slot machine for a virtual gambling experience."""
# slot_machine_2
# My 2nd slot machine

import random

ROWS = 3
COLUMNS = 5
TOTAL_PAYLINES = 5
PAYLINE_COST = 20
SYMBOLS = ["❤", "⭐", "🍒", "🍎"]
WIN = 150  # Winnings value
WHALE_THRESHOLD = 500


def menu():
    """Print the menu."""
    print("""
1. Spin
2. Paylines
3. Paytable
4. Buy credits
5. End simulation""")

    action = input("> ").strip()  # Retrieve input

    return action


def display_paylines():
    """Display paylines."""
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

    """)


def display_paytable():
    """Display paytable."""
    print(f"""
5 in a row: {WIN} credits
$ wins x2 credits""")


def retrieve_money():
    """Ask the user how much money they want to bet."""
    while True:
        try:
            money = int(input("How many credits will you buy? > "))
        except ValueError:  # Check for value errors
            print("Please enter a valid value")
            continue
        break

    return money


def increase_balance(credit, balance):
    """Increase the user's balance."""
    balance += credit

    return balance


def decrease_balance(credit, balance):
    """Decrease the user's balance."""
    balance -= credit

    return balance


def display_balance(balance):
    """Print the user's balance."""
    print(f"Balance: {balance} credits")  # Print balance


def buy_paylines():
    """Ask the user how many paylines they want to bet on."""
    while True:
        try:
            paylines = float(input("How many paylines will you buy? > "))
        except ValueError:
            print("Please enter a valid number of paylines")  # Error message
            continue

        if paylines % 1 != 0:  # Checks input is an integer
            print("Please enter a valid number of paylines")  # Error message
        elif paylines < 1:  # Checks input is within a valid range
            print("Please enter a valid number of paylines")
        elif paylines > TOTAL_PAYLINES:  # Checks input is within a valid range
            print("Please enter a valid number of paylines")
        else:
            break  # End loop if there are no errors

    return int(paylines)  # Makes paylines an integer


def check_balance(balance, cost):
    """Check if the user has enough credits to buy paylines."""
    payment_error = False

    if balance < cost:  # Check if the user has enough money for purchase
        payment_error = True

    return payment_error


def payment_message(payment_error):
    """Display a payment error or transaction confirmation in a purchase."""
    if payment_error is True:
        print("You do not have enough credits to make this purchase")

    elif payment_error is False:
        print("Transaction successful")


def paylines_cost(user_paylines):
    """Calculate the cost of the user's payline purchase."""
    cost = PAYLINE_COST * user_paylines  # Find paylines cost

    return cost


def create_slot_machine():
    """Create the slot machine."""
    slot_machine = []

    for i in range(ROWS):
        slot_machine.append([])  # Add new row
        for j in range(COLUMNS):
            slot_machine[i].append(random.choice(SYMBOLS))  # Add random symbol

    return slot_machine


def create_paylines(slot_machine):
    """Create lists of paylines from the slot machine display."""
    paylines = []

    for i in range(ROWS):
        paylines.append(slot_machine[i])  # Add first 3 paylines

    # Add 4th payline
    paylines.append([slot_machine[0][0],
                     slot_machine[1][1],
                     slot_machine[2][2],
                     slot_machine[1][3],
                     slot_machine[0][4]])

    # Add 5th payline
    paylines.append([slot_machine[2][0],
                     slot_machine[1][1],
                     slot_machine[0][2],
                     slot_machine[1][3],
                     slot_machine[2][4]])

    return paylines


def display_slot_machine(slot_machine):
    """Print the slot machine."""
    for row in slot_machine:
        print("\t".join(row))  # Print each row


def check_paylines(paylines, user_paylines):
    """Check if the user has any winning paylines."""
    win = False  # Initially win is defined as false

    for i in range(user_paylines):  # Checks user's bought paylines
        payline = paylines[i]  # Defines given payline
        if payline[0] == payline[1] == payline[2] == payline[3] == payline[4]:
            win = True  # Defines win as true
            break  # End loop, as the user has a winning payline

    return win


def calculate_winning_value(win):
    """Calculate the user's total winnings from the spin."""
    if win is True:  # Checks if the user won
        winnings = 150  # Defines winning value

    elif win is False:  # Checks if the user lost
        winnings = 0  # Defines winnings as 0 credits

    return winnings


def display_results(win, winnings):
    """Display the user's results from spin."""
    if win is True:
        print(f"You won {winnings} credits!")  # Winning message

    if win is False:
        print("You lost")  # Losing message


def make_profile():
    """Collect player's personal information."""
    player_profile = {}
    player_profile["name"] = input("Name: ")
    player_profile["location"] = input("Location: ")
    player_profile["high_score"] = 0
    player_profile["lifetime_losses"] = 0
    player_profile["target_ads"] = False

    return player_profile


def check_marketing_status(player_profile):
    """Identify high-spending whales."""
    if player_profile["lifetime_losses"] <= WHALE_THRESHOLD:
        print("Keep playing to climb the leaderboard!")

    elif player_profile["lifetime_losses"] > WHALE_THRESHOLD:
        print("Buy more credits now!")


def update_high_score(winnings, player_profile):
    """Update the player's highscore."""
    if winnings > player_profile["high_score"]:
        player_profile["high_score"] = winnings
        print("New high score!")  # Winning message


def buy_credits(balance):
    """Run deposit retrieval and display"""
    money = retrieve_money()
    updated_balance = increase_balance(money, balance)  # Adds credits
    display_balance(balance)  # Print user's balance

    return updated_balance


# Main program
if __name__ == "__main__":
    print("--- Slot Machine Simulation ---")  # Title

    balance = 0  # Set initial balance
    run = True  # Counter for running simulation
    player_profile = make_profile()

    while run is True:
        while True:
            action = menu()  # Prints menu and retrieves

            if action == "1":
                print("Initialising simulation...")
                break

            elif action == "2":
                display_paylines()

            elif action == "3":
                display_paytable()

            elif action == "4":
                balance = buy_credits(balance)

            elif action == "5":
                run = False
                break

            else:
                print("Please enter a valid option.")

        # Check if user ended game
        if run is False:
            continue

        # Buy paylines
        user_paylines = buy_paylines()  # User buys paylines
        cost = paylines_cost(user_paylines)  # Calculates cost of paylines
        payment_error = check_balance(balance, cost)  # Checks balance
        payment_message(payment_error)  # Displays transaction message

        if payment_error is False:  # Runs program after successful purchase
            balance = decrease_balance(cost, balance)  # Change balance
            player_profile["lifetime_losses"] += cost  # Change lifetime losses
            display_balance(balance)

            # Set up slot machine
            slot_machine = create_slot_machine()  # Create the slot machine
            display_slot_machine(slot_machine)  # Display the slot machine
            paylines = create_paylines(slot_machine)  # Define paylines

            # Checks user's winnings
            win = check_paylines(paylines, user_paylines)  # Checks for a win
            winnings = calculate_winning_value(win)  # Calculate winnings

            # Displays user's winnings
            display_results(win, winnings)  # Displays user's results
            balance = increase_balance(winnings, balance)  # Adds winnings
            player_profile["lifetime_losses"] -= winnings  # Update profile
            update_high_score(winnings, player_profile)  # Updates high score
            display_balance(balance)  # Displays user's balance

            # Checks for whales
            check_marketing_status(player_profile)

    print("Thank you for using my slot machine simulation")
