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
        self.BUTTONInstall = QPushButton(self.scrollAreaWidgetContents)
        self.BUTTONInstall.setObjectName(u"BUTTONInstall")

        self.gridLayout.addWidget(self.BUTTONInstall, 1, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # try to create a dynamic package item list using utils.package_item.PackageItemWidget
        try:
            utils_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'package_item.py'))
            spec = importlib.util.spec_from_file_location('package_item', utils_path)
            pkg_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(pkg_mod)
            PackageItemWidget = pkg_mod.PackageItemWidget

            # example: add a sample item (real code should populate dynamically)
            self.PACKAGE_LIST_CONTAINER = QWidget(self.scrollAreaWidgetContents)
            from PySide6.QtWidgets import QVBoxLayout as _QVBoxLayout
            self._pkg_list_layout = _QVBoxLayout(self.PACKAGE_LIST_CONTAINER)
            sample = PackageItemWidget(name="ros2-jazzy", link="ver", parent=self.PACKAGE_LIST_CONTAINER)
            self._pkg_list_layout.addWidget(sample)
            self.verticalLayout_3.addWidget(self.PACKAGE_LIST_CONTAINER)
        except Exception:
            # keep original spacer and static grid if utils missing
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
        self.BUTTONInstall.setText(QCoreApplication.translate("Widget", u"Instalar", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"ver", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Depende de", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"ros2-jazzy", None))
        self.BTNApply.setText(QCoreApplication.translate("Widget", u"Aplicar", None))
        self.BTNAccept.setText(QCoreApplication.translate("Widget", u"Aceptar", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

