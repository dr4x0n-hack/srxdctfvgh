function openTool(url) {
    window.open(url, "_blank");
}

// ---- GEOLOCATION TRAINER ----

let data = [
    { image: "tokyo.jpg", location: "Tokyo, Japan" },
    { image: "paris.jpg", location: "Paris, France" },
    { image: "dubai.jpg", location: "Dubai, UAE" }
];

let current = null;

function loadRandom() {
    current = data[Math.floor(Math.random() * data.length)];
    document.getElementById("geo-img").src = "images/" + current.image;
}
loadRandom();

function checkGuess() {
    let user = document.getElementById("guess").value.toLowerCase();
    let ans = current.location.toLowerCase();

    if (user.includes(ans.split(",")[0])) {
        document.getElementById("result").innerText = "Correct!";
    } else {
        document.getElementById("result").innerText = "Wrong! It was: " + current.location;
    }
    setTimeout(loadRandom, 2000);
}
