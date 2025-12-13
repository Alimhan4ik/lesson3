from user import User

# Создание нового пользователя
my_user = User("Аджиев","Алим")

# Вызов методов для вывода информации
print(my_user.get_first_name())      # Имя: Алим
print(my_user.get_last_name())       # Фамилия: Аджиев
print(my_user.get_full_name())       # Полное имя: Алим Аджиев
