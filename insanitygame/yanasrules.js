
function incrementScore() {
  score = score + 1;
  updateGame();
}

function addFiveToScore() {
  score = score + 5;
  updateGame();
}

function divideIfEven() {
  if (score%2 === 0) {
    score = score / 2;
  }
  updateGame();
}
