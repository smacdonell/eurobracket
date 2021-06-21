$( document ).ready(function() {
    initToggles();
});

function initToggles() {
    $('.toggle-container .toggle-button').on('click', function(event) {
        event.preventDefault();

        let target = $(this).data('target');
        $('.toggle-container .toggle-button').removeClass('active');
        $('.toggle-container .toggle-target').removeClass('active');
        $(this).addClass('active');
        $('.toggle-container .toggle-target.' + target).addClass('active');
    });
}