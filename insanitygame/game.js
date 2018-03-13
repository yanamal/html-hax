var score = 0;

function updateGame() {
  $('#s').text(score);

  // Put code for activating/deactivating your rule here:
function insanityRule() {
    if (score%2 === 2) {
      score = score * 2;
    }
    $('#interactive').append('<button>Click me!</button>');
    updateGame();

}
