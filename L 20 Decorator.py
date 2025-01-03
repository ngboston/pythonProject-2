import webbrowser
# Дикоратор
def validator(func):
    def wrapper(url):
#       print("Befor")
        if "." in url: # Перевіряємо на наявність крапки
            func(url)
#       print("After")
        else:
            print("Посилання не правельне")
    return wrapper

@validator  # Включення дикоратора
def open_url(url):       # Основна Функція
    webbrowser.open(url)

open_url("https://itproger.com/ua")
