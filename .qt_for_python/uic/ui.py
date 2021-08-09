# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TextureManger(object):
    def setupUi(self, TextureManger):
        if not TextureManger.objectName():
            TextureManger.setObjectName(u"TextureManger")
        TextureManger.resize(1300, 600)
        TextureManger.setMinimumSize(QSize(1300, 600))
        TextureManger.setMaximumSize(QSize(1300, 600))
        TextureManger.setAutoFillBackground(False)
        TextureManger.setStyleSheet(u"color:rgb(176, 190, 199);\n"
"background-color: rgb(25, 34, 46);\n"
"")
        self.tabWidget = QTabWidget(TextureManger)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 1301, 601))
        self.tabWidget.setStyleSheet(u"QTabBar::tab{ background-color: #1a1f26}\n"
"QTabBar::tab:selected {\n"
"\n"
"background-color:rgb(59, 67, 71);\n"
"}\n"
"\n"
"\n"
"\n"
"QTabWidget::pane\n"
"\n"
"{\n"
"border-width: 0px;\n"
"\n"
"border-color:white;\n"
"\n"
"border-style:outset;\n"
"\n"
"border-radius: 3px;\n"
"\n"
"\n"
"}\u200b")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
#if QT_CONFIG(statustip)
        self.tab.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet(u"")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 711, 561))
        self.groupBox_2.setStyleSheet(u"QLineEdit { background-color: rgb(29, 56, 89) }\n"
"\n"
"QPushButton {\n"
"\n"
" background-color: rgb(37, 79, 107) }\n"
"\n"
"QGroupBox {border-width: 1px;\n"
"    border-style: dashed;\n"
"    border-color: rgb(195, 199, 209);}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_2.addWidget(self.label)

        self.r_lineEdit = QLineEdit(self.groupBox_2)
        self.r_lineEdit.setObjectName(u"r_lineEdit")

        self.horizontalLayout_2.addWidget(self.r_lineEdit)

        self.r_pushButton = QPushButton(self.groupBox_2)
        self.r_pushButton.setObjectName(u"r_pushButton")
        font = QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.r_pushButton.setFont(font)
        self.r_pushButton.setAutoFillBackground(False)
        self.r_pushButton.setCheckable(False)
        self.r_pushButton.setAutoRepeat(False)
        self.r_pushButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.r_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.g_lineEdit = QLineEdit(self.groupBox_2)
        self.g_lineEdit.setObjectName(u"g_lineEdit")

        self.horizontalLayout_3.addWidget(self.g_lineEdit)

        self.g_pushButton = QPushButton(self.groupBox_2)
        self.g_pushButton.setObjectName(u"g_pushButton")

        self.horizontalLayout_3.addWidget(self.g_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.b_lineEdit = QLineEdit(self.groupBox_2)
        self.b_lineEdit.setObjectName(u"b_lineEdit")

        self.horizontalLayout_4.addWidget(self.b_lineEdit)

        self.b_pushButton = QPushButton(self.groupBox_2)
        self.b_pushButton.setObjectName(u"b_pushButton")

        self.horizontalLayout_4.addWidget(self.b_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.verticalSpacer = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.tex_json = QPushButton(self.widget)
        self.tex_json.setObjectName(u"tex_json")

        self.verticalLayout_2.addWidget(self.tex_json)


        self.verticalLayout_3.addWidget(self.widget)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.label_5)

        self.basename = QLineEdit(self.groupBox)
        self.basename.setObjectName(u"basename")

        self.horizontalLayout.addWidget(self.basename)

        self.r_name = QLineEdit(self.groupBox)
        self.r_name.setObjectName(u"r_name")

        self.horizontalLayout.addWidget(self.r_name)

        self.g_name = QLineEdit(self.groupBox)
        self.g_name.setObjectName(u"g_name")

        self.horizontalLayout.addWidget(self.g_name)

        self.b_name = QLineEdit(self.groupBox)
        self.b_name.setObjectName(u"b_name")

        self.horizontalLayout.addWidget(self.b_name)

        self.tex_file_line = QLineEdit(self.groupBox)
        self.tex_file_line.setObjectName(u"tex_file_line")

        self.horizontalLayout.addWidget(self.tex_file_line)

        self.mergeButton = QPushButton(self.groupBox)
        self.mergeButton.setObjectName(u"mergeButton")
        self.mergeButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.mergeButton)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 1)

        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(self.tab)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(730, 10, 561, 561))
        font1 = QFont()
        font1.setFamily(u"BIZ UDPGothic")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.groupBox1.setFont(font1)
        self.groupBox1.setAutoFillBackground(False)
        self.groupBox1.setStyleSheet(u"QGroupBox {border-width: 3px;\n"
"    border-style: dashed;\n"
"    border-color: rgba(71, 85, 104, 242);}\n"
"\n"
"QGroupBox {background-color: rgb(36, 49, 66);}")
        self.label_image = QLabel(self.groupBox1)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(30, 40, 501, 471))
        self.label_image.setScaledContents(False)
        self.label_image.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.groupBox1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 520, 221, 20))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(TextureManger)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TextureManger)
    # setupUi

    def retranslateUi(self, TextureManger):
        TextureManger.setWindowTitle(QCoreApplication.translate("TextureManger", u"TextureManger", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TextureManger", u"RGB", None))
        self.label.setText(QCoreApplication.translate("TextureManger", u"R\uff1a", None))
        self.r_pushButton.setText(QCoreApplication.translate("TextureManger", u"........", None))
        self.label_2.setText(QCoreApplication.translate("TextureManger", u"G\uff1a", None))
        self.g_pushButton.setText(QCoreApplication.translate("TextureManger", u"........", None))
        self.label_3.setText(QCoreApplication.translate("TextureManger", u"B\uff1a", None))
        self.b_pushButton.setText(QCoreApplication.translate("TextureManger", u"........", None))
        self.pushButton_2.setText(QCoreApplication.translate("TextureManger", u"\u5feb\u901f\u5bfc\u5165", None))
        self.label_4.setText(QCoreApplication.translate("TextureManger", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.label_6.setText(QCoreApplication.translate("TextureManger", u" \u5feb\u901f\u5bfc\u5165\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("TextureManger", u" \u4fdd\u5b58\u9884\u8bbe\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("TextureManger", u"\u91cd\u7f6e", None))
        self.tex_json.setText(QCoreApplication.translate("TextureManger", u"\u4fdd\u5b58\u9884\u8bbe", None))
        self.groupBox.setTitle(QCoreApplication.translate("TextureManger", u"\u8f93\u51fa\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("TextureManger", u"\u6587\u4ef6\u540d", None))
        self.basename.setText(QCoreApplication.translate("TextureManger", u"basename", None))
        self.r_name.setText(QCoreApplication.translate("TextureManger", u"_AO", None))
        self.g_name.setText(QCoreApplication.translate("TextureManger", u"_Rough", None))
        self.b_name.setText(QCoreApplication.translate("TextureManger", u"_Metal", None))
        self.tex_file_line.setText(QCoreApplication.translate("TextureManger", u".tga", None))
        self.mergeButton.setText(QCoreApplication.translate("TextureManger", u"\u5408\u5e76\u8f93\u51fa", None))
        self.groupBox1.setTitle(QCoreApplication.translate("TextureManger", u"\u9884\u89c8", None))
        self.label_image.setText(QCoreApplication.translate("TextureManger", u"image", None))
        self.label_8.setText(QCoreApplication.translate("TextureManger", u"name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TextureManger", u"TextureMerge", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TextureManger", u"TextureTransform", None))
    # retranslateUi

