from huggingface_hub import InferenceClient
from elevenlabs import play
from elevenlabs.client import ElevenLabs

speak_client = ElevenLabs(api_key="sk_f6844abb8728b9950c19ade00376fe2e918b29a39603bb11")
model_client = InferenceClient(api_key="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")
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def speak(text):
    # audio = speak_client.generate(
    #     text=text,
    #     model="eleven_turbo_v2_5",
    #     voice="Chris"
    # )
    # play(audio)

    wav = tts.tts(text=text, speaker_wav="my/cloning/audio.wav", language="en")
    print(wav)

prompt = ''

while prompt!="bye":
    prompt = input("ENter text: ")
    speak(prompt)
# while prompt!= "bye":

#     prompt = input("\nPrompt: ")

#     messages = [
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
#     try:
#         completion = model_client.chat.completions.create(
#             model="microsoft/Phi-3.5-mini-instruct", 
#             messages=messages, 
#             max_tokens=500
#         )

#         print(completion.choices[0].message.content)
#         speak(completion.choices[0].message.content)

#     except Exception as e:
#         print(e)