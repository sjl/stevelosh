#!/usr/local/bin/python2.5

import sys, os
sys.path.append('/home/sjl/webapps/stevelosh')
os.environ['DJANGO_SETTINGS_MODULE'] = 'stevelosh.settings'

import simplejson, urllib, urllib2
from stevelosh.thoughts.models import TextThought, LinkThought
from datetime import datetime


TUMBLR_API_URL = r'http://stevelosh.tumblr.com/api/read/json'

def parse_tumblr_json(data):
    tumblr_prefix = r'var tumblr_api_read = '
    if data.startswith(tumblr_prefix):
        data = data.strip()
        data = data[len(tumblr_prefix):-1]
    else:
        return None
    return simplejson.loads(data)

def fetch_tumblr_data(type):
    parameters = {'type': type, 'filter': 'none'}
    url_parameters = urllib.urlencode(parameters)
    full_api_url = TUMBLR_API_URL + '?' + url_parameters
    response = urllib2.urlopen(full_api_url)
    return parse_tumblr_json(response.read())

def update_text_thoughts():
    recent_thoughts = fetch_tumblr_data('regular')
    for thought in recent_thoughts['posts']:
        tumblr_id = thought['id']
        try:
            TextThought.objects.get(tumblr_id=tumblr_id)
        except TextThought.DoesNotExist:
            title = thought['regular-title'] \
                    if thought['regular-title'] != "" else None
            new_thought = TextThought(
                    tumblr_id=tumblr_id,
                    title=title,
                    body=thought['regular-body'],
                    posted=datetime.fromtimestamp(thought['unix-timestamp']) )
            new_thought.save()

def update_link_thoughts():
    recent_thoughts = fetch_tumblr_data('link')
    for thought in recent_thoughts['posts']:
        tumblr_id = thought['id']
        try:
            LinkThought.objects.get(tumblr_id=tumblr_id)
        except LinkThought.DoesNotExist:
            name = thought['link-text'] \
                    if thought['link-text'] != "" else None
            description = thought['link-description'] \
                    if thought['link-description'] != "" else None
            new_thought = LinkThought(
                    tumblr_id=tumblr_id,
                    name=name,
                    description=description,
                    url=thought['link-url'],
                    posted=datetime.fromtimestamp(thought['unix-timestamp']) )
            new_thought.save()

update_text_thoughts()
update_link_thoughts()
