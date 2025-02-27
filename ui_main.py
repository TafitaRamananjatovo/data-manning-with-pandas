# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importexportFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 623)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 0, 711, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(700, 300))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_8.setStyleSheet("border:none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_8)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.logo = QtWidgets.QLabel(self.splitter_4)
        self.logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(50, 0))
        self.logo.setMaximumSize(QtCore.QSize(85, 85))
        self.logo.setSizeIncrement(QtCore.QSize(50, 50))
        self.logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("image_2023-03-27.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.label_2 = QtWidgets.QLabel(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: rgb(0, 159, 207);\n"
"    text-alignement: center;\n"
"    font: oblique 30pt \"Umpush\";\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.splitter_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("*{\n"
"height:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_file = QtWidgets.QPushButton(self.frame)
        self.load_file.setStyleSheet("QPushButton{\n"
"width:100px;\n"
"height : 50px;\n"
"border:solid 1px;\n"
"background-color: rgb(136, 138, 133);\n"
"border-radius : 80px;\n"
"}\n"
"QPushButton:hover{\n"
"width:100px;\n"
"height : 50px;\n"
"border:solid 1px;\n"
"background:rgb(0, 159, 207);;\n"
"border-radius : 80px;\n"
"}")
        self.load_file.setObjectName("load_file")
        self.horizontalLayout.addWidget(self.load_file)
        self.file_name = QtWidgets.QLabel(self.frame)
        self.file_name.setObjectName("file_name")
        self.horizontalLayout.addWidget(self.file_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(50, 70))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.progressBar = QtWidgets.QProgressBar(self.frame_5)
        self.progressBar.setStyleSheet("color: rgb(0, 210, 22);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setStyleSheet("border:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.frame_6)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.traitment = QtWidgets.QPushButton(self.splitter)
        self.traitment.setMinimumSize(QtCore.QSize(100, 30))
        self.traitment.setMaximumSize(QtCore.QSize(100, 30))
        self.traitment.setStyleSheet("QPushButton{\n"
"width:100px;\n"
"height : 30px;\n"
"border:solid 1px;\n"
"background:rgb(136, 138, 133);\n"
"border-radius : 80px;\n"
"}\n"
"QPushButton:hover{\n"
"width:100px;\n"
"height : 30px;\n"
"border:solid 1px;\n"
"background:rgb(78, 154, 6);\n"
"border-radius : 80px;\n"
"}")
        self.traitment.setObjectName("traitment")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_6.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.spin_items = QtWidgets.QSpinBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_items.sizePolicy().hasHeightForWidth())
        self.spin_items.setSizePolicy(sizePolicy)
        self.spin_items.setProperty("value", 50)
        self.spin_items.setObjectName("spin_items")
        self.horizontalLayout_5.addWidget(self.spin_items)
        self.show_items = QtWidgets.QPushButton(self.frame_4)
        self.show_items.setStyleSheet("QPushButton{\n"
"width:100px;\n"
"height : 30px;\n"
"border:solid 1px;\n"
"background:rgb(136, 138, 133);\n"
"border-radius : 80px;\n"
"}\n"
"QPushButton:hover{\n"
"width:100px;\n"
"height : 30px;\n"
"border:solid 1px;\n"
"background:rgb(0, 159, 207);;\n"
"border-radius : 80px;\n"
"}")
        self.show_items.setObjectName("show_items")
        self.horizontalLayout_5.addWidget(self.show_items)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setStyleSheet("QFrame{\n"
"\n"
"border:none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 673, 137))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.list_content_file = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.list_content_file.setObjectName("list_content_file")
        self.list_content_file.setColumnCount(0)
        self.list_content_file.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.list_content_file)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(100, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 49))
        self.frame_7.setStyleSheet("border : none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.export_file = QtWidgets.QPushButton(self.frame_7)
        self.export_file.setMaximumSize(QtCore.QSize(16777215, 30))
        self.export_file.setStyleSheet("QPushButton{\n"
"width:100px;\n"
"height : 50px;\n"
"border:solid 1px;\n"
"background:rgb(136, 138, 133);\n"
"border-radius : 80px;\n"
"}\n"
"QPushButton:hover{\n"
"width:100px;\n"
"height : 50px;\n"
"border:solid 1px;\n"
"background:rgb(0, 159, 207);;\n"
"border-radius : 80px;\n"
"}")
        self.export_file.setObjectName("export_file")
        self.horizontalLayout_9.addWidget(self.export_file)
        self.splitter_2 = QtWidgets.QSplitter(self.frame_7)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.path_for_exporting_file = QtWidgets.QLineEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_for_exporting_file.sizePolicy().hasHeightForWidth())
        self.path_for_exporting_file.setSizePolicy(sizePolicy)
        self.path_for_exporting_file.setMinimumSize(QtCore.QSize(100, 30))
        self.path_for_exporting_file.setMaximumSize(QtCore.QSize(16777215, 30))
        self.path_for_exporting_file.setObjectName("path_for_exporting_file")
        self.horizontalLayout_9.addWidget(self.splitter_2)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QtCore.QSize(100, 50))
        self.frame_9.setMaximumSize(QtCore.QSize(200, 50))
        self.frame_9.setStyleSheet("border : none;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.xls = QtWidgets.QRadioButton(self.frame_9)
        self.xls.setMinimumSize(QtCore.QSize(100, 0))
        self.xls.setMaximumSize(QtCore.QSize(100, 50))
        self.xls.setIconSize(QtCore.QSize(16, 16))
        self.xls.setObjectName("xls")
        self.horizontalLayout_3.addWidget(self.xls)
        self.csv = QtWidgets.QRadioButton(self.frame_9)
        self.csv.setMinimumSize(QtCore.QSize(100, 0))
        self.csv.setMaximumSize(QtCore.QSize(100, 16777215))
        self.csv.setObjectName("csv")
        self.horizontalLayout_3.addWidget(self.csv)
        self.verticalLayout.addWidget(self.frame_9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "WooCommerce Tool"))
        self.load_file.setText(_translate("MainWindow", "Load File"))
        self.file_name.setText(_translate("MainWindow", "filename..."))
        self.traitment.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Rows to show "))
        self.show_items.setText(_translate("MainWindow", "Sample"))
        self.export_file.setText(_translate("MainWindow", "Export file"))
        self.xls.setText(_translate("MainWindow", "xlsx"))
        self.csv.setText(_translate("MainWindow", "csv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
