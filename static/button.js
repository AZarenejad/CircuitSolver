$("button").on("click", function() {
  $(this).html('<i class="fa fa-check"></i>');
  $(this).css('background-color', '#4CD698');
  
  
  setTimeout(function() {
    $("button").html('Reset');
    $("button").css('background-color', '#ef612d');
    //Send - #40B4DE
    }, 300);
});

