#!/usr/bin/env python
#-*- coding: utf-8 -*-

from gi.repository import Gtk

class GUI():
    builder = None
    formMain = None
    formNew =None
    formQuestion = None
    formScoring =None
    formAbout = None
    name = ""
    course = ""
    numQuestion = 1
    numQuestions = 0
    rightAnswer = 0
    rightAnswersCounter = 0
    controller = None
    FORMS = "/home/albert/workspace/python/quizz2/forms.glade"

    def setController(self, controller):
        self.controller = controller

    def initApp(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.FORMS)
        self.builder.connect_signals(self)
        
        self.formMain = self.builder.get_object("applicationwindow1")
        self.formMain.show()
        Gtk.main()
        
    def onClose(self, *args):
        print "onClose"
        Gtk.main_quit(*args)
        exit()
    
    def onMenuitemNou(self, widget):
        self.formNew = self.builder.get_object("dialog1")
        self.formNew.set_transient_for(self.formMain)
        self.numQuestions = self.controller.getNumQuestions()
        self.builder.get_object("entry3").set_text("")
        self.builder.get_object("entry2").set_text("")        
        self.formNew.show()
        print "onMenuitemNouClick"
        
    def onMenuitemSurt(self, widget):
        print "onMenuitemSurtClick"
        Gtk.main_quit()
        exit()
        
    def onMenuitemAbout(self, widget):
        self.formAbout = self.builder.get_object("aboutdialog1")
        self.formAbout.set_transient_for(self.formMain)
        self.formAbout.run()
        self.formAbout.hide()
            
        print "onMenuitemAbout"
        
    def onButton1AcceptarClick(self, widget):
        self.name = self.builder.get_object("entry3").get_text()
        self.course = self.builder.get_object("entry2").get_text()
        self.formNew.hide()

        self.formQuestion = self.builder.get_object("dialog2")
        self.formQuestion.set_transient_for(self.formMain)
        self.setFormQuestion(self.numQuestion)
        self.formQuestion.show()        
        
        print "Nom: %s; Curs: %s" % (self.name, self.course)
        print "onButton1AcceptarClick"

    def setFormQuestion(self, numQuestion):
        [question, answers, self.rightAnswer] = self.controller.getQuestion(numQuestion)
        self.builder.get_object("label8").set_text("%s de %s curs" % (self.name, self.course))
        self.builder.get_object("label3").set_text("Pregunta %d" % numQuestion)
        self.builder.get_object("label4").set_text(question)
        self.builder.get_object("checkbutton1").set_label(answers[1])
        self.builder.get_object("checkbutton2").set_label(answers[2])
        self.builder.get_object("checkbutton3").set_label(answers[3])
        self.builder.get_object("checkbutton4").set_label(answers[4])
        self.builder.get_object("checkbutton1").set_active(False)
        self.builder.get_object("checkbutton2").set_active(False)
        self.builder.get_object("checkbutton3").set_active(False)
        self.builder.get_object("checkbutton4").set_active(False)

    def onButton2CancelarClick(self, widget):
        self.formNew.hide()
        print "onButton2CancelarClick"

    def onButtonSeguir(self, widget):
        # validate right answer. increment question counter,
        myAnswer = (1 * self.builder.get_object("checkbutton1").get_active()) + \
                   (2 * self.builder.get_object("checkbutton2").get_active()) + \
                   (4 * self.builder.get_object("checkbutton3").get_active()) + \
                   (8 * self.builder.get_object("checkbutton4").get_active())
        rightAnswer = pow(2, self.rightAnswer - 1)

        if myAnswer == rightAnswer:
            self.rightAnswersCounter = self.rightAnswersCounter + 1

        self.numQuestion = self.numQuestion + 1

        if self.numQuestion <= self.numQuestions:
            self.setFormQuestion(self.numQuestion)
            self.formQuestion.show()
        else:
            self.formQuestion.hide()
            self.formScoring = self.builder.get_object("dialog3")
            self.formScoring.set_transient_for(self.formMain)
            self.builder.get_object("labelNom").set_text("%s de %s curs" % (self.name, self.course))
            self.builder.get_object("label6").set_text("%d preguntes" % self.rightAnswersCounter)
            self.builder.get_object("label7").set_text("d'un total de %d preguntes" % self.numQuestions)
            self.formScoring.show()        

        print "onButtonSeguir"
        
    def onCancelarQuizz(self, widget):
        self.reset()
        self.formQuestion.hide()
        print "onCancelarClick"

    def onTancarClick(self, widget):
        self.reset()
        self.formScoring.hide()
        print "onTancarClick"

    def reset(self):
        self.name = ""
        self.course = ""
        self.numQuestion = 1
        self.rightAnswer = 0
        self.rightAnswersCounter = 0

