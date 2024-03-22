import speech_recognition as sr
import streamlit as st
import parselmouth
import sounddevice as sd
import numpy as np
from parselmouth.praat import call

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
    def record_audio(duration=5, fs=44100):
        st.info("Speak now...")
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
        sd.wait()  # Wait until recording is finished
        return audio_data.flatten(), fs
        st.info("Transcribing...")
    def transcribe_audio(audio_data, sampling_frequency):
            snd = parselmouth.Sound(audio_data, sampling_frequency=sampling_frequency)
            waveform = snd.values.T[0]

            # Perform speech recognition
            speech = call(waveform, sampling_frequency, "To TextGrid (silences)", "praat")
            return speech
def main():
    st.title("Speech Recognition App")
    api_options = ["Google Speech Recognition", "Parselmouth"]
    selected_api=st.selectbox("Select speech recognition API:", api_options)
    if selected_api == "Google Speech Recognition":
        st.button("Start Recording")
        text = transcribe_speech()
        st.write("Transcription: ", text)
    else:
        st.button("Start Recording")
        speech = transcribe_voice()
        st.write("Transcribed text:", speech)

if __name__ == "__main__":
    main()