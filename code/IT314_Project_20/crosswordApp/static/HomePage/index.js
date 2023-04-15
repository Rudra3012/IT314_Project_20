let margin = 250

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#content').css('margin-left', `${margin}px`);
        $('.white-section').css('margin-left', `${margin}px`);
        margin = 250 - margin;
    });
});

