import speech_recognition
import pyttsx3
import os
import webbrowser
from datetime import date, datetime

#Initialize
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
today = date.today()
url = 'https://www.google.com/'



#listening
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    audio = robot_ear.listen(mic)

print("Robot: ...")

try:
    you = robot_ear.recognize_google(audio)
    you = you.lower()
except:
    you = "Unable to pick up audio"


print("You: " + you)

#Interpretation of speech
if you == "":
    robot_brain = "I can't understand you"
elif "hello" in you:
    robot_brain = "Hello Anh"
elif "today" in you:
    # Get date formatted: month, day and year
    today = date.today()
    robot_brain = today.strftime("%B %d, %Y")
elif "time" in you:
    now = datetime.now()
    robot_brain = now.strftime("%H hours %M minutes %S seconds")
elif "sleep" in you:
    print("Computer going to sleep mode...")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
elif "chrome" in you:
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    print(chrome_path)
    webbrowser.get(chrome_path).open(url)
elif "mute" in you:
    print("Mute, yet to implement")
else:
    robot_brain = "That's great"

print(robot_brain)


#Speak
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

