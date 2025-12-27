# Quick Start Guide

Get started with Messenger Image Downloader in 5 minutes!

## Prerequisites

- Python 3.7+ installed
- pip package manager
- A GUI-enabled system (Windows, macOS, or Linux with X11)

## Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/charllone/Messenger-image-downloader.git
   cd Messenger-image-downloader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration**
   ```bash
   cp config.example.json config.json
   ```
   
   Edit `config.json` and update:
   - `pushbullet_api_key`: (Optional) Your API key from https://www.pushbullet.com/#settings/account
   - Leave other settings at defaults for now

4. **Create button templates**
   
   a. Open the webpage/app with the buttons you want to automate
   
   b. Take screenshots of:
      - The download button → Save as `templates/download_button.png`
      - The next button → Save as `templates/next_button.png`
   
   c. Tips:
      - Crop tightly around each button
      - Use PNG format
      - Ensure buttons are clearly visible

5. **Test your setup**
   ```bash
   python test_implementation.py
   ```
   
   All tests should pass ✓

## Running the Script

1. Open the page with the images you want to download

2. Run the script:
   ```bash
   python messenger_image_downloader.py
   ```

3. The script will:
   - Search for the download button
   - Click it when found
   - Search for the next button
   - Click it to move to the next image
   - Repeat until complete

4. **To stop**: Press `Ctrl+C` or move mouse to upper-left corner

## Troubleshooting

### "Button not found"
- Lower `confidence_threshold` in config.json (try 0.7)
- Retake template images with better quality
- Ensure window size hasn't changed

### "Module not found" errors
- Run: `pip install -r requirements.txt`
- On Linux: `sudo apt-get install python3-tk python3-dev`

### Script clicking wrong places
- Increase `confidence_threshold` (try 0.9)
- Make template images more specific
- Check only one button is visible on screen

## Next Steps

- Check the logs in `image_downloader.log` for details
- Adjust timing in `config.json` if clicks are too fast/slow
- Set up Pushbullet for mobile notifications
- Read the full README.md for advanced configuration

## Support

For issues or questions, please open an issue on GitHub.

Happy automating! 🚀
