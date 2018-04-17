var score = 2;
var Status = false;
var Appeared = false;

function updateGame() {
  $('#s').text(score);
  // Put code for activating/deactivating your rule here:
  if( score >= 20 ) {
    $('#fivepointsbutton').css('display', 'inline');
  }
  if( score >= 10 ) {
    $('#twopointsbutton2').css('display', 'inline');
  }

  if( score <= 20  ) {
    $('#twopointsbutton').css('display', 'inline');
  }
  if( score > 20  ) {
    $('#twopointsbutton').css('display', 'none');

  }

  if(score >=5){
    $('#minusfive').css('display', 'inline');
  }

  if(score >=35){
    if (Appeared === false){
    $('#blackbutton').css('display', 'inline');
    setTimeout(timer, 4000)
    Appeared = true;
  }
  }

}

function timer(){
  if (Status === false){
  score = score - 100;
  $('#blackbutton').css('display', 'none');
  updateGame()
}
}
