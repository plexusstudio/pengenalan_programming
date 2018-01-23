# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:46:38 2018

@author: iqbal
"""

import random
import math
import time

print("PENGENALAN CLASS ==============================")
print("===============================================")

# DEKLARASI CLASS =========================
class Human():   
    def __init__(self, name, height = 170, weight = 60, gender = 0, skill=80):   #skill menentukan seberapa banyak ia bisa menangkis & menghindari bola     
        self.name = name
        self.height = height
        self.weight = weight
        self.skill = skill
        if gender == 0:
            self.gender = "lelaki"
        elif gender == 1:
            self.gender = "perempuan"
        else:
            self.gender = "lelaki"
            
    def pukul(self, obyek): #obyek argtype: string
        sentence = self.name+" memukul "+obyek.name+"!"
        return sentence
    
    def memukul_ke(self, lawan, obyek): #obyek argtype: string, #lawan argtype: Human object
        obyek.updateHolder(lawan)
        sentence = self.name+" memukul "+obyek.name+" kepada "+lawan.name
        resp_sentence = lawan.response(self, obyek)
        whole_sentence = sentence+", "+resp_sentence       
        return whole_sentence
    
    def response(self, lawan, obyek):        
        response_type = random.randint(0,100)
        if response_type <= int(0.9 * self.skill):
            waktu.updateTime(5)
            sentence = "\n"+self.name+" menahan "+obyek.name
            resp_sentence = self.memukul_ke(lawan, obyek)
            response = sentence +", "+resp_sentence
        elif response_type <= int(0.1 * self.skill):
            waktu.updateTime(7)
            sentence = "\n"+self.name+" menghindar dari "+obyek.name+"karena out, dan "+obyek.name+" terkapar di lantai"  
            holder_sentence = obyek.name+" giliran "+obyek.holder.name
            response = sentence+", "+holder_sentence
        else:
            waktu.updateTime(10)
            sentence = "\n"+self.name+" terpukul "+obyek.name+" dan "+obyek.name+" mengenai wajah"
            holder_sentence = obyek.name+" giliran "+obyek.holder.name
            response = sentence+", "+holder_sentence
            papan_skor.updateSkor(lawan)
        return response
                
class Pukulan():
    def __init__(self, name, radius, holder):
        self.name = name
        self.radius = radius
        self.holder = holder
    
    def updateHolder(self, holder):
        self.holder = holder
        
class PapanSkor():
    def __init__ (self, player1, player2, skor1, skor2):
        self.player1 = player1
        self.player2 = player2
        self.skor1 = skor1
        self.skor2 = skor2
    
    def updateSkor(self,player):
        self.declaration = "SKOR UNTUK "+player.name.upper()+"!!"
        if player.name == self.player1.name:
            self.skor1 += 1
        elif player.name == self.player2.name:
            self.skor2 += 1
        return self.skor1, self.skor2

class Timer():
    def __init__(self, time_start): #time_start argtype: integer argunit: detik
        self.time_start = time_start
        self.time_run = time_start
    def updateTime(self, time_update):
        self.time_run += time_update
        
# INSTANSIASI CLASS =========================
chris = Human('Chris', 168,89,0, 90)
tessy = Human('Tessy', 155, 40, 1, 10)
pukulan = Pukulan('pukulan', 10, None)
papan_skor = PapanSkor(chris, tessy, 0, 0)
waktu = Timer(0)

# MEMANGGIL PROPERTY DALAM CLASS =========================
print("tinggi "+chris.name+ " adalah "+str(chris.height)+" cm")
print("tinggi "+tessy.name+ " adalah "+str(tessy.height)+" cm")

# MEMANGGIL METHOD DALAM CLASS =========================
#print(andre.lempar(bola_basket))
#print(susi.lempar_ke(andre, bola_basket))


# SIMULASI PERMAINAN, YANG LEBIH DULU MENCAPAI 22 ADALAH PEMENANGNYA.
skor_menang = 22
pukulan.holder = chris

while papan_skor.skor1 < skor_menang and papan_skor.skor2 < skor_menang:
    if pukulan.holder == chris:
        other_player = tessy
    else:
        other_player = chris
        
    print(pukulan.holder.memukul_ke(other_player, pukulan))
    print(
            "-----------------------\n"+papan_skor.declaration+"\n"+"SKOR:\n"+ papan_skor.player1.name+" - "+str(papan_skor.skor1)
            +" | "+ papan_skor.player2.name+" - "+str(papan_skor.skor2)
            )
    print("-----------------------")
    time.sleep(0.5)

print("PERTANDINGAN SELESAI!===================================")

if papan_skor.skor1 == skor_menang:
    print(papan_skor.player1.name+" pemenangnya!!!")
else:
    print(papan_skor.player2.name+" pemenangnya!!!")
    

print("--------------------------------")
print("waktu pertandingan: "+str(int(math.floor(waktu.time_run/60)))+" menit dan "+str(int(waktu.time_run%60))+" detik.")


