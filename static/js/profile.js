var current_theme = document.querySelector("#settings #theme").getAttribute("current");
var current_move = 0;

document.querySelector(`#settings #theme option[value="${current_theme}"]`).setAttribute("selected", "");
document.querySelector("#settings #theme").addEventListener("click", function() {
    if (document.querySelector("#settings #theme").value != current_theme) {
        window.location = "/settings/theme/"+document.querySelector("#settings #theme").value;
    } 
});

document.querySelector("#profile-plus").addEventListener("click", function() {
    current_move += 1;

    if (current_move > 2) {
        current_move = 0;
    }

    document.querySelector("#current-wrapper").style.transform = `translateX(-${current_move*60}vw)`;
});

document.querySelector("#profile-minus").addEventListener("click", function() {
    current_move -= 1;
    
    if (current_move > 2) {
        current_move = 0;
    }
    
    document.querySelector("#current-wrapper").style.transform = `translateX(-${current_move*60}vw)`;
});