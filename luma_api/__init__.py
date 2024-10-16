import aiohttp
from typing import Optional

class LumaAPI():
  """
  Api wrapper for luma api
  """
  def __init__(
    self,
    key: str,
    url: str = "https://api.fulcrum.lol"
  ):
    self.apikey = key
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
          if r.content_type == "application/json":
            return await r.json()
          else:
            return await r.read()
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

  async def instagram_user(
    self,
    username: str
  ):
    """
    Get a user's instagram info

    Parameters
    ----------
    username: :class:`str`
      Instagram account username
    """
    data = await self.__do_request(
      "/instagram",
      params={"username": username}
    )
    return data

  async def tiktok_user(
    self,
    username: str
  ):
    """
    Get a user's tiktok profile

    Parameters
    ----------
    username: :class:`str`
      Tiktok account name
    """
    data = await self.__do_request(
      "/tiktok",
      params={"username": username}
    )
    return data
