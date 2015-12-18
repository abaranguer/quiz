#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

questions = (
    u"Com es diu el wookie que acompanya a Han Solo?",
    u"De quina especie són els ossets peluts de la lluna santuari d'Endor?",
    u"A quina batalla va ser destruida la primera Estrella de la Mort?",
    u"Quantes temporades té la serie de The Clone Wars?",
    u"Com es diu la padawan d'Anakin Skywalker?",
    u"Quin és el nom Sith del Comte Dooku?",
    u"De quin planeta és Luke Skywalker?",
    u"A quin planeta és el duel entre Anakin Skywalker i Obi-Wan Kenobi?",
    u"De quin color és l'espasa laser de Mace Windu?",
    u"De quin color és l'espasa laser dels lords Sith?"
)

answers = (
    (2, "Peret", "Chewbacca", "Sr. Spock", "Leia Organa"),
    (1, "Ewoks", "Wookies", "Mandalorians", "Corellians"),
    (4, "Waterloo", "Normandia", "Toth", "Yavin-4"),
    (3, "1000", "5", "6", "7"),
    (3, "Artiom", "Assaj Ventress", "Ahsoka Tano", "Kanan Jarrus"),
    (4, "Darth Sidious", "Darth Turo", "Darth Tenebre", "Darth Tyranus"),
    (2, "Naboo", "Tatooine", "Mandalore", "Alderaan"),
    (1, "Mustafar", "Kamino", "Vulcano", "Warsoom"),
    (4, "Blau", "Verd", "Vermell", "Violeta"),
    (2, "Blanc", "Vermell", "Blau", "Violeta")
)

CONNECTION_STRING = "/home/albert/workspace/python/quizz/db/quizz.db"
INSERT_QUESTION = "insert into questions(question) values (?)"
INSERT_ANSWER = "insert into answers(answer) values (?)"
INSERT_QUESTION_ANSWER = "insert into questions_answers(id_question, id_answer) values (?, ?)"
INSERT_RIGHT_ANSWER = "insert into question_right_answer(id_question, id_right_answer) values (?,?)"

if __name__ == '__main__':
    print "begin"
    conn = sqlite3.connect(CONNECTION_STRING)

    cur = conn.cursor()
    num_question = 0
    
    for question in questions:
        cur.execute(INSERT_QUESTION, (question,))
        id_question = cur.lastrowid

        right_answer = answers[num_question][0]

        for num_answer in range(1,5):
            cur.execute(INSERT_ANSWER, (answers[num_question][num_answer],))
            id_answer = cur.lastrowid

            cur.execute(INSERT_QUESTION_ANSWER, (id_question, id_answer))
            if num_answer == right_answer:
                cur.execute(INSERT_RIGHT_ANSWER, (id_question, id_answer))

        num_question = num_question + 1
        
    conn.commit()
    conn.close()

    print "done!"
