from style import estilos_menu

from PySide6.QtCore import *
from PySide6.QtWidgets import *

from __feature__ import snake_case, true_property


class Menu(QMainWindow):

    def setup_ui(self):

        self.size = QSize(450, 500) 

        #Layout
        self.root_layout = QVBoxLayout()

        self.frame_titulo = QFrame()
        self.frame_inputs = QFrame()

        self.root_layout.add_widget(self.frame_titulo, 30)
        self.root_layout.add_widget(self.frame_inputs, 70)

        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)


        self.set_central_widget(self.widget)
        self.style_sheet = estilos_menu
        self.setup_inputs_frame()
        self.setup_title_frame()

    def setup_title_frame(self):

        self.title = QLabel("TIC TAC TOE", object_name="titulo_principal", alignment=Qt.AlignCenter)
        self.title_layout = QVBoxLayout()
        self.title_layout.add_widget(self.title)
        self.frame_titulo.set_layout(self.title_layout)

    def setup_inputs_frame(self):

        self.inputs_title = QLabel("Ingrese el nombre de los jugadores", alignment=Qt.AlignCenter)

        self.player_1 = QLineEdit(placeholder_text = "Jugador 1")
        self.player_2 = QLineEdit(placeholder_text = "Jugador 2")

        self.play_button = QPushButton("Jugar")

        self.inputs_layout = QVBoxLayout()

        widgets = [self.inputs_title, self.player_1, self.player_2, self.play_button]
        
        for w in widgets:

            self.inputs_layout.add_widget(w)

            self.inputs_layout.add_spacing(10)

        # Relleno
        self.inputs_layout.add_stretch()

        self.frame_inputs.set_layout(self.inputs_layout)
    
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