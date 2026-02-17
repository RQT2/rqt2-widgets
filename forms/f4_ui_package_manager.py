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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(575, 350)
        Widget.setMinimumSize(QSize(575, 350))
        icon = QIcon()
        icon.addFile(u"icons/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Widget)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 555, 267))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TABLE = QTableWidget(self.scrollAreaWidgetContents)
        if (self.TABLE.columnCount() < 3):
            self.TABLE.setColumnCount(3)
        font = QFont()
        font.setHintingPreference(QFont.PreferFullHinting)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        self.TABLE.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.TABLE.setObjectName(u"TABLE")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TABLE.sizePolicy().hasHeightForWidth())
        self.TABLE.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.TABLE)

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
        ___qtablewidgetitem = self.TABLE.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Nombre", None));
        ___qtablewidgetitem1 = self.TABLE.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Depende de", None));
        ___qtablewidgetitem2 = self.TABLE.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Instal", None));
        self.BTNApply.setText(QCoreApplication.translate("Widget", u"Aplicar", None))
        self.BTNAccept.setText(QCoreApplication.translate("Widget", u"Aceptar", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

