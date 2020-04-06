const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Error message fadeout
setTimeout(function(){
    $('#message').fadeOut('slow');
},3000);
