import random
seq = range(10)
ans = random.sample(seq, k=4)

while True:
    raw_guess = input()
    guess = []
    for character in raw_guess:
        guess.append(int(character))

    repetition = 0
    for digit in ans:
        if digit in guess:
            repetition += 1

    n = 0
    for i in range(len(ans)):
        if ans[i] == guess[i]:
            n += 1

    m = repetition - n

    print(str(n) + "A" + str(m) + "B")

    if n == 4:
        print("Congratulation! You win!")
        break