# ---------------- IMPORT LIBRARIES ---------------- #

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests

# ---------------- TEXT TO SPEECH ---------------- #

engine = pyttsx3.init()

def speak(text):

    print("Assistant:", text)

    engine.say(text)

    engine.runAndWait()

# ---------------- SPEECH RECOGNITION ---------------- #

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:

        speak("Sorry, I could not understand.")

        return ""

    except sr.RequestError:

        speak("Network error.")

        return ""

# ---------------- WEATHER FUNCTION ---------------- #

def get_weather(city):

    api_key = "YOUR_OPENWEATHER_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:

        response = requests.get(url)

        data = response.json()

        temperature = data["main"]["temp"]

        weather = data["weather"][0]["description"]

        speak(
            f"The temperature in {city} is {temperature} degree Celsius with {weather}"
        )

    except:

        speak("Unable to fetch weather details.")

# ---------------- COMMAND FUNCTION ---------------- #

def execute_command(command):

    # Greeting
    if "hello" in command:

        speak("Hello, how can I help you?")

    # Time
    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

    # Open Google
    elif "open google" in command:

        webbrowser.open("https://www.google.com")

        speak("Opening Google")

    # Open YouTube
    elif "open youtube" in command:

        webbrowser.open("https://www.youtube.com")

        speak("Opening YouTube")

    # Weather
    elif "weather" in command:

        speak("Please say the city name")

        city = listen()

        get_weather(city)

    # Search
    elif "search" in command:

        search_query = command.replace("search", "")

        webbrowser.open(
            f"https://www.google.com/search?q={search_query}"
        )

        speak(f"Searching for {search_query}")

    # Exit
    elif "exit" in command or "stop" in command:

        speak("Goodbye!")

        return False

    else:

        speak("Sorry, I don't know that command.")

    return True

# ---------------- MAIN PROGRAM ---------------- #

speak("Voice Assistant Started")

running = True

while running:

    command = listen()

    if command:

        running = execute_command(command)