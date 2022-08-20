import discord
import googletrans
import os
from pprint import pprint


# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']
#int 整數
#float 浮點數 
#string 字串

client = discord.Client(intents=discord.Intents.default())
#test
# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        print(first,space, content)
        if content == '':# 如果用戶只@機器人 而不說話 content 內容為空
            content = first+"saysomething" #
            print(content)
            #await message.reply(content) 
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 

# Bot起動
client.run(TOKEN)
