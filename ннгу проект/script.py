import os
from yt_dlp import YoutubeDL
import argparse

def download_audio(link, folder_path="C:\\Users\\salom\\Project\\hams\\Cheks\\ннгу проект\\Downloaded_Videos"):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        ydl_opts = {
            'format': 'bestaudio/best',  # Выбирает лучшее доступное аудио
            'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print(f"Аудио успешно скачано в папку: {folder_path}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Попробуйте другую ссылку или проверьте соединение.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачивание аудио с RuTube")
    parser.add_argument("video_link", nargs="?", help="Ссылка на видео с RuTube")
    args = parser.parse_args()

    if not args.video_link:
        args.video_link = input("Введите ссылку на видео: ")

    download_audio(args.video_link)
