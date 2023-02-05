import sys
import random
from PyQt5 import QtWidgets, QtCore,QtGui
import PyQt5
from PyQt5.QtWidgets import QMessageBox
from v5_4 import Ui_MainWindow

import pandas as pd
from utils import *


class Program(QtWidgets.QMainWindow):

    def __init__(self):
        super(Program, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        #initial language stuff setting
        self.LG_pick(self.ui.LG_select_EN)

        #initial gamemodes
        self.gm1 = 'Cou_Cap'
        self.gm2 = 'Choose'

    def init_UI(self):

        self.setWindowTitle('Geography game')
        # self.setWindowIcon(QtGui.QIcon('./heart.png'))

        #setup for message about wrong answer
        self.ui.msg = QMessageBox()
        self.ui.msg.setWindowTitle('Mistake correction')

        #to start with initial page
        self.ui.Game_stage_StackedWidget.setCurrentIndex(0)

        #connect buttons
            #gm Choose    
    
        self.ui.Var1.clicked.connect(lambda: self.pushed(self.ui.Var1))
        self.ui.Var2.clicked.connect(lambda: self.pushed(self.ui.Var2))
        self.ui.Var3.clicked.connect(lambda: self.pushed(self.ui.Var3))
        self.ui.Var4.clicked.connect(lambda: self.pushed(self.ui.Var4))
        self.ui.Start_Button.clicked.connect(self.start_game)

            #gm Type
        self.ui.Input_line.returnPressed.connect(lambda :self.pushed(self.ui.Input_line))

        #language picking buttons connections
        self.ui.LG_select_EN.pressed.connect(
            lambda: self.LG_pick(self.ui.LG_select_EN))
        self.ui.LG_select_RU.pressed.connect(
            lambda: self.LG_pick(self.ui.LG_select_RU))

        #gamemode 1 buttons connections
        self.ui.Cap_Cou.pressed.connect(lambda: self.get_gm(self.ui.Cap_Cou))
        self.ui.Cou_Cap.pressed.connect(lambda: self.get_gm(self.ui.Cou_Cap))
        self.ui.Flag_Cou.pressed.connect(lambda: self.get_gm(self.ui.Flag_Cou))
        self.ui.Cou_Flag.pressed.connect(lambda: self.get_gm(self.ui.Cou_Flag))

        #gamemode 2 buttons connections
        self.ui.Choose_btn.pressed.connect(
            lambda: self.get_gm(self.ui.Choose_btn))
        self.ui.Type_btn.pressed.connect(lambda: self.get_gm(self.ui.Type_btn))

    def start_new_round(self):

        if self.questions_left:
            self.ui.Game_stage_StackedWidget.setCurrentIndex(1)
            if self.gm2 == 'Choose':
                #changing to gaming screen and setting labels
                self.ui.Gamemode_stackedWidget.setCurrentIndex(0)
                self.q, self.a = self.generate_round()
                self.ui.quest_label.setText(self.q)
                self.ui.Var1.setText(self.a[0])
                self.ui.Var2.setText(self.a[1])
                self.ui.Var3.setText(self.a[2])
                self.ui.Var4.setText(self.a[3])
            
            if self.gm2 == 'Type':
                self.ui.Gamemode_stackedWidget.setCurrentIndex(1)
                self.q = self.generate_round()
                self.ui.quest_label.setText(self.q)


            
        else:
            #if no questions left, change to start screen and show score
            self.ui.Game_stage_StackedWidget.setCurrentIndex(0)
            self.ui.Win_message.setText(
                f'{win_messages[self.language_selected]} {self.score}')
    #TODO change function name and btn so that it reflects common
    def pushed(self, btn):
        
        if self.info[self.q].lower() == btn.text().lower():
            print('correct')
            self.score += 1

        else:
            self.score -= 1
            print('incorrect')
            self.ui.msg.setText(f'{self.q}-{self.info[self.q]}')
            x = self.ui.msg.exec_()

        self.ui.Input_line.setText('')
        self.ui.Score_label.setText(f'{self.Score_label_txt}: {self.score}')
        self.start_new_round()

    def start_game(self):

        self.info, self.questions, self.answers = self.get_info()
        self.questions_left = self.questions.copy()
        #to hide winning label
        self.ui.Win_message.setText('')
        #initial score label
        self.ui.Score_label.setText(f'{self.Score_label_txt}: 0')

        self.score = 0
        self.start_new_round()

    #passing a button clicked
    def LG_pick(self, rd_btn):

        choice = rd_btn.text()
        self.language_selected = choice
        #TRANSLATE UI

        self.ui.Start_Button.setText(Start_games_texts[choice])
        self.Score_label_txt = Scores_texts[choice]
        self.ui.Score_label.setText(self.Score_label_txt)
        self.ui.LG_select_lb.setText(Language_lb_texts[choice])
        self.ui.Reg_select_lb.setText(Region_selector_texts[choice])
        #translate region buttons
        region_buttons = self.ui.Region_select.findChildren(
            QtWidgets.QCheckBox)
        for i, button in enumerate(
                region_buttons):  # i is button number from top
            button.setText(
                Regions_buttons_translations[i][self.language_selected])

    def get_gm(self, btn):

        if btn.objectName() == 'Choose_btn':
            self.gm2 = 'Choose'
        elif btn.objectName() == 'Type_btn':
            self.gm2 = 'Type'
        else:
            self.gm1 = btn.objectName()

        print(self.gm1)
        print(self.gm2)

    def generate_round(self):
        #choosing random question and 4 answers
        if self.gm2 == 'Choose':
            
            self.cur_question = self.questions_left.pop(
                random.randrange(len(self.questions_left)))
            self.cur_answers = random.sample(self.answers, 4)
            if self.info[self.cur_question] not in self.cur_answers:
                self.cur_answers[0] = self.info[self.cur_question]
            random.shuffle(self.cur_answers)
            return self.cur_question, self.cur_answers

        #choosing random question
        if self.gm2 == 'Type':
            self.cur_question = self.questions_left.pop(
                random.randrange(len(self.questions_left)))
            return self.cur_question

    def get_info(self):
        #load region with right language
        region_buttons = self.ui.Region_select.findChildren(
            QtWidgets.QCheckBox)
        #collect regions buttons that are picked
        self.selected_regions_buttons = [
            button.objectName() for button in region_buttons
            if button.isChecked()
        ]
        #collect region names from button names
        self.selected_regions = [
            regions_button_names_to_regions[button]
            for button in self.selected_regions_buttons
        ]
        info = {}
        # questions = []
        # answers = []
        for region in self.selected_regions:
            region_list = pd.read_excel(
                fr'C:\Users\cambo\Documents\repos\python\pyqt\geography game\{region}.xlsx',
                sheet_name=self.language_selected)

            info.update(
                dict(
                    zip(list(region_list.iloc[:, 0]),
                        list(region_list.iloc[:, 1]))))
        questions=list(info.keys())
        answers=list(info.values())

        #switching countries and capitals if gamemode is choosen
        if self.gm1 == 'Cap_Cou':
            info = {y: x for x, y in info.items()}
            questions, answers = answers, questions

        print(len(info))
        print(info)
        return info, questions, answers


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
application = Program()
application.show()
sys.exit(app.exec_())