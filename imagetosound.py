from gtts import gTTS
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
def image_to_sound(image):
    try:
        open_image = Image.open(image)
        text = pytesseract.image_to_string(open_image)
        text_file = " ".join(text.split("\n"))
        print(text_file)
        sound = gTTS(text_file,lang="en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as bugs:
        print("The error while executing the code is:",bugs)
        return
    
if __name__ == "__main__":
    image_to_sound("image.jpg")
    input()