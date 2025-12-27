#!/usr/bin/env python3
"""
Messenger Image Downloader
A Python automation script that automates downloading images by detecting 
on-screen buttons using image recognition.
"""

import pyautogui
import time
import json
import logging
import sys
from pathlib import Path
from typing import Optional, Tuple
from pushbullet import Pushbullet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('image_downloader.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Fail-safe: Move mouse to upper-left corner to abort
pyautogui.FAILSAFE = True


class ImageDownloader:
    """Main class for automating image downloads through button detection."""
    
    def __init__(self, config_path: str = 'config.json'):
        """Initialize the downloader with configuration."""
        self.config = self._load_config(config_path)
        self.download_count = 0
        self.pb = None
        
        # Initialize Pushbullet if API key is provided
        if self.config.get('pushbullet_api_key') and \
           self.config['pushbullet_api_key'] != 'YOUR_PUSHBULLET_API_KEY_HERE':
            try:
                self.pb = Pushbullet(self.config['pushbullet_api_key'])
                logger.info("Pushbullet initialized successfully")
            except Exception as e:
                logger.warning(f"Failed to initialize Pushbullet: {e}")
    
    def _load_config(self, config_path: str) -> dict:
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                logger.info(f"Configuration loaded from {config_path}")
                return config
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_path}")
            logger.info("Please copy config.example.json to config.json and configure it")
            sys.exit(1)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            sys.exit(1)
    
    def _find_button_on_screen(self, button_image_path: str) -> Optional[Tuple[int, int]]:
        """
        Find a button on screen using image recognition.
        
        Args:
            button_image_path: Path to the button template image
            
        Returns:
            Tuple of (x, y) coordinates if found, None otherwise
        """
        try:
            confidence = self.config.get('confidence_threshold', 0.8)
            location = pyautogui.locateOnScreen(
                button_image_path, 
                confidence=confidence
            )
            
            if location:
                # Get center of the button
                center = pyautogui.center(location)
                logger.debug(f"Button found at {center}")
                return center
            else:
                logger.debug(f"Button not found: {button_image_path}")
                return None
        except Exception as e:
            logger.error(f"Error finding button: {e}")
            return None
    
    def _click_button(self, x: int, y: int):
        """
        Click a button at the specified coordinates with human-like movement.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        try:
            if self.config.get('human_like_movement', True):
                duration = self.config.get('movement_duration', 0.5)
                pyautogui.moveTo(x, y, duration=duration)
                time.sleep(0.1)  # Brief pause before clicking
                pyautogui.click()
            else:
                pyautogui.click(x, y)
            
            logger.info(f"Clicked at position ({x}, {y})")
        except Exception as e:
            logger.error(f"Error clicking button: {e}")
    
    def _send_notification(self, title: str, body: str):
        """
        Send a Pushbullet notification.
        
        Args:
            title: Notification title
            body: Notification body
        """
        if self.pb:
            try:
                self.pb.push_note(title, body)
                logger.info("Pushbullet notification sent")
            except Exception as e:
                logger.error(f"Failed to send notification: {e}")
    
    def run(self):
        """
        Main automation loop.
        Continuously looks for download and next buttons and clicks them.
        """
        logger.info("Starting image download automation...")
        logger.info("Press Ctrl+C or move mouse to upper-left corner to stop")
        
        max_iterations = self.config.get('max_iterations', 100)
        delay = self.config.get('delay_between_clicks', 1.5)
        download_button_path = self.config.get('download_button_image')
        next_button_path = self.config.get('next_button_image')
        
        # Verify template images exist
        if not Path(download_button_path).exists():
            logger.error(f"Download button template not found: {download_button_path}")
            logger.info("Please provide a screenshot of the download button")
            sys.exit(1)
        
        if not Path(next_button_path).exists():
            logger.error(f"Next button template not found: {next_button_path}")
            logger.info("Please provide a screenshot of the next button")
            sys.exit(1)
        
        try:
            iteration = 0
            consecutive_failures = 0
            max_consecutive_failures = 5
            
            while iteration < max_iterations:
                iteration += 1
                logger.info(f"Iteration {iteration}/{max_iterations}")
                
                # Look for download button
                download_pos = self._find_button_on_screen(download_button_path)
                
                if download_pos:
                    logger.info("Download button detected!")
                    self._click_button(*download_pos)
                    self.download_count += 1
                    time.sleep(delay)
                    consecutive_failures = 0
                    
                    # Look for next button
                    next_pos = self._find_button_on_screen(next_button_path)
                    
                    if next_pos:
                        logger.info("Next button detected!")
                        self._click_button(*next_pos)
                        time.sleep(delay)
                    else:
                        logger.warning("Next button not found")
                        consecutive_failures += 1
                else:
                    logger.warning("Download button not found")
                    consecutive_failures += 1
                    time.sleep(delay)
                
                # Stop if too many consecutive failures
                if consecutive_failures >= max_consecutive_failures:
                    logger.info(f"Stopped after {max_consecutive_failures} consecutive failures")
                    break
            
            # Send completion notification
            summary = f"Downloaded {self.download_count} images in {iteration} iterations"
            logger.info(f"Automation complete! {summary}")
            self._send_notification(
                "Image Download Complete",
                summary
            )
            
        except KeyboardInterrupt:
            logger.info("\nAutomation stopped by user")
            self._send_notification(
                "Image Download Stopped",
                f"Downloaded {self.download_count} images before stopping"
            )
        except pyautogui.FailSafeException:
            logger.info("\nFail-safe triggered - mouse moved to corner")
            self._send_notification(
                "Image Download Stopped",
                f"Fail-safe activated. Downloaded {self.download_count} images"
            )
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            self._send_notification(
                "Image Download Error",
                f"Error occurred after downloading {self.download_count} images: {str(e)}"
            )


def main():
    """Main entry point."""
    print("=" * 60)
    print("Messenger Image Downloader")
    print("=" * 60)
    print()
    
    downloader = ImageDownloader()
    downloader.run()


if __name__ == "__main__":
    main()
