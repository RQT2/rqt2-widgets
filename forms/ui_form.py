# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import importlib.util
import os

# load icon helper from utils/icon_loader if available
load_qicon = None
load_qpixmap = None
placeholder = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'icons', 'placeholder.svg'))
try:
    _il_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'icon_loader.py'))
    spec = importlib.util.spec_from_file_location('icon_loader', _il_path)
    _il = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_il)
    load_qicon = _il.load_qicon
    load_qpixmap = _il.load_qpixmap
    _resolve_icon = _il._resolve_icon
except Exception:
    def load_qicon(rel_path, icon_dirs=None, fallback=None):
        ico = QIcon()
        try:
            ico.addFile(rel_path)
        except Exception:
            pass
        return ico

    def load_qpixmap(rel_path, icon_dirs=None, fallback=None):
        pix = QPixmap()
        try:
            pix.load(rel_path)
        except Exception:
            pass
        return pix

    def _resolve_icon(icon_dirs, rel_path):
        if not icon_dirs:
            return rel_path
        if isinstance(icon_dirs, (list, tuple)):
            for base in icon_dirs:
                cand = os.path.normpath(os.path.join(base, rel_path))
                if os.path.exists(cand):
                    return cand
            return rel_path
        else:
            return os.path.normpath(os.path.join(icon_dirs, rel_path))

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1060, 644)
        Widget.setMinimumSize(QSize(575, 350))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        # try to use NavButton from utils.nav
        try:
            utils_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'nav.py'))
            spec = importlib.util.spec_from_file_location('nav', utils_path)
            nav_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(nav_mod)
            NavButton = nav_mod.NavButton

            self.pushButton = NavButton(label="", target="code", parent=Widget)
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy)
            icon1 = QIcon()
            icon1_path = _resolve_icon(icon_dirs, os.path.join('icons', 'code', 'default.svg'))
            icon1.addFile(icon1_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton.setIcon(icon1)
            self.verticalLayout_2.addWidget(self.pushButton)
        except Exception:
            self.pushButton = QPushButton(Widget)
            self.pushButton.setObjectName(u"pushButton")
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy)
            icon1 = load_qicon(os.path.join('icons', 'code', 'default.svg'), icon_dirs, placeholder)
            self.pushButton.setIcon(icon1)

            self.verticalLayout_2.addWidget(self.pushButton)

        try:
            self.pushButton_2 = NavButton(label="", target="launch", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
            self.pushButton_2.setSizePolicy(sizePolicy)
            icon2 = QIcon()
            icon2_path = _resolve_icon(icon_dirs, os.path.join('icons', 'launch', 'default.svg'))
            icon2.addFile(icon2_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_2.setIcon(icon2)
            self.verticalLayout_2.addWidget(self.pushButton_2)
        except Exception:
            self.pushButton_2 = QPushButton(Widget)
            self.pushButton_2.setObjectName(u"pushButton_2")
            sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
            self.pushButton_2.setSizePolicy(sizePolicy)
            icon2 = load_qicon(os.path.join('icons', 'launch', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_2.setIcon(icon2)

            self.verticalLayout_2.addWidget(self.pushButton_2)

        try:
            self.pushButton_3 = NavButton(label="", target="teleop", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
            self.pushButton_3.setSizePolicy(sizePolicy)
            icon3 = QIcon()
            icon3_path = _resolve_icon(icon_dirs, os.path.join('icons', 'teleop', 'default.svg'))
            icon3.addFile(icon3_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_3.setIcon(icon3)
            self.verticalLayout_2.addWidget(self.pushButton_3)
        except Exception:
            self.pushButton_3 = QPushButton(Widget)
            self.pushButton_3.setObjectName(u"pushButton_3")
            sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
            self.pushButton_3.setSizePolicy(sizePolicy)
            icon3 = load_qicon(os.path.join('icons', 'teleop', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_3.setIcon(icon3)

            self.verticalLayout_2.addWidget(self.pushButton_3)

        try:
            self.pushButton_7 = NavButton(label="", target="nodes", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
            self.pushButton_7.setSizePolicy(sizePolicy)
            icon4 = QIcon()
            icon4_path = _resolve_icon(icon_dirs, os.path.join('icons', 'nodes', 'default.svg'))
            icon4.addFile(icon4_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_7.setIcon(icon4)
            self.verticalLayout_2.addWidget(self.pushButton_7)
        except Exception:
            self.pushButton_7 = QPushButton(Widget)
            self.pushButton_7.setObjectName(u"pushButton_7")
            sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
            self.pushButton_7.setSizePolicy(sizePolicy)
            icon4 = load_qicon(os.path.join('icons', 'nodes', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_7.setIcon(icon4)

            self.verticalLayout_2.addWidget(self.pushButton_7)

        try:
            self.pushButton_8 = NavButton(label="", target="ssh", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
            self.pushButton_8.setSizePolicy(sizePolicy)
            icon5 = QIcon()
            icon5_path = _resolve_icon(icon_dirs, os.path.join('icons', 'ssh', 'default.svg'))
            icon5.addFile(icon5_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_8.setIcon(icon5)
            self.verticalLayout_2.addWidget(self.pushButton_8)
        except Exception:
            self.pushButton_8 = QPushButton(Widget)
            self.pushButton_8.setObjectName(u"pushButton_8")
            sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
            self.pushButton_8.setSizePolicy(sizePolicy)
            icon5 = load_qicon(os.path.join('icons', 'ssh', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_8.setIcon(icon5)

            self.verticalLayout_2.addWidget(self.pushButton_8)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        try:
            self.pushButton_4 = NavButton(label="", target="3d", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
            self.pushButton_4.setSizePolicy(sizePolicy)
            icon6 = QIcon()
            icon6_path = _resolve_icon(icon_dirs, os.path.join('icons', '3d', 'default.svg'))
            icon6.addFile(icon6_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_4.setIcon(icon6)
            self.verticalLayout_2.addWidget(self.pushButton_4)
        except Exception:
            self.pushButton_4 = QPushButton(Widget)
            self.pushButton_4.setObjectName(u"pushButton_4")
            sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
            self.pushButton_4.setSizePolicy(sizePolicy)
            icon6 = load_qicon(os.path.join('icons', '3d', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_4.setIcon(icon6)

            self.verticalLayout_2.addWidget(self.pushButton_4)

        try:
            self.pushButton_5 = NavButton(label="", target="emulator", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
            self.pushButton_5.setSizePolicy(sizePolicy)
            icon7 = QIcon()
            icon7_path = _resolve_icon(icon_dirs, os.path.join('icons', 'emulator', 'default.svg'))
            icon7.addFile(icon7_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_5.setIcon(icon7)
            self.verticalLayout_2.addWidget(self.pushButton_5)
        except Exception:
            self.pushButton_5 = QPushButton(Widget)
            self.pushButton_5.setObjectName(u"pushButton_5")
            sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
            self.pushButton_5.setSizePolicy(sizePolicy)
            icon7 = load_qicon(os.path.join('icons', 'emulator', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_5.setIcon(icon7)

            self.verticalLayout_2.addWidget(self.pushButton_5)

        try:
            self.pushButton_6 = NavButton(label="", target="widgets", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
            self.pushButton_6.setSizePolicy(sizePolicy)
            icon8 = QIcon()
            icon8_path = _resolve_icon(icon_dirs, os.path.join('icons', 'widgets', 'default.svg'))
            icon8.addFile(icon8_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_6.setIcon(icon8)
            self.verticalLayout_2.addWidget(self.pushButton_6)
        except Exception:
            self.pushButton_6 = QPushButton(Widget)
            self.pushButton_6.setObjectName(u"pushButton_6")
            sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
            self.pushButton_6.setSizePolicy(sizePolicy)
            icon8 = load_qicon(os.path.join('icons', 'widgets', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_6.setIcon(icon8)

            self.verticalLayout_2.addWidget(self.pushButton_6)

        try:
            self.pushButton_9 = NavButton(label="", target="package", parent=Widget)
            sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
            self.pushButton_9.setSizePolicy(sizePolicy)
            icon9 = QIcon()
            icon9_path = _resolve_icon(icon_dirs, os.path.join('icons', 'package', 'default.svg'))
            icon9.addFile(icon9_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.pushButton_9.setIcon(icon9)
            self.verticalLayout_2.addWidget(self.pushButton_9)
        except Exception:
            self.pushButton_9 = QPushButton(Widget)
            self.pushButton_9.setObjectName(u"pushButton_9")
            sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
            self.pushButton_9.setSizePolicy(sizePolicy)
            icon9 = load_qicon(os.path.join('icons', 'package', 'default.svg'), icon_dirs, placeholder)
            self.pushButton_9.setIcon(icon9)

            self.verticalLayout_2.addWidget(self.pushButton_9)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQT2 IDE", None))
    # retranslateUi

