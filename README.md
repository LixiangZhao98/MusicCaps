# MusicCaps
[MusicCaps](https://paperswithcode.com/dataset/musiccaps) is a dataset composed of 5.5k music-text pairs, with rich text descriptions provided by human experts. For each 10-second music clip, MusicCaps provides:

1) A free-text caption consisting of four sentences on average, describing the music and

2) A list of music aspects, describing genre, mood, tempo, singer voices, instrumentation, dissonances, rhythm, etc.

# Usage

```install
conda create --name MusicCap python=3.9

conda activate MusicCap

pip install datasets yt-dlp pydub
```


## Install FFmpeg
For Windows:
Download [FFmpeg](https://ffmpeg.org/download.html), add the path to the system's environment variables.

For macOS/Linux:
```install
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg
```

## [Pass cookies to yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp)
- Log in YouTube
- Use a conforming browser extension to export cookies, such as [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) and [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) for Chrome, [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/) for Firefox.
- Copy and save the cookie (`Netscape` format) to the local file `cookies.txt`

## Run
```install
python Download.py
```
