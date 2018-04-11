var BlackCounter = 0;
function Blackone(){
  BlackCounter = BlackCounter + 1;
  console.log (BlackCounter)
 if (BlackCounter === 15){
   score = score + 100;
   $('#blackbutton').css('display', 'none');
   Status = true;
 }
updateGame()
}
