# Messenger Image Downloader

A Python automation script that automates downloading images by detecting on-screen buttons using image recognition. Built for personal automation, it simulates human mouse movement and sends a Pushbullet notification when the job is done.

## Features

- 🔍 **Image Recognition**: Automatically detects download and next buttons on screen
- 🖱️ **Human-like Movement**: Simulates natural mouse movements to avoid detection
- 📱 **Pushbullet Notifications**: Get notified when downloads complete
- ⚙️ **Configurable**: Customize confidence thresholds, delays, and iterations
- 🛡️ **Fail-safe**: Move mouse to upper-left corner to emergency stop
- 📝 **Logging**: Detailed logs of all actions and errors

## Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux with GUI support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/charllone/Messenger-image-downloader.git
cd Messenger-image-downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create your configuration file:
```bash
cp config.example.json config.json
```

4. Edit `config.json` with your settings (see Configuration section)

## Configuration

Edit `config.json` with the following parameters:

- **pushbullet_api_key**: Your Pushbullet API key (optional, get from https://www.pushbullet.com/#settings/account)
- **download_button_image**: Path to download button template image (default: `templates/download_button.png`)
- **next_button_image**: Path to next button template image (default: `templates/next_button.png`)
- **confidence_threshold**: Image matching confidence (0.0-1.0, recommended: 0.8)
- **max_iterations**: Maximum number of download attempts (default: 100)
- **delay_between_clicks**: Seconds to wait between clicks (default: 1.5)
- **human_like_movement**: Enable smooth mouse movement (default: true)
- **movement_duration**: Duration of mouse movement in seconds (default: 0.5)

## Creating Button Templates

1. Navigate to the page with the buttons you want to automate
2. Take screenshots of the download and next buttons
3. Crop the images to show only the button (include a small margin)
4. Save as PNG in the `templates/` directory
5. Update paths in `config.json`

See `templates/README.md` for detailed instructions.

## Usage

1. Ensure your configuration is set up correctly
2. Navigate to the page with the buttons in your browser
3. Run the script:
```bash
python messenger_image_downloader.py
```

4. The script will:
   - Look for the download button
   - Click it when found
   - Look for the next button
   - Click it to move to the next image
   - Repeat until max_iterations or manual stop

5. Stop the script:
   - Press `Ctrl+C`, or
   - Move mouse to upper-left corner (fail-safe)

## Troubleshooting

### Buttons not detected
- Ensure template images are clear and properly cropped
- Lower the `confidence_threshold` in config (try 0.7)
- Verify screen resolution matches when template was captured
- Check that button appearance is consistent (no hover effects)

### Script clicking wrong locations
- Increase `confidence_threshold` to be more strict (try 0.9)
- Recreate template images with better quality
- Ensure only one matching button is visible on screen

### Import errors
- Reinstall dependencies: `pip install -r requirements.txt --upgrade`
- On Linux, you may need: `sudo apt-get install python3-tk python3-dev`

## Logs

Detailed logs are saved to `image_downloader.log` in the same directory.

## Safety & Ethics

This tool is for **personal automation only**. Please:
- Respect website terms of service
- Don't use for unauthorized access or scraping
- Be mindful of rate limits and server load
- Use responsibly and ethically

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This software is provided as-is. Use at your own risk. The authors are not responsible for any misuse or damage caused by this software.
