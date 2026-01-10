import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
# engine.say("Hii ,this is code by amit . here is your joke")
# engine.runAndWait()
print("Hii , this me , the ai made by amit , i am here to help you \nhow may i help you")
engine.say("Hii , this me ,the ai made by amit , i am here to help you ")
engine.runAndWait()
engine.say("how may i help you ")
engine.runAndWait()

# Initialize Recognizer
recognizer = sr.Recognizer()

while(True):
    # Use Microphone as Source
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture audio

    # Convert Speech to Text
    try:
        text = recognizer.recognize_google(audio)  # Use recognizer instance
        print("You said:", text)
        engine.say(f"you said {text}")
        engine.runAndWait()
        if(text.lower() == "terminate yourself"):
            print("Terminating...")
            engine.say("you asked me for termination , i am terminating my self , have a good day sir")
            engine.runAndWait()
            break
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        engine.say("Sorry, I couldn't understand what you said.")
        engine.runAndWait()
    except sr.RequestError:
        print("Error with the API request.")
