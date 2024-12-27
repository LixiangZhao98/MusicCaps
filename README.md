# MusicCap
MusicCaps is a music description dataset released by Google, containing audio clips of music along with corresponding textual descriptions. Since the audio clips are extracted from YouTube videos, the dataset only provides the YouTube video IDs (ytid), start times (start_s), and end times (end_s), requiring users to download the audio clips themselves. This repo shows how to download MusicCap.


# Usage

```install
onda create --name MusicCap python=3.9

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

## Export Cookie
- Log in YouTube 
- Export the cookie with extensions (such as [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)) in `Netscape` format and save in `cookies.text`
