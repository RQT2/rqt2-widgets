from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
import os


class RemovableItemWidget(QWidget):
    """Widget simple que muestra un texto y un botón para eliminar/ocultar.

    Exposición mínima: `.label` y `.button` para compatibilidad.
    """

    removed = Signal()

    def __init__(self, text: str = "", parent=None, icon_path: str = None):
        super().__init__(parent)
        self.label = QLabel(text, self)
        self.button = QPushButton(self)
        if icon_path:
            icon = QIcon(icon_path)
            self.button.setIcon(icon)
        else:
            # default close icon next to repo icons
            default = os.path.join(os.path.dirname(__file__), '..', 'forms', 'icons', 'close.svg')
            self.button.setText('x')

        self.button.clicked.connect(self._on_remove)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def _on_remove(self):
        self.setParent(None)
        self.removed.emit()
