# Install necessary packages in Colab
!pip install pyttsx3==2.90 wikipedia SpeechRecognition pyaudio

import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import warnings

# Disable speech and microphone features not supported in Colab
warnings.filterwarnings("ignore")

# Initialize text-to-speech (NOTE: Won't play audio in Colab, so replaced with print)
def speak(text):
    print("JARVIS:", text)
    # engine.say(text)
    # engine.runAndWait()

# Send email (won’t actually work in Colab; simulating)
def sendEmail(to, content):
    print(f"Simulating sending email to {to} with content:\n{content}")
    # Actual code (disabled)
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login('your_email', 'your_password')
    # server.sendmail('your_email', to, content)
    # server.close()

MASTER = "ANUJ"

speak("Initializing JARVIS...")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning " + MASTER)
    elif hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)
    speak("I am JARVIS. How may I help you?")

# Simulate taking a command
def takeCommand():
    # In Colab, we simulate input instead of using a mic
    return input("Type your command here (simulate voice): ")

# Start interaction
wishMe()
query = takeCommand().lower()

if 'wikipedia' in query:
    speak("Searching Wikipedia...")
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif 'open youtube' in query:
    speak("Opening YouTube")
    webbrowser.open('https://www.youtube.com/')
elif 'open google' in query:
    speak("Opening Google")
    webbrowser.open('https://www.google.com/')
elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER}, the time is {strTime}")
elif 'email to' in query:
    try:
        speak("What should I send?")
        content = takeCommand()
        to = 'receiver@example.com'
        sendEmail(to, content)
        speak("Email sent successfully.")
    except Exception as e:
        speak("Sorry, I am not able to send this email.")
        print(e)
else:
    speak("Sorry, I didn't understand that command.")
