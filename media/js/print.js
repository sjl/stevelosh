$(function() {
    $('#leaf-content p:has(a)').add('#leaf-content ol:has(a)').add('#leaf-content ul:has(a)').each(function() {
        var printing_links = $(this).find('a')
                                    .not("[href^='#']")
                                    .not(":has(img)")
                                    .clone();
        $(this).after(printing_links);

        printing_links.wrap('<li></li>')
                      .parent()
                      .wrapAll('<ul class="print-links"></ul>');

        printing_links.each(function() {
            var href = $(this).attr('href');
            if (href.match("^/")) {
                href = 'http://stevelosh.com' + href;
            }
            $(this).after(': ' + href);
        });
    });
});
