$( document ).ready(function() {
    initToggles();
    initErrorHandlers();
    initPredictor();
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

function initPredictor() {
    $('.predictor').on('click', '.team-prediction', function(event) {
        event.preventDefault();

        let game_id = $(this).closest('.game-prediction').data('gameId');
        let winning_team_id = $(this).data('teamId');
        let losing_team_id = $(this).siblings('.team-prediction').data('teamId')

        $('.game-prediction-' + game_id + ' .team-prediction').removeClass('active');
        $(this).addClass('active');

        let $input = $('#predictor-input');
        let round = $input.data('round');
        let data = $input.val();
        let json = {
            'round': round,
            'games': {}
        };

        try {
            json = JSON.parse(data);
        } catch(err) {
            console.log(err);
        }

        json.games[game_id] = {
            'winner': winning_team_id,
            'loser': losing_team_id
        };

        window.dataJson = json;
        $input.val(JSON.stringify(json));
    });

    let $input = $('#predictor-input');
    let data = $input.val();
    try {
        let json = JSON.parse(data);
        for (let game_id in json['games']) {
            let team_id = json['games'][game_id]['winner'];
            $('.team-prediction-' + team_id).addClass('active');
        }
    } catch(err) {
        console.log(err);
    }
}