$(function() {
    $('div.gallery').each(function () {
        $(this).contents().filter(function() {
            return this.nodeType == Node.TEXT_NODE;
        }).remove();
        
        var cols = 4;
        var padding = 10;
        var total_width = $(this).width();
        var width = (total_width / cols) - 2 * padding;
        $(this).find('img').css({width: width, margin: padding});
        
        $(this).before('<div class="gallery-pane"></div>');
        $(this).find('img:first').clone()
                                 .addClass('gallery-display')
                                 .css({width: '', margin: ''})
                                 .appendTo('div.gallery-pane');
    });

    $('div.gallery img').click(function() {
        var new_image = $(this).clone()
                               .addClass('gallery-display')
                               .css({width: '', margin: '', display: 'none'});
        $('img.gallery-display').fadeOut('fast', function() {
            $(this).remove();
            new_image.appendTo('div.gallery-pane').fadeIn('slow');
        });
    });
});