function newScore(){
  $("#goal").text(score);
}
var score = 0
document.onkeypress = function(){
  var entry = event.key;

  if (entry == "a" || entry == "A"){
    score = score + 1;
    newScore();
  }

  if (entry == "s" || entry == "S"){
    if (score >= 5){
      score=score-5;
      newScore();
    }
  }

  if (entry == "w" || entry == "W"){
    if (score >= 5){
      score = score + 5;
      newScore();
    }
  }
}
