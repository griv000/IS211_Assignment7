import random
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help="Number of players in game", type=int, required=True)
    args = parser.parse_args()

    numPlayers = args.numPlayers #Number of players in Game
    die = Die()
    PlayersList = []
    for i in range(1, numPlayers + 1):
        PlayersList.append(Player('Player ' + str(i)))
    print("Starting a new game of Pig...")
    game = Game(PlayersList,numPlayers,die)
    game.play()


class Game:
    def __init__(self,players,num_players,die):
        self.players = players
        self.numberPlayers = num_players
        self.die = die


    def play(self):
        while True:
            
            for i in self.players:
                CurrentTurn = True
                while CurrentTurn:
                    Entered = input(str(i) + "\nEnter 'r' to roll, 'h' to hold, 'q' to quit: ")
                    if Entered == "r":
                        rollValue = self.die.roll()
                        if rollValue == 1:
                            print("\n" + i.name + " rolled a 1, Lost Turn")
                            i.turn_total = 0
                            CurrentTurn = False

                        else:
                            i.turn_total += rollValue
                            print("\n" + i.name + " rolled a " + str(rollValue))
                            self.check_winner()
                            print("Current turn total is " + str(i.turn_total))

                    elif Entered == "h":
                        i.total += i.turn_total
                        print("\n" + i.name + " holding at " + str(i.turn_total) + ", " + str(i))
                        i.turn_total = 0
                        self.check_winner()
                        CurrentTurn = False

                    elif Entered == "q":
                        print("\nQuitting Game...")
                        quit()
                    else:
                        print("\nIncorrect Entry...")

            
    def check_winner(self):
        for i in self.players:
            if i.total + i.turn_total >= 100:
                print(i.name + " current turn total is " + str(i.turn_total))
                print(i)
                print("Game Complete! " + i.name + " wins with total score of " + str(i.total + i.turn_total) + " (" + str(i.total) + " + " + str(i.turn_total) +")!")
                quit()


class Player:

    def __init__(self,name):
        self.name = name
        self.total = 0
        self.turn_total = 0

    def get_total(self):
        return self.total

    def __str__(self):
        return f"{self.name} total = {self.total}"

    def display(self):
        print(self.__str__())


class Die():

    def __init__(self):
        pass        

    def roll(self):
        self.amount = random.randint(1, 6)
        return self.amount


if __name__ == "__main__":
    main()