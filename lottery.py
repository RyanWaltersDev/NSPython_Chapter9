from random import choice
'''Modeling a simple lottery game.'''

lottery = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Lottery number select.
winner = []
while len(winner) < 4:
    value = choice(lottery)
    winner.append(value)

print("The wining ticket is: ", *winner, sep='')

# Looping until specific number is pulled
my_ticket = [6, 'c', 8, 1]
attempts = 0

while winner != my_ticket:
    winner = []
    while len(winner) < 4:
        value = choice(lottery)
        winner.append(value)
    attempts += 1
else:
    print("Success! My ticket and the winning ticket match: ", 
        *my_ticket, ' ', *winner, sep='')
    print(f"The loop ran {attempts} times before our match!")
