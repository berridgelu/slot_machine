# Slot Machine Simulation
print("SLOT MACHINE SIMULATOR")

# Import random
import random

# Print pay table
print("""
Pay table:
5 of a kind - 10,000 credits
4 of a kind - 1,000 credits
3 of a kind - 100 credits

Paylines are counted from left to right""")

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

""")

# Create symbol list
symbols = ["❤", "⭐", "$", "🍒", "🍎"]

# Create slot machine in the form of a list
slot_machine = []

# Create 3 rows and 5 columns with one random symbol on each row
# Print out each row
for a in range(3):
    slot_machine.append([])
    for b in range(5):
        slot_machine[a].append(random.choice(symbols))
    print(' '.join(slot_machine[a]))
    print('')

# Creates 2d payline list
paylines = []

# Adds paylines 1-3 by looping through slot_machine
for row in slot_machine:
    paylines.append(row)
    
# Manually creates paylines 4-5
paylines.append([slot_machine[0][0], slot_machine[1][1], slot_machine[2][2], slot_machine[1][3], slot_machine[0][4]])
paylines.append([slot_machine[2][0], slot_machine[1][1], slot_machine[0][2], slot_machine[1][3], slot_machine[2][4]])

# Checks and prints winning conditions
for a in range(5):
    # Consec  is a counter that checks for consecutive symbols in a payline
    consec = 0
    for b in range(5):
        if paylines[a][b] == paylines[a][0]:
            consec += 1
        else:
            break
    if consec >= 3:
        print(f"Payline {a+1} wins {10**(consec-1)} credits")
    else:
        print(f"Payline {a+1} wins nothing")

