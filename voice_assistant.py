import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("Sorry, I timed out waiting for your response. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said. Could you please repeat?")
        except sr.RequestError:
            speak("Sorry, I'm having trouble accessing the Google API. Please check your internet connection.")
        except Exception as e:
            print(e)
            speak("Sorry, I encountered an error. Please try again later.")
        return None
def execute_command(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
    elif 'play music' in query:
        music_dir = 'C:\\Users\\maham\\Music'
        songs = os.listdir(music_dir)
        random_song = random.choice(songs)
        os.startfile(os.path.join(music_dir, random_song))
    elif 'what is the time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'open code' in query:
        code_path = "C:\\Users\\maham\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code"
        os.startfile(code_path)
    elif 'exit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")
def run_assistant():
    greet()
    while True:
        query = take_command()
        if query:
            execute_command(query)
if __name__ == "__main__":
    run_assistant()

