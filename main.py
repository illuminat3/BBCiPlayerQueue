from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import queue
import time

def play_video(url, driver):
    driver.get(url)
    # Add code here to handle login if necessary

    try:
        # Example: wait for the play button and click it
        # Note: The actual element identifier will depend on BBC iPlayer's web structure
        play_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'play-button')]"))
        )
        play_button.click()

        # You might need additional code here to handle things like fullscreen, skip intro, etc.

    except Exception as e:
        print(f"Error playing video: {e}")

def play_videos(video_queue):
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed and in PATH

    while True:
        if not video_queue.empty():
            url = video_queue.get()
            play_video(url, driver)
            # Note: Detecting when the video ends is complex and depends on the player's behavior
            time.sleep(5)  # Placeholder for video duration
        else:
            print("No more videos in queue, waiting...")
            time.sleep(1)

    driver.quit()

def main():
    video_queue = queue.Queue()

    # Thread for playing videos
    play_thread = threading.Thread(target=play_videos, args=(video_queue,))
    play_thread.start()

    while True:
        new_video_url = input("Enter the BBC iPlayer video URL: ")
        video_queue.put(new_video_url)

if __name__ == "__main__":
    main()
