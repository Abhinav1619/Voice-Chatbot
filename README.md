# Voice-Chatbot

# 🎙️ Voice-Based AI Assistant (Gemini + Speech Recognition)

This project is a **voice-controlled AI assistant** built with Python. It listens to your speech, processes your query using **Google’s Gemini Generative AI**, and responds with both **spoken** and **textual** answers. The assistant can handle technical, creative, story-based, and biographical questions intelligently.

---

## 🚀 Features

* 🎧 **Speech Recognition** using `SpeechRecognition` and your system microphone
* 🗣️ **Text-to-Speech (TTS)** responses via `pyttsx3`
* 🧠 **AI-powered responses** from **Google Gemini 2.5 Pro**
* 💬 **Interactive conversation loop**
* ⚙️ **Custom prompt logic** for handling different types of queries efficiently
* 🛡️ Built-in **safety and content filtering**

---

## 🛠️ Technologies Used

* **Python 3.x**
* [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
* [`pyttsx3`](https://pypi.org/project/pyttsx3/)
* [`google-generativeai`](https://pypi.org/project/google-generativeai/)

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/voice-ai-assistant.git
   cd voice-ai-assistant
   ```

2. **Install dependencies:**

   ```bash
   pip install pyttsx3 SpeechRecognition google-generativeai
   ```

3. **Set up your Gemini API key:**
   Open the script and replace the line:

   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

   with your actual Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

4. **Ensure your microphone works properly.**

---

## ▶️ Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Say **“Hello”** to start the conversation.

3. Speak your query when prompted.

   * Example questions:

     * “Explain what is an API.”
     * “Tell me a short story about a dragon.”
     * “Who is Elon Musk?”
     * “Write something creative about space.”

4. Say **“Exit”** anytime to stop the assistant.

---

## 🧩 Example Interaction

```
Please speak...
You said: hello
Hello! What can I do for you?

Please speak...
You said: tell me a story about a brave knight
Response: Once upon a time, a brave knight ventured into the dark woods...
```

---

## ⚠️ Notes

* Make sure your microphone permissions are enabled.
* This assistant currently runs in the console — you can extend it with a GUI using `tkinter` or `PyQt`.
* Responses depend on your internet connection and Gemini API availability.

---

## 🧑‍💻 Author

**Abhinav Medasani**
[LinkedIn](https://www.linkedin.com/in/abhinav-medasani-18a032300) • [GitHub](https://github.com/Abhinav1619)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share it.

---

## 🌟 Future Improvements

* Add a **graphical interface**
* Enable **multi-language support**
* Integrate **memory** for context-aware conversations
* Add **hotword activation** (like “Hey AI”)

---

**Enjoy your AI-powered voice assistant!**
