import telegram
from datetime import datetime
now = datetime.now()

bot = telegram.Bot(token='485029394:AAEMIt1L0HkolhN-wpQ8aWLJh3J7zT-sNFk')

#chat_id = bot.getUpdates()[-1].message.chat.id
chat_id = '516485771'
#try:
#    chat_id = bot.getUpdates()[-1].update_id

#except IndexError:
#    chat_id = 0

bot.sendMessage(chat_id=chat_id, text=str(now)+' Hello World')


