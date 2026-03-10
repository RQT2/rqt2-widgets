import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtCore import Qt, QEvent

from .titlebar import TitleBar

class DemoWindow(QWidget):
    def __init__(self, ui_class, title: str = None, icon_dirs: list = None, parent=None, 
                 logo_variant: str = "color", show_daemon: bool = False, 
                 show_tab: bool = False, theme: str = "default.qss"):
        super().__init__(parent)
        
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self.main_container = QFrame(self)
        self.main_container.setObjectName("MainContainer")
        self.main_container.setProperty("state", "normal")
        container_layout = QVBoxLayout(self.main_container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        self.titlebar = TitleBar(self, show_daemon=show_daemon, logo_variant=logo_variant,
                                 show_tab=show_tab, icon_dirs=icon_dirs, theme=theme)
        if title:
            self.titlebar.setTitle(title)

        self.titlebar.minimizeRequested.connect(self.showMinimized)
        self.titlebar.maximizeRequested.connect(self._toggle_maximize)
        self.titlebar.closeRequested.connect(self.close)

        self.content = QWidget(self)
        self.content.setObjectName("Content")
        self.ui = ui_class()
        
        try:
            self.ui.setupUi(self.content, icon_dirs=icon_dirs, theme=theme)
        except TypeError:
            self.ui.setupUi(self.content)

        container_layout.addWidget(self.titlebar)
        container_layout.addWidget(self.content)
        layout.addWidget(self.main_container)

        self._drag_pos = None
        self._resizing = False
        self._resize_edge = None
        self.titlebar.installEventFilter(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            rect = self.rect()
            margin = 8
            
            if pos.x() > rect.width() - margin and pos.y() > rect.height() - margin:
                self._resize_edge = "both"
                self._resizing = True
            elif pos.x() > rect.width() - margin:
                self._resize_edge = "right"
                self._resizing = True
            elif pos.y() > rect.height() - margin:
                self._resize_edge = "bottom"
                self._resizing = True

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()
        rect = self.rect()
        margin = 8

        if self._resizing:
            new_width = rect.width()
            new_height = rect.height()

            if self._resize_edge in ["right", "both"]:
                new_width = pos.x()
            if self._resize_edge in ["bottom", "both"]:
                new_height = pos.y()

            self.resize(max(self.minimumWidth(), new_width), 
                        max(self.minimumHeight(), new_height))
            return

        if pos.x() > rect.width() - margin and pos.y() > rect.height() - margin:
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif pos.x() > rect.width() - margin:
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif pos.y() > rect.height() - margin:
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseReleaseEvent(self, event):
        self._resizing = False
        self._resize_edge = None
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def _toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.main_container.setProperty("state", "normal")
        else:
            self.showMaximized()
            self.main_container.setProperty("state", "maximized")
        
        self.main_container.style().unpolish(self.main_container)
        self.main_container.style().polish(self.main_container)

    def eventFilter(self, obj, event):
        if obj is self.titlebar:
            if event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                    return True
            elif event.type() == QEvent.MouseMove:
                if event.buttons() & Qt.LeftButton and self._drag_pos is not None:
                    self.move(event.globalPosition().toPoint() - self._drag_pos)
                    return True
            elif event.type() == QEvent.MouseButtonDblClick:
                self._toggle_maximize()
                return True
        return super().eventFilter(obj, event)

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            state = "maximized" if self.isMaximized() else "normal"
            self.main_container.setProperty("state", state)
            self.main_container.style().unpolish(self.main_container)
            self.main_container.style().polish(self.main_container)
        super().changeEvent(event)
