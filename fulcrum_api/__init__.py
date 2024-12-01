import aiohttp
from typing import (
  Optional,
  Dict,
  Any
)

class FulcrumAPI():
  """
  Fulcrum API Wrapper

  -------------------
  A wrapper for the Fulcrum API
  """
  def __init__(self: "FulcrumAPI"):
    super().__init__()

  async def __do_request(self, endpoint: str, params: Optional[dict] = None):
    """
    Make a request to the given endpoint
    """
    async with aiohttp.ClientSession() as cs:
      async with cs.get(f"https://api.fulcrum.lol/{endpoint}", params=params) as r:
        if r.status == 200:
          if r.content_type == "application/json":
            return await r.json()
          elif r.content_type == "text/html":
            return await r.text()
        else:
          return {
            "error code": r.status,
            "message": (await r.json())["detail"]
          }

  async def uwu(self, message: str) -> str:
    """
    Uwuify a message

    Parameters
    ----------
    message: :class:`str`
      The message that should be uwuified
    """
    data = await self.__do_request("uwu", params={"message": message})
    return data['message']
  
  async def instagram_user(self, username: str) -> Dict[str, Any]:
    """
    Get someones instagram account statistics

    Parameters
    ----------
    username: :class:`str`
      The instagram account username
    """
    data = await self.__do_request("instagram", params={"username": username})
    return data
  
  async def instagram_story(self, username: str) -> Dict[str, Any]:
    """
    Get someones instagram account stories (if they have any)

    Parameters
    ----------
    username: :class:`str`
      The instagram account username
    """
    data = await self.__do_request("instagram/story", params={"username": username})
    return data

  async def instagram_highlights(self, username: str) -> Dict[str, Any]:
    """
    Get someones instagram account highlights (if they have any)

    Parameters
    ----------
    username: :class:`str`
      The instagram account username
    """
    data = await self.__do_request("instagram/highlights", params={"username": username})
    return data

  async def tiktok_user(self, username: str) -> Dict[str, Any]:
    """
    Get info about someone's tiktok profile

    Parameters
    ----------
    username: :class:`str`
      The username of the tiktok profile
    """
    data = await self.__do_request("tiktok", params={"username": username})
    return data

  async def ocr(self, url: str) -> Dict[str, Any]:
    """
    Scan the image for text and return it

    Parameters
    ----------
    url: :class:`str`
      The url of the image it should search for text in
    """
    data = await self.__do_request("ocr", params={"url": url})
    return data

  async def weather(self, location: str) -> Dict[str, Any]:
    """
    Get information about the weather from a location

    Parameters
    ----------
    location: :class:`str`
      The location where it should get the weather info
    """
    data = await self.__do_request("weather", params={"location": location})
    return data

  async def images(self, query: str, safe: bool) -> Dict[str, Any]:
    """
    Return a list of images for the given query

    Parameters
    ----------
    query: :class:`str`
      The query to use when searching for images
    """
    data = await self.__do_request("images", params={"query": query, "safe": str(safe)})
    return data

  async def cashapp(self, username: str) -> Dict[str, Any]:
    """
    Get information about someone cashapp

    Parameters
    ----------
    username: :class:`str`
      The cashapp account username
    """
    data = await self.__do_request("cashapp", params={"username": username})
    return data

  async def twitter_user(self, username: str) -> Dict[str, Any]:
    """
    Get information about a twitter profile (also known as X)

    Paratemers
    ----------
    username: :class:`str`
      The twitter profile username
    """
    data = await self.__do_request("twitter", params={"username": username})
    return data

  async def roblox_user(self, username: str) -> Dict[str, Any]:
    """
    Get information and statistics of a roblox user

    Parameters
    ----------
    username: :class:`str`
      The user username
    """
    data = await self.__do_request("roblox", params={"username": username})
    return data

  async def screenshot(self, url: str, wait: int = 1) -> Dict[str, Any]:
    """
    Get a preview of a website

    Parameters
    ----------
    url: :class:`str`
      The website url
    wait: :class:`int`
      The time to wait before taking the screenshot
    """
    data = await self.__do_request("screenshot", params={"url": url, "wait": wait})
    return data

  async def snapchat(self, username: str) -> Dict[str, Any]:
    """
    Get a snapchat user profile

    Parameters
    ----------
    username: :class:`str`
      The snapchat username of the snapchat user
    """
    data = await self.__do_request("snapchat", params={"username": username})
    return data

  async def snapchat_story(self, username: str):
    """
    Get a snapchat user stories (if they have any)

    Parameters
    ----------
    username: :class:`str`
      The snapchat username of the user
    """
    data = await self.__do_request("snapchat/story", params={"username": username})
    return data

  async def lyrics(self, song: str) -> Dict[str, Any]:
    """
    Get the lyrics with some additional info from a song

    Parameters
    ----------
    song: :class:`str`
      The song name to fetch info
    """
    data = await self.__do_request("lyrics", params={"song": song})
    return data

  async def dominant(self, url: str) -> Dict[str, Any]:
    """
    Get the rgb, hex and name of the dominant color from an image

    Parameters
    ----------
    url: :class:`str`
      The url of the image
    """
    data = await self.__do_request("dominant", params={"url": url})
    return data
