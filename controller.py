#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gui import GUI
from db import Loader


class Controller():
    gui = None
    db = None
    
    def __init__(self):
        self.db = Loader()
        self.gui = GUI()
        self.gui.setController(self)

    def initApp(self):
        self.db.loadData()
        self.gui.initApp()

    def getQuestion(self, numQuestion):
        return self.db.getQuestion(numQuestion)

    def getNumQuestions(self):
        return self.db.getNumQuestions()
