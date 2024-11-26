import asyncio
from simli import SimliClient, SimliConfig
import simpleaudio as sa
import os
from utils.constants import simli_api

current_dir = os.path.dirname(os.path.abspath(__file__))


with open("sonic.raw","rb") as f:
    audio = f.read()
from simli.renderers import FileRenderer

import asyncio
from simli import SimliClient, SimliConfig
from simli.renderers import FileRenderer
async def main():
    async with SimliClient(
        SimliConfig(
            apiKey=simli_api,  # API Key
            faceId="5514e24d-6086-46a3-ace4-6a7264e5cb7c",  # Face ID
            maxSessionLength=20,
            maxIdleTime=10,
        )
    ) as connection:
        await connection.send(audio) # Audio is the raw PCM16 16khz mono audio data
        await FileRenderer(connection).render() # Write the output to an output.mp4 file

asyncio.run(main())