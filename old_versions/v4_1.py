# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v4_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(550, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(550, 550))
        MainWindow.setSizeIncrement(QtCore.QSize(8, 8))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 300))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.start_and_win_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_and_win_page.sizePolicy().hasHeightForWidth())
        self.start_and_win_page.setSizePolicy(sizePolicy)
        self.start_and_win_page.setObjectName("start_and_win_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.start_and_win_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 200, 0, 200)
        self.verticalLayout_3.setSpacing(28)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Win_message = QtWidgets.QLabel(self.start_and_win_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.Win_message.sizePolicy().hasHeightForWidth())
        self.Win_message.setSizePolicy(sizePolicy)
        self.Win_message.setMinimumSize(QtCore.QSize(275, 40))
        self.Win_message.setSizeIncrement(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Win_message.setFont(font)
        self.Win_message.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Win_message.setMouseTracking(False)
        self.Win_message.setAutoFillBackground(False)
        self.Win_message.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Win_message.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Win_message.setText("")
        self.Win_message.setScaledContents(True)
        self.Win_message.setAlignment(QtCore.Qt.AlignCenter)
        self.Win_message.setObjectName("Win_message")
        self.verticalLayout_3.addWidget(self.Win_message, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Start_Button = QtWidgets.QPushButton(self.start_and_win_page)
        self.Start_Button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.Start_Button.sizePolicy().hasHeightForWidth())
        self.Start_Button.setSizePolicy(sizePolicy)
        self.Start_Button.setMinimumSize(QtCore.QSize(275, 40))
        self.Start_Button.setSizeIncrement(QtCore.QSize(1, 1))
        self.Start_Button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Start_Button.setFont(font)
        self.Start_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Start_Button.setAutoFillBackground(False)
        self.Start_Button.setAutoDefault(False)
        self.Start_Button.setDefault(False)
        self.Start_Button.setFlat(False)
        self.Start_Button.setObjectName("Start_Button")
        self.verticalLayout_3.addWidget(self.Start_Button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.start_and_win_page)
        self.game_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_page.sizePolicy().hasHeightForWidth())
        self.game_page.setSizePolicy(sizePolicy)
        self.game_page.setObjectName("game_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.game_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_everything = QtWidgets.QFrame(self.game_page)
        self.frame_everything.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_everything.sizePolicy().hasHeightForWidth())
        self.frame_everything.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_everything.setFont(font)
        self.frame_everything.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_everything.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_everything.setObjectName("frame_everything")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_everything)
        self.verticalLayout_10.setContentsMargins(12, -1, -1, 18)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quest_label = QtWidgets.QLabel(self.frame_everything)
        self.quest_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quest_label.sizePolicy().hasHeightForWidth())
        self.quest_label.setSizePolicy(sizePolicy)
        self.quest_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.quest_label.setFont(font)
        self.quest_label.setObjectName("quest_label")
        self.horizontalLayout.addWidget(self.quest_label, 0, QtCore.Qt.AlignHCenter)
        self.Score_label = QtWidgets.QLabel(self.frame_everything)
        self.Score_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Score_label.sizePolicy().hasHeightForWidth())
        self.Score_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Score_label.setFont(font)
        self.Score_label.setObjectName("Score_label")
        self.horizontalLayout.addWidget(self.Score_label)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.Answer_buttons = QtWidgets.QFrame(self.frame_everything)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Answer_buttons.sizePolicy().hasHeightForWidth())
        self.Answer_buttons.setSizePolicy(sizePolicy)
        self.Answer_buttons.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Answer_buttons.setFont(font)
        self.Answer_buttons.setObjectName("Answer_buttons")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Answer_buttons)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 161, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 3, 0, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Var3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Var3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Var3.sizePolicy().hasHeightForWidth())
        self.Var3.setSizePolicy(sizePolicy)
        self.Var3.setObjectName("Var3")
        self.verticalLayout.addWidget(self.Var3)
        self.Var4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Var4.sizePolicy().hasHeightForWidth())
        self.Var4.setSizePolicy(sizePolicy)
        self.Var4.setObjectName("Var4")
        self.verticalLayout.addWidget(self.Var4)
        self.Var2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Var2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Var2.sizePolicy().hasHeightForWidth())
        self.Var2.setSizePolicy(sizePolicy)
        self.Var2.setObjectName("Var2")
        self.verticalLayout.addWidget(self.Var2)
        self.Var1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Var1.sizePolicy().hasHeightForWidth())
        self.Var1.setSizePolicy(sizePolicy)
        self.Var1.setObjectName("Var1")
        self.verticalLayout.addWidget(self.Var1)
        self.verticalLayout_10.addWidget(self.Answer_buttons)
        self.verticalLayout_2.addWidget(self.frame_everything)
        self.stackedWidget.addWidget(self.game_page)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_Button.setText(_translate("MainWindow", "Start game"))
        self.quest_label.setText(_translate("MainWindow", "TextLabel"))
        self.Score_label.setText(_translate("MainWindow", "Score: "))
        self.Var3.setText(_translate("MainWindow", "PushButton"))
        self.Var4.setText(_translate("MainWindow", "PushButton"))
        self.Var2.setText(_translate("MainWindow", "PushButton"))
        self.Var1.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
