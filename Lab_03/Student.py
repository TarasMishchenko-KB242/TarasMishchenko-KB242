class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __repr__(self):
        return f"Ім'я: {self.name}, Тел: {self.phone}, Email: {self.email}, Група: {self.group}"

    def to_dict(self):
        """Перетворює об'єкт у словник для збереження в CSV."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group
        }