# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:46:38 2018

@author: iqbal
"""

import random

print("PENGENALAN CLASS ==============================")
print("===============================================")

# DEKLARASI CLASS =========================
class Human():   
    def __init__(self, name, height = 170, weight = 60, gender = 0):        
        self.name = name
        self.height = height
        self.weight = weight
        if gender == 0:
            self.gender = "lelaki"
        elif gender == 1:
            self.gender = "perempuan"
        else:
            self.gender = "lelaki"
            
    def lempar(self, obyek): #obyek argtype: string
        sentence = self.name+" melempar "+obyek+"!"
        return sentence
    
    def lempar_ke(self, lawan, obyek): #obyek argtype: string, #lawan argtype: Human object
        obyek.updateHolder(lawan)
        sentence = self.name+" lempar "+obyek.name+" kepada "+lawan.name
        resp_sentence = lawan.response(self, obyek)
        whole_sentence = sentence+", "+resp_sentence       
        return whole_sentence
    
    def response(self, lawan, obyek):        
        response_type = random.randint(0,2)
        if response_type == 0:
            sentence = self.name+" menangkap "+obyek.name
            resp_sentence = self.lempar_ke(lawan, obyek)
            response = sentence +", "+resp_sentence
        elif response_type == 1:
            sentence = self.name+" gagal menangkap "+obyek.name+" dan "+obyek.name+" mental ke luar lapangan"
            holder_sentence = obyek.name+" ada di tangan "+obyek.holder.name
            response = sentence+", "+holder_sentence
        else:
            sentence = self.name+" menghindar dari "+obyek.name+" dan "+obyek.name+" memantul dari lantai"  
            holder_sentence = obyek.name+" ada di tangan "+obyek.holder.name
            response = sentence+", "+holder_sentence
        return response
                
class Bola():
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
    
    def updateHolder(self, holder):
        self.holder = holder
        
# INSTANSIASI CLASS =========================
andre = Human('andre', 168,89,0)
susi = Human('susi', 155, 40, 1)
bola_basket = Bola('bola basket', 10)

# MEMANGGIL PROPERTY DALAM CLASS =========================
print("tinggi "+andre.name+ " adalah "+str(andre.height)+" cm")
print("tinggi "+susi.name+ " adalah "+str(susi.height)+" cm")

# MEMANGGIL METHOD DALAM CLASS =========================
print(andre.lempar_ke(susi, bola_basket))


