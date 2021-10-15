from forex_python.converter import CurrencyRates as rate
import sys
import time
from vk_api import VkApi
login = str(input("Login: "))
password = str(input("Password: "))
vk_session = VkApi(login=login, password=password)
try:
    vk_session.auth()
    print("Vk susccessfully authed")
except Exception as e:
    print(e)
    sys.exit(1)
post_id = int(input("PostId: "))
print("Good! We starting work")
vk = vk_session.get_api()
c = rate()
while True:
    res = c.get_rate("USD", "RUB")
    val = round(res)
    try:
        vk.wall.edit(post_id=post_id, message=f"Текущий курс доллара: {val} рублей\nОбновление курса происходит автоматически каждые 24 часа\nПодробнее здесь: https://github.com/svelout/exchangeratevk")
    except Exception as e:
        vk.messages.send(message=f"Произошла ошибка: {e}")
        sys.exit(-1)
    time.sleep(3600)


