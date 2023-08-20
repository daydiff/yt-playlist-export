# yt-playlist

yt-playlist is a tool that allows to export YouTube playlists, export YouTube "Watch later" list and export YouTube "Liked videos". It supports exporting to JSON and CSV formats.

## Installation

```bash
git clone https://github.com/daydiff/yt-playlist.git
cd yt-playlist
python3 -m pip install -r requirements.txt
```

## Usage

```bash
yt-playlist -h
usage: yt-playlist [-h] [--browser BROWSER] [-f {csv,json}] [-o OUTPUT] [-v] playlist [playlist ...]

yt-playlist exports YouTube playlists to JSON or CSV

positional arguments:
  playlist              playlist URL

optional arguments:
  -h, --help            show this help message and exit
  --browser BROWSER     browser where you logged in to YouTube
  -f {csv,json}, --format {csv,json}
                        output's format
  -o OUTPUT, --output OUTPUT
                        filename to store output, by default it's printed to stdout
  -v, --verbose         verbose
```

## Show case

```bash
yt-playlist https://www.youtube.com/playlist\?list\=PL0XfG7TzasxNCl8a-SdyvSoazX1VYBweF -f csv -o test.csv
```

![YouTube playlist exported to CSV](/assets/format_csv.png)


## Dependencies

yt-playlist is using [yt-dlp](https://github.com/yt-dlp) under the hood.

## Keywords

YouTube export playlist. YouTube export Watch later list. YouTube export liked videos. YouTube export playlist to CSV. YouTube export playlist to JSON. YouTube export private playlist.
