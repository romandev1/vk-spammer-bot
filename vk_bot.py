import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
import random

vk_session = vk_api.VkApi(token="# токен")

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "# id группы (без 'club')")

memes = ["Привет", "Здравствуйте", "Как дела?"]
codes = [1029, 4887, 9935, 2939, 4485]
code = 0

def delcodes():
    if code == codes[0]:
        print("\nвызван " + id + ", " + str(num_call) + " раз, с интервалом " + str(interval) + " сек")
        print("код использован: " + str(codes[0]))
        codes[0] = random.randint(10000, 15000)
        print("Новый код:", codes[0])
        print(codes)
    if code == codes[1]:
        print("\nвызван " + id + ", " + str(num_call) + " раз, с интервалом " + str(interval) + " сек")
        print("код использован: " + str(codes[1]))
        codes[1] = random.randint(10000, 15000)
        print("Новый код:", codes[1])
        print(codes)
    if code == codes[2]:
        print("\nвызван " + id + ", " + str(num_call) + " раз, с интервалом " + str(interval) + " сек")
        print("код использован: " + str(codes[2]))
        codes[2] = random.randint(10000, 15000)
        print("Новый код:", codes[2])
        print(codes)
    if code == codes[3]:
        print("\nвызван " + id + ", " + str(num_call) + " раз, с интервалом " + str(interval) + " сек")
        print("код использован: " + str(codes[3]))
        codes[3] = random.randint(10000, 15000)
        print("Новый код:", codes[3])
        print(codes)
    if code == codes[4]:
        print("\nвызван " + id + ", " + str(num_call) + " раз, с интервалом " + str(interval) + " сек")
        print("код использован: " + str(codes[4]))
        codes[4] = random.randint(10000, 15000)
        print("Новый код:", codes[4])
        print(codes)

def call():
    delcodes()
    xcall = 0
    while xcall < num_call:
        if len(event.obj.text.split(' ')) == 6:
            vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message='@' + id + ', ' + u_mes)
        else:
            vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message='@' + id + ', ' + random.choice(memes))
        time.sleep(interval)
        xcall+=1

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        if event.obj.text.split(" ")[0] == "/call" and len(event.obj.text.split(' ')) > 2 and event.from_chat:
            id = event.obj.text.split(" ")[1]

            if len(event.obj.text.split(' ')) == 5:
                num_call = int(event.obj.text.split(" ")[2])
                interval = int(event.obj.text.split(" ")[3])
                code = int(event.obj.text.split(" ")[4])
            elif len(event.obj.text.split(' ')) == 6:
                num_call = int(event.obj.text.split(" ")[2])
                interval = int(event.obj.text.split(" ")[3])
                code = int(event.obj.text.split(" ")[4])
                u_mes = (event.obj.text.split(" ")[5])

            if len(event.obj.text.split(' ')) == 3:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Не введен интервал.")

            elif len(event.obj.text.split(' ')) == 4:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Не введен пароль.")

            elif len(event.obj.text.split(' ')) == 5 and not code in codes or len(event.obj.text.split(' ')) == 6 and not code in codes:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Вам нельзя использовать /call")

            elif interval > 60:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Слишком большой интервал.")

            elif interval < 0:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Интервал не может быть отрицательным.")

            elif num_call > 200:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Слишком большое количество вызовов.")

            elif num_call < 5:
                vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Слишком маленькое количество вызовов.")

            else:
                call()

        if event.obj.text == "/call" and event.from_chat:
            vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Для использования /call пиши\n/call *id* *кол. вызовов* *интервал* *одн. код-пароль* *сообщение (необязательно)*\nИнтервал от 0 до 60 cек. Количество вызовов от 5 до 200.")

        if event.obj.text == "/testbot" and event.from_chat:
            vk.messages.send(random_id=get_random_id(), peer_id=event.obj.peer_id, message="Бот работает.")