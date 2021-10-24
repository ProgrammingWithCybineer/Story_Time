from IPython.display import clear_output
import time
import pyttsx3
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import sys
import random


a = 2
b = 0.2
c = 0.08
storytime = True

# Get players name
name = input("Please type your name...  ")
Temp = input("Pick a temperature: Hot or Cold:  ").lower()

# declaring options for random choices
places = ["Mountains","Swamp","Ocean", "Island"]
quests = ["Slay the monster", "Super hero", "Murder", "Treasure hunter"]
roles = ["Knight", "Captain", "Ninja", "Ordinary Person"]

# declaring variables for random choices
randomplace = random.choice(places)
randomquest = random.choice(quests)
randomrole = random.choice(roles)

story = "Once upon a time there was a " + randomrole + " named " + name + " who was on a quest to "
print(story)

# if Temp == "hot":
#     answer = input(" Please choose a color: Red, Yellow, Orange:  ").lower()
#     print(answer)


# elif Temp == "cold":
#     answer = input(" Pick a color: Blue, Black, Purple, Green:  ").lower()
#     print(answer)