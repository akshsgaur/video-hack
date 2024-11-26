import asyncio
from simli import SimliClient, SimliConfig
from simli.renderers import FileRenderer
async def main():
    connection =  SimliClient(
        SimliConfig(
            apiKey="0svhul6ckcep0jhse79xh",  # API Key
            faceId="YOUR_FACE_ID",  # Face ID
            maxSessionLength=20,
            maxIdleTime=10,
        )
    )
    await connection.Initialize()
    await connection.sendSilence(1)  # to send 1 second of silence to the API
    await connection.send(audio)  # where audio is a bytes object representing the raw audio data


asyncio.run(main())

