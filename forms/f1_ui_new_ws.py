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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(730, 870)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(730, 870))
        icon = QIcon()
        icon.addFile(u"icons/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout_17 = QVBoxLayout(Widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.LABELWSNew = QLabel(Widget)
        self.LABELWSNew.setObjectName(u"LABELWSNew")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LABELWSNew.sizePolicy().hasHeightForWidth())
        self.LABELWSNew.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.LABELWSNew)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.EDITWSNew = QLineEdit(Widget)
        self.EDITWSNew.setObjectName(u"EDITWSNew")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.EDITWSNew.sizePolicy().hasHeightForWidth())
        self.EDITWSNew.setSizePolicy(sizePolicy2)
        self.EDITWSNew.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.EDITWSNew)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.LABELPKGNew = QLabel(Widget)
        self.LABELPKGNew.setObjectName(u"LABELPKGNew")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LABELPKGNew.sizePolicy().hasHeightForWidth())
        self.LABELPKGNew.setSizePolicy(sizePolicy3)
        self.LABELPKGNew.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.LABELPKGNew)

        self.EDITPKGNew = QLineEdit(Widget)
        self.EDITPKGNew.setObjectName(u"EDITPKGNew")
        sizePolicy2.setHeightForWidth(self.EDITPKGNew.sizePolicy().hasHeightForWidth())
        self.EDITPKGNew.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.EDITPKGNew)

        self.BTNPKGNew = QPushButton(Widget)
        self.BTNPKGNew.setObjectName(u"BTNPKGNew")
        icon1 = QIcon()
        icon1.addFile(u"icons/nes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPKGNew.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.BTNPKGNew)


        self.verticalLayout_17.addLayout(self.horizontalLayout_8)

        self.TABPKGNew = QTabWidget(Widget)
        self.TABPKGNew.setObjectName(u"TABPKGNew")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.TABPKGNew.sizePolicy().hasHeightForWidth())
        self.TABPKGNew.setSizePolicy(sizePolicy4)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.LABELPKGInfo = QLabel(self.tab)
        self.LABELPKGInfo.setObjectName(u"LABELPKGInfo")

        self.verticalLayout_4.addWidget(self.LABELPKGInfo)

        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 510))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.LABELPKGDescription = QLabel(self.scrollAreaWidgetContents)
        self.LABELPKGDescription.setObjectName(u"LABELPKGDescription")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.LABELPKGDescription.sizePolicy().hasHeightForWidth())
        self.LABELPKGDescription.setSizePolicy(sizePolicy5)
        self.LABELPKGDescription.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.LABELPKGDescription)

        self.EDITPKGDescription = QLineEdit(self.scrollAreaWidgetContents)
        self.EDITPKGDescription.setObjectName(u"EDITPKGDescription")

        self.horizontalLayout_15.addWidget(self.EDITPKGDescription)

        self.LABELPKGLicense = QLabel(self.scrollAreaWidgetContents)
        self.LABELPKGLicense.setObjectName(u"LABELPKGLicense")
        sizePolicy5.setHeightForWidth(self.LABELPKGLicense.sizePolicy().hasHeightForWidth())
        self.LABELPKGLicense.setSizePolicy(sizePolicy5)
        self.LABELPKGLicense.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.LABELPKGLicense)

        self.CBPKGLicense = QComboBox(self.scrollAreaWidgetContents)
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.setObjectName(u"CBPKGLicense")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.CBPKGLicense.sizePolicy().hasHeightForWidth())
        self.CBPKGLicense.setSizePolicy(sizePolicy6)

        self.horizontalLayout_15.addWidget(self.CBPKGLicense)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.GROUPPKGConf = QGroupBox(self.scrollAreaWidgetContents)
        self.GROUPPKGConf.setObjectName(u"GROUPPKGConf")
        sizePolicy5.setHeightForWidth(self.GROUPPKGConf.sizePolicy().hasHeightForWidth())
        self.GROUPPKGConf.setSizePolicy(sizePolicy5)
        self.horizontalLayout_5 = QHBoxLayout(self.GROUPPKGConf)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.GROUPPKGConf)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LABELPKGAment = QLabel(self.frame)
        self.LABELPKGAment.setObjectName(u"LABELPKGAment")
        sizePolicy1.setHeightForWidth(self.LABELPKGAment.sizePolicy().hasHeightForWidth())
        self.LABELPKGAment.setSizePolicy(sizePolicy1)
        self.LABELPKGAment.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.LABELPKGAment)

        self.CBPKGAment = QComboBox(self.frame)
        self.CBPKGAment.addItem("")
        self.CBPKGAment.addItem("")
        self.CBPKGAment.setObjectName(u"CBPKGAment")
        sizePolicy2.setHeightForWidth(self.CBPKGAment.sizePolicy().hasHeightForWidth())
        self.CBPKGAment.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.CBPKGAment)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.INFOPKGAment = QLabel(self.frame)
        self.INFOPKGAment.setObjectName(u"INFOPKGAment")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.INFOPKGAment.sizePolicy().hasHeightForWidth())
        self.INFOPKGAment.setSizePolicy(sizePolicy7)
        font = QFont()
        font.setItalic(True)
        self.INFOPKGAment.setFont(font)
        self.INFOPKGAment.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.INFOPKGAment)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.GROUPPKGConf)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LABELXMLVer = QLabel(self.frame_2)
        self.LABELXMLVer.setObjectName(u"LABELXMLVer")
        sizePolicy3.setHeightForWidth(self.LABELXMLVer.sizePolicy().hasHeightForWidth())
        self.LABELXMLVer.setSizePolicy(sizePolicy3)
        self.LABELXMLVer.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.LABELXMLVer)

        self.SPINXMLVer = QDoubleSpinBox(self.frame_2)
        self.SPINXMLVer.setObjectName(u"SPINXMLVer")
        self.SPINXMLVer.setDecimals(1)
        self.SPINXMLVer.setSingleStep(0.100000000000000)
        self.SPINXMLVer.setValue(1.000000000000000)

        self.horizontalLayout_6.addWidget(self.SPINXMLVer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.INFOXMLVer = QLabel(self.frame_2)
        self.INFOXMLVer.setObjectName(u"INFOXMLVer")
        sizePolicy3.setHeightForWidth(self.INFOXMLVer.sizePolicy().hasHeightForWidth())
        self.INFOXMLVer.setSizePolicy(sizePolicy3)
        self.INFOXMLVer.setFont(font)
        self.INFOXMLVer.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.INFOXMLVer)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.GROUPPKGConf)

        self.GROUPMainteiner = QGroupBox(self.scrollAreaWidgetContents)
        self.GROUPMainteiner.setObjectName(u"GROUPMainteiner")
        sizePolicy5.setHeightForWidth(self.GROUPMainteiner.sizePolicy().hasHeightForWidth())
        self.GROUPMainteiner.setSizePolicy(sizePolicy5)
        self.verticalLayout_12 = QVBoxLayout(self.GROUPMainteiner)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.LABELMAINTName = QLabel(self.GROUPMainteiner)
        self.LABELMAINTName.setObjectName(u"LABELMAINTName")
        self.LABELMAINTName.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.LABELMAINTName)

        self.EDITMAINTName = QLineEdit(self.GROUPMainteiner)
        self.EDITMAINTName.setObjectName(u"EDITMAINTName")

        self.horizontalLayout_11.addWidget(self.EDITMAINTName)

        self.LABELMAINTEmail = QLabel(self.GROUPMainteiner)
        self.LABELMAINTEmail.setObjectName(u"LABELMAINTEmail")
        self.LABELMAINTEmail.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.LABELMAINTEmail)

        self.EDITMAINTEmail = QLineEdit(self.GROUPMainteiner)
        self.EDITMAINTEmail.setObjectName(u"EDITMAINTEmail")

        self.horizontalLayout_11.addWidget(self.EDITMAINTEmail)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_2.addWidget(self.GROUPMainteiner)

        self.GROUPConf = QGroupBox(self.scrollAreaWidgetContents)
        self.GROUPConf.setObjectName(u"GROUPConf")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.GROUPConf.sizePolicy().hasHeightForWidth())
        self.GROUPConf.setSizePolicy(sizePolicy8)
        self.verticalLayout_8 = QVBoxLayout(self.GROUPConf)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.LABELPKGDir = QLabel(self.GROUPConf)
        self.LABELPKGDir.setObjectName(u"LABELPKGDir")
        sizePolicy1.setHeightForWidth(self.LABELPKGDir.sizePolicy().hasHeightForWidth())
        self.LABELPKGDir.setSizePolicy(sizePolicy1)
        self.LABELPKGDir.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.LABELPKGDir)

        self.EDITPKGDir = QLineEdit(self.GROUPConf)
        self.EDITPKGDir.setObjectName(u"EDITPKGDir")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.EDITPKGDir.sizePolicy().hasHeightForWidth())
        self.EDITPKGDir.setSizePolicy(sizePolicy9)

        self.horizontalLayout_12.addWidget(self.EDITPKGDir)

        self.BTNPKGDir = QPushButton(self.GROUPConf)
        self.BTNPKGDir.setObjectName(u"BTNPKGDir")
        self.BTNPKGDir.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.BTNPKGDir.sizePolicy().hasHeightForWidth())
        self.BTNPKGDir.setSizePolicy(sizePolicy10)
        self.BTNPKGDir.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.BTNPKGDir.setIcon(icon2)

        self.horizontalLayout_12.addWidget(self.BTNPKGDir)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.LABELPKGApts = QLabel(self.GROUPConf)
        self.LABELPKGApts.setObjectName(u"LABELPKGApts")
        sizePolicy1.setHeightForWidth(self.LABELPKGApts.sizePolicy().hasHeightForWidth())
        self.LABELPKGApts.setSizePolicy(sizePolicy1)
        self.LABELPKGApts.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.LABELPKGApts.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.LABELPKGApts)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.EDITPKGApts = QLineEdit(self.GROUPConf)
        self.EDITPKGApts.setObjectName(u"EDITPKGApts")

        self.horizontalLayout_14.addWidget(self.EDITPKGApts)

        self.BTNPKGApts = QPushButton(self.GROUPConf)
        self.BTNPKGApts.setObjectName(u"BTNPKGApts")
        self.BTNPKGApts.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.BTNPKGApts)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.FRAMEPKGAdded = QFrame(self.GROUPConf)
        self.FRAMEPKGAdded.setObjectName(u"FRAMEPKGAdded")
        self.FRAMEPKGAdded.setFrameShape(QFrame.Shape.Box)
        self.FRAMEPKGAdded.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.FRAMEPKGAdded)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LAYOUTPKGAdded = QHBoxLayout()
        self.LAYOUTPKGAdded.setObjectName(u"LAYOUTPKGAdded")
        self.LABELPKGAdded = QLabel(self.FRAMEPKGAdded)
        self.LABELPKGAdded.setObjectName(u"LABELPKGAdded")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.LABELPKGAdded.sizePolicy().hasHeightForWidth())
        self.LABELPKGAdded.setSizePolicy(sizePolicy11)

        self.LAYOUTPKGAdded.addWidget(self.LABELPKGAdded)

        self.BTNPKGAdded = QPushButton(self.FRAMEPKGAdded)
        self.BTNPKGAdded.setObjectName(u"BTNPKGAdded")
        icon3 = QIcon()
        icon3.addFile(u"icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPKGAdded.setIcon(icon3)

        self.LAYOUTPKGAdded.addWidget(self.BTNPKGAdded)


        self.verticalLayout_14.addLayout(self.LAYOUTPKGAdded)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)


        self.verticalLayout_7.addWidget(self.FRAMEPKGAdded)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_2.addWidget(self.GROUPConf)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.GROUPNode = QGroupBox(self.tab)
        self.GROUPNode.setObjectName(u"GROUPNode")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.GROUPNode.sizePolicy().hasHeightForWidth())
        self.GROUPNode.setSizePolicy(sizePolicy12)
        self.verticalLayout_10 = QVBoxLayout(self.GROUPNode)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.EDITNODENew = QLineEdit(self.GROUPNode)
        self.EDITNODENew.setObjectName(u"EDITNODENew")
        sizePolicy2.setHeightForWidth(self.EDITNODENew.sizePolicy().hasHeightForWidth())
        self.EDITNODENew.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.EDITNODENew)

        self.CBNODENew = QComboBox(self.GROUPNode)
        self.CBNODENew.addItem("")
        self.CBNODENew.addItem("")
        self.CBNODENew.setObjectName(u"CBNODENew")

        self.horizontalLayout_16.addWidget(self.CBNODENew)

        self.BTNNODENew = QPushButton(self.GROUPNode)
        self.BTNNODENew.setObjectName(u"BTNNODENew")
        self.BTNNODENew.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.BTNNODENew)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.FRAMENODEAdded = QScrollArea(self.GROUPNode)
        self.FRAMENODEAdded.setObjectName(u"FRAMENODEAdded")
        sizePolicy.setHeightForWidth(self.FRAMENODEAdded.sizePolicy().hasHeightForWidth())
        self.FRAMENODEAdded.setSizePolicy(sizePolicy)
        self.FRAMENODEAdded.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 315, 90))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.LAYOUTNODEAdded = QHBoxLayout()
        self.LAYOUTNODEAdded.setObjectName(u"LAYOUTNODEAdded")
        self.LABELNODEAdded = QLabel(self.scrollAreaWidgetContents_2)
        self.LABELNODEAdded.setObjectName(u"LABELNODEAdded")
        sizePolicy11.setHeightForWidth(self.LABELNODEAdded.sizePolicy().hasHeightForWidth())
        self.LABELNODEAdded.setSizePolicy(sizePolicy11)

        self.LAYOUTNODEAdded.addWidget(self.LABELNODEAdded)

        self.BTNNODEAdded = QPushButton(self.scrollAreaWidgetContents_2)
        self.BTNNODEAdded.setObjectName(u"BTNNODEAdded")
        self.BTNNODEAdded.setIcon(icon3)

        self.LAYOUTNODEAdded.addWidget(self.BTNNODEAdded)


        self.verticalLayout_16.addLayout(self.LAYOUTNODEAdded)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)

        self.FRAMENODEAdded.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.FRAMENODEAdded)


        self.horizontalLayout_26.addWidget(self.GROUPNode)

        self.GROUPLaunch = QGroupBox(self.tab)
        self.GROUPLaunch.setObjectName(u"GROUPLaunch")
        self.verticalLayout_15 = QVBoxLayout(self.GROUPLaunch)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.EDITLAUNCHNew = QLineEdit(self.GROUPLaunch)
        self.EDITLAUNCHNew.setObjectName(u"EDITLAUNCHNew")
        sizePolicy2.setHeightForWidth(self.EDITLAUNCHNew.sizePolicy().hasHeightForWidth())
        self.EDITLAUNCHNew.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.EDITLAUNCHNew)

        self.CBLAUNCHNew = QComboBox(self.GROUPLaunch)
        self.CBLAUNCHNew.addItem("")
        self.CBLAUNCHNew.addItem("")
        self.CBLAUNCHNew.addItem("")
        self.CBLAUNCHNew.setObjectName(u"CBLAUNCHNew")

        self.horizontalLayout_17.addWidget(self.CBLAUNCHNew)

        self.BTNLAUNCHNew = QPushButton(self.GROUPLaunch)
        self.BTNLAUNCHNew.setObjectName(u"BTNLAUNCHNew")
        self.BTNLAUNCHNew.setIcon(icon1)

        self.horizontalLayout_17.addWidget(self.BTNLAUNCHNew)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)

        self.FRAMELAUNCHAdd = QScrollArea(self.GROUPLaunch)
        self.FRAMELAUNCHAdd.setObjectName(u"FRAMELAUNCHAdd")
        sizePolicy.setHeightForWidth(self.FRAMELAUNCHAdd.sizePolicy().hasHeightForWidth())
        self.FRAMELAUNCHAdd.setSizePolicy(sizePolicy)
        self.FRAMELAUNCHAdd.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 315, 90))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.LAYOUTLAUNCHAdded = QHBoxLayout()
        self.LAYOUTLAUNCHAdded.setObjectName(u"LAYOUTLAUNCHAdded")
        self.LABELLAUNCHAdded = QLabel(self.scrollAreaWidgetContents_3)
        self.LABELLAUNCHAdded.setObjectName(u"LABELLAUNCHAdded")
        sizePolicy11.setHeightForWidth(self.LABELLAUNCHAdded.sizePolicy().hasHeightForWidth())
        self.LABELLAUNCHAdded.setSizePolicy(sizePolicy11)

        self.LAYOUTLAUNCHAdded.addWidget(self.LABELLAUNCHAdded)

        self.BTNLAUNCHAdded = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNLAUNCHAdded.setObjectName(u"BTNLAUNCHAdded")
        self.BTNLAUNCHAdded.setIcon(icon3)

        self.LAYOUTLAUNCHAdded.addWidget(self.BTNLAUNCHAdded)


        self.verticalLayout_13.addLayout(self.LAYOUTLAUNCHAdded)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.FRAMELAUNCHAdd.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_15.addWidget(self.FRAMELAUNCHAdd)


        self.horizontalLayout_26.addWidget(self.GROUPLaunch)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.TABPKGNew.addTab(self.tab, "")

        self.verticalLayout_17.addWidget(self.TABPKGNew)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.BTNMake = QPushButton(Widget)
        self.BTNMake.setObjectName(u"BTNMake")

        self.horizontalLayout_19.addWidget(self.BTNMake)

        self.BTNCancell = QPushButton(Widget)
        self.BTNCancell.setObjectName(u"BTNCancell")

        self.horizontalLayout_19.addWidget(self.BTNCancell)


        self.verticalLayout_17.addLayout(self.horizontalLayout_19)


        self.retranslateUi(Widget)

        self.TABPKGNew.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQT2 IDE / Nuevo espacio de trabajo", None))
        self.LABELWSNew.setText(QCoreApplication.translate("Widget", u"Nombre del nuevo espacio de trabajo:", None))
        self.EDITWSNew.setPlaceholderText(QCoreApplication.translate("Widget", u"ros2_ws", None))
        self.LABELPKGNew.setText(QCoreApplication.translate("Widget", u"Nombre del paquete a incluir:", None))
        self.EDITPKGNew.setPlaceholderText(QCoreApplication.translate("Widget", u"my_pkg", None))
        self.BTNPKGNew.setText(QCoreApplication.translate("Widget", u"Paquete", None))
        self.LABELPKGInfo.setText(QCoreApplication.translate("Widget", u"Sobre el nuevo paquete", None))
        self.LABELPKGDescription.setText(QCoreApplication.translate("Widget", u"Descripci\u00f3n:", None))
        self.EDITPKGDescription.setPlaceholderText(QCoreApplication.translate("Widget", u"Proposito del nuevo paquete de ROS2.", None))
        self.LABELPKGLicense.setText(QCoreApplication.translate("Widget", u"Licencia:", None))
        self.CBPKGLicense.setItemText(0, QCoreApplication.translate("Widget", u"Apache-2.0", None))
        self.CBPKGLicense.setItemText(1, QCoreApplication.translate("Widget", u"BSL-1.0", None))
        self.CBPKGLicense.setItemText(2, QCoreApplication.translate("Widget", u"MIT", None))
        self.CBPKGLicense.setItemText(3, QCoreApplication.translate("Widget", u"MIT-0", None))
        self.CBPKGLicense.setItemText(4, QCoreApplication.translate("Widget", u"GPL-3.0-only", None))
        self.CBPKGLicense.setItemText(5, QCoreApplication.translate("Widget", u"LGPL-3.0-only", None))
        self.CBPKGLicense.setItemText(6, QCoreApplication.translate("Widget", u"BSD-2.0", None))
        self.CBPKGLicense.setItemText(7, QCoreApplication.translate("Widget", u"BSD-2.Clause", None))
        self.CBPKGLicense.setItemText(8, QCoreApplication.translate("Widget", u"BSD-3.Clause", None))

        self.GROUPPKGConf.setTitle(QCoreApplication.translate("Widget", u"Configuraci\u00f3n del paquete", None))
        self.LABELPKGAment.setText(QCoreApplication.translate("Widget", u"Tipo de construcci\u00f3n:", None))
        self.CBPKGAment.setItemText(0, QCoreApplication.translate("Widget", u"Python [ament_python]", None))
        self.CBPKGAment.setItemText(1, QCoreApplication.translate("Widget", u"CMake [ament_cmake]", None))

        self.INFOPKGAment.setText(QCoreApplication.translate("Widget", u"Sistema de compilaci\u00f3n del nuevo paquete.", None))
        self.LABELXMLVer.setText(QCoreApplication.translate("Widget", u"XML Format versi\u00f3n:", None))
        self.INFOXMLVer.setText(QCoreApplication.translate("Widget", u"Versi\u00f3n de XML para el archivo package.xml generado para el nuevo paquete de ROS2.", None))
        self.GROUPMainteiner.setTitle(QCoreApplication.translate("Widget", u"Sobre el responsable del paquete", None))
        self.LABELMAINTName.setText(QCoreApplication.translate("Widget", u"Nombre: ", None))
        self.LABELMAINTEmail.setText(QCoreApplication.translate("Widget", u"Correo:", None))
        self.GROUPConf.setTitle(QCoreApplication.translate("Widget", u"Conexiones", None))
        self.LABELPKGDir.setText(QCoreApplication.translate("Widget", u"Ubicaci\u00f3n de instalaci\u00f3n", None))
        self.EDITPKGDir.setPlaceholderText(QCoreApplication.translate("Widget", u"ros2_ws/src/", None))
        self.LABELPKGApts.setText(QCoreApplication.translate("Widget", u"Dependencias:", None))
        self.LABELPKGAdded.setText(QCoreApplication.translate("Widget", u"rlcpp", None))
        self.GROUPNode.setTitle(QCoreApplication.translate("Widget", u"Nodos", None))
        self.CBNODENew.setItemText(0, QCoreApplication.translate("Widget", u".py", None))
        self.CBNODENew.setItemText(1, QCoreApplication.translate("Widget", u".cpp", None))

        self.LABELNODEAdded.setText(QCoreApplication.translate("Widget", u"my_node.py", None))
        self.GROUPLaunch.setTitle(QCoreApplication.translate("Widget", u"Lanzadores", None))
        self.CBLAUNCHNew.setItemText(0, QCoreApplication.translate("Widget", u".launch.py", None))
        self.CBLAUNCHNew.setItemText(1, QCoreApplication.translate("Widget", u".yaml", None))
        self.CBLAUNCHNew.setItemText(2, QCoreApplication.translate("Widget", u".xml", None))

        self.LABELLAUNCHAdded.setText(QCoreApplication.translate("Widget", u"my_launcher.python.py", None))
        self.TABPKGNew.setTabText(self.TABPKGNew.indexOf(self.tab), QCoreApplication.translate("Widget", u"my_pkg", None))
        self.BTNMake.setText(QCoreApplication.translate("Widget", u"Crear", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

