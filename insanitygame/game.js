var score = 0;

function updateGame() {
  $('#s').text(score);

  // Put code for activating/deactivating your rule here:
  if( score >= 10 ) {
    $('#fivepointsbutton').css('display', 'inline');
  }

}
