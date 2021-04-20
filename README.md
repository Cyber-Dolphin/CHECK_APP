Для скачивания и проверки хэша, версии и размера файла необходимо получить gsfId и authSubToken виртуального устройства выполнив скрипт reg_device.py.

Залогиньтесь в Google Play, заполнив соответствующие переменные:

mail = "myemail@gmail.com"

passwd = "mypasswd"

**Сохраните значения gsfId и authSubToken.**




После чего заполните переменные скрипта var_app.py в папке variable_app:

cloud_app = "App from Google Play"

local_app = "Path to my local app"

gsfId = int("My android ID")

authSubToken = "My token"

Файл из Google Play скачивается и проверяется в директории запуска скрипта.

Локальный файл расположите в директории local_app.
