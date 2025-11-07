# Install an external module and use it to perform an operation of your interest.

#  We will try pyttsx3 and use that.
# Import and Use the module.
import pyttsx3
engine = pyttsx3.init()

# Engine Commands
engine.say("I will speak this text")
engine.runAndWait()