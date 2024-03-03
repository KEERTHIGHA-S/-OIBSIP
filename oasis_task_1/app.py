import speech_recognition as sr
import datetime
import webbrowser
def greet_user():
    response = "Hello! I am your voice assistant. How can I help you?"
    print(response)

def get_date():
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    print(f"The current date is {date}")

def get_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"The current time is {time}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    greet_user()

    while True:
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)  # Add this line to print what was said

            if "hello" in text:
                greet_user()
            elif "date" in text:
                get_date()
            elif "time" in text:
                get_time()
            elif "search for" in text:
                query = text.split("search for")[1].strip()
                search_web(query)
            elif "exit" in text or "bye" in text:
                print("Goodbye!")
                break
            else:
                print("Sorry, I didn't catch that. Can you repeat?")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you repeat?")
if __name__ == "__main__":
    main()
