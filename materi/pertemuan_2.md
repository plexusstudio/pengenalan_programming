# Pertemuan 2

Pada pertamuan kali ini kita akan membicarakan lebih jauh mengenai function, dan dua konsep function yang akan sering ditemui: Iterative dan Recursive.
Script pelengkap untuk pertemuan kali ini bisa didownload di https://github.com/plexusstudio/pengenalan_programming/blob/master/scripts/lvl2_iterative_recursive.py

---
## Iterative 
Seperti namanya, fungsi-fungsi iterative digunakan untuk memperbarui sebuah variabel secara iteratif. Fungsi-fungsi ini dijalankan berulang dan memperbarui value dari sebuah variabel berdasarkan deret yang sudah ditentukan.

Contoh *Iterative Functions*:
```python
def integerSeqIterative(n):
    integer_sequence = []
    for i in range(1,n+1):
        integer_sequence.append(i)
    return integer_sequence
 
print(integerSeqIterative(5))
# akan menampilkan hasil 1, 2, 3, 4, 5
```
 
## Recursive
Mirip dengan Iterative Functions, Recursive Functions juga memperbarui value dari sebuah variabel. Ciri khas / perbedaan recursive functions adalah functions pada tipe ini memanggil dirinya sendiri untuk mendapatkan hasilnya. 

Contoh *Recursive Function*:
```python
def integerSeqRecursive(sequence, n):
    while n > 0:
            sequence.insert(0,n)
            return integerSeqRecursive(sequence, n-1)
    return sequence
    
print(integerSeqRecursive([],5))
# akan menampilkan hasil 1, 2, 3, 4, 5
```

## Ulasan
Baik Iterative maupun Recursive menggunakan loop untuk mengatur flownya. Pada contoh iterative kita bisa melihat for loop, pada recursive kita bisa melihat while loop. Pada umumnya, recursive functions dapat dituliskan dengan lebih singkat untuk mendapatkan hasil yang sama. Pada contoh di atas, keduanya memiliki jumlah baris yang sama yaitu 5 baris, tapi pada function yang lebih rumit, perbedaan tersebut akan lebih mudah terlihat, silakan lihat contoh di bawah ini:

```python
# kedua fungsi di bawah akan menghasilkan bilangan ke-n pada deret fibonacci 
# ITERATIVE FUNCTION:
def fibSearchIterative(n):
    fibonacci = []
    i = 0
    while i <= n:
        if i == 0 or i == 1:
            fib = i
        else: 
            fib = fibonacci[i-1]+fibonacci[i-2]        
        fibonacci.append(fib)
        i += 1    
    return fibonacci[n]
 
# RECURSIVE FUNCTION:
def fibSearchRecursive(fib_list, n):
    while len(fib_list) <= n:
        if len(fib_list) == 0 or len(fib_list) == 1:
            fib_list.append(len(fib_list))
        else:
            fib_list.append(fib_list[-1]+fib_list[-2])
        return fibSearchRecursive(fib_list, n)         
    return fib_list[-1]
```

Kedua fungsi tersebut melakukan hal yang persis sama, akan tetapi fungsi yang iteratif membutuhkan 11 baris, sementara yang recursive hanya 8 baris. Biasanya semakin rumit fungsinya, semakin terlihat perbedaan antara keduanya. 


## Latihan
Buatlah dua buah functions, yang satu iterative, yang satu recursive untuk menghitung sebuah deret angka. Silakan cari deret angka Anda sendiri. Berikut adalah beberapa contoh deret yang mungkin bisa dipakai:
- Deret bilangan prima
- Deret bilangan genap / ganjil
- Deret logaritmik
