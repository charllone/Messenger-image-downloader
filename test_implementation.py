#!/usr/bin/env python3
"""
Test script to validate the messenger_image_downloader.py logic
without requiring GUI dependencies.
"""

import json
import sys
from pathlib import Path


def test_config_validation():
    """Test configuration file validation."""
    print("Testing configuration validation...")
    
    # Test config.example.json can be loaded
    with open('config.example.json', 'r') as f:
        config = json.load(f)
    
    # Verify required keys
    required_keys = [
        'pushbullet_api_key',
        'download_button_image',
        'next_button_image',
        'confidence_threshold',
        'max_iterations',
        'delay_between_clicks',
        'human_like_movement',
        'movement_duration'
    ]
    
    for key in required_keys:
        assert key in config, f"Missing required key: {key}"
        print(f"  ✓ {key}: {config[key]}")
    
    # Verify data types
    assert isinstance(config['confidence_threshold'], (int, float)), "confidence_threshold must be numeric"
    assert 0 <= config['confidence_threshold'] <= 1, "confidence_threshold must be between 0 and 1"
    assert isinstance(config['max_iterations'], int), "max_iterations must be integer"
    assert config['max_iterations'] > 0, "max_iterations must be positive"
    assert isinstance(config['delay_between_clicks'], (int, float)), "delay_between_clicks must be numeric"
    assert config['delay_between_clicks'] > 0, "delay_between_clicks must be positive"
    assert isinstance(config['human_like_movement'], bool), "human_like_movement must be boolean"
    assert isinstance(config['movement_duration'], (int, float)), "movement_duration must be numeric"
    assert config['movement_duration'] > 0, "movement_duration must be positive"
    
    print("✓ Configuration validation passed!")
    return True


def test_file_structure():
    """Test that all required files exist."""
    print("\nTesting file structure...")
    
    required_files = [
        'messenger_image_downloader.py',
        'requirements.txt',
        'config.example.json',
        'README.md',
        '.gitignore',
        'templates/README.md'
    ]
    
    for file_path in required_files:
        assert Path(file_path).exists(), f"Missing required file: {file_path}"
        print(f"  ✓ {file_path} exists")
    
    print("✓ File structure validation passed!")
    return True


def test_requirements():
    """Test requirements.txt has necessary packages."""
    print("\nTesting requirements...")
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    required_packages = ['pyautogui', 'opencv-python', 'Pillow', 'numpy', 'pushbullet.py']
    
    for package in required_packages:
        assert package in content, f"Missing required package: {package}"
        print(f"  ✓ {package} listed in requirements")
    
    # Verify Pillow is safe version (>= 10.2.0) using regex
    import re
    pillow_match = re.search(r'Pillow[>=<]+(\d+\.\d+\.\d+)', content)
    assert pillow_match, "Pillow package not found in requirements"
    
    # Extract version and verify it's at least 10.2.0
    version_str = pillow_match.group(1)
    version_parts = [int(x) for x in version_str.split('.')]
    assert version_parts >= [10, 2, 0], f"Pillow version {version_str} is not secure (needs >= 10.2.0)"
    print(f"  ✓ Pillow version is secure (>= 10.2.0)")
    
    print("✓ Requirements validation passed!")
    return True


def test_syntax():
    """Test Python syntax is valid."""
    print("\nTesting Python syntax...")
    
    import py_compile
    try:
        py_compile.compile('messenger_image_downloader.py', doraise=True)
        print("  ✓ messenger_image_downloader.py syntax is valid")
    except py_compile.PyCompileError as e:
        print(f"  ✗ Syntax error: {e}")
        return False
    
    print("✓ Syntax validation passed!")
    return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running Messenger Image Downloader Tests")
    print("=" * 60)
    print()
    
    tests = [
        test_file_structure,
        test_config_validation,
        test_requirements,
        test_syntax
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            failed += 1
    
    print()
    print("=" * 60)
    print(f"Tests completed: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
