$(document).ready(function() {
    $('p:has(a)').add('ol:has(a)').add('ul:has(a)').each(function() {
        var printing_links = $(this).find('a').clone();
        $(this).after(printing_links);
        
        printing_links.wrap('<li></li>')
                      .parent()
                      .wrapAll('<ul class="print-links"></ul>');
        
        printing_links.each(function() {
            $(this).after(': ' + $(this).attr('href'));
        });
    });
});