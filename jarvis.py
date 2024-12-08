import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import pyjokes
import google.generativeai as genai

# Set Gemini API key
genai.configure(api_key="API_KEY")  # Replace with your actual API key

def get_response(input):
    if input == "let's fly RPS game":
        return "Let's go! Choose one: rock, paper, or scissors."

    elif input == "hello Jarvis" or input == "hey Jarvis":
        return "Hello Sir, what can I help you with?"

    elif input == "what the time is it" or input == "what time is it":
        d = datetime.datetime.now()
        hour = d.hour
        minute = d.minute
        return f"The time is {hour}:{minute}, Sir!"

    elif input == "give me a joke" or input == "give me a joke":
        return pyjokes.get_joke()

    elif input.startswith("what is "):
        person = input.replace('what is ', '')
        info = wikipedia.summary(person, sentences=1)
        return str(info)

    elif input == "goodbye":
        return "Talk to you later, Sir!"

    else:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input)
        return response.text


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        microphone = sr.Microphone(device_index=1)
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        print("Recognizing...")
        result = recognizer.recognize_google(audio)
        return result

    except AttributeError:
        print("PyAudio not installed. Falling back to audio file recognition.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Recognition request failed: ", str(e))

    try:
        print("Using fallback method with 'path_to_audio.wav'...")
        with sr.AudioFile("path_to_audio.wav") as source:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)
    except Exception as fallback_error:
        print(f"Fallback also failed: {fallback_error}")

    return None

while True:
    input_text = recognize_speech()
    if input_text:
        print(f"You said: {input_text}")
        response = get_response(input_text)
        print(f"Jarvis: {response}")
        speak(response)
        if input_text == "goodbye":
            break