import tkinter as tk
import asyncio
import edge_tts
import sounddevice as sd
import soundfile as sf

OUTPUT_FILE = "speech.mp3"
selected_voice = "en-US-GuyNeural"
#Choices for voice
voices = {
    "Guy": "en-US-GuyNeural",
    "Nanami": "ja-JP-NanamiNeural",
    "Soft": "en-US-AriaNeural",
    "High": "en-US-DavisNeural"
}
#Function
async def generate_speech(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(OUTPUT_FILE)

    data, samplerate = sf.read(OUTPUT_FILE)
    sd.play(data, samplerate)
    sd.wait()

def speak():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        asyncio.run(generate_speech(text, selected_voice))

def clear_text():
    text_box.delete("1.0", tk.END)

def set_voice(v):
    global selected_voice
    selected_voice = v
    voice_label.config(text=f"Voice: {v}")
#Window Layout and function buttons
window = tk.Tk()
window.title("Text To Speech")
window.geometry("460x360")

title = tk.Label(window, text="Text-to-Speech", font=("Arial", 18))
title.pack(pady=10)

voice_label = tk.Label(window, text="Voice: en-US-GuyNeural")
voice_label.pack(pady=5)

voice_frame = tk.Frame(window)
voice_frame.pack()

for name, voice in voices.items():
    btn = tk.Button(
        voice_frame,
        text=name,
        width=8,
        height=2,
        command=lambda v=voice: set_voice(v)
    )
    btn.pack(side=tk.LEFT, padx=5)

text_box = tk.Text(
    window,
    height=3,
    width=40,
    font=("Segoe UI", 13),
    padx=10,
    pady=10
)
text_box.pack(pady=15)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

speak_btn = tk.Button(button_frame, text="Speak", width=14, height=2, command=speak)
speak_btn.pack(side=tk.LEFT, padx=15)

clear_btn = tk.Button(button_frame, text="Clear", width=14, height=2, command=clear_text)
clear_btn.pack(side=tk.LEFT, padx=15)

window.mainloop()