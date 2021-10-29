import speech_recognition as sr
from pynput.keyboard import Key, Listener

r = sr.Recognizer()

def listen_for_cmd():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def del_me():
    print('hello')


def activate_assistant(key):
    if key == Key.f4:
        listen_for_cmd()
          
    # by pressing 'delete' button 
    # you can terminate the loop 
    if key == Key.delete: 
        return False

with Listener(on_press = activate_assistant) as listener:
    listener.join()