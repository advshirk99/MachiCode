# OCR-of-Devnagari-text
Code for change hackathon

##  Libraries used
### Numpy
### Pandas
### OpenCV
### pdf2image
### pytesseract
### pillow
### os
### xlwt
### matplotlib

## Steps for OCR
## 1. PDF to Image
The pdf is imported and later converted to image using pdf2image

## 2. Image PreProcessing
Table detection is done using OpenCV python and cropped using pillow library according to the data required for OCR recogniction

## 3. OCR
Using teserract, the characters will be recognised and stored into a text files

## 4. Save to Excel
Text file data will be sent to an excel sheet
