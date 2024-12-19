# YouTube Audio Downloader

This Python script allows you to search and download directly from YouTube as audio files in MP3 format. It's built using the `yt_dlp` library for downloading and extracting audio, and `urllib` for searching on YouTube. 

## Motivation

This project was created to solve a personal need: my radio only supports SD cards and USB sticks, so I can’t connect Spotify via Bluetooth. This script helps create a personalized collection of music in MP3 format that can be easily transferred to these devices for personal usage.

## Features

- Search for songs on YouTube using song titles.
- Automatically downloads the best available audio quality in MP3 format.
- Saves the downloaded audio files to a specified destination folder.

## Requirements

To run this script, you'll need the following Python libraries installed:

- [uv](https://github.com/astral-sh/uv): An extremely fast Python package and project manager, written in Rust.

## Usage

### Running as a Script

1. Clone the repository:

```bash
git clone https://github.com/rribeiro1/youtube-audio-downloader.git
cd youtube-audio-downloader
```

2. Edit the `songs` list in the script to include the titles of the songs you want to download:

```python
songs = [
    "Clipe Oficial - Vem Espírito de Deus",
    "Gabriel Guedes - Santo Pra Sempre",
]
```

3. Run the script:

> [!Note]
> Make sure you downloaded and configured [uv](https://github.com/astral-sh/uv) accordingly.

```bash
uv run main.py
```

4. The downloaded audio files will be saved to the folder specified in the `destination_folder` variable. By default, this is the current directory (`./`).

## Example Output

When the script is executed, it will:

1. Search for each song title on YouTube.
2. Print the first search result.
3. Download the audio from the video.
4. Save the audio in MP3 format.

## Contributing

Contributions are welcome! If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Disclaimer

This script is for personal use only. Ensure you respect copyright laws and the terms of service of YouTube when using this tool.
