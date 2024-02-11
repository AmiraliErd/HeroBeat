function more_text(){

    dots = document.getElementById('dots');
    txt_more = document.getElementById('more');
    btn = document.getElementById('btn');


    if(dots.style.display === "none"){

        dots.style.display="inline" ;
        btn.innerHtml = "Read More" ;
        txt_more.style.display="none";

    }else{
        dots.style.display="none";
        btn.innerHtml = "Read lass" ;
        txt_more.style.display="inline";
    }

}




var audio = document.getElementById('audio');
var time_start = document.getElementById('time-start');
var time_end = document.getElementById('time-end');
var time_line = document.getElementById('line-music-red');

var play = false;


function play_and_puse(){

    if (play === true){
        audio.pause();
       play = false ;

    }else {

        audio.play();
        play = true;

    }

}


function play_music(){

    document.getElementById('play-music').style.display="none";
    document.getElementById('puse-music').style.display="block";

}


function puse_music(){

    document.getElementById('play-music').style.display="block";
    document.getElementById('puse-music').style.display="none";

}




function change_format(time){

    var daghighe = parseInt(time / 60);

    var second = parseInt(time - (daghighe * 60));

    if(second > 9){
        return daghighe.toString() + ":" + second.toString();
    }else{
        return daghighe.toString() + ":0" + second.toString();
    }

}





audio.addEventListener('timeupdate' , function (){

    time_line.style.width = (audio.currentTime * 100 / audio.duration) + "%";

    time_start.innerText = change_format(audio.currentTime);

    time_end.innerText = change_format(audio.duration - audio.currentTime);

});





var audio2 = document.getElementById('audio');

var playy_music = false;


function omid_music(){

    if (playy_music === true){

        audio2.pause();
        playy_music = false;

    }else {

        audio2.play();
        playy_music = true ;

    }

}




function icon_play1(){

    document.getElementById('play_block1').style.display="none";
    document.getElementById('play_none1').style.display="block";

}


function icon_play_none1(){

    document.getElementById('play_block1').style.display="block";
    document.getElementById('play_none1').style.display="none";

}




function icon_play2(){

    document.getElementById('play_block2').style.display="none";
    document.getElementById('play_none2').style.display="block";

}


function icon_play_none2(){

    document.getElementById('play_block2').style.display="block";
    document.getElementById('play_none2').style.display="none";

}




function icon_play3(){

    document.getElementById('play_block3').style.display="none";
    document.getElementById('play_none3').style.display="block";

}


function icon_play_none3(){

    document.getElementById('play_block3').style.display="block";
    document.getElementById('play_none3').style.display="none";

}




function icon_play4(){

    document.getElementById('play_block4').style.display="none";
    document.getElementById('play_none4').style.display="block";

}


function icon_play_none4(){

    document.getElementById('play_block4').style.display="block";
    document.getElementById('play_none4').style.display="none";

}




function icon_play5(){

    document.getElementById('play_block5').style.display="none";
    document.getElementById('play_none5').style.display="block";

}


function icon_play_none5(){

    document.getElementById('play_block5').style.display="block";
    document.getElementById('play_none5').style.display="none";

}



function icon_play6(){

    document.getElementById('play_block6').style.display="none";
    document.getElementById('play_none6').style.display="block";

}


function icon_play_none6(){

    document.getElementById('play_block6').style.display="block";
    document.getElementById('play_none6').style.display="none";

}



function icon_play7(){

    document.getElementById('play_block7').style.display="none";
    document.getElementById('play_none7').style.display="block";

}


function icon_play_none7(){

    document.getElementById('play_block7').style.display="block";
    document.getElementById('play_none7').style.display="none";

}




function icon_play8(){

    document.getElementById('play_block8').style.display="none";
    document.getElementById('play_none8').style.display="block";

}


function icon_play_none8(){

    document.getElementById('play_block8').style.display="block";
    document.getElementById('play_none8').style.display="none";

}



function icon_play9(){

    document.getElementById('play_block9').style.display="none";
    document.getElementById('play_none9').style.display="block";

}


function icon_play_none9(){

    document.getElementById('play_block9').style.display="block";
    document.getElementById('play_none9').style.display="none";

}