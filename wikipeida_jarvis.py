"""
    Name: wikipedia_jarvis.py
    Author: Brock Bacon
"""

import wikipedia
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define voice recognition function
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None

# Define text-to-speech function
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Define method to retrieve information from Wikipedia
def get_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=3)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "Can you please clarify your question? You may be referring to one of the following: " + ", ".join(e.options)

# Loop to continuously prompt user for input
while True:
    # Prompt user for input
    speak_text("Please ask me a question or give me a command.")
    text = recognize_speech()

    # If user did not say anything, loop again
    if not text:
        continue

    # If user says "exit", terminate the program
    if "exit" in text.lower():
        speak_text("Goodbye.")
        break

    # If user says "search Wikipedia for", get information from Wikipedia
    if "search wikipedia for" in text.lower():
        query = text.lower().replace("search wikipedia for", "")
        result = get_wikipedia(query)
        speak_text(result)

    # If user says something else, ask for clarification
    else:
        speak_text("Sorry, I didn't understand. Please try again.")