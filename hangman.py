import random

def hangman(word):
    wrong = 0
    stages = [
        "",
        "__________      ",
        "                ",
        "|         |     ",
        "|         0     ",
        "|        /|\    ",
        "|        / \    ",
        "|               "
    ]
    remaining_word = list(word)
    board = ["__"] * len(word)
    win = False
    print("welcome to hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in remaining_word:
            cind = remaining_word.index(char)
            board[cind] = char
            remaining_word[cind] = "$"
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0: e]))
        if "__" not in board:
            print("you win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You Lose! It was {}".format(word))


x = ["big","cat","lunch","people"]
y = random.choice(x)
hangman(y)
