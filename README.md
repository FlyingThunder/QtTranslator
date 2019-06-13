# QtTranslator
A small Qt-based Translator using the google translator API + file importing, supporting only EN+DE+RU because im too lazy to add the full list of languages

# Used third-party modules
This programm uses
* googletrans (https://pypi.org/project/googletrans/)
* PyQt5 (https://pypi.org/project/PyQt5/)
* python-docx to extract text from .doc files (https://pypi.org/project/python-docx/)
* odfpy to extract text from .odt files(https://pypi.org/project/odfpy/)
* tika to extract text from .pdf files (https://pypi.org/project/tika/)

and a variety of built-in python modules

# Setup
Navigate to the root folder of the project.
Install the requirements with `pip install -r requirements.txt`

To build an executable, simply `pip install cx-Freeze`, then `Python export.py build`.

# Usage
This program is a translator, thus obviously focusing on translating.

Here is an overview over the main GUIs functionality:

![Image](https://i.imgur.com/fcVpBJ1.png)


There are three ways to translate text with this tool:
* Enter text manually into the "Input" Textbox
* Via the "Import..." menu button, you can import a:
*   file (made to work with .txt, .doc, .odt or .pdf, might work with other plain-text formats)
*   website (should work with any kind of website)

The supported languages as of now are English, German and Russian (works with latin and kyrillic letters)

There are a few preferences that you can set in the "Settings" menu:
* Removing URLs from Siteimport
* Automatically saving the translated result as a .txt file
* Automatically saving the imported *source* website as a .pdf
* Leetspeech. Because reasons.

# Troubleshooting
After making use of the _Import Site_ function a couple times, you will probably experience your device going slower and slower.
To solve this, close the process _QtWebEngine_ in your task manager.
This is a bug in PyQt5 thats probably causing the pdf printer to stay opened.

The translated text will be cut off after 5000 characters, this is a limitation by the Google Translate API.

# Credits
The main window was built with QtDesigner.
