#!/usr/bin/env python3
"""
Example usage of the Messenger Image Downloader

This demonstrates how to use the ImageDownloader class programmatically
with custom configurations.
"""

import json
from pathlib import Path


def example_basic_usage():
    """Basic usage example with default configuration."""
    print("Example 1: Basic Usage")
    print("-" * 40)
    print("""
# Basic usage with default config.json
from messenger_image_downloader import ImageDownloader

downloader = ImageDownloader()
downloader.run()
""")
    print("This would start the automation with default config")
    print()


def example_custom_config():
    """Example with custom configuration file."""
    print("Example 2: Custom Configuration")
    print("-" * 40)
    
    # Create custom config
    custom_config = {
        "pushbullet_api_key": "YOUR_API_KEY",
        "download_button_image": "templates/custom_download.png",
        "next_button_image": "templates/custom_next.png",
        "confidence_threshold": 0.85,
        "max_iterations": 50,
        "delay_between_clicks": 2.0,
        "human_like_movement": True,
        "movement_duration": 0.7
    }
    
    print("Custom configuration example:")
    print(f"{json.dumps(custom_config, indent=2)}")
    print("""
# Save custom config and use it
import json
from messenger_image_downloader import ImageDownloader

with open('config_custom.json', 'w') as f:
    json.dump(custom_config, f, indent=2)

downloader = ImageDownloader('config_custom.json')
downloader.run()
""")
    print()


def example_testing_detection():
    """Example of testing button detection without clicking."""
    print("Example 3: Testing Button Detection")
    print("-" * 40)
    
    from pathlib import Path
    
    # Check if template files exist
    templates = [
        "templates/download_button.png",
        "templates/next_button.png"
    ]
    
    print("Checking for template images:")
    for template in templates:
        exists = Path(template).exists()
        status = "✓ Found" if exists else "✗ Missing"
        print(f"  {status}: {template}")
    
    print("\nTo test button detection:")
    print("1. Ensure template images are in place")
    print("2. Open the page with the buttons")
    print("3. Run: python messenger_image_downloader.py")
    print()


def show_configuration_options():
    """Display all available configuration options."""
    print("Available Configuration Options")
    print("=" * 40)
    
    options = {
        "pushbullet_api_key": {
            "type": "string",
            "description": "Your Pushbullet API key for notifications",
            "default": "Optional"
        },
        "download_button_image": {
            "type": "string",
            "description": "Path to download button template image",
            "default": "templates/download_button.png"
        },
        "next_button_image": {
            "type": "string",
            "description": "Path to next button template image",
            "default": "templates/next_button.png"
        },
        "confidence_threshold": {
            "type": "float (0.0-1.0)",
            "description": "Image matching confidence level",
            "default": "0.8"
        },
        "max_iterations": {
            "type": "integer",
            "description": "Maximum number of download attempts",
            "default": "100"
        },
        "delay_between_clicks": {
            "type": "float",
            "description": "Seconds to wait between clicks",
            "default": "1.5"
        },
        "human_like_movement": {
            "type": "boolean",
            "description": "Enable smooth mouse movement",
            "default": "true"
        },
        "movement_duration": {
            "type": "float",
            "description": "Duration of mouse movement in seconds",
            "default": "0.5"
        }
    }
    
    for key, info in options.items():
        print(f"\n{key}:")
        print(f"  Type: {info['type']}")
        print(f"  Description: {info['description']}")
        print(f"  Default: {info['default']}")
    print()


def main():
    """Run all examples."""
    print("=" * 60)
    print("Messenger Image Downloader - Examples")
    print("=" * 60)
    print()
    
    example_basic_usage()
    example_custom_config()
    example_testing_detection()
    show_configuration_options()
    
    print("=" * 60)
    print("Note: Examples are for demonstration only.")
    print("Uncomment the run() calls to actually execute automation.")
    print("=" * 60)


if __name__ == "__main__":
    main()
