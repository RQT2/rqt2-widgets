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
from f5_ui_wizard_init import Ui_Widget as Ui_WizInit
from f6_ui_wizard_opt import Ui_Widget as Ui_WizOpt
from f7_ui_wizard_install_config import Ui_Widget as Ui_WizConfig
from f8_ui_wizard_installed import Ui_Widget as Ui_WizProgress
from f9_ui_wizard_close import Ui_Widget as Ui_WizClose

from g1_ui_text_editor import Ui_Widget as Ui_TextEditor
from g2_ui_compiler import Ui_Widget as Ui_Compiler
from g3_ui_twist_controller import Ui_Widget as Ui_Twist
from g4_ui_ssh import Ui_Widget as Ui_Ssh

try:
    from ..utils.base_window import DemoWindow
except (ImportError, ValueError):
    import os
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.base_window import DemoWindow
    
theme = 'dark.qss'  # or 'light.qss'
logo_variant = 'color'  # or 'dark' or 'light'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    import os
    base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

    try:
        fonts_base = os.path.normpath(os.path.join(base, '..', 'rqt2-components', 'assets', 'fonts'))
        candidates = [
            os.path.join(fonts_base, 'Nunito_Sans'),
            os.path.join(fonts_base, 'Ubuntu_Mono'),
            os.path.join(fonts_base, 'Ubuntu_Mono_Nerd_Font'),
            fonts_base,
        ]
        loaded_families = []
        for fd in candidates:
            if not fd or not os.path.exists(fd):
                continue
            if os.path.isdir(fd):
                for fn in os.listdir(fd):
                    if not fn.lower().endswith(('.ttf', '.otf')):
                        continue
                    path = os.path.join(fd, fn)
                    try:
                        fid = QFontDatabase.addApplicationFont(path)
                        if fid != -1:
                            families = QFontDatabase.applicationFontFamilies(fid)
                            if families and families[0] not in loaded_families:
                                loaded_families.append(families[0])
                    except Exception:
                        pass
        app_default = None
        for fam in loaded_families:
            if "nunito" in fam.lower():
                app_default = fam
                break
        if not app_default and loaded_families:
            app_default = loaded_families[0]
        if app_default:
            app.setFont(QFont(app_default))
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
        #(Ui_Form, "RQT2 IDE / *", True, True),
        #(Ui_Main, "RQT2 IDE", False, False),
        #(Ui_New, "RQT2 IDE / Nuevo espacio de trabajo", False, False),
        #(Ui_Clone, "RQT2 IDE / Clonar espacio de trabajo", False, False),
        #(Ui_Pkg, "RQT2 IDE / Gestor de instalación", False, False),
        #(Ui_WizInit, "RQT2 IDE / Asistente de Instalación", False, False),
        #(Ui_WizOpt, "RQT2 IDE / Opciones de Instalación", False, False),
        #(Ui_WizConfig, "RQT2 IDE / Versión de ROS2", False, False),
        #(Ui_WizProgress, "RQT2 IDE / Progreso de Instalación", False, False),
        #(Ui_WizClose, "RQT2 IDE / Finalizar Instalación", False, False),
        #(Ui_TextEditor, "RQT2 IDE / *", True, True),
        #(Ui_Compiler, "RQT2 IDE / *", True, False),
        #(Ui_Twist, "RQT2 IDE / *", True, False),
        (Ui_Ssh, "RQT2 IDE / *", True, False)
    ]

    for ui_class, title, show_daemon, show_tab in mapping:
        w = DemoWindow(ui_class, title=title, icon_dirs=icons_dirs, show_daemon=show_daemon, 
            logo_variant=logo_variant, show_tab=show_tab, theme=theme)
        w.show()
        windows.append(w)

    sys.exit(app.exec())
