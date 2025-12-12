class User:
    # Конструктор класса
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Методы для отображения информации
    def get_first_name(self):
        print("Имя:", self.first_name)

    def get_last_name(self):
        print("Фамилия:", self.last_name)

    def get_full_name(self):
        print("Полное имя:", f"{self.first_name} {self.last_name}")
