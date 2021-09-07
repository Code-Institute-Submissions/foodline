// Load the users last scroll position on product page in sessionStorage
document.addEventListener('DOMContentLoaded', function (event) {
    const scrollPosition = sessionStorage.getItem('scrollPosition');

    if (scrollPosition) window.scrollTo(0, scrollPosition);
});

// Save the users last scroll position on product page 
// and the users last filters and sort selection in sessionStorage
window.onbeforeunload = function (p) {
    sessionStorage.setItem('scrollPosition', window.scrollY);
    sessionStorage.setItem("userFilter", window.location);
};
