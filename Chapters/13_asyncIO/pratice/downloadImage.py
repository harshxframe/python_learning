import asyncio
import threading
import time
import aiohttp

imageUrl = [
    "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg?cs=srgb&dl=pexels-christian-heitz-285904-842711.jpg",
    "https://static.vecteezy.com/system/resources/thumbnails/049/855/489/small_2x/nature-background-high-resolution-wallpaper-for-a-serene-and-stunning-view-free-photo.jpg",
    "https://c4.wallpaperflare.com/wallpaper/314/106/421/5bd0d3fa0d9e0-wallpaper-preview.jpg"
    ]


async def downloadImage(session, url):
    async with session.get(url) as response:

       imageFile = await response.read()
       file = open(f"./temp{str(time.time())}.jpg", "wb")
       file.write(imageFile)
       file.close()
       print("Image downloaded")


async def main():
    async with aiohttp.ClientSession() as session:
          tasks = [downloadImage(session,url) for url in imageUrl]
          await asyncio.gather(*tasks)


def asyncCall():
    asyncio.run(main())



print("Execution Started")
trd1 = threading.Thread(target=asyncCall)
trd1.start()



#Rest of the code, I don't want to block
print("Rest of the code is goingOn....")
