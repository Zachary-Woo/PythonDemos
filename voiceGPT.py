import openai
import pyttsx3
import speech_recognition as sr


def transcribe_audio_to_text(filename):
    """Transcribe audio from the given file using Google Speech Recognition"""
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception:
        print('Skipping unknown error')


def generate_response(prompt):
    """Generate a response using the OpenAI API"""
    openai.api_key = "***** OpenAI_API_KEY *****"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return response["choices"][0]["text"]


def speak_text(text):
    """Speak the given text using a text-to-speech engine"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    print("Say 'Question' to start recording your question")
    recognizer = sr.Recognizer()

    while True:
        try:
            # Wait for user to say "question"
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                transcription = recognizer.recognize_google(audio)

                if transcription.lower() == "question":
                    # Record and transcribe the user's question
                    print("Say your question...")
                    with sr.Microphone() as source:
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        filename = "input.wav"
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)

                    if text:
                        print(f"You said: {text}")

                        # Generate and speak the response using ChatGPT
                        response = generate_response(text)
                        print(f"ChatGPT says: {response}")
                        speak_text(response)

        except KeyboardInterrupt:
            print("\nStopping the program...")
            break
        except Exception as e:
            print("An error has occurred: {}".format(e))


if __name__ == "__main__":
    main()
