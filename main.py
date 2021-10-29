import speech_recognition as sr
from pynput.keyboard import Key, Listener

r = sr.Recognizer()

def listen_for_cmd():
    """
    Convert's the user's speech to text

    Using the SpeechRecognition library (https://github.com/Uberi/speech_recognition), 
    the microphone records the user's voice and converts it to usable text. 
    
    The program can also run in the background.
    """
    with sr.Microphone() as source:
        print("\nSay a command")
        audio = r.listen(source)

    try:
        # TODO: add functionality to the user's commands
        print("Google speech recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google speech recognition service; {e}")


def activate_assistant(key):
    """
    This function waits for the f4 key to be pressed, then it fires the listen_for_cmd function
    """

    if key == Key.f4:
        listen_for_cmd()
          
    # by pressing 'delete' button 
    # you can terminate the loop 
    if key == Key.delete: 
        return False


with Listener(on_press = activate_assistant) as listener:
    print('When you are ready to speak a command, press the F4 key: ')
    listener.join()