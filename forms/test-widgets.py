import sys

from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import Qt
from PySide6.QtCore import QEvent

# Small demo runner that opens all generated forms from this folder.
from ui_form import Ui_Widget as Ui_Form
from f0_ui_main import Ui_Widget as Ui_Main
from f1_ui_new_ws import Ui_Widget as Ui_New
from f3_ui_clone_ws import Ui_Widget as Ui_Clone
from f4_ui_package_manager import Ui_Widget as Ui_Pkg

try:
    from ..utils.titlebar import TitleBar
except Exception:
    import importlib.util as _il, os as _os
    _spec = _il.spec_from_file_location("titlebar", _os.path.join(_os.path.dirname(__file__), "..", "utils", "titlebar.py"))
    _mod = _il.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    TitleBar = _mod.TitleBar
    
theme = 'dark.qss'  # or 'light.qss'
logo_variant = 'color'  # or 'dark' or 'light'


class DemoWindow(QWidget):
    def __init__(self, ui_class, title: str = None, icon_dirs: list = None, parent=None, logo_variant: str = "color",
                 show_daemon: bool = False, show_tab: bool = False, theme: str = "default.qss"):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
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

        if show_daemon:
            self.titlebar.restartDaemonRequested.connect(lambda: print("[demo] restartDaemonRequested"))
        if show_tab:
            self.titlebar.splitTerminalRequested.connect(lambda: print("[demo] splitTerminalRequested"))
        self.titlebar.minimizeRequested.connect(self.showMinimized)
        self.titlebar.maximizeRequested.connect(self._toggle_maximize)
        self.titlebar.closeRequested.connect(self.close)

        layout.addWidget(self.main_container)

        self.content = QWidget(self)
        self.content.setObjectName("Content")
        self.ui = ui_class()
        try:
            self.ui.setupUi(self.content, icon_dirs=icon_dirs, theme=theme)
        except TypeError:
            self.ui.setupUi(self.content)
        container_layout.addWidget(self.titlebar)
        container_layout.addWidget(self.content)

        self._drag_pos = None
        self.titlebar.installEventFilter(self)
        self.content.setProperty('role', 'mainbox')
        self.content.setProperty('variant', 'default')
        self.content.setProperty('state', 'normal')

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.main_container.setProperty("state", "maximized")
            else:
                self.main_container.setProperty("state", "normal")
        
            self.main_container.style().unpolish(self.main_container)
            self.main_container.style().polish(self.main_container)

        super().changeEvent(event)
    
    def _toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def eventFilter(self, obj, event):
        from PySide6.QtCore import QEvent, Qt
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    import os
    base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

    try:
        fonts_base = os.path.normpath(os.path.join(base, '..', 'rqt2-components', 'assets', 'fonts'))
        candidates = [
            os.path.join(fonts_base, 'Nunito_Sans'),
            os.path.join(fonts_base, 'nunito'),
            fonts_base,
        ]
        loaded_family = None
        for fd in candidates:
            if not fd or not os.path.exists(fd):
                continue
            for fn in os.listdir(fd):
                if not fn.lower().endswith(('.ttf', '.otf')):
                    continue
                path = os.path.join(fd, fn)
                try:
                    fid = QFontDatabase.addApplicationFont(path)
                    if fid != -1:
                        families = QFontDatabase.applicationFontFamilies(fid)
                        if families:
                            loaded_family = families[0]
                except Exception:
                    pass
            if loaded_family:
                break
        if loaded_family:
            app.setFont(QFont(loaded_family))
    except Exception as e:
        pass

    qss_path = os.path.normpath(os.path.join(base, '..', 'rqt2-components', 'styles/themes', theme))
    try:
        if os.path.exists(qss_path):
            with open(qss_path, 'r') as _f:
                app.setStyleSheet(_f.read())
    except Exception as e:
        pass

    windows = []
    # define icon directories to try (order matters)
    # icon directories (order matters)
    icons_dirs = [
        os.path.join(base, '..', 'rqt2-widgets', 'icons'),
        os.path.join(base, '..', 'rqt2-components', 'assets/branding'),
        os.path.join(base, '..', 'rqt2-components', 'assets/icons')
    ]

    mapping = [
        (Ui_Form, "RQT2 IDE / *", True, True),
        (Ui_Main, "RQT2 IDE", False, False),
        (Ui_New, "RQT2 IDE / Nuevo espacio de trabajo", False, False),
        (Ui_Clone, "RQT2 IDE / Clonar espacio de trabajo", False, False),
        (Ui_Pkg, "RQT2 IDE / Gestor de instalación", False, False)
    ]

    for ui_class, title, show_daemon, show_tab in mapping:
        w = DemoWindow(ui_class, title=title, icon_dirs=icons_dirs, show_daemon=show_daemon, 
            logo_variant=logo_variant, show_tab=show_tab, theme=theme)
        w.show()
        windows.append(w)

    sys.exit(app.exec())
