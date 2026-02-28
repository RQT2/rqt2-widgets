# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import importlib.util
import os
from PySide6 import QtWidgets as _qtw

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
        Widget.resize(575, 350)
        Widget.setMinimumSize(QSize(575, 350))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout = _qtw.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LABELSearch = QLabel(Widget)
        self.LABELSearch.setObjectName(u"LABELSearch")

        self.horizontalLayout.addWidget(self.LABELSearch)

        self.EDITSearch = QLineEdit(Widget)
        self.EDITSearch.setObjectName(u"EDITSearch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EDITSearch.sizePolicy().hasHeightForWidth())
        self.EDITSearch.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.EDITSearch)

        self.CBOPT1Search = QCheckBox(Widget)
        self.CBOPT1Search.setObjectName(u"CBOPT1Search")
        self.CBOPT1Search.setChecked(True)

        self.horizontalLayout.addWidget(self.CBOPT1Search)

        self.CBOPT2Search = QCheckBox(Widget)
        self.CBOPT2Search.setObjectName(u"CBOPT2Search")
        self.CBOPT2Search.setChecked(True)

        self.horizontalLayout.addWidget(self.CBOPT2Search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 555, 262))
        self.verticalLayout_3 = _qtw.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        # try to use helper from utils.package_item to add rows into the grid
        try:
            utils_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'package_item.py'))
            spec = importlib.util.spec_from_file_location('package_item', utils_path)
            pkg_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(pkg_mod)
            add_package_row = pkg_mod.add_package_row

            # add an example row (grid row 1, logical index 0)
            #for i in range(20):
            #    add_package_row(self.gridLayout, i+1, i, f"ros2-jazzy{i}", "ver", parent=self.scrollAreaWidgetContents)
        except Exception:
            # fallback: create simple widgets matching the original naming
            self.BUTTONInstall0 = QPushButton(self.scrollAreaWidgetContents)
            self.BUTTONInstall0.setObjectName(u"BUTTONInstall0")
            self.gridLayout.addWidget(self.BUTTONInstall0, 1, 3, 1, 1)

            self.PKGLINKS0 = QLabel(self.scrollAreaWidgetContents)
            self.PKGLINKS0.setObjectName(u"PKGLINKS0")
            self.PKGLINKS0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.gridLayout.addWidget(self.PKGLINKS0, 1, 1, 1, 1)

            self.PKGName0 = QLabel(self.scrollAreaWidgetContents)
            self.PKGName0.setObjectName(u"PKGName0")
            sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
            sizePolicy3.setHorizontalStretch(0)
            sizePolicy3.setVerticalStretch(0)
            sizePolicy3.setHeightForWidth(self.PKGName0.sizePolicy().hasHeightForWidth())
            self.PKGName0.setSizePolicy(sizePolicy3)
            self.gridLayout.addWidget(self.PKGName0, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # ensure we keep the spacer below the grid; package rows should be
        # inserted into the gridLayout (columns: 0=name, 1=links, 3=action)
        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.BTNApply = QPushButton(Widget)
        self.BTNApply.setObjectName(u"BTNApply")

        self.horizontalLayout_2.addWidget(self.BTNApply)

        self.BTNAccept = QPushButton(Widget)
        self.BTNAccept.setObjectName(u"BTNAccept")

        self.horizontalLayout_2.addWidget(self.BTNAccept)

        self.BTNCancell = QPushButton(Widget)
        self.BTNCancell.setObjectName(u"BTNCancell")

        self.horizontalLayout_2.addWidget(self.BTNCancell)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQT2 IDE / Gestor de paquetes", None))
        self.LABELSearch.setText(QCoreApplication.translate("Widget", u"Buscar", None))
        self.EDITSearch.setText(QCoreApplication.translate("Widget", u"*", None))
        self.CBOPT1Search.setText(QCoreApplication.translate("Widget", u"Herramientas", None))
        self.CBOPT2Search.setText(QCoreApplication.translate("Widget", u"Dependencias", None))
        #self.BUTTONInstall0.setText(QCoreApplication.translate("Widget", u"Instalar", None))
        # links text for first package row
        #self.PKGName0.setText(QCoreApplication.translate("Widget", u"ros2-jazzy", None))
        self.BTNApply.setText(QCoreApplication.translate("Widget", u"Aplicar", None))
        self.BTNAccept.setText(QCoreApplication.translate("Widget", u"Aceptar", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

