from smartphone import Smartphone

# Список телефонов
catalog = [
    Smartphone("Apple", "iPhone 16 Pro Max", "+79285372738"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79287654321"),
    Smartphone("Xiaomi", "Redmi Note 11S", "+79289876543"),
    Smartphone("Huawei", "P50 Pro", "+79281112233"),
    Smartphone("Google", "Pixel 7 Pro", "+79285556677")
]

# Цикл для вывода списка телефонов
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")