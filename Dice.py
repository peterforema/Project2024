from Die import rollFairDie, rollUnfairDie


def rollDice(N=1, fair=True):
    '''this function takes an argument in the form of N which is the number of dice to be rolled, using rollFairDie
    and rollUnfairDie'''
    total_score = 0

    if fair:
        for _ in range(N):
            total_score += rollFairDie()
    else:
        for _ in range(N):
            total_score += rollUnfairDie()

    return total_score

result = rollDice(1, False)
print(f"The total score is : {result}")