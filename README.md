# Pengenalan Programming Untuk Personil Non-teknis / Non-Produksi Plexus Studio
## Tentang Repo Ini
Repo ini dibuat untuk memperkenalkan personil non-teknis / non-produksi (selanjutnya disebut PNP) di Plexus ( http://plexustechdev.com ) untuk memahami dasar-dasar programming sehingga mereka memiliki bayangan pekerjaan seperti apa yang dilakukan oleh tim teknis / produksi (selanjutnya disebut PP) dan dapat bekerjasama dengan lebih baik. 

*Script-script* di repo ini dibuat dengan bayangan bahwa mereka dibuka dan diperkenalkan kepada PNP oleh salah satu PP dalam bentuk workshop hands-on di mana PNP dapat mencoba mengeksekusi dan memodifikasi script-script tersebut. Script-script ini akan ditulis dalam berbagai macam bahasa pemrograman agar PNP memiliki sense atas variasi bahasa-bahasa yang digunakan oleh PP.

## Apa Itu Programming? 
Secara sederhana, programming adalah cara kita berkomunikasi dan memberikan instruksi kepada komputer. Banyak bahasa programming yang tersedia di dunia, bahasa-bahasa tersebut diciptakan agar instruksi-instruksi kepada komputer yang pada dasarnya adalah deret biner 1 dan 0 --on dan off-- menjadi lebih bisa terbaca oleh manusia.

Tiap bahasa pemrograman memiliki sintaks yang berbeda-beda, dan memiliki kekuatan dan kelemahan yang berbeda-beda pula, sehingga kegunaan masing-masing pun berbeda. 

Untuk pengenalan konsep-konsep dasar programming kita akan menggunakan bahasa Python, untuk instalasi interpreter dan IDE, kita akan memakai distribusi Python populer yang bernama Anaconda. Silakan download di sini: https://www.anaconda.com/download/

### Konsep Dan Istilah Dalam Programming
#### *Variables* Dan *Values*
*Variables* dan *values* adalah konsep paling kecil dan paling dasar dalam programming. Untuk mempermudah pemahaman, *variable* dapat dibayangkan sebagai nama sebuah *value*. *Variable* adalah cara supaya kita bisa memanggil sebuah *value* dan melakukan operasi terhadapnya. Deklarasi sebuah variable biasanya menggunakan simbol '=', di sebelah kiri simbol tersebut adalah *variable*, di sebelah kanan adalah *value*-nya

**Contoh variable assignment:**
```python
#contoh assignment di Python
angka1 = 1
angka_dua = 2.3
```
```javascript
//contoh assignment di Javascript
var angka3 = 3.0;
var angka_enam = 6;
```
```c++
//contoh assignment di C++
int angka_7 = 7;
float angka_delapan = 8.3;
```
#### Constants
Constants serupa dengan variable, hanya saja Constant bersifat permanen dan tidak dapat berubah *(immutable)* seumur hidup program yang kita tulis. Perlu dicatat bahwa Python tidak memiliki constant, untuk itu sepanjang pembahasan yang menggunakan Python kita tidak akan menemukan deklarasi constant. Apabila memerlukan sebuah constant dalam bahasa Python, deklarasikan sebuah variable, dan jangan rubah variable tersebut.

```c++
//contoh constant di C++
const int konstanta1 = 7;
const float tak_berubah_2 = 8.3;
```

#### *Object Types*
Object types adalah pengelompokan obyek-obyek dalam pemrograman yang didasarkan dari ciri-ciri / property yang dimiliki obyek tersebut. Secara umum, macam-macam object type adalah sebagai berikut:

**1. Boolean.** Value yang masuk ke dalam tipe ini hanya dua yaitu True atau False. Boolean type berguna untuk menguji apakah suatu kondisi terpenuhi atau tidak terpenuhi.
```python
is_beautiful = True
are_snails_can_fly = False
```
**2. String.** Type ini adalah untuk value-value teks / tulisan. Ciri khas dari object type ini adalah value-nya diawali simbol **"** dan diakhiri dengan simbol **"** atau simbol **'** dan simbol **'**
```python
sila_pertama = "Ketuhanan Yang Maha Esa."
```
**3. Integer.** Value yang masuk ke dalam type ini adalah bilangan-bilangan bulat, baik positif maupun negatif.
```python
jumlah_sila = 5
```
**4. Float.** Value yang masuk ke dalam type ini adalah bilang-bilangan pecahan / desimal. Baik positif maupun negatif.
```python
pi = 3.14
```
**5. Array.** Yang termasuk dalam type ini adalah list, yang dideklarasikan menggunakan simbol **[** dan **]**. Untuk memanggil satu value di dalam array, kita menggunakan sintaks **nama_array[nomor index]** , nomor index selalu dimulai dari 0 (nol), lihat contoh di bawah ini:
```python
nomor_nomor_sila = [1,2,3,4,5]

print(nomor_nomor_sila[0])
# '1' akan tertampil sebagai hasil
```
**6. Tuple.** Serupa dengan array, akan tetapi ia bersifat immutable, sekali dideklarasikan maka ia tidak akan dapat diubah seumur hidup program yang kita tulis. Dideklarasikan menggunakan simbol **(** dan **)**. Untuk memanggil satu value di dalam tuple, kita menggunakan sintaks **nama_tuple[nomor index]** , nomor index selalu dimulai dari 0 (nol), lihat contoh di bawah ini: 
```python
nomor_nomor_sila = (1,2,3,4,5)

print(nomor_nomor_sila[3])
# '4' akan tertampil sebagai hasil
```

**7. Dictionary.** Serupa dengan array, akan tetapi ia berisi pasangan 'key' dan 'value'. Dideklarasikan menggunakan simbol **{** dan **}**. Untuk memanggil satu value di dalam dictionary, kita menggunakan sintaks **nama_dict[key]** . Berbeda dengan array dan tuple, elemen-elemen di dalam dictionary tidak memiliki index sehingga tidak dapat dipanggil menggunakan nomor index, lihat contoh di bawah ini: 
```python
pancasila = {'banyak_sila': 5, 'judul':'PANCASILA', 'sila_kesatu': 'Ketuhanan Yang Maha Esa'}

print(pancasila['judul'])
# 'PANCASILA' akan tertampil sebagai hasil
```

#### Operators
Operation adalah manipulasi data dalam sebuah program. Operator adalah simbol yang dipakai dalam proses manipulasi data tersebut Beberapa operator yang sering digunakan adalah:
**+ (tanda plus)**, untuk menjumlahkan satu data dengan data lainnya
**- (tanda minus)**, untuk operasi pengurangan antar beberapa data
__* (asterisk)__, untuk operasi perkalian
**/ (slash)**, untuk operasi pembagian antara beberapa data
**% (persen)**, untuk operasi modulo, mencari sisa dari sebuah pembagian. 

Berikut beberapa sampel operasi:
```python
a = 5
b = 10
c = 12

print(a+b)
# akan menampilkan hasil 15 

print(b-a)
# akan menampilkan hasil 5 

print(b*a)
# akan menampilkan hasil 50

print(b/a)
# akan menampilkan hasil 2

print(c%a)
# akan menampilkan hasil 2
```

#### Flow , Loops dan Conditionals
Secara umum sebuah program akan dijalankan dari baris paling atas menuju baris paling bawah. Akan tetapi untuk beberapa kasus tertentu, kita perlu mengubah flow / jalannya program tersebut. 

**Conditional / if statement**
Conditional membuat sebuah program bercabang, sehingga apabila beberapa keadaan terpenuhi, ia akan berjalan berbeda dengan apabila keadaan-keadaan tersebut tidak terpenuhi. Loop mengulang beberapa bagian dari kode sampai sebuah keadaan tertentu terpenuhi. 

Contoh conditional:
```python
if 3 < 5:
  print("ini benar!")
else:
  print("ini salah!")

# akan menampilkan hasil "ini benar!"
# di sini karena hasil evaluasi 3 < 5 adalah True, maka program akan melakukan print("ini benar!") 
# sebagai operasi berikutnya.

a = 2
b = 5

if b-a < 1:
  print("reaksi 1")
else:
  print("reaksi 2")
 
# akan menampilkan hasil "reaksi 2"
# karena b-a = 5-2 = 3, dan eveluasi 3 < 1 adalah False, maka program akan melewatkan print("reaksi 1") 
# dan menjalankan print("reaksi 2")
```

**For Loop**
For loop adalah sebuah loop yang dijalankan untuk kali yang sudah ditentukan. Pada dasarya For loop adalah memerintahkan program untuk mengulangi sebuah blok kode untuk beberapa kali yang sudah ditentukan.

Contoh For loop:
```python
for i in range(0,5):
  print("hitung "+str(i))

# akan menampilkan hasil: "hitung 0", "hitung 1", "hitung 2", "hitung 3", "hitung 4" 
# masing-masing di baris yang berbeda
```

**While Loop**
Dengan while loop, kita bisa mememerintahkan sebuah program untuk terus mengulangi blok tertentu, sampai kondisi yang diminta oleh loop tersebut tidak lagi terpenuhi. While loop dapat dibayangkan sebagai pernyataan if (conditional) yang dijalankan berulang-ulang sampai keadaan yang ditentukan tidak lagi terpenuhi.

Contoh While loop:
```python
while True:
  print ("saya senang!")

# akan menampilkan "saya senang!" berulang-ulang sampai program dimatikan

while buttonPressed == False:
  print ("button is not pressed!")
print("button is pressed!")

# akan menampilkan "button is not pressed!" berulang-ulang sampai program dimatikan,
# atau value buttonPressed berubah
```


#### Functions
Function adalah cara mengelompokkan dan memberi nama beberapa operasi yang sering dipakai agar mudah untuk dipakai berulang-ulang. Setelah dideklarasikan, sebuah fungsi dapat dipanggil dan dijalankan tanpa perlu menuliskan ulang operasi-operasi yang terjadi didalamnya. Deklarasi sebuah function berbeda dari satu bahasa ke bahasa lainnya. Pada Python kita mendeklarasikan function dengan menggunakan keyword 'def' , diikuti nama function, lalu argumen-argumen yang diperlukan di dalam tanda **()**. Setelah operasi dilakukan, sebuah function bisa mengembalikan result dari operasi-operasi tersebut.

Contoh function dan cara memanggilnya

```python
def penjumlahan(a,b,c): #deklarasi function. a, b, c adalah argumen yang harus ditulis ketika memanggil function
  c = a+b
  return c

print(penjumlahan(10, 20, 3)) #memanggil function bernama 'penjumlahan' di atas, dengan argumen seperti di dalam tanda kurung.
# akan menampilkan hasil 30
```


## Daftar Scripts 
1. [lvl1_hello_world.py](https://github.com/plexusstudio/pengenalan_programming/blob/master/scripts/lvl1_hello_world.py) : pengenalan, printing teks "hello world", konsep-konsep variable dan value, operasi-operasi dasar, pengenalan conditionals dan flow control.
2. [lvl2_iterative_recursive.py](https://github.com/plexusstudio/pengenalan_programming/blob/master/scripts/lvl2_iterative_recursive.py) : pengenalan konsep fungsi-fungsi iteratif dan rekursif.

-- dokumen ini akan terus diupdate
-- terakhir diupdate tanggal 8 Jan 2018 --
