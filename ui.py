

class UI:

    def welcome(self, player1, player2, startingStack):
        print('Welcome to this match ' + player1._name + ' and ' + player2._name)
        print('Each player starts with ' + str(startingStack) + ' good luck')

    def getPlayerNames(self):
        players = []
        players.append(input("Please enter name for player 1: "))
        players.append(input("Please enter name for player 2: "))
        return players
