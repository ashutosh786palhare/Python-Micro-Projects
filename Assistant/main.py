import tkinter as tk
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User: {query}")
            return query
        except Exception as e:
            print("Couldn't recognize the audio. Please try again.")
            return ""

def process_query():
    user_query = get_audio()
    # Perform NLP and actions based on user_query
    if user_query:
        response_label.config(text=user_query)
        speak(user_query)

# GUI Setup
root = tk.Tk()
root.title("Virtual Assistant by AP")

query_button = tk.Button(root, text="Speak", command=process_query)
query_button.pack()

response_label = tk.Label(root, text="")
response_label.pack()

root.mainloop()
