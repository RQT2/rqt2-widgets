from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal


class PackageItemWidget(QWidget):
    """Widget reutilizable para un elemento del gestor de paquetes.

    Emite `install_requested` con el nombre del paquete cuando se pulsa el botón.
    """

    install_requested = Signal(str)

    def __init__(self, name: str = "", link: str = "", parent=None):
        super().__init__(parent)
        self._name = name
        self._link = link

        self.label_name = QLabel(name)
        self.label_link = QLabel(link)
        self.btn_action = QPushButton("Instalar")
        self.btn_action.clicked.connect(self._on_clicked)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label_name)
        layout.addWidget(self.label_link)
        layout.addWidget(self.btn_action)

    def _on_clicked(self):
        self.install_requested.emit(self._name)

    def setName(self, name: str):
        self._name = name
        self.label_name.setText(name)

    def setLink(self, link: str):
        self._link = link
        self.label_link.setText(link)

    def setButtonText(self, text: str):
        self.btn_action.setText(text)
