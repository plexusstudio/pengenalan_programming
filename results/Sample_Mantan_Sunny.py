# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:36:55 2018

@author: Sunny
"""
import random

print("PENGENALAN CLASS ==============================")
print("===============================================")

# DEKLARASI CLASS =========================
class Mantan():
    def __init__(self, name, nilai = 170, weight = 60, status = 0): 
        self.name = name
        self.nilai = nilai
        self.weight = weight
        if status == 0:
            self.status = "udah putus"
        elif status == 1:
            self.status = "pacaran"
        else:
            self.status = "pendekatan"
            
    def Berantem (self, lawan):
        sentence = "si "+self.name+" cakar si "+lawan+" sampe meriang!!"
        return sentence
    
    def BerantemDimana(self, lawan, dimana):
        dimana.updateHolder(lawan)
        sentence = "Anjir si "+self.name+" berantem sama si "+lawan.name+" di "+dimana.name
        return sentence       
        
    def response(self, lawan, dimana):
        response_type = random.randint(0,2)
        if response_type == 0:
            sentence = self.name+" ngontrog "+dimana.name
            resp_sentence = self.BerantemDimana(lawan, dimana)
            response = sentence +", "+resp_sentence+"."
        if response_type == 1:
            sentence = self.name+" gagal ngontrog ke"+dimana.name+" soalnya salah alamat"
            holder_sentence = dimana.name+" aman sama si "+dimana.holder.name+"."
            response = sentence+", "+holder_sentence
        if response_type == 2:
            sentence = self.name+" ngelewat depan "+dimana.name+" padahal di "+dimana.name+" gw lagi asek"  
            holder_sentence = self.name+" pengen banget marahin si"+dimana.holder.name+"."
            response = sentence+", "+holder_sentence
        return response
        
class Lokasi():
    def __init__(self, name, sifat):
        self.name = name
        self.sifat = sifat
    
    def updateHolder(self, holder):
        self.holder = holder
        
# INSTANSIASI CLASS =========================
Bunga = Mantan('Bunga', 7,89,0)
Mawar = Mantan('Mawar', 10, 40,1)
RumahCalonMertua = Lokasi('Rumah Calon Mertua', 10)

# MEMANGGIL PROPERTY DALAM CLASS =========================
print("si "+Bunga.name+ " point muka nya "+str(Bunga.nilai)+" point")
print("si "+Mawar.name+ " point muka nya "+str(Mawar.nilai)+" point")

# MEMANGGIL METHOD DALAM CLASS =========================
print(Bunga.BerantemDimana(Mawar, RumahCalonMertua)+","+Bunga.Berantem("Mawar")+", "+Bunga.response(Mawar, RumahCalonMertua))

