import deploy
import urllib2

def feeds(request, url, feed_dict):
    headers = {'HTTP_HOST':'Host',
               'HTTP_USER_AGENT':'User-Agent',
               'HTTP_ACCEPT_ENCODING':'Accept-Encoding',
               'HTTP_ACCEPT_LANGUAGE':'Accept-Language',
               'HTTP_REFERER':'Referer',
               'HTTP_COOKIE':'Cookies'}
    
    feed_name = [p.capitalize() for p in url.split('/') if p.strip() != ''][-1]
    
    # Call into BirdFeeder with the request headers.
    o = urllib2.build_opener()
    o.addheaders = [ (headers[k], request.META.get(k, '')) 
                     for k in request.META.keys() if k in headers.keys()]
    f = o.open( "http://stevelosh.com/feeder/index.php?pw=%s&feed_name=%s" % 
                (deploy.FEEDER_PASSWORD, feed_name) )
    f.read()
    f.close()

    return django.contrib.syndication.views.feed(request, url=url, 
                                                 feed_dict=feed_dict)