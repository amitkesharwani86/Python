import speech_recognition as sr

# Initialize Recognizer
recognizer = sr.Recognizer()

# Use Microphone as Source
with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    audio = recognizer.listen(source)  # Capture audio

# Convert Speech to Text
try:
    text = recognizer.recognize_google(audio)  # Use recognizer instance
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
except sr.RequestError:
    print("Error with the API request.")
