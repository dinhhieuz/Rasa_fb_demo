# %%
# Package from Google translate
from gtts import gTTS
# Operate system
import os
# Multi stream
import asyncio


async def remove_file(delay = 3, path = ''):
    # Delay task
    await asyncio.sleep(delay)
    # Remove file in system
    os.remove(path)

myText = 'Doanh thu tháng 5 trong ngày 03/05/2021: 3,000,000 Vnđ'

output = gTTS(text = myText, lang = 'vi', slow = False)
print(output.save("voice_text.mp4"))
# Open task multi stream 
loop = asyncio.get_event_loop()
loop.create_task(remove_file(delay=3, path='voice_text.mp4'))
print('Done')


# %%
