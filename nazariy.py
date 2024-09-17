#  1 - Javob:
#    kompilyator - yozilgan kodni mahsus dastur bilan kompilyatsiya qilinadi. kompilyator kodni o'qiydi, xatolarni tekshiradi va mashina kodiga aylantiradi.
#    interpretator - yozilgan kodni kompilyatsiya qilmasdan, bevosita bajariladi. interpretator kodni qator-qator o'qiydi, xatolarni tekshiradi va bajaradi.
#---------------------------------------------------------------------
#  2 - Javob:
#    Python da quyidagi ma'lumot turlari mavjud:
#      1. Butun sonlar (int)
#      2. Haqiqiy sonlar (float)
#      3. Matnlar (str)
#      4. Mantiqiy qiymatlar (bool)
#      5. Ro'yxatlar (list)
#      6. Lug'atlar (dict)
#      7. To'plamlar (set)
#      8. Tuple (tuple)
#---------------------------------------------------------------------
#  3 - Javob:
# Tuple - o'zgartirib bo'lmaydigan ro'yxat. 
# List - o'zgartiriladigan ro'yxat.
# Set - takrorlanmaydigan qiymatlar to'plami.
# Dictionary - kalit-qiymat juftligidan iborat ma'lumotlar to'plami.
#---------------------------------------------------------------------
#4 - Javob:
# Iterative function
def factorial_iterative(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

# Recursive function
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Lambda function
factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)

# Test
print(factorial_iterative(5))  # 120
print(factorial_recursive(5))  # 120
print(factorial_lambda(5))  # 120

#---------------------------------------------------------------------
# 5 - Javob:
# Modul misoli
import math
print(math.pi)

# Exception misoli
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas")

#---------------------------------------------------------------------
# 6 - Javob:
# Foydalanuvchi ismini faylga yozish
ism = input("Ismingizni kiriting: ")
f = open("ism.txt", "w")
f.write(ism)
f.close()

# Fayldan ma'lumot o'qish
f = open("ism.txt", "r")
print(f.read())
f.close()

# Faylga ma'lumot qo'shish
f = open("ism.txt", "a")
f.write("\nSalom, men Python dasturchiman!")
f.close()

# Fayldan ma'lumot o'qish
f = open("ism.txt", "r")
print(f.read())
f.close()

# JSON file lar bilan ishlash
import json
# JSON fayl yaratish
data = {
    "ism": "John",
    "yosh": 30,
    "shahar": "New York"
}
with open("data.json", "w") as f:
    json.dump(data, f)

# JSON fayldan ma'lumot o'qish
with open("data.json", "r") as f:
    data = json.load(f)
print(data)

# JSON faylga ma'lumot qo'shish
data["mamlakat"] = "AQSh"
with open("data.json", "w") as f:
    json.dump(data, f)

# JSON fayldan ma'lumot o'qish
with open("data.json", "r") as f:
    data = json.load(f)
print(data)

#---------------------------------------------------------------------
# 7 - Javob:
from abc import ABC, abstractmethod

class Telefon(ABC):
    def __init__(self, brendi, modeli):
        self.brendi = brendi
        self.modeli = modeli
        self._id = f"{brendi}_{modeli}_ID"
        self._narxi = 0

    @abstractmethod
    def id_sini_korish(self):
        pass

    @abstractmethod
    def narx_qoyish(self, narx):
        pass

    @abstractmethod
    def narxini_korish(self):
        pass


class IPhone(Telefon):
    def id_sini_korish(self):
        return self._id

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi


class Samsung(Telefon):
    def id_sini_korish(self):
        return self._id

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi


def save_phones_to_file(phones, filename):
    with open(filename, 'w') as file:
        for phone in phones:
            file.write(f"{phone.brendi},{phone.modeli},{phone.narxini_korish()}\n")


def load_phones_from_file(filename):
    phones = []
    with open(filename, 'r') as file:
        for line in file:
            brendi, modeli, narx = line.strip().split(',')
            if brendi == "Samsung":
                phone = Samsung(brendi, modeli)
            elif brendi == "iPhone":
                phone = IPhone(brendi, modeli)
            phone.narx_qoyish(int(narx))
            phones.append(phone)
    return phones


def main():
    phones = []
    while True:
        print("0. Chiqish")
        print("1. Telefon qo'shish")
        print("2. Telefonlarni ko'rish")
        print("3. Telefon ustida amallar")
        choice = int(input("Tanlov: "))

        if choice == 0:
            break
        elif choice == 1:
            brendi = input("Brendi: ")
            modeli = input("Modeli: ")
            narx = int(input("Narx: "))
            if brendi == "Samsung":
                phone = Samsung(brendi, modeli)
            elif brendi == "iPhone":
                phone = IPhone(brendi, modeli)
            phone.narx_qoyish(narx)
            phones.append(phone)
        elif choice == 2:
            for phone in phones:
                print(f"Brendi: {phone.brendi}, Modeli: {phone.modeli}, Narxi: {phone.narxini_korish()}")
        elif choice == 3:
            id_to_find = input("ID ni kiriting: ")
            for phone in phones:
                if phone.id_sini_korish() == id_to_find:
                    print(f"Telefon: {phone.brendi} {phone.modeli}")
                    print(f"Narx: {phone.narxini_korish()}")
                    new_price = int(input("Yangi narx: "))
                    phone.narx_qoyish(new_price)
                    print(f"Yangi narxi: {phone.narxini_korish()}")
                    break
            else:
                print("Telefon topilmadi.")

    save_phones_to_file(phones, 'phones.txt')
    phones = load_phones_from_file('phones.txt')
    
#---------------------------------------------------------------------
# 8 - Javob:
    GitHub_link = "https://github.com/M624T/Uyga-vazifa-11-dars-Asosiy.git"
