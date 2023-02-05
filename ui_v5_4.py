# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v5_4.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(626, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(580, 550))
        MainWindow.setSizeIncrement(QSize(8, 8))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(300, 300))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto Thin"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.Game_stage_StackedWidget = QStackedWidget(self.centralwidget)
        self.Game_stage_StackedWidget.setObjectName(u"Game_stage_StackedWidget")
        sizePolicy1.setHeightForWidth(self.Game_stage_StackedWidget.sizePolicy().hasHeightForWidth())
        self.Game_stage_StackedWidget.setSizePolicy(sizePolicy1)
        self.Game_stage_StackedWidget.setMinimumSize(QSize(300, 300))
        self.Game_stage_StackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.Game_stage_StackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.start_and_win_page = QWidget()
        self.start_and_win_page.setObjectName(u"start_and_win_page")
        sizePolicy1.setHeightForWidth(self.start_and_win_page.sizePolicy().hasHeightForWidth())
        self.start_and_win_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.start_and_win_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Win_message = QLabel(self.start_and_win_page)
        self.Win_message.setObjectName(u"Win_message")
        sizePolicy.setHeightForWidth(self.Win_message.sizePolicy().hasHeightForWidth())
        self.Win_message.setSizePolicy(sizePolicy)
        self.Win_message.setMinimumSize(QSize(275, 40))
        self.Win_message.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.Win_message.setFont(font1)
        self.Win_message.setCursor(QCursor(Qt.ArrowCursor))
        self.Win_message.setMouseTracking(False)
        self.Win_message.setAutoFillBackground(False)
        self.Win_message.setFrameShape(QFrame.NoFrame)
        self.Win_message.setFrameShadow(QFrame.Plain)
        self.Win_message.setScaledContents(True)
        self.Win_message.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Win_message)

        self.Settings_field = QWidget(self.start_and_win_page)
        self.Settings_field.setObjectName(u"Settings_field")
        sizePolicy1.setHeightForWidth(self.Settings_field.sizePolicy().hasHeightForWidth())
        self.Settings_field.setSizePolicy(sizePolicy1)
        self.Settings_field.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_12 = QHBoxLayout(self.Settings_field)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.Language_selector = QFrame(self.Settings_field)
        self.Language_selector.setObjectName(u"Language_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Language_selector.sizePolicy().hasHeightForWidth())
        self.Language_selector.setSizePolicy(sizePolicy2)
        self.verticalLayout_18 = QVBoxLayout(self.Language_selector)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 9)
        self.LG_select_lb = QLabel(self.Language_selector)
        self.LG_select_lb.setObjectName(u"LG_select_lb")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.LG_select_lb.sizePolicy().hasHeightForWidth())
        self.LG_select_lb.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(15)
        self.LG_select_lb.setFont(font2)

        self.verticalLayout_18.addWidget(self.LG_select_lb)

        self.LG_select_EN = QRadioButton(self.Language_selector)
        self.LG_select_EN.setObjectName(u"LG_select_EN")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.LG_select_EN.sizePolicy().hasHeightForWidth())
        self.LG_select_EN.setSizePolicy(sizePolicy4)
        self.LG_select_EN.setChecked(True)

        self.verticalLayout_18.addWidget(self.LG_select_EN)

        self.LG_select_RU = QRadioButton(self.Language_selector)
        self.LG_select_RU.setObjectName(u"LG_select_RU")
        sizePolicy4.setHeightForWidth(self.LG_select_RU.sizePolicy().hasHeightForWidth())
        self.LG_select_RU.setSizePolicy(sizePolicy4)

        self.verticalLayout_18.addWidget(self.LG_select_RU)


        self.horizontalLayout_12.addWidget(self.Language_selector, 0, Qt.AlignHCenter)

        self.Region_select = QWidget(self.Settings_field)
        self.Region_select.setObjectName(u"Region_select")
        sizePolicy2.setHeightForWidth(self.Region_select.sizePolicy().hasHeightForWidth())
        self.Region_select.setSizePolicy(sizePolicy2)
        self.verticalLayout_19 = QVBoxLayout(self.Region_select)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 9)
        self.Reg_select_lb = QLabel(self.Region_select)
        self.Reg_select_lb.setObjectName(u"Reg_select_lb")
        sizePolicy1.setHeightForWidth(self.Reg_select_lb.sizePolicy().hasHeightForWidth())
        self.Reg_select_lb.setSizePolicy(sizePolicy1)
        self.Reg_select_lb.setFont(font2)

        self.verticalLayout_19.addWidget(self.Reg_select_lb)

        self.Reg_EU_box = QCheckBox(self.Region_select)
        self.Reg_EU_box.setObjectName(u"Reg_EU_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Reg_EU_box.sizePolicy().hasHeightForWidth())
        self.Reg_EU_box.setSizePolicy(sizePolicy5)

        self.verticalLayout_19.addWidget(self.Reg_EU_box)

        self.Reg_AS_box = QCheckBox(self.Region_select)
        self.Reg_AS_box.setObjectName(u"Reg_AS_box")

        self.verticalLayout_19.addWidget(self.Reg_AS_box)

        self.Reg_3_box = QCheckBox(self.Region_select)
        self.Reg_3_box.setObjectName(u"Reg_3_box")
        self.Reg_3_box.setEnabled(False)
        self.Reg_3_box.setCheckable(True)

        self.verticalLayout_19.addWidget(self.Reg_3_box)

        self.Reg_4_box = QCheckBox(self.Region_select)
        self.Reg_4_box.setObjectName(u"Reg_4_box")
        self.Reg_4_box.setEnabled(False)

        self.verticalLayout_19.addWidget(self.Reg_4_box)


        self.horizontalLayout_12.addWidget(self.Region_select, 0, Qt.AlignHCenter)

        self.Gamemode_selector = QFrame(self.Settings_field)
        self.Gamemode_selector.setObjectName(u"Gamemode_selector")
        sizePolicy2.setHeightForWidth(self.Gamemode_selector.sizePolicy().hasHeightForWidth())
        self.Gamemode_selector.setSizePolicy(sizePolicy2)
        self.Gamemode_selector.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(11)
        self.Gamemode_selector.setFont(font3)
        self.Gamemode_selector.setFrameShape(QFrame.StyledPanel)
        self.Gamemode_selector.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Gamemode_selector)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, -1, -1, 9)
        self.Cou_Cap = QRadioButton(self.Gamemode_selector)
        self.Cou_Cap.setObjectName(u"Cou_Cap")
        self.Cou_Cap.setChecked(True)

        self.verticalLayout_22.addWidget(self.Cou_Cap)

        self.Cap_Cou = QRadioButton(self.Gamemode_selector)
        self.Cap_Cou.setObjectName(u"Cap_Cou")

        self.verticalLayout_22.addWidget(self.Cap_Cou)

        self.Flag_Cou = QRadioButton(self.Gamemode_selector)
        self.Flag_Cou.setObjectName(u"Flag_Cou")
        self.Flag_Cou.setEnabled(False)

        self.verticalLayout_22.addWidget(self.Flag_Cou)

        self.Cou_Flag = QRadioButton(self.Gamemode_selector)
        self.Cou_Flag.setObjectName(u"Cou_Flag")
        self.Cou_Flag.setEnabled(False)

        self.verticalLayout_22.addWidget(self.Cou_Flag)


        self.horizontalLayout_12.addWidget(self.Gamemode_selector, 0, Qt.AlignHCenter)

        self.Pick_or_type_selector = QFrame(self.Settings_field)
        self.Pick_or_type_selector.setObjectName(u"Pick_or_type_selector")
        sizePolicy2.setHeightForWidth(self.Pick_or_type_selector.sizePolicy().hasHeightForWidth())
        self.Pick_or_type_selector.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        self.Pick_or_type_selector.setFont(font4)
        self.verticalLayout_24 = QVBoxLayout(self.Pick_or_type_selector)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.Choose_btn = QRadioButton(self.Pick_or_type_selector)
        self.Choose_btn.setObjectName(u"Choose_btn")
        self.Choose_btn.setCheckable(True)
        self.Choose_btn.setChecked(True)

        self.verticalLayout_24.addWidget(self.Choose_btn)

        self.Type_btn = QRadioButton(self.Pick_or_type_selector)
        self.Type_btn.setObjectName(u"Type_btn")

        self.verticalLayout_24.addWidget(self.Type_btn)


        self.horizontalLayout_12.addWidget(self.Pick_or_type_selector, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.Settings_field)

        self.Start_Button = QPushButton(self.start_and_win_page)
        self.Start_Button.setObjectName(u"Start_Button")
        self.Start_Button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Start_Button.sizePolicy().hasHeightForWidth())
        self.Start_Button.setSizePolicy(sizePolicy)
        self.Start_Button.setMinimumSize(QSize(275, 40))
        self.Start_Button.setMaximumSize(QSize(200, 75))
        self.Start_Button.setSizeIncrement(QSize(1, 1))
        self.Start_Button.setBaseSize(QSize(0, 0))
        self.Start_Button.setFont(font4)
        self.Start_Button.setLayoutDirection(Qt.LeftToRight)
        self.Start_Button.setAutoFillBackground(False)
        self.Start_Button.setAutoDefault(False)
        self.Start_Button.setFlat(False)

        self.verticalLayout_2.addWidget(self.Start_Button, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Game_stage_StackedWidget.addWidget(self.start_and_win_page)
        self.game_page = QWidget()
        self.game_page.setObjectName(u"game_page")
        sizePolicy1.setHeightForWidth(self.game_page.sizePolicy().hasHeightForWidth())
        self.game_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_23 = QVBoxLayout(self.game_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.Question_score_widget = QWidget(self.game_page)
        self.Question_score_widget.setObjectName(u"Question_score_widget")
        self.horizontalLayout_10 = QHBoxLayout(self.Question_score_widget)
        self.horizontalLayout_10.setSpacing(12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 1, -1, 1)
        self.quest_label = QLabel(self.Question_score_widget)
        self.quest_label.setObjectName(u"quest_label")
        self.quest_label.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.quest_label.sizePolicy().hasHeightForWidth())
        self.quest_label.setSizePolicy(sizePolicy2)
        self.quest_label.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamilies([u"MS Sans Serif"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.quest_label.setFont(font5)
        self.quest_label.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.quest_label, 0, Qt.AlignHCenter)

        self.Score_label = QLabel(self.Question_score_widget)
        self.Score_label.setObjectName(u"Score_label")
        self.Score_label.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.Score_label.sizePolicy().hasHeightForWidth())
        self.Score_label.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setPointSize(18)
        self.Score_label.setFont(font6)

        self.horizontalLayout_10.addWidget(self.Score_label)


        self.verticalLayout_23.addWidget(self.Question_score_widget)

        self.Gamemode_stackedWidget = QStackedWidget(self.game_page)
        self.Gamemode_stackedWidget.setObjectName(u"Gamemode_stackedWidget")
        self.Choose_page = QWidget()
        self.Choose_page.setObjectName(u"Choose_page")
        self.verticalLayout_20 = QVBoxLayout(self.Choose_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalWidget = QWidget(self.Choose_page)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.verticalWidget.setMinimumSize(QSize(200, 0))
        self.verticalLayout_21 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 3, -1, 15)
        self.Var3 = QPushButton(self.verticalWidget)
        self.Var3.setObjectName(u"Var3")
        self.Var3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Var3.sizePolicy().hasHeightForWidth())
        self.Var3.setSizePolicy(sizePolicy1)

        self.verticalLayout_21.addWidget(self.Var3)

        self.Var4 = QPushButton(self.verticalWidget)
        self.Var4.setObjectName(u"Var4")
        sizePolicy1.setHeightForWidth(self.Var4.sizePolicy().hasHeightForWidth())
        self.Var4.setSizePolicy(sizePolicy1)

        self.verticalLayout_21.addWidget(self.Var4)

        self.Var2 = QPushButton(self.verticalWidget)
        self.Var2.setObjectName(u"Var2")
        self.Var2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Var2.sizePolicy().hasHeightForWidth())
        self.Var2.setSizePolicy(sizePolicy1)

        self.verticalLayout_21.addWidget(self.Var2)

        self.Var1 = QPushButton(self.verticalWidget)
        self.Var1.setObjectName(u"Var1")
        sizePolicy1.setHeightForWidth(self.Var1.sizePolicy().hasHeightForWidth())
        self.Var1.setSizePolicy(sizePolicy1)

        self.verticalLayout_21.addWidget(self.Var1)


        self.verticalLayout_20.addWidget(self.verticalWidget, 0, Qt.AlignLeft)

        self.Gamemode_stackedWidget.addWidget(self.Choose_page)
        self.Type_page = QWidget()
        self.Type_page.setObjectName(u"Type_page")
        self.verticalLayout_5 = QVBoxLayout(self.Type_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Input_line = QLineEdit(self.Type_page)
        self.Input_line.setObjectName(u"Input_line")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Input_line.sizePolicy().hasHeightForWidth())
        self.Input_line.setSizePolicy(sizePolicy6)
        self.Input_line.setMaximumSize(QSize(300, 16777215))
        self.Input_line.setFont(font3)
        self.Input_line.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.Input_line)

        self.Gamemode_stackedWidget.addWidget(self.Type_page)

        self.verticalLayout_23.addWidget(self.Gamemode_stackedWidget)

        self.Game_stage_StackedWidget.addWidget(self.game_page)

        self.verticalLayout.addWidget(self.Game_stage_StackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Game_stage_StackedWidget.setCurrentIndex(0)
        self.Start_Button.setDefault(False)
        self.Gamemode_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pre-alpha", None))
        self.Win_message.setText("")
        self.LG_select_lb.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.LG_select_EN.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.LG_select_RU.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.Reg_select_lb.setText(QCoreApplication.translate("MainWindow", u"Region", None))
        self.Reg_EU_box.setText(QCoreApplication.translate("MainWindow", u"Europe", None))
        self.Reg_AS_box.setText(QCoreApplication.translate("MainWindow", u"Asia", None))
        self.Reg_3_box.setText(QCoreApplication.translate("MainWindow", u"Region 3", None))
        self.Reg_4_box.setText(QCoreApplication.translate("MainWindow", u"Region 4", None))
        self.Cou_Cap.setText(QCoreApplication.translate("MainWindow", u"Country - Capital", None))
        self.Cap_Cou.setText(QCoreApplication.translate("MainWindow", u"Capital - Country", None))
        self.Flag_Cou.setText(QCoreApplication.translate("MainWindow", u"Flag - Country", None))
        self.Cou_Flag.setText(QCoreApplication.translate("MainWindow", u"Country - Flag", None))
        self.Choose_btn.setText(QCoreApplication.translate("MainWindow", u"Choose", None))
        self.Type_btn.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.Start_Button.setText(QCoreApplication.translate("MainWindow", u"Start game", None))
        self.quest_label.setText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.Score_label.setText(QCoreApplication.translate("MainWindow", u"Score: ", None))
        self.Var3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Var4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Var2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Var1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

