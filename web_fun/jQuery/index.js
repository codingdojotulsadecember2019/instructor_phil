$(document).ready(function(){

  // $('button').click(runMeAfterButtonIsClicked);

  var change;
  $('h1').hover(function(){
    change = $(this).css('color');
    console.log(change);
    $(this).css('color', 'red');
  },
  function(){
    $(this).css('color', change);
  })

  $('.addClass').click(function(){
    // $('p').addClass('red');
    $(this).siblings('div').children('p').addClass('red');
  })
})

// function runMeAfterButtonIsClicked(){
//   alert('button clicked');
// }
