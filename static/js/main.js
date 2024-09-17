// -----------------reach live----------------

function incrementCount(key, elementId, initialValue) {
    let count = localStorage.getItem(key);
    if (!count) {
        count = initialValue;
    } else {
        count = parseInt(count) + 1;
    }
    localStorage.setItem(key, count);
    document.getElementById(elementId).innerText = count + "+";
}
document.addEventListener("DOMContentLoaded", function() {
    incrementCount('reachCount', 'reachCount', 15);
});


setTimeout(function() {
    const flashMessages = document.querySelector('.flashes');
    if (flashMessages) {
        flashMessages.style.display = 'none';
    }
}, 2000); // 2000 milliseconds = 2 seconds