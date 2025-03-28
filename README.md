# yt-playlist-export

yt-playlist-export is a tool that allows to export YouTube playlists, export YouTube "Watch later" list and export YouTube "Liked videos". It supports exporting to JSON and CSV formats.

## Installation

```bash {"id":"01J4HFTRJ1CK76GD127E1R65GX"}
python3 -m pip install yt-playlist-export
```

## Usage

```bash {"id":"01J4HFTRJ1CK76GD127F41SF28"}
yt-playlist-export -h
usage: yt-playlist-export [-h] [--browser BROWSER] [--cookies COOKIES] [-f {csv,json}] [-o OUTPUT] [-v] playlist [playlist ...]

yt-playlist-export exports YouTube playlists to JSON or CSV

positional arguments:
  playlist              playlist URL

optional arguments:
  -h, --help            show this help message and exit
  --browser BROWSER     browser where you logged in to YouTube
  --cookies COOKIES     absolute path to a Netscape formatted cookie file
  -f {csv,json}, --format {csv,json}
                        output's format
  -o OUTPUT, --output OUTPUT
                        filename to store output, by default it's printed to stdout
  -v, --verbose         verbose
```

### Use case: Exporting public playlist

```bash
yt-playlist-export -f csv -o test.csv https://www.youtube.com/playlist?list=PLO4kDC0EWkeCnf8PBRk7XDPhrzmAxHLah
```

### Use case: Exporting using cookies from default browser (firefox)

```bash
yt-playlist-export -f csv -o test.csv https://www.youtube.com/playlist?list=PLO4kDC0EWkeCnf8PBRk7XDPhrzmAxHLah
```

### Use case: Exporting using Chrome browser

At the moment of writing this supported browsers are: firefox, safari, brave, chrome, chromium, edge, opera, vivaldi, whale.

For the `--browser` agrument one can also pass `BROWSER[+KEYRING][:PROFILE][::CONTAINER]` as it's described in [yt-dlp](https://github.com/yt-dlp/yt-dlp) documentation.
Check out `--cookies-from-browser` option in yt-dlp documentation to understand how it works.

```bash
yt-playlist-export --browser chrome -f csv -o test.csv https://www.youtube.com/playlist?list=PLO4kDC0EWkeCnf8PBRk7XDPhrzmAxHLah
```

### Use case: Exporting using cookie file

The cookie file must be in a Netscape format. You can follow [this guide](https://github.com/yt-dlp/yt-dlp/issues/10927) and use [this extension](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) for Chrome.

```bash
yt-playlist-export --cookies /home/daydiff/cookie.txt -f csv -o test.csv https://www.youtube.com/playlist?list=PLO4kDC0EWkeCnf8PBRk7XDPhrzmAxHLah
```


## Show case

```bash {"id":"01J4HFTRJ1CK76GD127FGZF1W0"}
yt-playlist-export https://www.youtube.com/playlist?list=PLO4kDC0EWkeCnf8PBRk7XDPhrzmAxHLah
```

![YouTube playlist exported to CSV](/assets/format_csv.png)

## Dependencies

yt-playlist-export is using [yt-dlp](https://github.com/yt-dlp) under the hood.

## Keywords

YouTube export playlist. YouTube export Watch later list. YouTube export liked videos. YouTube export playlist to CSV. YouTube export playlist to JSON. YouTube export private playlist.
