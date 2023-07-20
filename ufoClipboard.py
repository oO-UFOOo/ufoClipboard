import os
import time
import pyperclip
from PIL import ImageGrab
import imagehash

def image_difference(image1, image2):
    hash1 = imagehash.average_hash(image1)
    hash2 = imagehash.average_hash(image2)
    return hash1 - hash2

def create_directory_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def save_clipboard_content(folder):
    create_directory_if_not_exists(folder)
    previous_text_content = None
    previous_image_data   = None

    while True:
        # Check for text data
        text_content = pyperclip.paste()
        if text_content and text_content != previous_text_content:
            filename = os.path.join(folder, f"clipboard_{time.time()}.txt")
            with open(filename, "w") as file:
                file.write(text_content)
            previous_text_content = text_content

        # Check for image data
        image_data = ImageGrab.grabclipboard()
        if image_data is not None:
            if previous_image_data is None or image_difference(image_data, previous_image_data) > 5:
                image_filename = os.path.join(folder, f"clipboard_{time.time()}.png")
                image_data.save(image_filename)
                previous_image_data = image_data

        time.sleep(1)  # Adjust the sleep time (in seconds) to avoid excessive checking

if __name__ == "__main__":
    folder_to_save = "C:\iCopiedThis"  # Replace with the actual folder path you want to save the clipboard data
    save_clipboard_content(folder_to_save)
