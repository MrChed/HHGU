
# Скрипт для скачивания аудио с RuTube

Данный скрипт позволяет скачивать аудио из видео на RuTube и сохранять их в формате MP3.

## Установка и настройка

### 1. Установите Python
Убедитесь, что у вас установлен Python версии 3.12 или выше. Если Python не установлен, загрузите его с официального сайта:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Создайте и активируйте виртуальное окружение
Для изоляции зависимостей создайте виртуальное окружение:
```bash
python -m venv .venv
```

Активируйте виртуальное окружение:
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **MacOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Установите необходимые зависимости
Установите библиотеку `yt-dlp`, которая используется для скачивания видео:
```bash
pip install yt-dlp
```

### 4. Настройте директорию для сохранения файлов
Скрипт по умолчанию сохраняет аудиофайлы в папку:
```
C:\Users\salom\Project\hams\Cheks\ннгу проект\Downloaded_Videos
```
Если папка не существует, она будет создана автоматически. Вы можете изменить путь к папке, редактируя код скрипта.

## Запуск скрипта

1. Склонируйте или скачайте репозиторий с кодом.
2. Перейдите в папку с проектом.
3. Запустите скрипт с помощью Python:
```bash
python script.py
```

Скрипт попросит вас ввести ссылку на видео с RuTube. После этого аудиофайл будет скачан в указанную директорию.

## Возможные ошибки
Если возникают ошибки при скачивании, убедитесь, что видео доступно для загрузки и ссылка правильная. В случае проблем с форматом видео или ошибками подключения, обратитесь к документации библиотеки yt-dlp для уточнений.

