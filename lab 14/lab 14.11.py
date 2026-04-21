users = {}

# добавление
users["Иван"] = 20
users["Анна"] = 22

# поиск
print(users.get("Анна"))

# удаление
del users["Иван"]

print(users)