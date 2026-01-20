import sys

from menu import Menu
from game import GameWindow

from PySide6.QtCore import *
from PySide6.QtWidgets import *



class TicTacToe:

    def __init__(self):

        self.menu = Menu()
        self.game = GameWindow()

        self.menu.setup_ui()
        self.game.setup_ui()

        self.menu.play_button.clicked.connect(self.abrir_juego)

        self.game.game_finished.connect(self.volver_menu)
    
    def abrir_juego(self):

        self.menu.hide()

        self.game.show()

        self.game.setup_title(self.menu.player_1.text(), self.menu.player_2.text())
    
    def volver_menu(self, winner):
        print(f"Ganador: {winner}")
        self.game.hide()
        self.menu.show()
    
    




app = QApplication(sys.argv)

main = TicTacToe()
main.menu.show()

sys.exit(app.exec())