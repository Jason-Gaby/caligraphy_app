# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#### SOME IDEAS:
# USE USPS API for address verification
# Use tesseract for OCR
# create some kind of integration with an excel spread sheet
# what to do with GUI???

# How will this flow?
'''
    Import excel sheet
    Check each of the addresses using USPS:
        https://www.usps.com/business/web-tools-apis/
    Flag the ones that might be incorrect
    Then, use a camera to check an address against the excel sheet
    TESSERACT: https://pypi.org/project/pytesseract/
        Things to check:
        Address
        Name of recipient
        Misc???
    It should give an error if there is a typo somewhere...


'''

from PIL import Image
import pytesseract

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(pytesseract.image_to_string(Image.open("images/IMG_8516.jpg")))
    print("HELLO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
