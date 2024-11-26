import os
import subprocess
from cartesia import Cartesia
import simpleaudio as sa
import os
from utils.constants import cartesian_api

# Access the keys
current_dir = os.path.dirname(os.path.abspath(__file__))

client = Cartesia(api_key=cartesian_api)


data = client.tts.bytes(
    model_id="sonic-english",
    transcript="""Create a new project with Cursor, Replit or your favorite tool

​Design a character with FLUX or your favorite image model

​Add a personality with the world's fastest LLMs

​Connect a custom voice with Cartesia's 95ms Sonic TTS API

​Bring your avatar to life with Simli's 300ms Avatar API""",
    voice_id="a0e99841-438c-4a64-b679-ae501e7d6091",  # Barbershop Man
    # You can find the supported `output_format`s at https://docs.cartesia.ai/api-reference/tts/bytes
    output_format={
        "container": "raw",
        "encoding": "pcm_s16le",
        "sample_rate": 16000,
    },
)

#print(data)
with open("sonic.raw", "wb") as f:
    f.write(data)
