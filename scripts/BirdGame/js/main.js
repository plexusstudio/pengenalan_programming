var bird; //object burung
var pipes; //kumpulan object pipa

// bikin phaser game di canvas, dengan resolusi 480 x 800
var game = new Phaser.Game(480, 800, Phaser.AUTO, 'game-area');

// bikin variable yang didalemnya bakal ada fungsi2 untuk game phaser
var mainState = {
    preload: function() { 
        // fungsi yang dijalanin pas pertama halaman muncul  

    },

    create: function() { 
        // fungsi ini dijalanin setelah preload beres

    },

    update: function() {
        //ini fungsi yang jalan terus2an kalo kata forum2 detailnya tuh dijalanin 60kali dalam satu detik

    },
};


// masukin mainState tadi ke game phaser
game.state.add('main', mainState); 

// jalanin game phaser
game.state.start('main');

// fungsi Helper
var Helper = new function(){

    this.getRandomInt = function(min, max){
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
    }

    this.MouseOnDown = false;
}
