function wrong(){
  $('#function_wrong').text('Nice work!');
  window.location.href = '?pass={{ passphrase }}';
}

function right() {
  $('#function_wrong').text('Hey, you clicked me!');
  $('body').append('<div>How about changing my onclick="right()" to be wrong()?</div>')
}
