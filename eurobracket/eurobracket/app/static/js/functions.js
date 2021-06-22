$( document ).ready(function() {
    initToggles();
    initErrorHandlers();
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

function initErrorHandlers() {
    $('.form-input input.has-error').on('keyup', function(event) {
        let value = $(this).val();
        if(hasStringValue(value)) {
            $(this).removeClass('has-error');
            $(this).addClass('had-error');
        }
    });

    $('.form-input').on('keyup', 'input.had-error', function(event) {
        let value = $(this).val();
        if(!hasStringValue(value)) {
            $(this).removeClass('had-error');
            $(this).addClass('has-error');
        }
    });
}

function hasStringValue(val) {
    return  val !== undefined && val !== null && val !== '';
}