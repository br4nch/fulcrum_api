import aiohttp
from typing import Optional

class FulcrumAPI():
  """
  Api wrapper for fulcrum api
  """
  def __init__(
    self,
    url: str = "https://api.fulcrum.lol"
  ):
    self.base_url = url

  async def __do_request(
    self,
    endpoint: str,
    method = "GET",
    params: Optional[dict] = None
  ):
    """
    Make a reqeuest to the api
    """
    async with aiohttp.ClientSession() as cs:
      async with cs.request(
        method,
        f"{self.base_url}{endpoint}",
        params=params
      ) as r:
        if r.ok:
          return await r.json()
        return {
          "code": r.status,
          "detail": (await r.json())['detail']
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
      "/uwu",
      params={"message": message}
    )
    return data['message']

  async def tiktok_user(
    self,
    username: str
  ):
    """
    Get someone's tiktok profile

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "/tiktok",
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
      "/ocr",
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
      "/weather",
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
      "/images",
      params={"query": query, "safe": "True"}
    )
    return data

  async def cashapp(
    self,
    name: str
  ):
    """
    Get someone's cashapp profile

    Parameters
    ----------
    name: :class:`str`
    """
    data = await self.__do_request(
      "/cashapp",
      params={"username": name}
    )
    return data

  async def twitter_user(
    self,
    username: str
  ):
    """
    Get someone's twitter profile

    Paratemers
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "/twitter",
      params={"username": username}
    )
    return data

  async def roblox(
    self,
    username: str
  ):
    """
    Get someone's roblox profile

    Parameters
    ----------
    username: :class:`str`
    """
    data = await self.__do_request(
      "/roblox",
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
