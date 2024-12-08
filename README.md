# Speech Recognition and Generative AI Voice Assistant

This project implements a voice-controlled AI assistant named **Jarvis**, designed to interact with users using natural language. The assistant responds to predefined commands and queries, and uses Google's Gemini AI for advanced conversational responses.

## Features

1. **Voice Recognition:**  
   - Recognizes user input via the microphone.
   - Supports fallback recognition using a `.wav` audio file.

2. **Voice Responses:**  
   - Converts text responses into speech using `pyttsx3`.

3. **Predefined Commands:**  
   - Provides the current time.
   - Tells jokes using the `pyjokes` library.
   - Fetches brief Wikipedia summaries.
   - Plays a simple "Rock, Paper, Scissors" game.

4. **Generative AI Integration:**  
   - Uses **Google Gemini AI** for handling custom queries.

5. **Exit Command:**  
   - Safely ends the program when the user says, "goodbye."

---

## Setup Instructions

### 1. Prerequisites

Ensure the following tools and libraries are installed:

- Python 3.8+
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `wikipedia`
  - `pyjokes`
  - `google-generativeai`

Install these libraries using the following command:
```bash
pip install speechrecognition pyttsx3 wikipedia pyjokes google-generativeai
```

### 2. PyAudio Installation (Optional)

For Windows, install PyAudio using a prebuilt wheel if the direct installation fails:
```bash
pip install pipwin
pipwin install pyaudio
```

For Linux or macOS, install via the system's package manager:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

---

### 3. API Configuration

1. Obtain your **Google Gemini API key** from the [Google Generative AI platform](https://cloud.google.com/vertex-ai).  
2. Replace the placeholder `API_KEY` in the following line of code:
   ```python
   genai.configure(api_key="API_KEY")
   ```

---

## Usage

1. Save the script as `jarvis.py`.
2. Run the program:
   ```bash
   python jarvis.py
   ```
3. Speak to the assistant using a microphone. Example commands:
   - "hello Jarvis"  
   - "what time is it"  
   - "give me a joke"  
   - "what is Python"  
   - "goodbye" (to exit)

---

## Troubleshooting

### 1. Speech Recognition Issues
- **Problem:** Microphone not detected.  
  **Solution:** Ensure your microphone is enabled and recognized by your system. Specify the correct `device_index` in the code:
  ```python
  microphone = sr.Microphone(device_index=1)
  ```

- **Problem:** Speech not recognized.  
  **Solution:** Speak clearly or use a fallback `.wav` file by placing it in the working directory as `path_to_audio.wav`.

### 2. API Errors
- **Problem:** Invalid or exceeded quota on Gemini AI.  
  **Solution:** Verify your API key and account quota on the [Google Cloud Console](https://console.cloud.google.com).

---

## Example Interactions

| User Command                  | Jarvis Response                               |
|-------------------------------|-----------------------------------------------|
| "hello Jarvis"                | "Hello Sir, what can I help you with?"        |
| "what time is it"             | "The time is 15:30, Sir!"                     |
| "give me a joke"              | "Why don’t skeletons fight each other? They don’t have the guts." |
| "what is Python"              | "Python is an interpreted, high-level programming language." |
| "goodbye"                     | "Talk to you later, Sir!"                     |

---

## License

This project is released under the MIT License. Use it freely and modify as needed.

---

For any issues or questions, feel free to contact the developer!
