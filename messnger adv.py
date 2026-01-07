import pyautogui
import time
import sys
import tkinter as tk
from tkinter import messagebox
from pushbullet import Pushbullet
import random

time.sleep(5)

DOWNLOAD_IMAGE = "download.png"
NEXT_IMAGE = "next.png"
CONFIDENCE = 0.4

#CHANGE THESE REGIONS
DOWNLOAD_REGION = (1241, 115, 74, 50)
NEXT_REGION = (0, 323, 54, 133)

#Pushbullet setup
PUSHBULLET_API_KEY = "Put Your API Key Here"
pb = Pushbullet(PUSHBULLET_API_KEY)

def send_pushbullet_notification(title, message, retries=3):
    for attempt in range(retries):
        try:
            pb.push_note(title, message)
            print("Pushbullet notification sent.")
            break
        except Exception as e:
            print(f"[Warning] Attempt {attempt+1} failed: {e}")
            time.sleep(1)
    else:
        print("[Error] Could not send Pushbullet notification after multiple attempts.")


def task_complete_popup():
    send_pushbullet_notification("Task Complete", "All images have been downloaded.")
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Task Complete", "All images have been downloaded.")
    root.destroy()

while True:
    # Download button
    try:
        download_btn = pyautogui.locateCenterOnScreen(
            DOWNLOAD_IMAGE,
            region=DOWNLOAD_REGION,
            confidence=CONFIDENCE,
            grayscale=True
        )
        if download_btn:
            pyautogui.click(download_btn)
            time.sleep(1)
    except pyautogui.ImageNotFoundException:
        pass

    # Wait for Next button to appear
    timeout = 10  # seconds to wait initially
    start_time = time.time()
    next_btn = None

    # Initial wait loop
    while (time.time() - start_time) < timeout:
        try:
            next_btn = pyautogui.locateCenterOnScreen(
                NEXT_IMAGE,
                region=NEXT_REGION,
                confidence=CONFIDENCE,
                grayscale=True
            )
            if next_btn:
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5)

    if not next_btn:
        # Mimic human: move mouse slightly while checking for the Next button
        current_pos = pyautogui.position()
        move_x = random.randint(-50, 50)
        move_y = random.randint(-50, 50)
        # Move mouse gradually while continuously checking
        steps = 10
        for i in range(steps):
            pyautogui.moveRel(move_x/steps, move_y/steps, duration=0.1)
            try:
                next_btn = pyautogui.locateCenterOnScreen(
                    NEXT_IMAGE,
                    region=NEXT_REGION,
                    confidence=CONFIDENCE,
                    grayscale=True
                )
                if next_btn:
                    break  # Exit the movement loop immediately if button appears
            except pyautogui.ImageNotFoundException:
                pass

        pyautogui.moveTo(current_pos, duration=0.5)  # return to original position

        # Check once more after movement
        if not next_btn:
            extra_wait = 5
            start_extra = time.time()
            while (time.time() - start_extra) < extra_wait:
                try:
                    next_btn = pyautogui.locateCenterOnScreen(
                        NEXT_IMAGE,
                        region=NEXT_REGION,
                        confidence=CONFIDENCE,
                        grayscale=True
                    )
                    if next_btn:
                        break
                except pyautogui.ImageNotFoundException:
                    pass
                time.sleep(0.5)

    if next_btn:
        pyautogui.click(next_btn)
        time.sleep(1)
    else:
        # Next button still not found → task complete
        task_complete_popup()
        sys.exit()
