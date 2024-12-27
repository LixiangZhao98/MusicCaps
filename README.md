# MusicCap
MusicCaps is a music description dataset released by Google, containing audio clips of music along with corresponding textual descriptions. Since the audio clips are extracted from YouTube videos, the dataset only provides the YouTube video IDs (ytid), start times (start_s), and end times (end_s), requiring users to download the audio clips themselves. This repo shows how to download MusicCap.


# Usage

```install
$ pip install datasets yt-dlp pydub
```


## Install FFmpeg for Windows
Download [FFmpeg](https://ffmpeg.org/download.html), add the path to the system's environment variables.
## Install FFmpeg for macOS/Linux
```install
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg
```
