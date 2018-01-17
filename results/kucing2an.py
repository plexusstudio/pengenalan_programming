# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:41:09 2018

@author: sancita
"""
import random

class Kucing():
    def __init__ (self, warna, usia = 1, gender = 0):
        self.warna = warna
        self.usia = usia
        if gender == 0:
            self.gender = "jantan"
        else:
            self.gender = "betina"
            
    def kegiatan(self, lawan, benda):
        benda.updateHolder(lawan)
        sentence = self.warna+" membawa "+benda.warna+" ke "+lawan.warna
        resp_sentence = lawan.respon(self, benda)
        whole_sentence = sentence+", "+resp_sentence
        return whole_sentence
    
    def respon(self, lawan, benda):
        respon_type = random.randint(0,2)
        if respon_type == 0:
            sentence = self.warna+" merebut "+benda.warna
            resp_sentence = self.kegiatan(lawan, benda)
            respon = sentence +", "+resp_sentence
        elif respon_type == 1:
            sentence = self.warna+" membiarkan "+benda.warna+" lalu tidur"
            holder_sentence = benda.warna+" tidak diambil "+benda.holder.warna
            respon = sentence+", "+holder_sentence
        else:
            sentence = self.warna+" memegang "+benda.warna+" lalu lari"
            holder_sentence = benda.warna+" digigit "+benda.holder.warna
            respon = sentence+", "+holder_sentence
        return respon
    
class Benang():
    def __init__(self, warna):
        self.warna = warna
        
    def updateHolder(self, holder):
        self.holder = holder
        
kuning = Kucing('Kucing kuning', 0, 1)
abu = Kucing('Kucing Abu', 1, 0)
wol = Benang('Benang Wol')

print(kuning.warna+ " adalah " +str(kuning.gender))
print(abu.warna+ " adalah " +str(abu.gender))

print(abu.kegiatan(kuning, wol))
