import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1  
RATE = 44100  
CHUNK = 1024  
RECORD_SECONDS = 10  
OUTPUT_FILENAME = "output.wav"  

audio = pyaudio.PyAudio()

print("Recording...")

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

frames = []

