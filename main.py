import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QRect, Qt

from __feature__ import snake_case, true_property


class MyFirstWindow(QMainWindow):

    def setup_ui(self):
        self.set_fixed_size(500, 330)  # Cambiamos tamaño de la aplicación
        self.style_sheet = "background: #242526;"

        # Agregar primer QFrame
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry = QRect(10, 10, 480, 100)
        self.fr_titulo.style_sheet = "background: #0CA8AC;"

        self.titulo = QLabel(self.fr_titulo)
        self.titulo.text = "Hola!"
        self.titulo.geometry = QRect(0, 20, 480, 40)
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
        """
    

        self.fr_inputs = QFrame(self)
        self.fr_inputs.geometry = QRect(10, 120, 480, 200)
        self.fr_inputs.style_sheet = "background: #0CA8AC;"

        self.header = QLabel(self.fr_inputs)
        self.header.text = "Ingresa tu Nombre!"
        self.header.geometry = QRect(0, 20, 480, 40)
        self.header.alignment = Qt.AlignCenter
        self.header.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
        """

        # input
        self.input = QLineEdit(self.fr_inputs)
        self.input.geometry = QRect(10, 70, 460, 45)
        self.input.style_sheet = """
            background: white;
        """

        #button
        self.boton = QPushButton(self.fr_inputs)
        self.boton.text = "Click me!"
        self.boton.clicked.connect(self.obtieneTexto)
        self.boton.geometry = QRect(10, 125, 460, 40)

        #Cuadro de dialogo
        self.dialogo = QDialog(self)
        #self.dialogo.show()
        self.dialogo.set_fixed_size(300, 300)

        #Frames del dialogo
        self.fr_titulo_dialogo = QFrame(self.dialogo)
        self.fr_titulo_dialogo.geometry = QRect(10, 10, 280, 100)
        self.fr_titulo_dialogo.style_sheet = """
            background: #0CA8AC;
        """

        self.titulo_dialogo = QLabel(self.fr_titulo_dialogo)        
        self.titulo_dialogo.geometry = QRect(0, 0, 280, 100)
        self.titulo_dialogo.alignment = Qt.AlignCenter
        self.titulo_dialogo.style_sheet = """
            color: white;
            font-size: 25px;
            font-weight: bold;
        """
        #self.titulo_dialogo.text = "Hola!"

        # Imagen
        self.fr_imagen = QFrame(self.dialogo)
        self.fr_imagen.geometry = QRect(10, 120, 280, 170)
        self.fr_imagen.style_sheet = """
            background: url(./ia.jpg);
            background-position: center;
            background-repeat: no-repeat;
        """

        


    def obtieneTexto(self):

        self.titulo_dialogo.text = f"Bienvenido {self.input.text.lower().capitalize() if self.input.text else 'Capo'}"

        self.dialogo.show()

        print(self.input.text.upper())



# Ejecutar aplicación
app = QApplication(sys.argv)

window = MyFirstWindow()
window.setup_ui()
window.show()

sys.exit(app.exec())