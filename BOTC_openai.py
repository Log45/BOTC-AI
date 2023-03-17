import openai
import sounddevice as sd
from scipy.io.wavfile import write

def record_question():
    fs = 44100  # Sample rate
    seconds = int(input("How long do you want to ask your question? (In seconds): ").strip())  # Duration of recording
    print("Beginning Recording...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    # We could create a global time limit for recording time and use sd.stop() in order to make a recording shorter than the time limit (it will be inputted by a user probably through a button press).
    sd.wait()  # Wait until recording is finished
    print("Ending Recording...")
    write('output.wav', fs, myrecording)  # Save as WAV file 

def player_input_type():
    # This should eventually be changed to work with buttons rather than plaintext input
    itype = input("How will you be asking your question? ('t' for text, 'a' for audio): ")
    if itype.lower() == "t":
        return "text"
    elif itype.lower() == "a":
        return "audio"
    else:
        return None

def player_question():
    itype = player_input_type()
    if itype == "audio":
        record_question()
        f = open("output.wav", "rb")
        return openai.Audio.transcribe("whisper-1", f)["text"]
    elif itype == "text":
        return input("Enter your question: ")
    else:
        return None
    
def main():
    openai.api_key = input("Enter openai key: ")
    print(player_question())

if __name__ == "__main__":
    main()