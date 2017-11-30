import vk_api,vk
import json
from gtts import gTTS #pip install gTTS
#попытка реализации функции отправки голосого сообщения
def send(txt):
   tts = gTTS(text=txt, lang='ru', slow=True)
   tts.save("voice.mp3")#сохранили
   #https://api.vk.com/method/docs.getUploadServer?access_token=your_token&type=audio_message&v=5.38
   #нужен импорт vkbotapi для доступа к апи и access tocken!
   #api.docs.getUploadServer()
   
   
   
