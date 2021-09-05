import random


class RockPaperScissors:
    def __init__(self, figure):
        global list_of_options

        self.figure = figure
        self.computer_figure = random.choice(list_of_options)
        self.dict_of_options = {
            "rock": ["fire", "scissors", "snake", "human",
                     "tree", "wolf", "sponge"],
            "fire": ["scissors", "snake", "human", "tree",
                     "wolf", "sponge", "paper"],
            "scissors": ["snake", "human", "tree", "wolf",
                         "sponge", "paper", "air"],
            "snake": ["human", "tree", "wolf", "sponge",
                      "paper", "air", "water"],
            "human": ["tree", "wolf", "sponge", "paper",
                      "air", "water", "dragon"],
            "tree": ["wolf", "sponge", "paper", "air",
                     "water", "dragon", "devil"],
            "wolf": ["sponge", "paper", "air", "water",
                     "dragon", "devil", "lightning"],
            "sponge": ["paper", "air", "water", "dragon",
                       "devil", "lightning", "gun"],
            "paper": ["air", "water", "dragon", "devil",
                      "lightning", "gun", "rock"],
            "air": ["water", "dragon", "devil", "lightning",
                    "gun", "rock", "fire"],
            "water": ["dragon", "devil", "lightning", "gun",
                      "rock", "fire", "scissors"],
            "dragon": ["devil", "lightning", "gun", "rock",
                       "fire", "scissors", "snake"],
            "devil": ["lightning", "gun", "rock", "fire",
                      "scissors", "snake", "human"],
            "lightning": ["gun", "rock", "fire", "scissors",
                          "snake", "human", "tree"],
            "gun": ["rock", "fire", "scissors", "snake",
                    "human", "tree", "wolf"]
        }

    def victory(self):
        global score, list_of_options

        for option in list_of_options:
            if self.figure == option \
                    and self.computer_figure in self.dict_of_options[option]:
                print(f"Well done. The computer chose "
                      f"{self.computer_figure} and failed")
                score += 100
                return "1"
            elif self.computer_figure == option \
                    and self.figure in self.dict_of_options[option]:
                print(f"Sorry, but the computer chose {self.computer_figure}")
                return "0"

        score += 50
        print(f"There is a draw ({self.figure})")

    def main(self):
        global score, players

        self.victory()

        players.insert(0, user_name + ' ' + str(score) + '\n')

        new_file = open('rating.txt', 'w', encoding='utf-8')
        for player in players:
            new_file.write(player)
        new_file.close()


if __name__ == '__main__':
    score = 0

    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    file = open('rating.txt', 'r', encoding='utf-8')
    players = file.readlines()
    for i in players:
        if i[:len(user_name)] == user_name:
            score = int(i[len(user_name) + 1:])
            players.remove(i)
    file.close()

    options = input()
    list_of_options = options.replace(',', ' ').split()

    if len(list_of_options) == 0:
        list_of_options = ["rock", "paper", "scissors"]

    print("Okay, let's start")

    while True:
        user_figure = input()

        if user_figure == "!exit":
            print("Buy!")
            break
        elif user_figure == "!rating":
            print(f"Your rating: {score}", end='')
            continue
        elif user_figure not in list_of_options:
            print("Invalid input")
            continue

        user = RockPaperScissors(user_figure)
        user.main()
