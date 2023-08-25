function search() {
    window.location.search = "?search="+document.querySelector("#search-input").value;
}

var searchParams = new URLSearchParams(window.location.search);

if (searchParams.has("search")) {
    document.querySelector("#search-input").value = searchParams.get("search");
}

document.querySelector("#search-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.querySelector("#search-button").click();
    }
});