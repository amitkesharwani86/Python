import pyttsx3
import pyjokes

#def jokes():
engine=pyttsx3.init()
engine.say("Hii ,this is code by amit . here is your joke")
engine.runAndWait()

joke=pyjokes.get_joke()
print(joke )
engine.say(joke )
engine.runAndWait()