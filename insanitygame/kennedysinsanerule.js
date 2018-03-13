function insaneRule() {
    if (score%2 === 2) {
      score = score * 2;
    }
    $('#interactive').append('<button>Click me!</button>');
    updateGame();

}
