# QtTranslator
A small Qt-based Translator using the google translator API + file importing, supporting only EN+DE+RU because im too lazy to add the full list of languages


# Setup
Navigate to the root folder of the project.
Install the requirements with `pip install -r requirements.txt`

To build an executable, simply `pip install cx-Freeze`, then `Python export.py build`.

# Troubleshooting
After making use of the _Import Site_ function a couple times, you will probably experience your device going slower and slower.
To solve this, close the process _QtWebEngine_ in your task manager.
This is a bug in PyQt5 thats probably causing the pdf printer to stay opened.

The translated text will be cut off after 5000 characters, this is a limitation by the Google Translate API.

# Credits
The main window was built with QtDesigner.