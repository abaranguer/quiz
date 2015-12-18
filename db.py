#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class Loader:
    CONNECTION_STRING = "/home/albert/workspace/python/quizz2/db/quizz.db"
    SELECT_QUESTIONS = "select id, question from questions"
    SELECT_ANSWERS = "select a.id, a.answer " + \
                     " from answers a, questions_answers qa " + \
                     " where qa.id_question = ? " + \
                     " and qa.id_answer = a.id"
    SELECT_RIGHT_ANSWER = "select id_right_answer " + \
                          " from question_right_answer " + \
                          " where id_question = ? "

    questions = []
    answer = []
    answers = []
    numQuestions = 0
    
    def loadData(self):
        conn = sqlite3.connect(self.CONNECTION_STRING)
        cur_questions = conn.cursor()
        cur_answers = conn.cursor()
        cur_right_answer = conn.cursor()
    
        cur_questions.execute(self.SELECT_QUESTIONS)
        self.numQuestions = 0
        for row_question in cur_questions:
            # load question
            self.questions.append(row_question[1])
            # load right answer
            cur_right_answer.execute(self.SELECT_RIGHT_ANSWER, (row_question[0],))
            id_right_answer = cur_right_answer.fetchone()[0]
            self.answer = []
            self.answer.append(id_right_answer)
            # load answers for this question
            cur_answers.execute(self.SELECT_ANSWERS, (row_question[0],))
            num_right_answer = 1
            for r_answer in cur_answers:
                self.answer.append(r_answer[1])
                if id_right_answer == r_answer[0]:
                    self.answer[0] = num_right_answer
                num_right_answer = num_right_answer + 1
            self.answers.append(self.answer)
            self.numQuestions = self.numQuestions + 1
        conn.close()
    
    def getQuestion(self, numQuestion):
        return [self.questions[numQuestion-1],
                self.answers[numQuestion-1],
                self.answers[numQuestion-1][0]] 

    def getNumQuestions(self):
        return self.numQuestions
        
