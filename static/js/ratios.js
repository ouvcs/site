let flags = document.querySelectorAll(".country-flag");
let photos = document.querySelectorAll(".valute-photo");


flags.forEach(function(e) {
    let img = new Image();

    img.onload = function() {
        let width = img.naturalWidth;
        let height = img.naturalHeight;
        let nod = 1;
        if (width != 0 && height != 0) {
            for (let i = Math.max(width, height); i > 0; i--) {
                if ((width/i)-Math.floor((width/i)) == 0) {
                    if ((height/i)-Math.floor((height/i)) == 0) {
                        e.style.aspectRatio = `${width/nod}/${height/nod}`;
                    }
                }
            }
        }
    };

    img.src = e.getAttribute("src");
});

photos.forEach(function(e) {
    let img = new Image();

    img.onload = function() {
        let width = img.naturalWidth;
        let height = img.naturalHeight;
        let nod = 1;
        if (width != 0 && height != 0) {
            for (let i = Math.max(width, height); i > 0; i--) {
                if ((width/i)-Math.floor((width/i)) == 0) {
                    if ((height/i)-Math.floor((height/i)) == 0) {
                        e.style.aspectRatio = `${width/nod}/${height/nod}`;
                    }
                }
            }
        }
    };

    img.src = e.getAttribute("src");
});