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
          "status_code": r.status,
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
      Convert a message to uwu
    """
    data = await self.__do_request(
      "/uwu",
      params={"message": message}
    )
    return data['message']

  """async def instagram_user(
    self,
    username: str
  ):
    "
    Get a user's instagram info

    Parameters
    ----------
    username: :class:`str`
      Instagram account username
    "
    data = await self.__do_request(
      "/instagram",
      params={"username": username}
    )
    return data"""

  async def tiktok_user(
    self,
    username: str
  ):
    """
    Get someone's tiktok profile

    Parameters
    ----------
    username: :class:`str`
      tiktok account name
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
      image link
    """
    data = await self.__do_request(
      "/ocr",
      params={"url": url}
    )
    return data
