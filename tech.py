# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:42:28 2020

@author: Ansu Mathew
"""

class learnment:
    enc=1
    def _init_(self,stack,time,ml):
        self.stack=stack
        self.time=time
        self.ml=ml
    def addStacks(self):
        self.stack=input('Enter interests and Expertise\n')
    def setMentorOrLearner(self):
        self.ml=input('Enter m for mentor and l for learner\n')
    def setAvailableTime(self):
        if self.ml=='m':
           self.time=input('Enter time available from( which hour to which)\n')
        else:
            print('mee\n')
    def getMentor(self,stk,tm):
        if self.time==tm and self.stack==stk:
            return learnment()


f=learnment()
f.addStacks()
f.setMentorOrLearner()
f.setAvailableTime()
k=f.getMentor('p','m')


        
        
            
            