from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal


class NavButton(QPushButton):
    """Botón de navegación que emite la ruta/target al ser pulsado."""

    navigate = Signal(str)

    def __init__(self, label: str = "", target: str = "", parent=None):
        super().__init__(label, parent)
        self._target = target
        self.clicked.connect(self._on_clicked)

    def _on_clicked(self):
        self.navigate.emit(self._target)

    def setTarget(self, target: str):
        self._target = target
