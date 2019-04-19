class Player():
    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name
    


class Move():
    def __init__(self, author, position):
        self.author = author
        self.position = position

    def render_new_board():
        pass



class Board():
    moves = []

    def display(self):
        """
        Displays a current version of the board.

        """
        board = [["_", "_", "_"],
                 ["_", "_", "_"],
                 ["_", "_", "_"]]

        display = "\n".join([" ".join(line) for line in board])

        print(display)

    def add_move(self, move):
        """ Adds the new move to the board and re-renders the display.

        """


    pass



class Game():
    def __init__(self):
        self.board = Board()

    def start_game(self):
        player1_name = input("Player 1, what is your name? ")
        player1_piece = input("Player 1, would you like to play X or O? ")
        player2_name = input("Player 2, what is your name? ")
        player2_piece = ("O" if player1_piece == "X" else "X")
        print(f"{player2_name}, you are playing {player2_piece}")

        self.player1 = Player(player1_piece, player1_name)
        self.player2 = Player(player2_piece, player2_name)

        pass

