# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:30:00 2018
@author: dicky jaya umbara
"""

import random

print("=================================")
print("=== KUCING MAEN CAKAR CAKARAN ===")
print("=================================")
print("")

class Kucing():
    def __init__(self, name, score):
        self.name = name
        self.score = score
            
    def cakar_ke(self, lawan):
        sentence = self.name + " nyakar " + lawan.name
        resp_sentence = lawan.response(self)
        whole_sentence = sentence+", "+resp_sentence
        info_score = whole_sentence
        return info_score
        
    def cakar(self, lawan): #obyek argtype: string
        sentence = self.name+" nyakar "+lawan.name+"!"
        return sentence
    
    def response(self, lawan):        
        response_type = random.randint(0,2)
        if response_type == 0:
            sentence = self.name+" menghindar cakaran "+lawan.name 
            response = sentence
        elif response_type == 1:
            sentence = self.name+" pasrah ama cakaran "+lawan.name + " || 1 POIN UNTUK " + lawan.name 
            lawan.score += 1
            response = sentence
        else:
            sentence = self.name+" menangkis cakaran "+lawan.name
            response = sentence
        return response


def CakarCakaran(kucing1, kucing2):
    ronde = 0
    while (kucing1.score != 3) and (kucing2.score != 3):
       ronde += 1
       print("=== RONDE "+ str(ronde) + " ===")
       print(kucing1.cakar_ke(kucing2))
       print(kucing2.cakar_ke(kucing1))
       print("score = " + kucing1.name + " : " + str(kucing1.score) + " | " + kucing2.name + " : " + str(kucing2.score))
       print("")
       
    if kucing1.score > kucing2.score:
        print("=== PEMENANG " + kucing1.name + " ===" )
    elif kucing1.score < kucing2.score:
        print("=== PEMENANG " + kucing2.name + " ===" )
    else:
        print("=== HASIL SERI ===")
        
kiti = Kucing("Kiti", 0)
miau = Kucing("Miau", 0)

CakarCakaran(kiti, miau)
