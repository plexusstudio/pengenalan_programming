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

**6. Dictionary.** Serupa dengan array, akan tetapi ia berisi pasangan 'key' dan 'value'. Dideklarasikan menggunakan simbol **{** dan **}**. Untuk memanggil satu value di dalam dictionary, kita menggunakan sintaks **nama_dict[key]** . Berbeda dengan array dan tuple, elemen-elemen di dalam dictionary tidak memiliki index sehingga tidak dapat dipanggil menggunakan nomor index, lihat contoh di bawah ini: 
```python
pancasila = {'banyak_sila': 5, 'judul':'PANCASILA', 'sila_kesatu': 'Ketuhanan Yang Maha Esa'}

print(pancasila['judul'])
# 'PANCASILA' akan tertampil sebagai hasil
```


## Daftar Scripts 
1. [lvl1_hello_world.py](https://github.com/plexusstudio/pengenalan_programming/blob/master/scripts/lvl1_hello_world.py) : pengenalan, printing teks "hello world", konsep-konsep variable dan value, operasi-operasi dasar, pengenalan conditionals dan flow control.
2. [lvl2_iterative_recursive.py](https://github.com/plexusstudio/pengenalan_programming/blob/master/scripts/lvl2_iterative_recursive.py) : pengenalan konsep fungsi-fungsi iteratif dan rekursif.

-- dokumen ini akan terus diupdate
-- terakhir diupdate tanggal 8 Jan 2018 --
