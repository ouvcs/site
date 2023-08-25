window.onload = async function() {
    let user_name_calculate = document.createElement("span");
    let user_name_span = document.querySelector('.menu-item#last span');
    
    user_name_calculate.style.font = document.body.style.font;
    user_name_calculate.style.fontSize = "1.25em";
    user_name_calculate.style.height = "auto";
    user_name_calculate.style.width = "auto";
    user_name_calculate.style.position = "absolute";
    user_name_calculate.style.top = "1000vh";
    user_name_calculate.style.whiteSpace = "no-wrap";
    user_name_calculate.innerHTML = user_name_span.innerHTML;
    
    document.body.appendChild(user_name_calculate);
    let width = Math.ceil(100*user_name_calculate.clientWidth/window.innerWidth);
    document.body.removeChild(user_name_calculate);
    
    user_name_span.setAttribute("style", "--width: "+width+"vw;");
}