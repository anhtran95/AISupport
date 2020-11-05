import speech_recognition
import pyttsx3
from datetime import date, datetime

#Initialize
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
today = date.today()



#listening
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    audio = robot_ear.listen(mic)

print("Robot: ...")

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""

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
    #print("Date: " + formatted_date)
elif "time" in you:
    now = datetime.now()
    robot_brain = now.strftime("%H hours %M minutes %S seconds")
else:
    robot_brain = "That's great"

print(robot_brain)


#Speak
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

