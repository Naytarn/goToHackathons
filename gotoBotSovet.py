import telebot
import requests, json
import pymorphy2
import random

morph = pymorphy2.MorphAnalyzer()

domain = 'anekidot'
count = 75
token = 'f18bd2f5f18bd2f5f18bd2f5d2f1e7bc34ff18bf18bd2f5acd6839696b93b08c8cef272'
v=5.211
url = "https://api.vk.com/method/wall.get?domain={}&count={}&access_token={}&v=5.74".format(domain, count, token)
veroyatnost = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

response = requests.get(url)
answer = json.loads(response.text)
print(answer)
with open('memes.txt', 'w', encoding='utf-8')as file:
    for post in answer['response']['items']:
        file.write(post['text'] + '\n\n\n'.lower())
token = '1397971713:AAGsI-sz9v8uLWKtttQgwwPr4tkWUyA1EIA'
bot = telebot.TeleBot(token=token)

roct_words = ['О, у меня есть классный анекдот на эту тему!', 'Вспомнил шутку!', 'Ха-ха, что придумал!', 'Вы все сейчас упадете со смеха', 'Тут должна быть шутка', 'Эта шутка будет посмешнее чем "колобок повесился"']

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    bot.send_message(user_id, 'всем привет, я бот рост. мой создатель - бородин рост. вы можете подумать что это проект розочек-цветочков,но это не так. у них ничего не ботает, а я ботаю))')
    print('started')

@bot.message_handler(content_types=['text'])
def save(message):
    print("got message")
    vozmozhno = []
    user_id = message.chat.id
    joined = ''
    jo = ' '
    res = 0
    theMessage = message.text.replace(',', '').lower()
    theMessage = theMessage.replace('!', '')
    theMessage = theMessage.replace('?', '')
    theMessage = theMessage.replace('.', '')
    theMessage = theMessage.replace(':', '')
    theMessage = theMessage.replace('-', '')
    theMessage = theMessage.replace('(', '')
    theMessage = theMessage.replace(')', '')
    theMessage = theMessage.replace('*', '')
    theMessage = theMessage.replace("'", '')
    theMessage = theMessage.replace('"', '')
    theMessage = theMessage.split(' ')
    print(theMessage, '=theMessage')
    with open('memes.txt', 'r', encoding='utf-8') as fle:
        allMemes = fle.read()
        memesOtdelno = allMemes.split('\n\n\n')
        result = None
        for i in theMessage:
            indexx = theMessage.index(i)
            while res == 0:
                joined = jo.join([theMessage[indexx], theMessage[indexx+1]])
                print(memesOtdelno)
                for j in memesOtdelno:
                    print('joke', j)
                    res = j.find(joined)
                    if res != -1:
                        result = j
        if result:
            howChasto = random.choice(veroyatnost)
            print(howChasto)
            if howChasto == 1:
                bot.send_message(user_id, result)

bot.polling(none_stop=True)