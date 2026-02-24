import sys

from PySide6.QtWidgets import QApplication, QWidget

# Small demo runner that opens all generated forms from this folder.
from ui_form import Ui_Widget as Ui_Form
from f0_ui_main import Ui_Widget as Ui_Main
from f1_ui_new_ws import Ui_Widget as Ui_New
from f3_ui_clone_ws import Ui_Widget as Ui_Clone
from f4_ui_package_manager import Ui_Widget as Ui_Pkg


class DemoWindow(QWidget):
    def __init__(self, ui_class, title=None, icon_dirs=None, parent=None):
        super().__init__(parent)
        self.ui = ui_class()
        # call setupUi with icon_dirs if the signature accepts it
        try:
            self.ui.setupUi(self, icon_dirs)
        except TypeError:
            # fallback for UI classes that don't accept icon_dirs
            self.ui.setupUi(self)
        if title:
            self.setWindowTitle(title)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    windows = []
    # define icon directories to try (order matters)
    import os
    base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
    icons_dirs = [
        os.path.join(base, '..', 'rqt2-widgets', 'icons'),
        os.path.join(base, '..', 'rqt2-components', 'assets/branding'),
        os.path.join(base, '..', 'rqt2-components', 'assets/icons')
    ]

    mapping = [
        (Ui_Form, "UI Form"),
        (Ui_Main, "Main"),
        (Ui_New, "New Workspace"),
        (Ui_Clone, "Clone Workspace"),
        (Ui_Pkg, "Package Manager")
    ]

    for ui_cls, title in mapping:
        w = DemoWindow(ui_cls, title=title, icon_dirs=icons_dirs)
        w.show()
        windows.append(w)

    sys.exit(app.exec())