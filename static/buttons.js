buttons = document.querySelectorAll("a");
function toggleActiveClass(){
    buttons.forEach(function(button){ // cycle over buttons
    button.classList.remove('active'); // remove active class from it
    });
}
buttons.forEach(function(button){
    button.addEventListener("click", function(){
        buttons.forEach(function(button){ // cycle over buttons
        button.classList.remove('active'); // remove active class from it
        });
        button.classList.add('active');
    });
})