import os.path

from typing import List, Optional


API_ID: int = "18025020"
API_HASH: str = "8fde3ef8961c892c8f3455de6d9327e9"
TOKEN: str = "5624471850:AAFtWV9n7VMKewlYOuRcZIfVrxrm0b7Tn_g"

log_chat: int = -1001879129251
sudoers: List[int] = [5518263253, 5518263253]
super_sudoers: List[int] = [5518263253, 5518263253]

prefix: List[str] = ["/", "!", ".", "$", "-"]

disabled_plugins: List[str] = []

WORKERS = 24

DATABASE_PATH = os.path.join("eduu", "database", "eduu.db")

TENOR_API_KEY: Optional[str] = "X9HD35B7ZGP6"

sudoers.extend(super_sudoers)

# notes

# 1. api_id & api_hash get from my.telegram.org
# 2. token fill with your bot_token get from @BotFather
# 3. log_chat fill with the chat id of a group that you should create for the bot logger
# 4. [optional] var disabled_plugins let you to disable an plugin to be loaded. Example:
# You don't want the youtube plugin to be loaded, then fill disabled_plugins var with youtube (or any name of the plugins file)
