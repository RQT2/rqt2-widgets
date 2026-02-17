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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1209, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(670, 550))
        icon = QIcon()
        icon.addFile(u"icons/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NAVHome = QPushButton(Widget)
        self.NAVHome.setObjectName(u"NAVHome")
        self.NAVHome.setEnabled(False)

        self.verticalLayout.addWidget(self.NAVHome)

        self.NAVInstall = QPushButton(Widget)
        self.NAVInstall.setObjectName(u"NAVInstall")
        self.NAVInstall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.NAVInstall)

        self.NAVDocs = QPushButton(Widget)
        self.NAVDocs.setObjectName(u"NAVDocs")
        self.NAVDocs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.NAVDocs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.LABELTitleWelcome = QLabel(Widget)
        self.LABELTitleWelcome.setObjectName(u"LABELTitleWelcome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LABELTitleWelcome.sizePolicy().hasHeightForWidth())
        self.LABELTitleWelcome.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(64)
        self.LABELTitleWelcome.setFont(font)
        self.LABELTitleWelcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LABELTitleWelcome.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.LABELTitleWelcome)

        self.LABELInfoWelcome = QLabel(Widget)
        self.LABELInfoWelcome.setObjectName(u"LABELInfoWelcome")
        sizePolicy1.setHeightForWidth(self.LABELInfoWelcome.sizePolicy().hasHeightForWidth())
        self.LABELInfoWelcome.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setItalic(True)
        self.LABELInfoWelcome.setFont(font1)
        self.LABELInfoWelcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LABELInfoWelcome.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.LABELInfoWelcome)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FRAMENew = QFrame(Widget)
        self.FRAMENew.setObjectName(u"FRAMENew")
        self.FRAMENew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FRAMENew.setAutoFillBackground(True)
        self.FRAMENew.setFrameShape(QFrame.Shape.Box)
        self.FRAMENew.setFrameShadow(QFrame.Shadow.Plain)
        self.FRAMENew.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.FRAMENew)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ICONNew = QLabel(self.FRAMENew)
        self.ICONNew.setObjectName(u"ICONNew")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(32)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ICONNew.sizePolicy().hasHeightForWidth())
        self.ICONNew.setSizePolicy(sizePolicy2)
        self.ICONNew.setMaximumSize(QSize(256, 256))
        self.ICONNew.setPixmap(QPixmap(u"icons/nes.svg"))
        self.ICONNew.setScaledContents(True)
        self.ICONNew.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.ICONNew)

        self.LABELTitleNew = QLabel(self.FRAMENew)
        self.LABELTitleNew.setObjectName(u"LABELTitleNew")
        sizePolicy1.setHeightForWidth(self.LABELTitleNew.sizePolicy().hasHeightForWidth())
        self.LABELTitleNew.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setBold(True)
        self.LABELTitleNew.setFont(font2)

        self.verticalLayout_3.addWidget(self.LABELTitleNew)

        self.LABELInfoNew = QLabel(self.FRAMENew)
        self.LABELInfoNew.setObjectName(u"LABELInfoNew")
        sizePolicy1.setHeightForWidth(self.LABELInfoNew.sizePolicy().hasHeightForWidth())
        self.LABELInfoNew.setSizePolicy(sizePolicy1)
        self.LABELInfoNew.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.LABELInfoNew)


        self.horizontalLayout_2.addWidget(self.FRAMENew)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.FRAMEOpen = QFrame(Widget)
        self.FRAMEOpen.setObjectName(u"FRAMEOpen")
        self.FRAMEOpen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FRAMEOpen.setAutoFillBackground(True)
        self.FRAMEOpen.setFrameShape(QFrame.Shape.Box)
        self.verticalLayout_4 = QVBoxLayout(self.FRAMEOpen)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ICONOpen = QLabel(self.FRAMEOpen)
        self.ICONOpen.setObjectName(u"ICONOpen")
        self.ICONOpen.setMaximumSize(QSize(256, 256))
        self.ICONOpen.setPixmap(QPixmap(u"icons/open.svg"))
        self.ICONOpen.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.ICONOpen)

        self.LABELTitleOpen = QLabel(self.FRAMEOpen)
        self.LABELTitleOpen.setObjectName(u"LABELTitleOpen")
        sizePolicy1.setHeightForWidth(self.LABELTitleOpen.sizePolicy().hasHeightForWidth())
        self.LABELTitleOpen.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        self.LABELTitleOpen.setFont(font3)

        self.verticalLayout_4.addWidget(self.LABELTitleOpen)

        self.LABELInfoOpen = QLabel(self.FRAMEOpen)
        self.LABELInfoOpen.setObjectName(u"LABELInfoOpen")
        sizePolicy1.setHeightForWidth(self.LABELInfoOpen.sizePolicy().hasHeightForWidth())
        self.LABELInfoOpen.setSizePolicy(sizePolicy1)
        self.LABELInfoOpen.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.LABELInfoOpen)


        self.horizontalLayout_2.addWidget(self.FRAMEOpen)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.FRAMEClone = QFrame(Widget)
        self.FRAMEClone.setObjectName(u"FRAMEClone")
        self.FRAMEClone.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FRAMEClone.setAutoFillBackground(True)
        self.FRAMEClone.setFrameShape(QFrame.Shape.Box)
        self.verticalLayout_5 = QVBoxLayout(self.FRAMEClone)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ICONClone = QLabel(self.FRAMEClone)
        self.ICONClone.setObjectName(u"ICONClone")
        self.ICONClone.setMaximumSize(QSize(256, 256))
        self.ICONClone.setPixmap(QPixmap(u"icons/clone.svg"))
        self.ICONClone.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.ICONClone)

        self.LABELTitleClone = QLabel(self.FRAMEClone)
        self.LABELTitleClone.setObjectName(u"LABELTitleClone")
        sizePolicy1.setHeightForWidth(self.LABELTitleClone.sizePolicy().hasHeightForWidth())
        self.LABELTitleClone.setSizePolicy(sizePolicy1)
        self.LABELTitleClone.setFont(font2)

        self.verticalLayout_5.addWidget(self.LABELTitleClone)

        self.LABELInfoClone = QLabel(self.FRAMEClone)
        self.LABELInfoClone.setObjectName(u"LABELInfoClone")
        sizePolicy1.setHeightForWidth(self.LABELInfoClone.sizePolicy().hasHeightForWidth())
        self.LABELInfoClone.setSizePolicy(sizePolicy1)
        self.LABELInfoClone.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.LABELInfoClone)


        self.horizontalLayout_2.addWidget(self.FRAMEClone)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQT2 IDE", None))
        self.NAVHome.setText(QCoreApplication.translate("Widget", u"Proyectos", None))
        self.NAVInstall.setText(QCoreApplication.translate("Widget", u"Dependencias", None))
        self.NAVDocs.setText(QCoreApplication.translate("Widget", u"Documentaci\u00f3n", None))
        self.LABELTitleWelcome.setText(QCoreApplication.translate("Widget", u"Bienvenido a RQT2 IDE", None))
        self.LABELInfoWelcome.setText(QCoreApplication.translate("Widget", u"Crea un nuevo espacio de trabajo para iniciar desde cero.\n"
"O carga un espacio de trabajo existente en el almacenamiento local", None))
        self.ICONNew.setText("")
        self.LABELTitleNew.setText(QCoreApplication.translate("Widget", u"Nuevo", None))
        self.LABELInfoNew.setText(QCoreApplication.translate("Widget", u"espacio de trabajo", None))
        self.ICONOpen.setText("")
        self.LABELTitleOpen.setText(QCoreApplication.translate("Widget", u"Cargar", None))
        self.LABELInfoOpen.setText(QCoreApplication.translate("Widget", u"espacio de trabajao", None))
        self.ICONClone.setText("")
        self.LABELTitleClone.setText(QCoreApplication.translate("Widget", u"Clonar", None))
        self.LABELInfoClone.setText(QCoreApplication.translate("Widget", u"espacio de trabajo", None))
    # retranslateUi

