var h2s = null;

function place_scrolly_header () {
    var soff = 75;

    var y = $(window).scrollTop();

    var target_content = null;
    var opacity = null;
    var header_y = null;
    h2s.each(function() {
        var pre_header_y = $(this).position()['top'] - soff;
        if (y < pre_header_y) {
            return false;
        };
        header_y = pre_header_y;

        target_content = $(this).html().replace(/&nbsp;/g, ' ');

        var opacity_y = y - (header_y + soff);
        opacity = opacity_y / soff;
        if (opacity > 1.0) {
            opacity = 1.0;
        }

        if (opacity > 0.99) {
            var next_headers = $(this).nextAll('h2');
            if (next_headers.length) {
                var next_header_y = next_headers.first().position()['top'];
                var next_header_distance = next_header_y - y;
                if (next_header_distance <= soff*2) {
                    opacity = 1.0 / (soff - next_header_distance/2);
                };
            }
        }
    });
    $('#scrolling-header').css({ opacity: opacity })
                          .css('left', h2s.first().position()['left'] - 180 - 35)
                          .html(target_content);
}

$(function() {
    jQuery('span.timeago').timeago();

    if ($('#leaf-stats').length) {
        $('body').append('<div id="scrolling-header"></div>');
        h2s = $('#leaf-content h2');

        $(window).scroll(function () {
            place_scrolly_header();
        });
    }
});
