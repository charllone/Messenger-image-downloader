# Button Template Images

This directory should contain screenshots of the buttons you want to detect.

## Required Templates

1. **download_button.png** - Screenshot of the download button
2. **next_button.png** - Screenshot of the next button

## How to Create Template Images

1. Take a screenshot of the button you want to detect
2. Crop the image to include only the button (with a small margin)
3. Save it as PNG format in this directory
4. Update the paths in `config.json` to match your filenames

## Tips for Better Detection

- Use high-quality, clear screenshots
- Ensure the button is clearly visible and not obscured
- Keep consistent screen resolution when running the script
- Test different confidence thresholds (0.7-0.9) in config.json
- Make sure the button appearance doesn't change (no hover effects in screenshot)
