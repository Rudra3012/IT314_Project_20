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
