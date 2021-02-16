import json
import random as rnd
import string

# 1. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

path = "names.txt"
result = []

with open(path, "r") as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.strip())

    for stroka in data:
        stroka = stroka.split('\t')
        result.append(stroka[1])

print(result)

###

# 2. Создать функцию для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

result = {}


def generate_rnd_str():
    letters = string.ascii_lowercase
    rand_str = ''.join(rnd.choice(letters) for i in range(6))
    return rand_str


def generate_rnd_value(chance):
    rnd_value = 0
    if chance <= 4:
        rnd_value = rnd.randint(-100, 100)
    elif 4 < chance <= 8:
        rnd_value = rnd.random()
    elif 8 < chance <= 12:
        rnd_value = bool(rnd.randint(0, 1))
    return rnd_value


def generate_rnd_dict(tmp=rnd.randint(5, 20)):
    for i in range(tmp):
        chance = rnd.randint(1, 12)
        result[generate_rnd_str()] = generate_rnd_value(chance)
    return result


# print(generate_rnd_dict())

###

# 3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
# Сгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.

filename = "json.json"


def generate_and_write_json(filename):
    with open(filename, "w") as json_file:
        data = generate_rnd_dict()
        json.dump(data, json_file, indent=2)


generate_and_write_json(filename)
