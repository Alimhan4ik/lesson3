# lesson_3_task_3.py
from address import Address
from mailing import Mailing

# Создаем адреса отправки и доставки
to_addr = Address(index='368060', city='Бабаюрт', street='Буйнакская', house='15', apartment='0')
from_addr = Address(index='367000', city='Махачкала', street='Гамидова', house='100', apartment='5')

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=2500,
    track='TRACK123'
)

# Форматируем и выводим отправление
output = f"""
Отправление {mailing.track}
из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment}
в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}.
Стоимость {mailing.cost} рублей."""

print(output.strip())