[app]
# Имя вашего приложения
title = WarriorTask
package.name = task
package.domain = org.example

# Укажите ваш основной Python-скрипт
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = pyc,pyo

# Данные о зависимости
dependencies = kivy, python3, sqlite3  # Добавьте необходимые зависимости

# Параметры Android
android.sdk_path = /usr/lib/android-sdk
android.ndk_path = /usr/lib/android-ndk
android.api = 28  # Версия API Android
android.minapi = 21  # Минимальная версия Android
android.arch = armeabi-v7a  # Архитектура для сборки
android.permissions = INTERNET,ACCESS_FINE_LOCATION  # Разрешения, которые вам нужны

# Параметры для сборки
log_level = 2  # Уровень логирования, 2 - это для отладки
