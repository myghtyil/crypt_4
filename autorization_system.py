import hashlib
import time

#hash_s = hashlib.sha3_224(data.encode('utf-8')).hexdigest()

base = {}
def registration():
    print("Введите логин: ")
    login = input()
    while True:
        print("Введите пароль: ")
        password = hashlib.sha3_224(input().encode('utf-8')).hexdigest()
        print("подтвердите пароль: ")
        conf_password = hashlib.sha3_224(input().encode('utf-8')).hexdigest()
        if password == conf_password:
            break
        else:
            print ("Пароли не совпадают!")
            time.sleep(1)
    base.update([(login , password)])
    print("Регистрация выполнена успешно!")
    time.sleep(1)
    print(base)

def autorisation():
    while True:
        print("Введите логин: ")
        login = input()
        print("Введите пароль: ")
        password = hashlib.sha3_224(input().encode('utf-8')).hexdigest()
        if base.get(login) == password:
            print("Авторизация выполнена!")
            time.sleep(1)
            break
        else:
            print ("Неправильный пароль!")
            time.sleep(1)
    
def menu():
    print(" 1 - регистрация / 2 - авторизация / exit - выход")
    ans = input()
    if ans == '1':
        registration()
    elif ans == '2':
        autorisation()
    else:
        exit()

while True:
    menu()

time.sleep(100)
    
