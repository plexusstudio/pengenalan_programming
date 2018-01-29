# Pertemuan 4

Pada pertemuan kali ini kita akan coba mempelajari Game Framework PHASER (https://phaser.io/).

#### Persiapan Untuk Pertemuan 4
- Download file phaser.js https://phaser.io/download
- Download dan install web server https://www.apachefriends.org/index.html
- Download dan Install salah satu text editor :
  - Sublime https://www.sublimetext.com/
  - Visual Code https://code.visualstudio.com/
  - Notepad++ https://notepad-plus-plus.org/download/v7.5.4.html
  - dll 
  
karena framework ini menggunakan bahasa pemograman JavaScript, untuk itu sebelumnya kita akan membahas sekilas mengenai JavaScript.

### JAVASCRIPT
JavaScript adalah bahasa pemrograman tingkat tinggi dan dinamis, dimana javscript ini merupakan bahasa pemrograman web yang bersifat Client Side Programming Language. Client Side Programming Language adalah tipe bahasa pemrograman yang pemrosesannya dilakukan oleh client.

Fungsi JavaScript : pada awal perkembangannya berfungsi untuk membuat interaksi antara user dengan situs web menjadi lebih cepat tanpa harus menunggu pemrosesan di web server. Sebelum adanya javascript, setiap interaksi dari user harus diproses oleh web server.
Dalam perkembangan selanjutnya, JavaScript tidak hanya berguna untuk validasi form, namun untuk berbagai keperluan yang lebih modern. Berbagai animasi untuk mempercantik halaman web, fitur chatting, efek-efek modern, games, semuanya bisa dibuat menggunakan JavaScript.

Contoh *Penulisan Systax JavaScript*:
```javascript
<script type="text/javascript">
	var pesan = "Halo Plexus";
	alert(pesan);
</script>
```

Cara memanggil JavaScript pada file HTML:
1. Script diletakan di antara Tag "head" HTML:
```javascript
<html>
<head>
<script type="text/javascript">
  //code javascript
</script>
</head>
...
</html>
desc: fungsi javascript akan dipanggil pada saat file html mulai di load
```

2. Script diletakan di antara Tag "body" HTML:
```javascript
<html>
...
<body>
<script type="text/javascript">
  //code javascript
</script>
</body>
</html>
desc: fungsi javascript akan dipanggil setelah semua kontenn pada file html selesai di load
```
  
3. JavaScript juga bisa dipisahkan menjadi file tersendiri
```javascript
<html>
...
<script src="xxx.js"></script>
...
</html>
```

### PHASER
...........
