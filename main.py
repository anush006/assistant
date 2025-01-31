from huggingface_hub import InferenceClient
from elevenlabs import play
from elevenlabs.client import ElevenLabs

speak_client = ElevenLabs(api_key="sk_f6844abb8728b9950c19ade00376fe2e918b29a39603bb11")
model_client = InferenceClient(api_key="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")

def speak(text):
    audio = speak_client.generate(
        text=text,
        model="eleven_turbo_v2_5",
        voice="Chris"
    )
    play(audio)

prompt = ''

# while prompt!="bye":
#     prompt = input("Enter text: ")
#     speak(prompt)
    
while prompt!= "bye":

    prompt = input("\nPrompt: ")

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    try:
        completion = model_client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", 
            messages=messages, 
            max_tokens=500
        )

        print(completion.choices[0].message.content)
        # speak(completion.choices[0].message.content)

    except Exception as e:
        print(e)