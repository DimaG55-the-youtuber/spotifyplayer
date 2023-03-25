var previousId;
// Create a reference for the Wake Lock.
let wakeLock = null;

// create an async function to request a wake lock
async function requestWakeLock() {
    try {
        wakeLock = await navigator.wakeLock.request("screen");
        console.log("Wake Lock is active");
    } catch (err) {
        // The Wake Lock request has failed - usually system related, such as battery.
        console.log(`${err.name}, ${err.message}`);
    }
}

requestWakeLock();
function playrand() {
    var random = Math.floor(Math.random() * 30);
    document.querySelectorAll('audio').forEach(el => {
        el.pause();
        el.currentTime = 0;
    });
    while (random === previousId) {
        random = Math.floor(Math.random() * 30);
    }
    previousId = random;

    var audio = document.getElementById(random);
    audio.play();
}

function stopall() {
    document.querySelectorAll('audio').forEach(el => {
        el.pause();
        el.currentTime = 0;
    });
}