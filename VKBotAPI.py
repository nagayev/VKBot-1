import vk
from VKBotToken import *
session = vk.Session(access_token=token)
api = vk.API(session)  # Нужно для работы API VK
