#!/bin/env python3

import argparse
import csv
import sys
import json
import yt_dlp

parser = argparse.ArgumentParser(description='yt-playlist-export exports YouTube playlists to JSON or CSV')
parser.add_argument('--browser', type=str, required=False, default='firefox', help='browser where you logged in to YouTube')
parser.add_argument('-f', '--format', type=str, choices=['csv', 'json'], required=False, default='csv', help='output\'s format')
parser.add_argument('-o', '--output', type=str, required=False, help='filename to store output, by default it\'s printed to stdout')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
parser.add_argument('playlist', nargs='+', help='playlist URL')
args = parser.parse_args()


# print(args)
# exit(0)

playlist = args.playlist[0]
format = args.format
output = args.output
verbose = args.verbose

id = 'id'
url = 'url'
title = 'title'
duration = 'duration'
channel_id = 'channel id'
channel_name = 'channel name'
channel_url = 'channel url'
duration = 'duration (seconds)'
view_count = 'view count'
thumbnail_xs = 'thumbnail xs'
thumbnail_s = 'thumbnail s'
thumbnail_m = 'thumbnail m'
thumbnail_l = 'thumbnail l'

header = [
    id,
    url,
    title,
    duration,
    channel_id,
    channel_name,
    channel_url,
    view_count,
    thumbnail_xs,
    thumbnail_s,
    thumbnail_m,
    thumbnail_l,
]

# Converts ytl JSON structure to yt-playlist-export, in particular removing all not populated field
def convert_to_csv(info: any) -> any:
    for entry in info['entries']:
        yield {
            id: entry['id'],
            url: entry['url'],
            title: entry['title'],
            duration: entry['duration'],
            channel_id: entry['channel_id'],
            channel_name: entry['channel'],
            channel_url: entry['channel_url'],
            view_count: entry['view_count'],
            thumbnail_xs: entry['thumbnails'][0]['url'] if len(entry['thumbnails']) > 0 else "",
            thumbnail_s: entry['thumbnails'][1]['url'] if len(entry['thumbnails']) > 1 else "",
            thumbnail_m: entry['thumbnails'][2]['url'] if len(entry['thumbnails']) > 2 else "",
            thumbnail_l: entry['thumbnails'][3]['url'] if len(entry['thumbnails']) > 3 else "",
        }

def print_csv(info: any):
    global output
    if output is None:
        csv_file = sys.stdout
    else:
        csv_file = open(output, mode='w', newline='', encoding='utf-8')
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for row in convert_to_csv(info):
        writer.writerow(row)

def print_json(info: any):
    global output
    if output is None:
        print(json.dumps(info))
    else:
        with open(output, 'w') as f:
            f.write(json.dumps(info))

# See the yt-dlp main page for the --cookies-from-browser syntax description
# which in brief is browser+keyring:profile::container
# This function converts it to a tuple as per help(yt_dlp.YoutubeDL)
# On errors fall back to assuming the entire string is a browser, which was behaviour before this function was added
def parse_browser_string(browserCookieString):
    # This is probably doable with a single encompassing regex with capturing groups but I couldnt get it to work perfectly in all 16+ edge cases
    # For now it is ugly but functional
    keyring_pos = browserCookieString.find('+')
    profile_pos = browserCookieString.find(':')
    container_pos = browserCookieString.find('::')
    #print(keyring_pos, profile_pos, container_pos)
    if (profile_pos > 0 and profile_pos < keyring_pos) or (container_pos > 0 and container_pos < profile_pos) or keyring_pos == 0 or profile_pos == 0:
        return (browserCookieString,)
    browser = browserCookieString[0:profile_pos if keyring_pos < 0 else keyring_pos]
    keyring = None if keyring_pos < 0 else browserCookieString[keyring_pos+1:None if profile_pos < 0 else profile_pos]
    if profile_pos == container_pos: # no profile - the first colon is a double
        profile = None
    else:
        profile = browserCookieString[profile_pos+1:None if container_pos < 0 else container_pos]
    container = None if container_pos < 0 else browserCookieString[container_pos+2:]

    # the order is swapped for the Python ytdlp api
    return (browser, profile, keyring, container)

# See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {
    'cookiesfrombrowser': parse_browser_string(args.browser),
    'ignoreerrors': 'only_download',
    'extract_flat': True,
    'quiet': not verbose
}

def main():
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist, download=False)
        # ydl.sanitize_info makes the info json-serializable
        info_sanitized = ydl.sanitize_info(info)
        if format == 'json':
            print_json(info_sanitized)
        else:
            print_csv(info_sanitized)
