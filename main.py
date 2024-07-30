import speech_recognition as sr
import pyttsx4
import datetime
import webbrowser

engine = pyttsx4.init()

def say_to_me(talk):
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


record = sr.Recognizer()

try:
    with find_microphone() as source:
        # with sr.Microphone() as source:
        record.adjust_for_ambient_noise(source, 5)
        print("Speak...")
        audio = record.listen(source)
        result = record.recognize_google(audio, language='en')
        # result = record.recognize_google_cloud(audio, language='ru')
        result = result.lower()
        if result == 'say time':
            now = datetime.datetime.now()
            str_date = f'Now {str(now.hour)}:{str(now.minute)}'
            print(str_date)
            say_to_me(str_date)
        elif result == 'open web-browser':
            webbrowser.open('https://itproger.com')
            say_to_me('opening web-browser')
except sr.UnknownValueError:
    print("Unknown voice")
except sr.RequestError:
    print('Something went wrong')
