# FAB-related-utility-scripts
some utilities for fellow card gamers. they usually are fore fetching some info on cards. Most of them made for FABONLINE 


download_imgs.py
    - fetches all card's images in jpg format with their card codes as filename from the official fab website https://fabtcg.com/

download_imgsFabDB.py
    - does the same using the fab api (some data errors may occur on the side of the fabdb api)
    - also fetches additional information using the api
    - can be used to generate templates for spread sheats
generate_php.py
    - generates a function written in php that returns the name of the given the cardcode (set code + number) and also generates a reverse function

card_text_recognition.py 
    - uses the fetched images
    - generates a csv database of a cards information (stats + information) using Tesseract (ocr)
    - also can generate crops of the part of these images
    - prints a cropped image of each card's face image to a file 

