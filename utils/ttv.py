import os
from utils.constants import simli_api
from utils.constants import cartesian_api
from cartesia import Cartesia
import asyncio
from simli import SimliClient, SimliConfig
from simli.renderers import FileRenderer

current_dir = os.path.dirname(os.path.abspath(__file__))


class Pipeline:
    def tts(self,text=None):
        client = Cartesia(api_key=cartesian_api)
        data = client.tts.bytes(
            model_id="sonic-english",
            transcript=text,
            voice_id="a0e99841-438c-4a64-b679-ae501e7d6091",  # Barbershop Man
            # You can find the supported `output_format`s at https://docs.cartesia.ai/api-reference/tts/bytes
            output_format={
                "container": "raw",
                "encoding": "pcm_s16le",
                "sample_rate": 16000,
            },
        )
        # print(data)
        with open("sonic.raw", "wb") as f:
            f.write(data)
            return f.name


    def stv(self,audio=None):
        with open("sonic.raw", "rb") as f:
            audio = f.read()


        async def main():
            async with SimliClient(
                    SimliConfig(
                        apiKey=simli_api,  # API Key
                        faceId="5514e24d-6086-46a3-ace4-6a7264e5cb7c",  # Face ID
                        maxSessionLength=10,
                        maxIdleTime=5,
                    )
            ) as connection:
                await connection.send(audio)  # Audio is the raw PCM16 16khz mono audio data
                await FileRenderer(connection).render()  # Write the output to an output.mp4 file

        asyncio.run(main())

    def run(self,text=None):
        self.stv(audio=self.tts(text))


if __name__ == "__main__":
    text = """
    Hello Akshit,
    Today is great day for INNOVATION!
    LEARN TOGETHER AND MAKE GOOD FOR WORLD!
    """

    Pipeline().run(text)

