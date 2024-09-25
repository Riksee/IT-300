import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write

freq = 48100
dur = 10

recording = sd.rec(int(dur * freq), samplerate= freq, channels = 2)

sd.wait()

wv.write("Rec1.wav", recording, freq, sampwidth=2)
write("Rec3.wav", freq, recording)