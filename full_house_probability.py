import random

fullHouseCount = 0
straightCount = 0
repetition = 1e6

for i in range(int(repetition)):
    cardsInHand = random.sample(range(52), 5)
    cardsInHand.sort()

    cardsInNumbers = [card // 4 + 1 for card in cardsInHand]
    if cardsInNumbers[0] == cardsInNumbers[1] and cardsInNumbers[-1] == cardsInNumbers[-2]:
            if cardsInNumbers[1] == cardsInNumbers[2] or cardsInNumbers[2] == cardsInNumbers[3]:
                fullHouseCount += 1

    if cardsInNumbers[0] + 1 == cardsInNumbers[1]:
        if cardsInNumbers[1] + 1 == cardsInNumbers[2]:
            if cardsInNumbers[2] + 1 == cardsInNumbers[3]:
                if cardsInNumbers[3] + 1 == cardsInNumbers[4]:
                    straightCount += 1

print(fullHouseCount / repetition, straightCount / repetition)