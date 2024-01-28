# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import imgs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1177, 801)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setStyleSheet(u"border-image: url(:/img/img/6.jpg);")

        self.verticalLayout_2.addWidget(self.img)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(8)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.from_station = QLineEdit(self.frame_2)
        self.from_station.setObjectName(u"from_station")

        self.horizontalLayout_2.addWidget(self.from_station)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.to = QLineEdit(self.frame_2)
        self.to.setObjectName(u"to")

        self.horizontalLayout_2.addWidget(self.to)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.date = QLineEdit(self.frame_2)
        self.date.setObjectName(u"date")

        self.horizontalLayout_2.addWidget(self.date)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(180, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.GC = QCheckBox(self.frame_3)
        self.GC.setObjectName(u"GC")
        self.GC.setChecked(False)

        self.horizontalLayout_3.addWidget(self.GC)

        self.D = QCheckBox(self.frame_3)
        self.D.setObjectName(u"D")

        self.horizontalLayout_3.addWidget(self.D)

        self.Z = QCheckBox(self.frame_3)
        self.Z.setObjectName(u"Z")

        self.horizontalLayout_3.addWidget(self.Z)

        self.T = QCheckBox(self.frame_3)
        self.T.setObjectName(u"T")

        self.horizontalLayout_3.addWidget(self.T)

        self.K = QCheckBox(self.frame_3)
        self.K.setObjectName(u"K")

        self.horizontalLayout_3.addWidget(self.K)

        self.tips = QLabel(self.frame_3)
        self.tips.setObjectName(u"tips")
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(10)
        self.tips.setFont(font1)
        self.tips.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_3.addWidget(self.tips)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_3)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(7)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.horizontalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u53d1\u5730\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u7684\u5730\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u53d1\u65e5\u671f\uff1a", None))
        self.date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f: \u5e74-\u6708-\u65e5", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u6b21\u7c7b\u578b\uff1a", None))
        self.GC.setText(QCoreApplication.translate("MainWindow", u"GC-\u9ad8\u94c1", None))
        self.D.setText(QCoreApplication.translate("MainWindow", u"D-\u52a8\u8f66", None))
        self.Z.setText(QCoreApplication.translate("MainWindow", u"Z-\u76f4\u8fbe", None))
        self.T.setText(QCoreApplication.translate("MainWindow", u"T-\u7279\u5feb", None))
        self.K.setText(QCoreApplication.translate("MainWindow", u"K-\u5feb\u901f", None))
        self.tips.setText("")
    # retranslateUi

