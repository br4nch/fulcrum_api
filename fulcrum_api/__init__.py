import aiohttp
from typing import Optional

class FulcrumAPI():
  """
  A wrapper for the fulcrum API
  """
  def __init__(self):
    super().__init__()

  async def __do_request(
    self,
    endpoint: str,
    params: Optional[dict] = None
  ):
    """
    Make a request to the api
    """
    async with aiohttp.ClientSession() as cs:
      async with cs.get(
        f"https://api.fulcrum.lol/{endpoint}",
        params=params
      ) as r:
        if r.ok:
          return await r.json()
        return {
          "code": r.status,
          "message": (await r.json())['detail']
        }

  async def uwu(
    self,
    message: str
  ) -> str:
    """
    Uwuify a message

    Parameters
    ----------
    message: :class:`str`
    """
    data = await self.__do_request(
      "uwu",
      params={"message": message}
    )
    return data['message']

  async def tiktok_user(
    self,
    username: str
  ):
    """
    Get info about someone's tiktok profile

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "tiktok",
      params={"username": username}
    )
    return data

  async def ocr(
    self,
    url: str
  ):
    """
    Read text from the given image

    Parameters
    ----------
    url: :class:`str`
    """
    data = await self.__do_request(
      "ocr",
      params={"url": url}
    )
    return data

  async def weather(
    self,
    location: str
  ):
    """
    Get informations about a location weather

    Parameters
    ----------
    location: :class:`str`
    """
    data = await self.__do_request(
      "weather",
      params={"location": location}
    )
    return data

  async def images(
    self,
    query: str
  ):
    """
    Get images from the internet

    Parameters
    ----------
    query: :class:`str`
    """
    data = await self.__do_request(
      "images",
      params={"query": query, "safe": "True"}
    )
    return data

  async def cashapp(
    self,
    username: str
  ):
    """
    Get someone's cashapp profile

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "cashapp",
      params={"username": username}
    )
    return data

  async def twitter_user(
    self,
    username: str
  ):
    """
    Get info about someone's twitter profile

    Paratemers
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "twitter",
      params={"username": username}
    )
    return data

  async def roblox(
    self,
    username: str
  ):
    """
    Get info about someone's roblox profile

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "roblox",
      params={"username": username}
    )
    return data

  async def screenshot(
    self,
    url: str,
    wait: int = 1
  ):
    """
    Screenshot a website

    Parameters
    ----------
    url: :class:`str`
    wait: :class:`int`
    """
    data = await self.__do_request(
      "/screenshot",
      params={"url": url, "wait": wait}
    )
    return data

  async def snapchat(
    self,
    username: str
  ):
    """
    Get info about someone's snapchat profile

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "snapchat",
      params={"username": username}
    )
    return data

  async def snapchat_story(
    self,
    username: str
  ):
    """
    Get someone's snapchat stories

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "snapchat/story",
      params={"username": username}
    )
    return data
