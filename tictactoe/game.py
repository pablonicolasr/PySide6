from style import estilos_juego

from functools import partial

from PySide6.QtCore import *
from PySide6.QtWidgets import *

from __feature__ import snake_case, true_property



class GameWindow(QMainWindow):    

    current_player = "X"
    x_moves = set()
    o_moves = set()
    n_movs = 0
    game_finished = Signal(str) 

    winner_moves = [
        {"11", "12", "13"},
        {"21", "22", "23"},
        {"31", "32", "33"},

        {"11", "21", "31"},
        {"12", "22", "32"},
        {"13", "23", "33"},

        {"11", "22", "33"},
        {"13", "22", "31"}
    ]

    def setup_ui(self):

        from __feature__ import snake_case, true_property

        self.size = QSize(450, 500)

        self.frame_titulo = QFrame()

        self.frame_buttons = QFrame()

        self.root_layout = QVBoxLayout()

        self.root_layout.add_widget(self.frame_titulo, 30)

        self.root_layout.add_widget(self.frame_buttons, 70)

        self.widget = QWidget()

        self.widget.set_layout(self.root_layout)

        self.set_central_widget(self.widget)

        self.setup_buttons_frame()

        self.style_sheet = estilos_juego
    
    def setup_title(self, player1, player2):

        self.title = QLabel(f"{player1} vs {player2}", object_name="titulo_principal", alignment=Qt.AlignCenter)
        self.title_layout = QVBoxLayout()
        self.title_layout.add_widget(self.title)
        self.frame_titulo.set_layout(self.title_layout)

    def setup_buttons_frame(self):

        self.buttons_layout = QGridLayout()               

        for i in range(1, 4):

            for j in range(1, 4):

                coordinates = f"{i}{j}"

                button = QPushButton(coordinates)

                button.clicked.connect(partial(self.record_move, coordinates, button))          

                self.buttons_layout.add_widget(button, i, j)

        self.frame_buttons.set_layout(self.buttons_layout)

    
    def record_move(self, coordinates, button):

        button.text = self.current_player

        button.enabled = False

        print("Click", coordinates)    

        if self.current_player == "X":
            self.x_moves.add(coordinates) 
            self.n_movs += 1           
            self.verify_moves()
            self.current_player = "O"

        else:
            self.o_moves.add(coordinates)
            self.n_movs += 1          
            self.verify_moves()                     
            
            self.current_player = "X"        

        self.is_draw()
        

    def verify_moves(self):        

        if self.current_player == "X":

            player_moves = self.x_moves
        
        else:

            player_moves = self.o_moves      
        
        
        for move in self.winner_moves:

            if move.issubset(player_moves):

                print(f"El jugador {self.current_player} ha ganado")

                self.game_finished.emit(self.current_player)

                return            


    def is_draw(self):

        if self.n_movs == 9:

            print("La partida es un empate")
    

    def closeEvent(self, event):
        
        reply = QMessageBox.question(
            self,
            "Salir",
            "¿Seguro que querés salir?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
            QApplication.quit()
        else:
            event.ignore()