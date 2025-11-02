import pyttsx3
import speech_recognition as sr
import google.generativeai as genai

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text 
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Configure Google Generative AI
genai.configure(api_key="AIzaSyA8XrHtT456XWd_1E-OwakLNW8Y1cvMa5Q")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
model = genai.GenerativeModel(
    model_name="gemini-2.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Define conversation prompt
prompt = "1. If the question is technical, write answers in 2 to 3 lines which are understandable to us." \
         "2. If the question is a story, give a short story." \
         "3. If the question is creative, give creative answers." \
         "4. Give answers in paragraph format." \
         "5. If the question is a biography of a person, answer in short including all his events in short." \
         "6. Answer the questions in an efficient manner." \
         "7. Do not include asterisk in any of the answers."

# Start the conversation
while True:
    speech_text = recognize_speech()

    if speech_text:
        if "hello" in speech_text.lower():
            print("Hello! What can I do for you?")
            speak("Hello! What can I do for you?")
            convo = model.start_chat(history=[])
            while True:
                speech_text = recognize_speech()  # Listen to user's response
                if speech_text:
                    if speech_text.lower() == "exit":
                        print("Exiting conversation...")
                        speak("Goodbye! Have a nice day")
                        break
                    else:
                        # Concatenate user's input with the requirement prompt
                        prompt = prompt + " " + speech_text
                        convo.send_message(prompt)
                        response = convo.last.text
                        print("Response:", response)
                        speak(response)
                else:
                    print("No speech detected.")
            break
        elif speech_text.lower() == "exit":
            print("Exiting conversation...")
            speak("Goodbye!")
            break
        else:
            print("Please say 'hello' to start the conversation.")
    else:
        print("No speech detected.")

