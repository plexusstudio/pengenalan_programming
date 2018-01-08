# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:29:02 2018
@author: iqbal

"""

import math

# hello world
print("hello world!=======================")

# VARIABLES AND VALUES =========================================================
ini_variable = "ini_value"

# OBJECT TYPES =================================================================:
# string, teks , ditandai dengan tanda kutip buka dan tutup " dan "
ini_string = "selamat tahun baru!"

# integer, bilangan bulat
ini_int = 1280

# float, bilangan pecahan 
ini_float = 3.142

# array, bisa disebut juga dengan list, ditandai dengan [ dan ]
ini_array = [1, 2, "budi", 6, 8, "sendal"]

# tuple, seperti array, tapi immutable, tidak bisa dirubah-rubah urutannya, ditandai dengan ( dan )
ini_tuple = (3, 4, 5, "iwan", "cindy", 7)

# dictionary, seperti array, tapi tiap elemennya punya komponen key (yang bisa dipanggil) dan value. ditandai dengan { dan }
ini_dict = {"joko":"ayah", "sandra":"ibu", "budi":"anak sulung", "santi":"anak bungsu"}

# boolean, boolean hanya memiliki 2 alternatif value: True atau False
manusia_butuh_air = True
katak_hidup_di_angkasa_luar = False

#cara mengambil value
print(ini_string)
print(ini_int)
print(ini_float)
print(ini_array[2])
print(ini_dict["sandra"])

print(ini_array)
del ini_array[-3]
print(ini_array)


# OPERATIONS =================================================================
# additions
a, b = 6, 14
c = a+b
print("C= "+str(c))

d,e = "ibu", 23
f = d+str(e)
print("F= "+str(f))

g = b - a
h = a * b
i = b / a
j = b % a
k = 2**3
l = math.sqrt(16)
#bagaimana dengan akar?

print(l)

# FLOW, LOOPS & CONDITIONALS ========================================================

# while loop
count = 0
while count < 10:
    print("while, count: "+str(count))
    count += 1
    #count = count + 1

#ange(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for loop 
for count in range(0,10):
    print("for, count: "+str(count))

list_untuk_loop = ["ayah", "ibu", "kakak", "adik", "kakek", "nenek"]
for anggota_kel in list_untuk_loop:
    print(anggota_kel)
    if anggota_kel == "adik":
        print(anggota_kel+" ketemu!!")
    elif anggota_kel == "kakek":
        print(anggota_kel+" gigi palsunya ketemu.")
    else:
        print(anggota_kel+" pergi ke pantai.")

# FUNCTIONS =================================================================
def percobaan(var_a, var_b, var_c):
    print("var_a: "+str(var_a)+", var_b: "+str(var_b)+", var_c: "+str(var_c))
    penjumlahan = var_a + var_b
    pengurangan = var_c - var_b
    return penjumlahan, pengurangan

hasil_jumlah, hasil_kurang = percobaan(30, 10, 20)

print("penjumlahan: "+str(hasil_jumlah))
print("pengurangan: "+str(hasil_kurang))

list1 = ["plexus", "oray"]
list2 = ["keren", "mantap"]

def cobacoba(list_a, list_b):
    for studio in list_a:
        for status in list_b:
            print(studio+" "+status)

def cobacobi():
    for i in range(0,10):
        print ("ulang: "+str(i))        

def bilangan1():
    return 5

def bilangan2():
    return 6

print(bilangan1()+bilangan2())

# Memanggil function:
cobacobi()
cobacoba(list1, list2)
cobacoba(list2, list1)




    


#latihan: buatlah sebuah function yang menghitung dari nol sampai sepuluh
    
