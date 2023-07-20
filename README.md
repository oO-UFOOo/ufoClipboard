# ufoClipboard


## Hello Ufozzz, it's time to stop our clipboard loss!

Do you often find yourself losing valuable clipboard content on Windows? Well, fear not! This Python script aims to make your life easier by saving all your clipboard content to a designated folder, ensuring you never lose important information again!

## How does it work?

1. **Run on Startup:** The script is designed to run on startup, so you don't need to worry about manually starting it every time you boot up your computer.

2. **Save Clipboard Text:** Every time you copy text to your clipboard, the script will automatically save it as a text file in the specified folder. No more worrying about accidentally overwriting your copied text!

3. **Capture Screenshots:** If you ever copy a screenshot to the clipboard, the script will detect it and save it as an image file in the same folder. Now you can easily keep track of all your screenshots.

## Usage Instructions:

1. Make sure you have Python installed on your system.
2. Install the required libraries by running the following commands in your terminal or command prompt:

pip install pyperclip
pip install pillow
pip install imagehash

4. Clone this repository or download the `ufoClipboard.py` script.
5. Edit the script to specify the folder where you want to save the clipboard data on line :41 otherwise default is "C:\iCopiedThis"
6. Run the script: Double-click the `ufoClipboard.py` file, and it will start running in the background, automatically saving your clipboard data.
7. Make sure to stop the script if you don't need it anymore.

If you like it , 
1. make a shortcut of the script (shorctut target = "C:\path\to\pythonw.exe" "C:\path\to\clipboard_savior.py"
2. copy to windows startup folder , so as to run on startup
3. now you can sleep sleep calm.....

Enjoy!

###uFOo after sensitive clipboard Loss
