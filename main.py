import speech_recognition as sr
import streamlit as st
def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."
def transcribe_voice():
    # Initialize recognizer class
    c = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = c.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            speech = c.recognize_google(audio_text)
            return speech
        except:
            return "Sorry, I did not get that."
def main():
    st.title("Speech Recognition App")
    api_options = ["Google Speech Recognition", "Vosk"]
    selected_api=st.selectbox("Select speech recognition API:", api_options)
    if selected_api == "Google Speech Recognition":
        st.button("Start Recording")
        text = transcribe_speech()
        st.write("Transcription: ", text)

        file_name = "transcribed_text.txt"
        with open(file_name, "w") as file:
            file.write(text)
    else:
        st.button("Start Recording")
        speech = transcribe_voice()
        st.write("Transcribed text:", speech)

        file_name = "transcribed_text.txt"
        with open(file_name, "w") as file:
            file.write(speech)

if __name__ == "__main__":
    main()