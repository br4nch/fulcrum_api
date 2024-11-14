# fulcrum API
A python wrapper for fulcrum API

# Instalation
python required >=3.9.0

```sh
pip install -U git+https://github.com/br4nch/fulcrum_api
```

# Example
```py
import asyncio
from fulcrum_api import FulcrumAPI

api = FulcrumAPI()

async def get_instagram_user(username: str):
    return await api.instagram_user(username)

async def main():
    user = await get_instagram_user("cristiano")
    print(user)

asyncio.run(main())
```