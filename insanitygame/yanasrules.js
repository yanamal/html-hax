
function incrementScore() {
  score = score + 1;
  updateGame();
}

function addtwoToScore() {
  score = score + 2;
  updateGame();
}

function insanityRule() {
  if (score%2 === 0) {
    score = score / 2;
  }
  $('#interactive').append('<button>try me!</button>');
  updateGame();
}
