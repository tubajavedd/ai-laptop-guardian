import whisper
import sounddevice as sd


seconds=10
sample_rate=16000
sample=seconds*sample_rate

print("\nSPEAK NOW..\n")

audio=sd.rec(sample,samplerate=sample_rate,channels=1)
sd.wait()
audio=audio.flatten()

print("\n RECORDING FINISHES.\n")

model=whisper.load_model("base",download_root="./whisper_models")

print("\nTRANSCRIBING..\n")

result=model.transcribe(audio)

print("\n  YOU SAID : ", result["text"])
