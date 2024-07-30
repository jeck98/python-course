#imports for speech recognition
import speech_recognition as sr
import pyttsx4
import datetime
import webbrowser
import pytesseract

# imports for text recognition
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
from PIL import Image
from pytesseract import image_to_string

import sys

def say_to_me(talk):
    engine = pyttsx4.init()
    engine.say(talk)
    engine.runAndWait()


def find_microphone():
    m = None
    for device_index in sr.Microphone.list_working_microphones():
        m = sr.Microphone(device_index=device_index)
        break
    else:
        say_to_me("No working microphones found!")
        raise Exception("No working microphones found!")

    if m is not None:
        print(device_index)
        print("Mic ready")
        say_to_me("Microphone ready!")
    return m


def write_file(text):
    with open('image_text/image_text.txt', "w", encoding="utf-8") as target_file:
        target_file.write(text)


def recognize_text():
    text = image_to_string(Image.open('images/photo_en.png'), lang="eng")
    return text

def read_file():
    with open('image_text/image_text.txt', "r", encoding="utf-8") as target_file:
        print(target_file.read())

def main():
    record = sr.Recognizer()
    try:
        with find_microphone() as source:
            record.adjust_for_ambient_noise(source, 5)
            print("Speak...")
            audio = record.listen(source)
            result = record.recognize_google(audio, language='en')
            result = result.lower()
            if result == 'write file':
                print('write file')
                text = recognize_text()
                write_file(text)
                say_to_me('write file complete')
            if result == 'read file':
                print('read file\n')
                read_file()
                say_to_me('read file complete')
            if result == 'exit':
                say_to_me('exit from program')
                sys.exit()
            else:
                msg = 'Unknown command. Please, try again'
                say_to_me(msg)
                print(msg)
    except sr.UnknownValueError:
        print("Unknown voice")
    except sr.RequestError:
        print('Something went wrong')

if __name__ == "__main__":
    main()
