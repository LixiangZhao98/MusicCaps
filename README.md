# MusicCap
MusicCaps is a music description dataset released by Google, containing audio clips of music along with corresponding textual descriptions. Since the audio clips are extracted from YouTube videos, the dataset only provides the YouTube video IDs (ytid), start times (start_s), and end times (end_s), requiring users to download the audio clips themselves. This repo shows how to download MusicCap.


## Usage

```install
$ pip install datasets yt-dlp pydub
```
