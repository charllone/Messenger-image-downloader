# Messenger Image Downloader

A Python automation tool that bulk-downloads images from Facebook Messenger's media viewer. It uses image recognition to locate and click the Download and Next buttons automatically, simulates human-like mouse movement to avoid stalling, and sends a Pushbullet notification when all images are done.

## Files

- `messnger adv.py` — main script, runs the download loop
- `region.py` — helper to find the screen coordinates of a button region
- `seperate.py` — sorts downloaded files into subfolders by type (GIFs, Videos)
- `download.PNG` / `next.PNG` — reference images used for button detection
- `requirements.txt` — Python dependencies

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get your Pushbullet API key
Go to https://www.pushbullet.com/#settings/account, copy your Access Token, and paste it into `messnger adv.py`:
```python
PUSHBULLET_API_KEY = "your_api_key_here"
```

### 3. Find your button regions
Run `region.py` and follow the prompts to get the correct `DOWNLOAD_REGION` and `NEXT_REGION` values for your screen. Update them in `messnger adv.py`:
```python
DOWNLOAD_REGION = (x, y, width, height)
NEXT_REGION = (x, y, width, height)
```

### 4. Run
Open Messenger in your browser, open the media viewer on the first image, then run:
```bash
python "messnger adv.py"
```
You have 5 seconds to switch to the Messenger window before it starts.

## Notes

- Tested on Windows with Messenger in a browser
- Confidence threshold is set to `0.4` — lower it if detection is too strict, raise it if there are false positives
- Downloaded files go to your browser's default download folder; run `seperate.py` afterward to sort GIFs and videos into subfolders
