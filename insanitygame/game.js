var score = 0;

function updateGame() {
  $('#s').text(score);

  // Put code for activating/deactivating your rule here:
function insanityRule() {
    if (score%2 === 0) {
      score = score x 2;
    }
    $('#interactive').append('<button>try me!</button>');
    updateGame();
  if( score >= 10 ) {
    $('#fivepointsbutton').css('display', 'inline');
  }

}
