#
#   We Want Soviet Men! Character Generator
#
#############################################

"""
WWSM Chargen 0.0.2 Beta
-----------------------------------------------------------------------

This program generates characters for the We Want Soviet Men! RPG.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
from mainwindow_002b import Ui_MainWindow
from aboutdialog_002b import Ui_aboutDialog
from alertdialog_002b import Ui_alertDialog
from savedialog_002b import Ui_saveDialog
import sys
import os
import logging
import json
from fpdf import FPDF

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'WWSM CharGen 0.0.2 (Beta)'
__version__ = '0.0.2b'
__expired_tag__ = False

class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self):
        '''
        Open the About dialog window
        '''
        super().__init__()
        log.info('PyQt5 aboutDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 aboutDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the About dialog window
        '''
        log.info('PyQt5 aboutDialog closing...')
        self.close()

class alertDialog(QDialog, Ui_alertDialog):
    def __init__(self):
        '''
        Open the Alert dialog window
        '''
        super().__init__()
        log.info('PyQt5 alertDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 alertDialog initialized.')
        
    def acceptOKButtonClicked(self):
        '''
        Close the Alert dialog window
        '''
        log.info('PyQt5 alertDialog closing...')
        self.close()

class saveDialog(QDialog, Ui_saveDialog):
    def __init__(self):
        '''
        Open the Save dialog window
        '''
        super().__init__()
        log.info('PyQt5 saveDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.saveOKButton.clicked.connect(self.acceptOKButtonClicked)
        self.saveDisplay.setText('Character saved.')
        log.info('PyQt5 saveDialog initialized.')

    def acceptOKButtonClicked(self):
        '''
        Close the Save dialog window
        '''
        log.info('PyQt5 saveDialog closing...')
        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        Display the main app window.
        Connect all the buttons to their functions.
        Initialize their value ranges.
        '''
        super().__init__()
        log.info('PyQt5 MainWindow initializing...')
        self.setupUi(self)
        self.actionAbout_WWSM_CharGen.triggered.connect(self.actionAbout_triggered)
        self.actionQuitProg.triggered.connect(self.actionQuitProg_triggered)
        self.bodyScore.valueChanged.connect(self.bodyScore_valueChanged)
        self.clearButton.clicked.connect(self.clearButton_clicked)
        self.actionClear.triggered.connect(self.clearButton_clicked)
        self.loadButton.clicked.connect(self.loadButton_clicked)
        self.actionLoad.triggered.connect(self.loadButton_clicked)
        self.saveButton.clicked.connect(self.saveButton_clicked)
        self.actionSave.triggered.connect(self.saveButton_clicked)
        self.printButton.clicked.connect(self.printButton_clicked)
        self.actionPrint.triggered.connect(self.printButton_clicked)
        self.actionVisit_Blog.triggered.connect(self.Visit_Blog)
        self.actionFeedback.triggered.connect(self.Feedback)
        self.actionOverview.triggered.connect(self.Overview_menu)
        self.mindScore.valueChanged.connect(self.mindScore_valueChanged)
        self.spiritScore.valueChanged.connect(self.spiritScore_valueChanged)
        self.agilitySkill.setDisabled(True)
        self.beautySkill.setDisabled(True)
        self.strengthSkill.setDisabled(True)
        self.knowledgeSkill.setDisabled(True)
        self.perceptionSkill.setDisabled(True)
        self.technologySkill.setDisabled(True)
        self.charismaSkill.setDisabled(True)
        self.empathySkill.setDisabled(True)
        self.focusSkill.setDisabled(True)
        self.boxingSkill.setDisabled(True)
        self.meleeSkill.setDisabled(True)
        self.rangedSkill.setDisabled(True)
        self.artSkill.setDisabled(True)
        self.languagesSkill.setDisabled(True)
        self.scienceSkill.setDisabled(True)
        self.clairvoyanceSkill.setDisabled(True)
        self.psychokinesisSkill.setDisabled(True)
        self.telepathySkill.setDisabled(True)
        self.saveButton.setDisabled(True)
        self.actionSave.setDisabled(True)
        self.printButton.setDisabled(True)
        self.actionPrint.setDisabled(True)
        self.charnameEdit.setDisabled(True)
        self.ageEdit.setDisabled(True)
        self.genderEdit.setDisabled(True)
        self.deptBox.setDisabled(True)
        self.rankDisplay.setDisabled(True)
        self.levelBox.setDisabled(True)
        self.xpEdit.setDisabled(True)
        self.agilitySkill.valueChanged.connect(self.agilitySkill_valueChanged)
        self.beautySkill.valueChanged.connect(self.beautySkill_valueChanged)
        self.strengthSkill.valueChanged.connect(self.strengthSkill_valueChanged)
        self.knowledgeSkill.valueChanged.connect(self.knowledgeSkill_valueChanged)
        self.perceptionSkill.valueChanged.connect(self.perceptionSkill_valueChanged)
        self.technologySkill.valueChanged.connect(self.technologySkill_valueChanged)
        self.charismaSkill.valueChanged.connect(self.charismaSkill_valueChanged)
        self.empathySkill.valueChanged.connect(self.empathySkill_valueChanged)
        self.focusSkill.valueChanged.connect(self.focusSkill_valueChanged)
        self.boxingSkill.valueChanged.connect(self.boxingSkill_valueChanged)
        self.meleeSkill.valueChanged.connect(self.meleeSkill_valueChanged)
        self.rangedSkill.valueChanged.connect(self.rangedSkill_valueChanged)
        self.artSkill.valueChanged.connect(self.artSkill_valueChanged)
        self.languagesSkill.valueChanged.connect(self.languagesSkill_valueChanged)
        self.scienceSkill.valueChanged.connect(self.scienceSkill_valueChanged)
        self.clairvoyanceSkill.valueChanged.connect(self.clairvoyanceSkill_valueChanged)
        self.psychokinesisSkill.valueChanged.connect(self.psychokinesisSkill_valueChanged)
        self.telepathySkill.valueChanged.connect(self.telepathySkill_valueChanged)

        self.charnameEdit.setText('Sample Char')
        self.rewardDisplay.setText('None')
        self.armorDisplay.setPlainText('None')
        self.weaponDisplay.setPlainText('None')
        self.starting_items = 'Shipsuit, Uniform, Ration ID Card, Socialist Media Account'
        self.itemsDisplay.setPlainText(self.starting_items)
        self.specialDisplay.setPlainText('None')
        self.traitsDisplay.setPlainText('')
        self.backstoryDisplay.setPlainText('')
        self.notesDisplay.setPlainText('')
        self.dept_choice = ['Choose', 'Fitness', 'Mechanics', 'Counseling', 'Compliance', 'Propaganda', 'Espionage', 'Custodial', 'Medicine', 'Politics', 'Military', 'Academics', 'Telepathics']
        for i in self.dept_choice:
            self.deptBox.addItem(i)
        self.deptBox.setCurrentIndex(0)
        self.deptBox.currentIndexChanged.connect(self.deptBox_changed)
        self.dept_choice = ['Choose', 'Fitness', 'Mechanics', 'Counseling', 'Compliance', 'Propaganda', 'Espionage', 'Custodial', 'Medicine', 'Politics', 'Military', 'Academics', 'Telepathics']
        self.dept_rank = 'Comrade'
        self.dept_skill = ['', 'Body', 'Mind', 'Spirit', 'Combat', 'Strange', 'Psionic', 'Body', 'Mind', 'Spirit', 'Combat', 'Strange', 'Psionic']
        self.dept_item = ['', 'First Aid Spray', 'Toolkit', 'Therapy Goggles', 'Baton', 'Video Drone', 'Stunner Pistol', 'Mop + Bucket', 'Bioscanner', 'Extra Ration Card', 'Stunner Rifle', 'Computer Watch', 'Psychic ID Card']

        self.department_not_chosen = True

        self.char_level = 1
        self.levelBox.addItem('1')
        self.levelBox.addItem('2')
        self.levelBox.addItem('3')
        self.levelBox.addItem('4')
        self.levelBox.addItem('5')
        self.levelBox.setCurrentIndex(0)
        self.levelBox.currentIndexChanged.connect(self.levelBox_changed)

        self.char_xp = 0

        self.game_name = 'WE WANT SOVIET MEN!'
        self.char_folder = 'We Want Soviet Men Characters'
        self.file_extension = '.tps'
        self.file_format = 1.2

        # Set the About menu item
        self.popAboutDialog = aboutDialog()

        # Set the Alert menu item
        self.popAlertDialog=alertDialog()

        # Set the Save menu item
        self.popSaveDialog=saveDialog()

        log.info('PyQt5 MainWindow initialized.')

        if __expired_tag__ is True:
            '''
            Beta for this app has expired!
            '''
            log.warning(__app__ + ' expiration detected...')
            self.alert_window()
            '''
            display alert message and disable all the things
            '''
            self.clearButton.setDisabled(True)
            self.actionClear.setDisabled(True)
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.loadButton.setDisabled(True)
            self.actionLoad.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
            self.actionVisit_Blog.setDisabled(True)
            self.actionFeedback.setDisabled(True)
            self.actionOverview.setDisabled(True)
            self.actionAbout_WWSM_CharGen.setDisabled(True)
            self.bodyScore.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.additional1Display.setDisabled(True)
            self.agilitySkill.setDisabled(True)
            self.beautySkill.setDisabled(True)
            self.strengthSkill.setDisabled(True)
            self.knowledgeSkill.setDisabled(True)
            self.perceptionSkill.setDisabled(True)
            self.technologySkill.setDisabled(True)
            self.charismaSkill.setDisabled(True)
            self.empathySkill.setDisabled(True)
            self.focusSkill.setDisabled(True)
            self.boxingSkill.setDisabled(True)
            self.meleeSkill.setDisabled(True)
            self.rangedSkill.setDisabled(True)
            self.artSkill.setDisabled(True)
            self.languagesSkill.setDisabled(True)
            self.scienceSkill.setDisabled(True)
            self.clairvoyanceSkill.setDisabled(True)
            self.psychokinesisSkill.setDisabled(True)
            self.telepathySkill.setDisabled(True)
            self.additional2Display.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.deptBox.setDisabled(True)
            self.rankDisplay.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.xpEdit.setDisabled(True)
            self.armorDisplay.setDisabled(True)
            self.weaponDisplay.setDisabled(True)
            self.itemsDisplay.setDisabled(True)
            self.specialDisplay.setDisabled(True)
            self.traitsDisplay.setDisabled(True)
            self.backstoryDisplay.setDisabled(True)
            self.notesDisplay.setDisabled(True)
        else:
            '''
            Create .tpsrpg folder and tps.ini file the first time this program is run.
            Also, create the save folder for this program to save its .tps files in.
            '''
            self.temp_dir = os.path.expanduser('~')
            os.chdir(self.temp_dir)
            if not os.path.exists('.tpsrpg'):
                os.mkdir('.tpsrpg')
            os.chdir(self.temp_dir + '\.tpsrpg')
            if not os.path.exists(self.char_folder):
                os.mkdir(self.char_folder)
                log.info(self.char_folder + ' folder created')
            if not os.path.exists('tps.ini'):
                with open('tps.ini', 'w') as f:
                    f.write('[CharGen Folders]\n')
                    f.write(self.char_folder + '\n')
                log.info('tps.ini created and initialized')
            else:
                self.contains_foldername = False
                with open('tps.ini', 'r') as f:
                    if self.char_folder in f.read():
                        self.contains_foldername = True
                if not self.contains_foldername:
                    with open('tps.ini', 'a') as f:
                        f.write(self.char_folder + '\n')
                    log.info(self.char_folder + ' added to TPS folder list')

    #   Initialize Attribute Scores
    
        self.body = 0
        self.mind = 1
        self.spirit = 2

        self.attribute_name = ['BODY', 'MIND', 'SPIRIT']
        self.attribute_score = [1, 1, 1]

    #   Initialize Status Levels

        self.health = 0
        self.sanity = 1
        self.morale = 2

        self.status_name = ['HEALTH', 'SANITY', 'MORALE']
        self.status_level = [2, 2, 2]

        self.bodyScore.setValue(self.attribute_score[self.body])
        self.mindScore.setValue(self.attribute_score[self.mind])
        self.spiritScore.setValue(self.attribute_score[self.spirit])
        self.tempbodyScore = self.bodyScore.value()
        self.tempmindScore = self.mindScore.value()
        self.tempspiritScore = self.spiritScore.value()

        self.additional_attribute_points = 3
        self.additional1Display.setText(str(self.additional_attribute_points))

        self.healthDisplay.setText(str(self.status_level[self.health] + self.attribute_score[self.body]))
        self.sanityDisplay.setText(str(self.status_level[self.sanity] + self.attribute_score[self.mind]))
        self.moraleDisplay.setText(str(self.status_level[self.morale] + self.attribute_score[self.spirit]))        

    #   Initialize Skill Levels

        self.agilitySkill.setValue(0)
        self.beautySkill.setValue(0)
        self.strengthSkill.setValue(0)
        self.knowledgeSkill.setValue(0)
        self.perceptionSkill.setValue(0)
        self.technologySkill.setValue(0)
        self.charismaSkill.setValue(0)
        self.empathySkill.setValue(0)
        self.focusSkill.setValue(0)
        self.boxingSkill.setValue(0)
        self.meleeSkill.setValue(0)
        self.rangedSkill.setValue(0)
        self.artSkill.setValue(0)
        self.languagesSkill.setValue(0)
        self.scienceSkill.setValue(0)
        self.clairvoyanceSkill.setValue(0)
        self.psychokinesisSkill.setValue(0)
        self.telepathySkill.setValue(0)
        self.tempagilitySkill = self.agilitySkill.value()
        self.tempbeautySkill = self.beautySkill.value()
        self.tempstrengthSkill = self.strengthSkill.value()
        self.tempknowledgeSkill = self.knowledgeSkill.value()
        self.tempperceptionSkill = self.perceptionSkill.value()
        self.temptechnologySkill = self.technologySkill.value()
        self.tempcharismaSkill = self.charismaSkill.value()
        self.tempempathySkill = self.empathySkill.value()
        self.tempfocusSkill = self.focusSkill.value()
        self.tempboxingSkill = self.boxingSkill.value()
        self.tempmeleeSkill = self.meleeSkill.value()
        self.temprangedSkill = self.rangedSkill.value()
        self.tempartSkill = self.artSkill.value()
        self.templanguagesSkill = self.languagesSkill.value()
        self.tempscienceSkill = self.scienceSkill.value()
        self.tempclairvoyanceSkill = self.clairvoyanceSkill.value()
        self.temppsychokinesisSkill = self.psychokinesisSkill.value()
        self.temptelepathySkill = self.telepathySkill.value()

        self.additional_skill_points = 12
        self.additional2Display.setText(str(self.additional_skill_points))
        
    #   Initialize Movement and Range

        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')

    def clearButton_clicked(self):
        '''
        Clear all the fields
        '''
        log.info('Clear all fields')
        self.status_level = [2, 2, 2]

        self.bodyScore.setValue(self.attribute_score[self.body])
        self.mindScore.setValue(self.attribute_score[self.mind])
        self.spiritScore.setValue(self.attribute_score[self.spirit])
        self.tempbodyScore = self.bodyScore.value()
        self.tempmindScore = self.mindScore.value()
        self.tempspiritScore = self.spiritScore.value()

        self.additional_attribute_points = 3
        self.additional1Display.setText(str(self.additional_attribute_points))

        self.healthDisplay.setText(str(self.status_level[self.health] + self.attribute_score[self.body]))
        self.sanityDisplay.setText(str(self.status_level[self.sanity] + self.attribute_score[self.mind]))
        self.moraleDisplay.setText(str(self.status_level[self.morale] + self.attribute_score[self.spirit]))

        self.agilitySkill.setValue(0)
        self.beautySkill.setValue(0)
        self.strengthSkill.setValue(0)
        self.knowledgeSkill.setValue(0)
        self.perceptionSkill.setValue(0)
        self.technologySkill.setValue(0)
        self.charismaSkill.setValue(0)
        self.empathySkill.setValue(0)
        self.focusSkill.setValue(0)
        self.boxingSkill.setValue(0)
        self.meleeSkill.setValue(0)
        self.rangedSkill.setValue(0)
        self.artSkill.setValue(0)
        self.languagesSkill.setValue(0)
        self.scienceSkill.setValue(0)
        self.clairvoyanceSkill.setValue(0)
        self.psychokinesisSkill.setValue(0)
        self.telepathySkill.setValue(0)
        self.tempagilitySkill = self.agilitySkill.value()
        self.tempbeautySkill = self.beautySkill.value()
        self.tempstrengthSkill = self.strengthSkill.value()
        self.tempknowledgeSkill = self.knowledgeSkill.value()
        self.tempperceptionSkill = self.perceptionSkill.value()
        self.temptechnologySkill = self.technologySkill.value()
        self.tempcharismaSkill = self.charismaSkill.value()
        self.tempempathySkill = self.empathySkill.value()
        self.tempfocusSkill = self.focusSkill.value()
        self.tempboxingSkill = self.boxingSkill.value()
        self.tempmeleeSkill = self.meleeSkill.value()
        self.temprangedSkill = self.rangedSkill.value()
        self.tempartSkill = self.artSkill.value()
        self.templanguagesSkill = self.languagesSkill.value()
        self.tempscienceSkill = self.scienceSkill.value()
        self.tempclairvoyanceSkill = self.clairvoyanceSkill.value()
        self.temppsychokinesisSkill = self.psychokinesisSkill.value()
        self.temptelepathySkill = self.telepathySkill.value()

        self.deptBox.setCurrentIndex(0)

        self.department_not_chosen = True

        self.levelBox.setCurrentIndex(0)

        self.agilitySkill.setDisabled(True)
        self.beautySkill.setDisabled(True)
        self.strengthSkill.setDisabled(True)
        self.knowledgeSkill.setDisabled(True)
        self.perceptionSkill.setDisabled(True)
        self.technologySkill.setDisabled(True)
        self.charismaSkill.setDisabled(True)
        self.empathySkill.setDisabled(True)
        self.focusSkill.setDisabled(True)
        self.boxingSkill.setDisabled(True)
        self.meleeSkill.setDisabled(True)
        self.rangedSkill.setDisabled(True)
        self.artSkill.setDisabled(True)
        self.languagesSkill.setDisabled(True)
        self.scienceSkill.setDisabled(True)
        self.clairvoyanceSkill.setDisabled(True)
        self.psychokinesisSkill.setDisabled(True)
        self.telepathySkill.setDisabled(True)

        self.additional_skill_points = 12
        self.additional2Display.setText(str(self.additional_skill_points))

        self.deptBox.setDisabled(True)
        self.levelBox.setDisabled(True)

        self.charnameEdit.setText('')
        self.charnameEdit.setDisabled(True)
        self.ageEdit.setText('')
        self.ageEdit.setDisabled(True)
        self.genderEdit.setText('')
        self.genderEdit.setDisabled(True)
        self.rewardDisplay.setText('None')
        self.healthStatus.setText('')
        self.sanityStatus.setText('')
        self.moraleStatus.setText('')
        self.bodyScore.setDisabled(False)
        self.mindScore.setDisabled(False)
        self.spiritScore.setDisabled(False)
        self.armorDisplay.setPlainText('None')
        self.weaponDisplay.setPlainText('None')
        self.itemsDisplay.setPlainText(self.starting_items)
        self.specialDisplay.setPlainText('None')
        self.traitsDisplay.setPlainText('')
        self.backstoryDisplay.setPlainText('')
        self.notesDisplay.setPlainText('')

        self.char_level = 1

        self.char_xp = 0

    def bodyScore_valueChanged(self):
        '''
        A Body Score was entered.
        Add/substract from additional Attribute points.
        '''
        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
        self.additional_attribute_points += self.tempbodyScore - self.bodyScore.value()
        if self.additional_attribute_points >= 0:
            self.additional1Display.setText(str(self.additional_attribute_points))
        else:
            self.additional1Display.setText('<span style=" color:#ff0000;">' + str(self.additional_attribute_points) + '</span>')
        self.tempbodyScore = self.bodyScore.value()
        self.healthDisplay.setText(str(self.status_level[self.health] + self.bodyScore.value()))
        if self.additional_attribute_points == 0:
            self.agilitySkill.setDisabled(False)
            self.beautySkill.setDisabled(False)
            self.strengthSkill.setDisabled(False)
            self.knowledgeSkill.setDisabled(False)
            self.perceptionSkill.setDisabled(False)
            self.technologySkill.setDisabled(False)
            self.charismaSkill.setDisabled(False)
            self.empathySkill.setDisabled(False)
            self.focusSkill.setDisabled(False)
            self.boxingSkill.setDisabled(False)
            self.meleeSkill.setDisabled(False)
            self.rangedSkill.setDisabled(False)
            self.artSkill.setDisabled(False)
            self.languagesSkill.setDisabled(False)
            self.scienceSkill.setDisabled(False)
            #self.clairvoyanceSkill.setDisabled(False)
            #self.psychokinesisSkill.setDisabled(False)
            #self.telepathySkill.setDisabled(False)
        else:
            self.agilitySkill.setDisabled(True)
            self.beautySkill.setDisabled(True)
            self.strengthSkill.setDisabled(True)
            self.knowledgeSkill.setDisabled(True)
            self.perceptionSkill.setDisabled(True)
            self.technologySkill.setDisabled(True)
            self.charismaSkill.setDisabled(True)
            self.empathySkill.setDisabled(True)
            self.focusSkill.setDisabled(True)
            self.boxingSkill.setDisabled(True)
            self.meleeSkill.setDisabled(True)
            self.rangedSkill.setDisabled(True)
            self.artSkill.setDisabled(True)
            self.languagesSkill.setDisabled(True)
            self.scienceSkill.setDisabled(True)
            #self.clairvoyanceSkill.setDisabled(True)
            #self.psychokinesisSkill.setDisabled(True)
            #self.telepathySkill.setDisabled(True)

    def mindScore_valueChanged(self):
        '''
        A Mind Score was entered.
        Add/substract from additional Attribute points.
        '''
        self.additional_attribute_points += self.tempmindScore - self.mindScore.value()
        if self.additional_attribute_points >= 0:
            self.additional1Display.setText(str(self.additional_attribute_points))
        else:
            self.additional1Display.setText('<span style=" color:#ff0000;">' + str(self.additional_attribute_points) + '</span>')
        self.tempmindScore = self.mindScore.value()
        self.sanityDisplay.setText(str(self.status_level[self.sanity] + self.mindScore.value()))
        if self.additional_attribute_points == 0:
            self.agilitySkill.setDisabled(False)
            self.beautySkill.setDisabled(False)
            self.strengthSkill.setDisabled(False)
            self.knowledgeSkill.setDisabled(False)
            self.perceptionSkill.setDisabled(False)
            self.technologySkill.setDisabled(False)
            self.charismaSkill.setDisabled(False)
            self.empathySkill.setDisabled(False)
            self.focusSkill.setDisabled(False)
            self.boxingSkill.setDisabled(False)
            self.meleeSkill.setDisabled(False)
            self.rangedSkill.setDisabled(False)
            self.artSkill.setDisabled(False)
            self.languagesSkill.setDisabled(False)
            self.scienceSkill.setDisabled(False)
            # self.clairvoyanceSkill.setDisabled(False)
            # self.psychokinesisSkill.setDisabled(False)
            # self.telepathySkill.setDisabled(False)
        else:
            self.agilitySkill.setDisabled(True)
            self.beautySkill.setDisabled(True)
            self.strengthSkill.setDisabled(True)
            self.knowledgeSkill.setDisabled(True)
            self.perceptionSkill.setDisabled(True)
            self.technologySkill.setDisabled(True)
            self.charismaSkill.setDisabled(True)
            self.empathySkill.setDisabled(True)
            self.focusSkill.setDisabled(True)
            self.boxingSkill.setDisabled(True)
            self.meleeSkill.setDisabled(True)
            self.rangedSkill.setDisabled(True)
            self.artSkill.setDisabled(True)
            self.languagesSkill.setDisabled(True)
            self.scienceSkill.setDisabled(True)
            # self.clairvoyanceSkill.setDisabled(True)
            # self.psychokinesisSkill.setDisabled(True)
            # self.telepathySkill.setDisabled(True)

    def spiritScore_valueChanged(self):
        '''
        A Spirit Score was entered.
        Add/substract from additional Attribute points.
        '''
        self.additional_attribute_points += self.tempspiritScore - self.spiritScore.value()
        if self.additional_attribute_points >= 0:
            self.additional1Display.setText(str(self.additional_attribute_points))
        else:
            self.additional1Display.setText('<span style=" color:#ff0000;">' + str(self.additional_attribute_points) + '</span>')
        self.tempspiritScore = self.spiritScore.value()
        self.moraleDisplay.setText(str(self.status_level[self.morale] + self.spiritScore.value()))
        if self.additional_attribute_points == 0:
            self.agilitySkill.setDisabled(False)
            self.beautySkill.setDisabled(False)
            self.strengthSkill.setDisabled(False)
            self.knowledgeSkill.setDisabled(False)
            self.perceptionSkill.setDisabled(False)
            self.technologySkill.setDisabled(False)
            self.charismaSkill.setDisabled(False)
            self.empathySkill.setDisabled(False)
            self.focusSkill.setDisabled(False)
            self.boxingSkill.setDisabled(False)
            self.meleeSkill.setDisabled(False)
            self.rangedSkill.setDisabled(False)
            self.artSkill.setDisabled(False)
            self.languagesSkill.setDisabled(False)
            self.scienceSkill.setDisabled(False)
            # self.clairvoyanceSkill.setDisabled(False)
            # self.psychokinesisSkill.setDisabled(False)
            # self.telepathySkill.setDisabled(False)
        else:
            self.agilitySkill.setDisabled(True)
            self.beautySkill.setDisabled(True)
            self.strengthSkill.setDisabled(True)
            self.knowledgeSkill.setDisabled(True)
            self.perceptionSkill.setDisabled(True)
            self.technologySkill.setDisabled(True)
            self.charismaSkill.setDisabled(True)
            self.empathySkill.setDisabled(True)
            self.focusSkill.setDisabled(True)
            self.boxingSkill.setDisabled(True)
            self.meleeSkill.setDisabled(True)
            self.rangedSkill.setDisabled(True)
            self.artSkill.setDisabled(True)
            self.languagesSkill.setDisabled(True)
            self.scienceSkill.setDisabled(True)
            # self.clairvoyanceSkill.setDisabled(True)
            # self.psychokinesisSkill.setDisabled(True)
            # self.telepathySkill.setDisabled(True)
    
    def agilitySkill_valueChanged(self):
        '''
        An Agility Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
        self.additional_skill_points += self.tempagilitySkill - self.agilitySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempagilitySkill = self.agilitySkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def beautySkill_valueChanged(self):
        '''
        A Beauty Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempbeautySkill - self.beautySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempbeautySkill = self.beautySkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)

    def strengthSkill_valueChanged(self):
        '''
        A Strength Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
        self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
        self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
        self.additional_skill_points += self.tempstrengthSkill - self.strengthSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempstrengthSkill = self.strengthSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def knowledgeSkill_valueChanged(self):
        '''
        A Knowledge Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempknowledgeSkill - self.knowledgeSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempknowledgeSkill = self.knowledgeSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def perceptionSkill_valueChanged(self):
        '''
        A Perception Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempperceptionSkill - self.perceptionSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempperceptionSkill = self.perceptionSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def technologySkill_valueChanged(self):
        '''
        A Technology Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temptechnologySkill - self.technologySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temptechnologySkill = self.technologySkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
        
    def charismaSkill_valueChanged(self):
        '''
        A Charisma Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempcharismaSkill - self.charismaSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempcharismaSkill = self.charismaSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def empathySkill_valueChanged(self):
        '''
        An Empathy Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempempathySkill - self.empathySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempempathySkill = self.empathySkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def focusSkill_valueChanged(self):
        '''
        A Focus Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempfocusSkill - self.focusSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempfocusSkill = self.focusSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def boxingSkill_valueChanged(self):
        '''
        A Boxing Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempboxingSkill - self.boxingSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempboxingSkill = self.boxingSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def meleeSkill_valueChanged(self):
        '''
        A Melee Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempmeleeSkill - self.meleeSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempmeleeSkill = self.meleeSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def rangedSkill_valueChanged(self):
        '''
        A Ranged Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temprangedSkill - self.rangedSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temprangedSkill = self.rangedSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def artSkill_valueChanged(self):
        '''
        A Art Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempartSkill - self.artSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempartSkill = self.artSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def languagesSkill_valueChanged(self):
        '''
        A Languages Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.templanguagesSkill - self.languagesSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.templanguagesSkill = self.languagesSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def scienceSkill_valueChanged(self):
        '''
        A Science Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempscienceSkill - self.scienceSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempscienceSkill = self.scienceSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def clairvoyanceSkill_valueChanged(self):
        '''
        A Clairvoyance Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.tempclairvoyanceSkill - self.clairvoyanceSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.tempclairvoyanceSkill = self.clairvoyanceSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def psychokinesisSkill_valueChanged(self):
        '''
        A Psychokinesis Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temppsychokinesisSkill - self.psychokinesisSkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temppsychokinesisSkill = self.psychokinesisSkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def telepathySkill_valueChanged(self):
        '''
        A Telepathy Skill was entered.
        Add/substract from additional Skill points.
        '''
        self.additional_skill_points += self.temptelepathySkill - self.telepathySkill.value()
        if self.additional_skill_points >= 0:
            self.additional2Display.setText(str(self.additional_skill_points))
        else:
            self.additional2Display.setText('<span style=" color:#ff0000;">' + str(self.additional_skill_points) + '</span>')
        self.temptelepathySkill = self.telepathySkill.value()
        if self.additional_skill_points == 0:
            if self.department_not_chosen:
                self.deptBox.setDisabled(False)
            else:
                self.levelBox.setDisabled(False)
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setDisabled(False)
                self.genderEdit.setDisabled(False)
                self.rewardDisplay.setText(str(self.agilitySkill.value() + self.beautySkill.value() + self.strengthSkill.value() +
                        self.knowledgeSkill.value() + self.perceptionSkill.value() + self.technologySkill.value() +
                        self.charismaSkill.value() + self.empathySkill.value() + self.focusSkill.value() +
                        self.boxingSkill.value() + self.meleeSkill.value() + self.rangedSkill.value() +
                        self.artSkill.value() + self.languagesSkill.value() + self.scienceSkill.value() +
                        self.clairvoyanceSkill.value() + self.psychokinesisSkill.value() + self.telepathySkill.value()) + 'xp')
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
        else:
            self.deptBox.setDisabled(True)
            self.levelBox.setDisabled(True)
            self.charnameEdit.setDisabled(True)
            self.ageEdit.setDisabled(True)
            self.genderEdit.setDisabled(True)
            self.rewardDisplay.setText('None')
            self.saveButton.setDisabled(True)
            self.actionSave.setDisabled(True)
            self.printButton.setDisabled(True)
            self.actionPrint.setDisabled(True)
    
    def deptBox_changed(self):
        '''
        A crew department was chosen for the character
        '''
        self.itemsDisplay.setPlainText(self.starting_items)
        if self.deptBox.currentIndex() == 0:
            self.dept_chosen = ''
            self.rankDisplay.setDisabled(True)
            self.rankDisplay.setText('')
            self.bodyScore.setDisabled(False)
            self.mindScore.setDisabled(False)
            self.spiritScore.setDisabled(False)
            self.agilitySkill.setDisabled(False)
            self.beautySkill.setDisabled(False)
            self.strengthSkill.setDisabled(False)
            self.knowledgeSkill.setDisabled(False)
            self.perceptionSkill.setDisabled(False)
            self.technologySkill.setDisabled(False)
            self.charismaSkill.setDisabled(False)
            self.empathySkill.setDisabled(False)
            self.focusSkill.setDisabled(False)
            self.boxingSkill.setDisabled(False)
            self.meleeSkill.setDisabled(False)
            self.rangedSkill.setDisabled(False)
            self.artSkill.setDisabled(False)
            self.languagesSkill.setDisabled(False)
            self.scienceSkill.setDisabled(False)
            self.clairvoyanceSkill.setDisabled(True)
            self.psychokinesisSkill.setDisabled(True)
            self.telepathySkill.setDisabled(True)
            self.additional_skill_points = 0
            self.additional2Display.setText(str(self.additional_skill_points))
            self.department_not_chosen = True
        else:
            self.bodyScore.setDisabled(True)
            self.mindScore.setDisabled(True)
            self.spiritScore.setDisabled(True)
            self.agilitySkill.setDisabled(True)
            self.beautySkill.setDisabled(True)
            self.strengthSkill.setDisabled(True)
            self.knowledgeSkill.setDisabled(True)
            self.perceptionSkill.setDisabled(True)
            self.technologySkill.setDisabled(True)
            self.charismaSkill.setDisabled(True)
            self.empathySkill.setDisabled(True)
            self.focusSkill.setDisabled(True)
            self.boxingSkill.setDisabled(True)
            self.meleeSkill.setDisabled(True)
            self.rangedSkill.setDisabled(True)
            self.artSkill.setDisabled(True)
            self.languagesSkill.setDisabled(True)
            self.scienceSkill.setDisabled(True)
            self.clairvoyanceSkill.setDisabled(True)
            self.psychokinesisSkill.setDisabled(True)
            self.telepathySkill.setDisabled(True)
            self.dept_chosen = self.dept_choice[self.deptBox.currentIndex()]
            self.rankDisplay.setDisabled(False)
            self.rankDisplay.setText(self.dept_rank)
            self.dept_skill_chosen = self.dept_skill[self.deptBox.currentIndex()]
            self.dept_item_chosen = self.dept_item[self.deptBox.currentIndex()]
            if self.dept_skill_chosen == 'Body':
                self.agilitySkill.setDisabled(False)
                self.beautySkill.setDisabled(False)
                self.strengthSkill.setDisabled(False)
            elif self.dept_skill_chosen == 'Mind':
                self.knowledgeSkill.setDisabled(False)
                self.perceptionSkill.setDisabled(False)
                self.technologySkill.setDisabled(False)
            elif self.dept_skill_chosen == 'Spirit':
                self.charismaSkill.setDisabled(False)
                self.empathySkill.setDisabled(False)
                self.focusSkill.setDisabled(False)
            elif self.dept_skill_chosen == 'Combat':
                self.boxingSkill.setDisabled(False)
                self.meleeSkill.setDisabled(False)
                self.rangedSkill.setDisabled(False)
            elif self.dept_skill_chosen == 'Strange':
                self.artSkill.setDisabled(False)
                self.languagesSkill.setDisabled(False)
                self.scienceSkill.setDisabled(False)
            elif self.dept_skill_chosen == 'Psionic':
                self.clairvoyanceSkill.setDisabled(False)
                self.psychokinesisSkill.setDisabled(False)
                self.telepathySkill.setDisabled(False)
            self.additional_skill_points = 3
            self.additional2Display.setText(str(self.additional_skill_points))
            self.department_not_chosen = False
            self.temp_item = self.itemsDisplay.toPlainText()
            self.itemsDisplay.setPlainText(self.temp_item + ', ' + self.dept_item_chosen)

    def levelBox_changed(self):
        self.char_level = self.levelBox.currentIndex() + 1
    
    def loadButton_clicked(self):
        '''
        Load a .tps file for an already saved character.
        The file is stored in JSON format.
        '''
        self.filename = QFileDialog.getOpenFileName(self, 'Open TPS Character File', self.char_folder, 'TPS files (*' + self.file_extension + ')')
        if self.filename[0] != '':
            #print(self.filename)
            log.info('Loading ' + self.filename[0])
            with open(self.filename[0], 'r') as json_file:
                self.char_data = json.load(json_file)
                #pprint.pprint(self.char_data)
                self.format_read = self.char_data['Fileformat']
                log.info('File format is: ' + str(self.format_read))
                self.charnameEdit.setText(self.char_data['Name'])
                self.charnameEdit.setDisabled(False)
                self.ageEdit.setText(self.char_data['Age'])
                self.ageEdit.setDisabled(False)
                self.genderEdit.setText(self.char_data['Gender'])
                self.genderEdit.setDisabled(False)
                self.temp_field = self.char_data['Dept']
                self.dept_chosen = self.dept_choice.index(self.temp_field)
                self.deptBox.setCurrentIndex(self.dept_chosen)
                self.rankDisplay.setText(self.char_data['Rank'])
                self.bodyScore.setValue(self.char_data['BODY'])
                self.bodyScore.setDisabled(True)
                self.mindScore.setValue(self.char_data['MIND'])
                self.mindScore.setDisabled(True)
                self.spiritScore.setValue(self.char_data['SPIRIT'])
                self.spiritScore.setDisabled(True)
                self.healthStatus.setText('')
                self.sanityStatus.setText('')
                self.moraleStatus.setText('')
                self.healthDisplay.setText(self.char_data['HEALTH'])
                if self.healthDisplay.text() == '2':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.healthDisplay.text() == '1':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.healthDisplay.text() == '0':
                    self.healthStatus.setText('<span style=" color:#ff0000;">Incapacitated</span>')
                    log.debug('Character is incapacitated!')
                if int(self.healthDisplay.text()) < 0:
                    self.healthStatus.setText('<span style=" color:#ff0000;">Expire</span>')
                    log.debug('Character has expired!')
                self.sanityDisplay.setText(self.char_data['SANITY'])
                if self.sanityDisplay.text() == '2':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.sanityDisplay.text() == '1':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.sanityDisplay.text() == '0':
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Erratic</span>')
                    log.debug('Character is erratic!')
                if int(self.sanityDisplay.text()) < 0:
                    self.sanityStatus.setText('<span style=" color:#ff0000;">Snap</span>')
                    log.debug('Character has snapped!')
                self.moraleDisplay.setText(self.char_data['MORALE'])
                if self.moraleDisplay.text() == '2':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Hurt</span>')
                if self.moraleDisplay.text() == '1':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Wounded</span>')
                if self.moraleDisplay.text() == '0':
                    self.moraleStatus.setText('<span style=" color:#ff0000;">In Fear</span>')
                    log.debug('Character is in fear!')
                if int(self.moraleDisplay.text()) < 0:
                    self.moraleStatus.setText('<span style=" color:#ff0000;">Submit</span>')
                    log.debug('Character has submit!')
                self.additional1Display.setText('0')
                self.agilitySkill.setValue(self.char_data['Agility'])
                self.agilitySkill.setDisabled(True)
                self.beautySkill.setValue(self.char_data['Beauty'])
                self.beautySkill.setDisabled(True)
                self.strengthSkill.setValue(self.char_data['Strength'])
                self.strengthSkill.setDisabled(True)
                self.knowledgeSkill.setValue(self.char_data['Knowledge'])
                self.knowledgeSkill.setDisabled(True)
                self.perceptionSkill.setValue(self.char_data['Perception'])
                self.perceptionSkill.setDisabled(True)
                self.technologySkill.setValue(self.char_data['Technology'])
                self.technologySkill.setDisabled(True)
                self.charismaSkill.setValue(self.char_data['Charisma'])
                self.charismaSkill.setDisabled(True)
                self.empathySkill.setValue(self.char_data['Empathy'])
                self.empathySkill.setDisabled(True)
                self.focusSkill.setValue(self.char_data['Focus'])
                self.focusSkill.setDisabled(True)
                self.boxingSkill.setValue(self.char_data['Boxing'])
                self.boxingSkill.setDisabled(True)
                self.meleeSkill.setValue(self.char_data['Melee'])
                self.meleeSkill.setDisabled(True)
                self.rangedSkill.setValue(self.char_data['Ranged'])
                self.rangedSkill.setDisabled(True)
                self.artSkill.setValue(self.char_data['Art'])
                self.artSkill.setDisabled(True)
                self.languagesSkill.setValue(self.char_data['Languages'])
                self.languagesSkill.setDisabled(True)
                self.scienceSkill.setValue(self.char_data['Science'])
                self.scienceSkill.setDisabled(True)
                self.clairvoyanceSkill.setValue(self.char_data['Clairvoyance'])
                self.clairvoyanceSkill.setDisabled(True)
                self.psychokinesisSkill.setValue(self.char_data['Psychokinesis'])
                self.psychokinesisSkill.setDisabled(True)
                self.telepathySkill.setValue(self.char_data['Telepathy'])
                self.telepathySkill.setDisabled(True)
                self.additional2Display.setText('0')
                self.rewardDisplay.setText(self.char_data['Reward'])
                if int(self.healthDisplay.text()) > 1:
                    self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
                    self.movementDisplay.setText(str(1 + self.bodyScore.value() + self.agilitySkill.value()) + ' spaces')
                    self.rangeDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' miles')
                    log.debug('Character can move fine.')
                elif int(self.healthDisplay.text()) == 1:
                    self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
                    self.movementDisplay.setText('<span style=" color:#ff0000;">' + str((1 + self.bodyScore.value() + self.agilitySkill.value()) // 2) + ' spaces</span>')
                    self.rangeDisplay.setText('<span style=" color:#ff0000;">' + str((1 + self.bodyScore.value() + self.strengthSkill.value()) // 2) + ' miles</span>')
                    log.debug("Character's movement is cut in half.")
                elif int(self.healthDisplay.text()) < 1:
                    self.encumbranceDisplay.setText(str(1 + self.bodyScore.value() + self.strengthSkill.value()) + ' items')
                    self.movementDisplay.setText('<span style=" color:#ff0000;">0 spaces</span>')
                    self.rangeDisplay.setText('<span style=" color:#ff0000;">0 miles</span>')
                    log.debug("Character can't move.")
                self.armorDisplay.setPlainText(self.char_data['ARMOR'])
                self.weaponDisplay.setPlainText(self.char_data['WEAPON'])
                self.itemsDisplay.setPlainText(self.char_data['ITEMS'])
                self.specialDisplay.setPlainText(self.char_data['SPECIAL'])
                self.traitsDisplay.setPlainText(self.char_data['TRAITS'])
                self.backstoryDisplay.setPlainText(self.char_data['BACKSTORY'])
                self.notesDisplay.setPlainText(self.char_data['NOTES'])
                self.saveButton.setDisabled(False)
                self.actionSave.setDisabled(False)
                self.printButton.setDisabled(False)
                self.actionPrint.setDisabled(False)

    def saveButton_clicked(self):
        '''
        Save the .tps file for a generated or edited character.
        The name of the saved file is the name of the character.
        The file is stored in JSON format.
        '''
        if self.charnameEdit.text() == '':
            print('NO NAME!')
            log.debug("Can't save because of NO NAME!")
        else:
            json_file_out = open(self.char_folder + '/' + self.charnameEdit.text() + self.file_extension, 'w')
            self.char_data = {}
            self.char_data['Fileformat'] = self.file_format
            self.char_data['Name'] = self.charnameEdit.text()
            self.char_data['Age'] = self.ageEdit.text()
            self.char_data['Gender'] = self.genderEdit.text()
            self.char_data['Reward'] = self.rewardDisplay.text()
            self.char_data['BODY'] = self.bodyScore.value()
            self.char_data['MIND'] = self.mindScore.value()
            self.char_data['SPIRIT'] = self.spiritScore.value()
            self.char_data['HEALTH'] = self.healthDisplay.text()
            self.char_data['SANITY'] = self.sanityDisplay.text()
            self.char_data['MORALE'] = self.moraleDisplay.text()
            self.char_data['Agility'] = self.agilitySkill.value()
            self.char_data['Beauty'] = self.beautySkill.value()
            self.char_data['Strength'] = self.strengthSkill.value()
            self.char_data['Knowledge'] = self.knowledgeSkill.value()
            self.char_data['Perception'] = self.perceptionSkill.value()
            self.char_data['Technology'] = self.technologySkill.value()
            self.char_data['Charisma'] = self.charismaSkill.value()
            self.char_data['Empathy'] = self.empathySkill.value()
            self.char_data['Focus'] = self.focusSkill.value()
            self.char_data['Boxing'] = self.boxingSkill.value()
            self.char_data['Melee'] = self.meleeSkill.value()
            self.char_data['Ranged'] = self.rangedSkill.value()
            self.char_data['Art'] = self.artSkill.value()
            self.char_data['Languages'] = self.languagesSkill.value()
            self.char_data['Science'] = self.scienceSkill.value()
            self.char_data['Clairvoyance'] = self.clairvoyanceSkill.value()
            self.char_data['Psychokinesis'] = self.psychokinesisSkill.value()
            self.char_data['Telepathy'] = self.telepathySkill.value()
            self.char_data['Dept'] = self.dept_chosen
            self.char_data['Rank'] =self.rankDisplay.text()
            self.char_data['ARMOR'] = self.armorDisplay.toPlainText()
            self.char_data['WEAPON'] = self.weaponDisplay.toPlainText()
            self.char_data['ITEMS'] = self.itemsDisplay.toPlainText()
            self.char_data['SPECIAL'] = self.specialDisplay.toPlainText()
            self.char_data['TRAITS'] = self.traitsDisplay.toPlainText()
            self.char_data['BACKSTORY'] = self.backstoryDisplay.toPlainText()
            self.char_data['NOTES'] = self.notesDisplay.toPlainText()
            self.char_data['Level'] = self.char_level
            self.char_data['XP'] = self.char_xp
            json.dump(self.char_data, json_file_out, ensure_ascii=True)
            json_file_out.close()
            log.info('Character saved as ' + self.charnameEdit.text() + self.file_extension + ' in file format ' + str(self.file_format))
            self.printButton.setDisabled(False)
            self.actionPrint.setDisabled(False)
            self.popSaveDialog.show()
    
    def printButton_clicked(self):
        '''
        Print the character as a PDF.
        '''
        print('Printing as PDF...')
        pdf = FPDF(orientation='P', unit='in', format='Letter')
        pdf.add_page()
        pdf.image(name=CURRENT_DIR + '\\wwsm_logo.png')
        pdf.add_font(family='Comic Sans MS', style='', fname=r'C:\Windows\Fonts\comic.ttf', uni='True')
        pdf.add_font(family='Comic Sans MS', style='B', fname=r'C:\Windows\Fonts\comicbd.ttf', uni='True')
        pdf.set_font('Comic Sans MS', 'B', 20)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt=self.game_name, ln=1)
        pdf.cell(txt='CHARACTER LOGBOOK', ln=1)
        pdf.set_font('Comic Sans MS', '', 16)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='Name: ' + self.charnameEdit.text(), ln=1)
        pdf.cell(txt='Age: ' + self.ageEdit.text(), ln=1)
        pdf.cell(txt='Gender: ' + self.genderEdit.text(), ln=1)
        pdf.cell(txt='Dept: ' + self.dept_chosen, ln=1)
        pdf.cell(txt='Rank: ' + self.rankDisplay.text(), ln=1)
        pdf.cell(txt='Level: ' + str(self.char_level) + '    XP: ' + str(self.char_xp), ln=1)
        pdf.cell(txt=' ', ln=1)
        pdf.set_font('Comic Sans MS', '', 22)
        pdf.cell(txt='BODY: ' + str(self.bodyScore.value()), ln=1)
        pdf.cell(txt='MIND: ' + str(self.mindScore.value()), ln=1)
        pdf.cell(txt='SPIRIT: ' + str(self.spiritScore.value()), ln=1)
        pdf.cell(txt='HEALTH: ' + str(self.healthDisplay.text()), ln=1)
        pdf.cell(txt='SANITY: ' + str(self.sanityDisplay.text()), ln=1)
        pdf.cell(txt='MORALE: ' + str(self.moraleDisplay.text()), ln=1)
        pdf.set_font('Comic Sans MS', '', 16)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='      Body Skills', ln=1)
        pdf.cell(txt='Agility: ' + str(self.agilitySkill.value()), ln=1)
        pdf.cell(txt='Beauty: ' + str(self.beautySkill.value()), ln=1)
        pdf.cell(txt='Strength: ' + str(self.strengthSkill.value()), ln=1)
        pdf.cell(txt='      Mind Skills', ln=1)
        pdf.cell(txt='Knowledge: ' + str(self.knowledgeSkill.value()), ln=1)
        pdf.cell(txt='Perception: ' + str(self.perceptionSkill.value()), ln=1)
        pdf.cell(txt='Technology: ' + str(self.technologySkill.value()), ln=1)
        pdf.cell(txt='      Spirit Skills', ln=1)
        pdf.cell(txt='Charisma: ' + str(self.charismaSkill.value()), ln=1)
        pdf.cell(txt='Empathy: ' + str(self.empathySkill.value()), ln=1)
        pdf.cell(txt='Focus: ' + str(self.focusSkill.value()), ln=1)
        pdf.cell(txt='      Combat Skills', ln=1)
        pdf.cell(txt='Boxing: ' + str(self.boxingSkill.value()), ln=1)
        pdf.cell(txt='Melee: ' + str(self.meleeSkill.value()), ln=1)
        pdf.cell(txt='Ranged: ' + str(self.rangedSkill.value()), ln=1)
        pdf.add_page()
        pdf.set_font('Comic Sans MS', '', 10)
        pdf.cell(txt=self.game_name + '   ...continuing with character: ' + self.charnameEdit.text(), ln=1)
        pdf.set_font('Comic Sans MS', '', 16)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='      Strange Skills', ln=1)
        pdf.cell(txt='Art: ' + str(self.artSkill.value()), ln=1)
        pdf.cell(txt='Languages: ' + str(self.languagesSkill.value()), ln=1)
        pdf.cell(txt='Science: ' + str(self.scienceSkill.value()), ln=1)
        pdf.cell(txt='      Psionic Skills', ln=1)
        pdf.cell(txt='Clairvoyance: ' + str(self.clairvoyanceSkill.value()), ln=1)
        pdf.cell(txt='Psychokinesis: ' + str(self.psychokinesisSkill.value()), ln=1)
        pdf.cell(txt='Telepathy: ' + str(self.telepathySkill.value()), ln=1)
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='ARMOR:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        pdf.cell(txt=self.armorDisplay.toPlainText(), ln=1)
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='WEAPON:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        pdf.cell(txt=self.weaponDisplay.toPlainText(), ln=1)
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='ITEMS:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        some_text = self.itemsDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 14:
                for i in range(14):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = some_text[14:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = ''
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='SPECIAL:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        pdf.cell(txt=self.specialDisplay.toPlainText(), ln=1)
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='PERSONALITY / APPEARANCE:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        some_text = self.traitsDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 14:
                for i in range(14):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = some_text[14:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = ''
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='BACKSTORY:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        some_text = self.backstoryDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 14:
                for i in range(14):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = some_text[14:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = ''
        pdf.set_font('Comic Sans MS', '', 18)
        pdf.cell(txt=' ', ln=1)
        pdf.cell(txt='NOTES:', ln=1)
        pdf.set_font('Comic Sans MS', '', 14)
        some_text = self.notesDisplay.toPlainText()
        some_text = some_text.split()
        while len(some_text) > 0:
            some_words = ''
            if len(some_text) > 14:
                for i in range(14):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = some_text[14:]
            else:
                for i in range(len(some_text)):
                    some_words += some_text[i] + ' '
                pdf.cell(txt=some_words, ln=1)
                some_text = ''

        pdf.output(self.char_folder + '/' + self.charnameEdit.text() + '.pdf')
        log.info('Character printed as ' + self.charnameEdit.text() + '.pdf')

    def Visit_Blog(self):
        '''
        open web browser to blog URL
        '''
        os.startfile('http://shawndriscoll.blogspot.com')
        
    def Feedback(self):
        '''
        open an email letter to send as feedback to the author
        '''
        os.startfile('mailto:shawndriscoll@hotmail.com?subject=Feedback: ' + __app__ + ' for Total Party Skills RPG')
    
    def Overview_menu(self):
        '''
        open this app's PDF manual
        '''
        log.info(__app__ + ' looking for PDF manual...')
        os.startfile(CURRENT_DIR + '\\wwsm_chargen_manual.pdf')
        log.info(__app__ + ' found PDF manual. Opening...')

    def actionAbout_triggered(self):
        '''
        open the About window
        '''
        log.info(__app__ + ' show about...')
        self.popAboutDialog.show()

    def alert_window(self):
        '''
        open the Alert window
        '''
        log.warning(__app__ + ' show Beta expired PyQt5 alertDialog...')
        self.popAlertDialog.show()

    def actionQuitProg_triggered(self):
        '''
        select "Quit" from the drop-down menu
        '''
        log.info(__app__ + ' quiting...')
        log.info(__app__ + ' DONE.')
        self.close()

if __name__ == '__main__':
    
    '''
    Technically, this program starts right here when run.
    If this program is imported instead of run, none of the code below is executed.
    '''

    log = logging.getLogger('WWSM_Chargen_' + __version__)
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/wwsm_chargen.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s', datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    
    log.info('Logging started.')
    log.info(__app__ + ' starting...')
    
    trange = time.localtime()

    log.info(__app__ + ' started, and running...')

    #if trange[0] > 2021 or trange[1] > 11:
    if trange[0] > 2021:
        __expired_tag__ = True
        __app__ += ' [EXPIRED]'
        
    app = QApplication(sys.argv)

    mainApp = MainWindow()
    mainApp.show()
    
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    app.exec_()
