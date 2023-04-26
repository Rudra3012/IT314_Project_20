function collapseSidebar() {
    const sidebar = document.getElementById("sidebar");
    const content = document.getElementById("content");
    const image = document.getElementById("img_btn");
    const para = document.getElementById("word");

    if (sidebar.classList.contains("active")) {
        sidebar.classList.remove("active");
        content.style.marginLeft = "280px";
        content.style.transition = "0.5s";
        para.style.marginLeft = "555px";
        image.style.marginLeft = "-50px";
    } else {
        sidebar.classList.add("active");
        content.style.marginLeft = "80px";
        image.style.marginLeft = "70px";
        para.style.marginLeft = "470px";
        content.style.transition = "0.5s";
    }
    image.style.transition = "0.5s";
    para.style.transition = "0.5s";

}


document.getElementById("collapse-btn").addEventListener("click", collapseSidebar);

const collapseButton = document.querySelector('#collapse-btn');
const sidebarItems = document.querySelectorAll('.list-group-item');
const menuButtons = document.querySelector('.menu-buttons');

collapseButton.addEventListener('click', function () {
    document.querySelector('#sidebar').classList.toggle('collapsed');

    sidebarItems.forEach(function (item) {
        item.querySelector('.sidebar-text').classList.toggle('collapsed');
    });

    menuButtons.classList.toggle('collapsed');
});


// Check if the user is logged in by looking for a cookie named 'loggedIn'
const loggedIn = document.cookie.indexOf('loggedIn') !== -1;

// Get references to the buttons
const loginButton = document.getElementById('login-button');
const signupButton = document.getElementById('signup-button');
const logoutButton = document.getElementById('logout-button');

// Toggle the display of the buttons based on whether the user is logged in or not
if (loggedIn) {
    loginButton.style.display = 'none';
    signupButton.style.display = 'none';
    logoutButton.style.display = 'block';
} else {
    loginButton.style.display = 'block';
    signupButton.style.display = 'block';
    logoutButton.style.display = 'none';
}

burger = document.querySelector('.burger');
sidebar = document.getElementById('sidebar');
listgroup = document.querySelector('.list-group');
contentManipulation = document.getElementById('content');
// Check if media query matches

// Add styles for small screens
burger.addEventListener('click', () => {
    listgroup.classList.toggle('vclass');
    sidebar.classList.toggle('active');

    if (sidebar.classList.contains('active')) {
        // sidebar.classList.remove("inactive");
        sidebar.style.width = "265px";
    }
    else {
        sidebar.style.width = "50px";
    }
})