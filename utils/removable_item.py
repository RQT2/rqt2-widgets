from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
import os


class RemovableItemWidget(QWidget):
    """Small widget that shows a label and a removable button.

    Backwards-compatible: exposes `.label` and `.button` attributes.

    This refactor makes parameters optional and ensures the label uses
    `QSizePolicy.MinimumExpanding` by default so it behaves like the fallback
    QLabel used in generated forms when `RemovableItemWidget` can't be loaded.
    """

    removed = Signal()

    def __init__(self, text: str = "", parent=None, icon_path: str = None, *, expand_label: bool = True):
        super().__init__(parent)
        self.setProperty('role', 'removable-item')
        self.setProperty('variant', 'default')
        self.setProperty('state', 'normal')

        # robustly handle missing/None text
        self.label = QLabel(text or "", self)

        # ensure label expands like the fallback QLabel used across forms
        if expand_label:
            sp = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
            sp.setHorizontalStretch(0)
            sp.setVerticalStretch(0)
            sp.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
            self.label.setSizePolicy(sp)

        self.button = QPushButton(self)
        self.button.setProperty('role', 'close')
        self.button.setProperty('variant', 'default')
        self.button.setProperty('state', 'normal')

        # try to set an icon if provided and valid, otherwise use a fallback text
        icon_set = False
        if icon_path:
            try:
                icon = QIcon(icon_path)
                if not icon.isNull():
                    self.button.setIcon(icon)
                    icon_set = True
            except Exception:
                icon_set = False

        if not icon_set:
            # do not attempt to load a bundled default icon path that may not exist;
            # show a small 'x' as a safe fallback
            self.button.setText('x')

        self.button.clicked.connect(self._on_remove)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def _on_remove(self):
        self.setParent(None)
        self.removed.emit()

    # convenience helpers that downstream code may use
    def set_text(self, text: str):
        self.label.setText(text or "")

    def set_icon(self, icon_path: str):
        try:
            icon = QIcon(icon_path)
            if not icon.isNull():
                self.button.setIcon(icon)
                self.button.setText('')
                return True
        except Exception:
            pass
        return False
