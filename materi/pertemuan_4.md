# Pertemuan 4

Pada pertemuan kali ini kita akan coba mempelajari Game Framework PHASER (https://phaser.io/).

#### Persiapan Untuk Pertemuan 4
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
Phaser adalah framework game HTML5 open source yang dibuat oleh Photon Storm (http://www.photonstorm.com). Phaser dirancang untuk membuat game yang akan berjalan di desktop dan mobile web browser. Perhatian lebih diberikan pada aspek performa game dalam mobile web browser.

Langsung aja yah kita coba buat sebuah game dengan menggunakan PHASER, game yang akan kita buat yaitu game dengan gameplay seperti Flappy Bird.

#### INFO GAME
- user harus tap/klik layar agar burung bisa terus terbang, namun hati-hati karena burung juga harus bisa menghindari pipa pipa yang dilewatinya agar tidak menabrak pipa tersebut.

Dari deskripsi tersebut kita harus bisa membagi menjadi beberapa fungsi yang nantinya akan mempermudah kita pada saat ngodingnya, kurang lebih kita bisa menjabarkannya menjadi seperti ini:
1. Object Burung : 
   - burung jatuh dari atas
   - burung bisa terbang kalo layar di tap/klik
2. Object Pipa :
   - ada 2 pipa, 1 pipa di atas, dan 1 lagi pipa di bawah, dimana di tengahnya akan ada ruang kosong untuk bisa di lalui oleh burung
   - posisi ruang kosong pipa tersebut akan acak, bisa di atas, bawah atau tengah
   - pipa akan terus muncul selama burung masih terbang
3. Status Permainan Berakhir :
   - permainan berakhir apabila burung terbang terlalu atas, terbang terlalu bawah atau nabrak pipa.


#### HAYU KITA BIKIN GAME
##### 1. Download satu folder file (https://github.com/plexusstudio/pengenalan_programming/blob/master/scripts/BirdGame)
##### 2. Simpan folder tersebut di folder "htdocs" web server yang sudah kita install (XAMPP), biasanya pathnya seperti ini (C:\xampp\htdocs)
##### 3. Jalankan module Apache dari XAMPP Control Panel, lalu buka browser anda (Chrome, Firefox, dll) dan ketikan url http://localhost/phaser/BirdGame/, jika muncul persegi panjang berwarna hitam di tengah browser anda bearti phaser sudah jalan dengan baik.
##### 4. buka file "main.js" (C:\xampp\htdocs\BirdGame\js\main.js).
##### 5. buat object burung :
   - ketikan kode berikut didalam "fungsi preload (preload: function())"
     ```javascript
     game.load.image('bird', 'assets/images/character/bird_0001.png'); //mengakses image bird_0001.png dan menamakannya dengan nama "bird"
     ```
     
   - ketikan kode berikut didalam "fungsi create (create: function())"
     ```javascript
     game.physics.startSystem(Phaser.Physics.ARCADE); //mengaktifkan system physics pada game
     
     bird = game.add.sprite(100, 0, 'bird'); //menambahkan object bird kedalam stage game dengan posisi x=100
     game.physics.arcade.enable(bird); //mengaktifkan physics pada object bird
     bird.body.gravity.y = 1000; //menambahkan body gravity pada bird agar bisa jatuh
     ```
     
   - buat fungsi baru "(terbang : function(){})" dibawah/setelah "fungsi update"
     ```javascript
     ...
     terbang: function(){
    	//logic terbang
        bird.body.velocity.y = -450; //burung akan terbang ke atas (sumbu y) sebesar 450, dan fungsi ini akan jalan jika fungsi terbang di panggil
     }
     ...
     ```

   - ketikan kode berikut didalam "fungsi update (update : function())"
     ```javascript
     if (game.input.activePointer.isDown) //jika mouse di teken (kiri/kanan)
        {
            this.terbang(); //menjalankan fungsi terbang
        }
     ```

   - code pada var mainState akan menjadi seperti ini
     ```javascript
     var mainState = {
	    preload: function() { 
		// fungsi yang dijalanin pas pertama halaman muncul  
		game.load.image('bird', 'assets/images/character/bird_0001.png'); //mengakses image bird_0001.png dan menamakannya dengan nama "bird"
	    },

	    create: function() { 
		// fungsi ini dijalanin setelah preload beres
		game.physics.startSystem(Phaser.Physics.ARCADE); //mengaktifkan system physics pada game

		bird = game.add.sprite(100, 0, 'bird'); //menambahkan object bird kedalam stage game dengan posisi x=100
		game.physics.arcade.enable(bird); //mengaktifkan physics pada object bird
     		bird.body.gravity.y = 1000; //menambahkan body gravity pada bird agar bisa jatuh
	    },

	    update: function() {
		//ini fungsi yang jalan terus2an kalo kata forum2 detailnya tuh dijalanin 60kali dalam satu detik
		if (game.input.activePointer.isDown) //jika mouse di teken (kiri/kanan)
		{
		    this.terbang(); //menjalankan fungsi terbang
		}
	    },

	    terbang: function(){
		//logic terbang
		bird.body.velocity.y = -450; //burung akan terbang ke atas (sumbu y) sebesar 450, dan fungsi ini akan jalan jika fungsi terbang di panggil
	    }
     };
     ```
     
   - coba refresh/jalankan url http://localhost/phaser/BirdGame/, akan terlihat object burung terjatuh dan jika layar di tap/klik burung akan terbang terus ke atas
   
##### 6. buat object pipa :
   - ketikan kode berikut didalam "fungsi preload (preload: function())"
     ```javascript
     game.load.image('pipe', 'assets/images/obstacle/pipe.png'); //mengakses image pipe.png dan menamakannya dengan nama "pipe"
     ```
     
   - ketikan kode berikut didalam "fungsi create (create: function())"
     ```javascript
     pipes = game.add.group(); //variable pipes dijadikan varibale group
     ```
     
   - buat fungsi baru "(addPipa : function(){})" dibawah/setelah "fungsi terbang"
     ```javascript
     ...
     addPipa: function() {
        var lobang = 100; //jarak ruang kosong antara pipa atas dan bawah
        var x = 520; //posisi pipa pada saat muncul
        var randJarakPipe = Helper.getRandomInt(0, 250); //variable bantuan untuk membuat posisi pipa atas dan bawah menjadi acak

        //pipa atas
        var pipaAtas = game.add.sprite(x, (randJarakPipe - 0) - lobang, 'pipe'); //menambahkan object pipa kedalam stage game
        pipaAtas.anchor.setTo(.5,.5); //set pivot object pipa di tengah
        pipaAtas.scale.y *= -1; //rotate vertical posisi pipa
        game.physics.arcade.enable(pipaAtas); //mengaktifkan physics pada object pipa atas
        pipaAtas.body.velocity.x = -100; //buat pipa atas bergerak ke arah kiri
        pipes.add(pipaAtas); //menambahkan pipa atas ke dalam group pipes

        // otomatis menghilangkan pipa atas jika sudah tidak terlihat di layar
        pipaAtas.checkWorldBounds = true; 
        pipaAtas.outOfBoundsKill = true; 


        //pipa bawah
        var pipaBawah = game.add.sprite(x, (randJarakPipe + 800) + lobang, 'pipe'); //menambahkan object pipa kedalam stage game
        pipaBawah.anchor.setTo(.5,.5); //set pivot object pipa di tengah
        game.physics.arcade.enable(pipaBawah); //mengaktifkan physics pada object pipa atas
        pipaBawah.body.velocity.x = -100; //buat pipa atas bergerak ke arah kiri
        pipes.add(pipaBawah); //menambahkan pipa atas ke dalam group pipes

       
        // otomatis menghilangkan pipa bawah jika sudah tidak terlihat di layar
        pipaBawah.checkWorldBounds = true; 
        pipaBawah.outOfBoundsKill = true; 
     },
     ...
     ```
     
   - ketikan kode berikut didalam "fungsi create (create: function())"
     ```javascript
     this.timer = game.time.events.loop(3000, this.addPipa, this); //memanggil fungsi addPipa berulang-ulang dengan jarak selama 3 detik
     ```
     
   - coba refresh/jalankan url http://localhost/phaser/BirdGame/, akan terlihat object burung terjatuh dan jika layar di tap/klik burung akan terbang terus ke atas, lalu akan muncul pipa-pipa yang bergerak ke arah kiri.

##### 7. buat logic status permainan berakhir jika burung terbang terlalu atas terbang terlalu bawah:
   - buat fungsi baru "(restartGame : function(){})" dibawah/setelah "fungsi addPipa"
     ```javascript
     ...
     restartGame: function() {
        game.state.start('main'); //menjalankan ulang game (restart game)
     },
     ...
     ```
     
   - ketikan kode berikut didalam "fungsi update (update: function())"
     ```javascript
     if (bird.y < 0 || bird.y > 800) //check posisi y object burung
     {
     	this.restartGame(); //memanggil fungsi restart jika posisi y burung kurang dari 0 dan lebih dari 800
     }     
     ```
 
##### 8. buat logic status permainan berakhir jika burung menabrak pipa:
   - buat fungsi baru "(nabrakPipa : function(){})" dibawah/setelah "fungsi restartGame"
      ```javascript
      ...
      nabrakPipa: function() {
        //check status burung
        if (bird.alive == false) 
            return;

        bird.alive = false; //set status bird menjadi false
        game.time.events.remove(this.timer); //membuang fungsi looping timer

        // akses semua pipa lalu menghentiakn gerakannya
        pipes.forEach(function(p){
            p.body.velocity.x = 0;
        }, this);
      },
      ...
      ```
     
   - ketikan kode berikut didalam "fungsi update (update: function())"
      ```javascript
      game.physics.arcade.overlap(bird, pipes, this.nabrakPipa, null, this); //check jika burung dan pipa bertabrakan akan memanggil fungsi nabrakPipa
      ```
     
    - ketikan kode berikut diawal "fungsi terbang (terbang: function())"
      ```javascript
      //logic terbang
      //check status burung
      if (bird.alive == false)
        return; 
      ```
      
##### 9. update tap/klik logic agar burung hanya terbang sekali jika di tap/klik
   - modif dan ketikan kode berikut didalam "fungsi update (update: function())"
       ```javascript
        if (game.input.activePointer.isDown)
        {
            if(!Helper.MouseOnDown){
                Helper.MouseOnDown = true;
                this.terbang();
            }
        }

        if (game.input.activePointer.isUp)
        {
             Helper.MouseOnDown = false;
        }
       ```
       
##### 10. coba refresh/jalankan url http://localhost/phaser/BirdGame/, maka kamu sudah bisa memainkan game Flappy Bird buatan kamu sendiri.

##### 11. game yang sudah sedikit modif bisa kamu mainkan juga di http://plexustechdev.com/game/flappybird/, 

