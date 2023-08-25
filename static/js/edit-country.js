var interval = setInterval(newImage, 100);

function newImage() {
    if (document.querySelector("#country-flag").style.backgroundImage != "url("+document.querySelector("#country-flag").value+")") {
        document.querySelector("#country-flag").style.backgroundImage = "url("+document.querySelector("#country-flag").value+")";
    }
}

console.log(document.querySelector("form"));
document.querySelector("form").onsubmit = async function(event) {
    let flag = document.querySelector("#country-flag");
    let cid = document.querySelector("#country-id");
    let date = document.querySelector("#country-date");
    let name = document.querySelector("#country-name");
    let group = document.querySelector("#country-group");
    let flag_check, cid_check, date_check, name_check, group_check = false;

    cid_check = /^([a-z]){2,30}$/.test(cid.value);
    name_check = name.value.length <= 100 && name.value.length >= 3;
    group_check = /^(http(s)?:\/\/)?vk\.com\/[a-zA-Z_]+$/.test(group.value);
    date_check = /^\d\d\.\d\d\.\d\d\d\d$/.test(date.value);

    if (!date_check) {
        date.setCustomValidity("Введите данные в указаном формате.");
        return false;
    }
    if (new Date(date.value) > new Date()) {
        date.setCustomValidity("Дата должна быть меньше чем завтра.")
    }
    if (new Date(date.value) < new Date("2000-01-01")) {
        date.setCustomValidity("Дата должна быть больше чем 1 Января 2000 года.")
    }
    if (!cid_check) {
        cid.setCustomValidity("Введите данные в указаном формате.");
        return false;
    }
    if (!name_check) {
        name.setCustomValidity("Введите данные в указаном формате."+name.value.leght);
        return false;
    }
    if  (!group_check) {
        group.setCustomValidity("Неверная ссылка.");
        return false;
    } 

    await fetch("/profile/country/check/?link="+flag.value).then((response) => response).then((status_code) => {
        if (status_code.status == "200") flag_check = true;
    });

    if (!flag_check) {
        flag.setCustomValidity("Неверная ссылка.");
        return false;
    }

    return true;
};

document.querySelectorAll("input:not([type=submit])").forEach(function(e) {
    e.onclick = function() {
        document.querySelectorAll("input").forEach(function(e2) {
            e2.setCustomValidity("");
        });
    };
});