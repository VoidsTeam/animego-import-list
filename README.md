[For English](#English) - | --- | - [Для Русских](#Русский)

[Technical support](mailto:voidemptiness63@gmail.com) - [Тех.Подержка](mailto:voidemptiness63@gmail.com)

## English

The README was written with the help of AI. If you find any inconsistencies, write to technical support.

# animego-import-list

A tool for importing anime lists from Animego.org to Shikimori.one. Convert and transfer your anime collection with preserved watching status, episode counts, and ratings.

## Features

- Parsing HTML file with anime list from Animego.org
- Saving data to intermediate CSV file for verification
- Converting to JSON format for Shikimori import
- Automatic anime ID retrieval via Shikimori API
- Correct mapping of watching statuses between platforms
- Processing various anime types (TV, movies, OVA, etc.)
- Error handling and detailed logging

## Requirements

- Python 3.x
- Dependencies from requirements.txt:
  - aiohttp>=3.8.0
  - beautifulsoup4>=4.9.3
  - requests>=2.25.1
  - typing-extensions>=4.0.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VoidsTeam/animego-import-list.git
cd animego-import-list
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Export your anime list from Animego.org:
   - Log in to your Animego.org account
   - Go to your profile's anime list
   - Save the entire page (Ctrl+S or ⌘+S) as HTML file
   - Name the saved file as `list-anime.html`
   - Place the file in the same directory as the script

2. Prepare for conversion:
   - If you are importing a new anime list, delete the cache file `anime_id_cache.json` if it exists
   - This step is important to avoid using cached IDs from previous imports

3. Run the script:
```bash
python anime_converter.py
```

4. Check the conversion:
   - The script will create intermediate file `anime_list.csv` for verification
   - The final result will be in `shikimori_import.json`
   - Check the console output for any warnings or errors
   - Verify that all anime titles are correctly listed in the CSV file

5. Import to Shikimori:
   - Go to Shikimori.one
   - Use the `shikimori_import.json` file for import

> **Important Notes**: 
> - Always delete `anime_id_cache.json` before importing a different anime list
> - If you see any errors during conversion, check the console output for details
> - The script creates backup files in case of conversion issues

## Troubleshooting

If you encounter issues:
1. Make sure your `list-anime.html` file is valid and complete
2. Check that all dependencies are installed correctly
3. Look for error messages in the console output
4. Verify the content of `anime_list.csv` for any missing or incorrect data
5. Contact technical support if problems persist

---

## Русский

Readme был написан с помощью ИИ, если нашли несостыковки, напишите в техподдержку.

# animego-import-list

Инструмент для импорта списка аниме с Animego.org на Shikimori.one. Конвертирует и переносит вашу коллекцию аниме с сохранением статусов просмотра, количества эпизодов и оценок.

## Возможности

- Парсинг HTML-файла со списком аниме с Animego.org
- Сохранение данных в промежуточный CSV-файл для проверки
- Конвертация в JSON-формат для импорта на Shikimori
- Автоматическое получение ID аниме через API Shikimori
- Корректное сопоставление статусов просмотра между платформами
- Обработка различных типов аниме (ТВ, фильмы, OVA и т.д.)
- Обработка ошибок и подробное логирование

## Требования

- Python 3.x
- Зависимости из requirements.txt:
  - aiohttp>=3.8.0
  - beautifulsoup4>=4.9.3
  - requests>=2.25.1
  - typing-extensions>=4.0.0

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/VoidsTeam/animego-import-list.git
cd animego-import-list
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

1. Экспорт списка аниме с Animego.org:
   - Войдите в свой аккаунт на Animego.org
   - Перейдите в список аниме в своём профиле
   - Сохраните всю страницу (Ctrl+S или ⌘+S) как HTML файл
   - Назовите сохранённый файл `list-anime.html`
   - Поместите файл в ту же папку, где находится скрипт

2. Подготовка к конвертации:
   - Если вы импортируете новый список аниме, удалите файл кэша `anime_id_cache.json`, если он существует
   - Этот шаг важен, чтобы избежать использования кэшированных ID от предыдущих импортов

3. Запустите скрипт:
```bash
python anime_converter.py
```

4. Проверка конвертации:
   - Скрипт создаст промежуточный файл `anime_list.csv` для проверки
   - Финальный результат будет в `shikimori_import.json`
   - Проверьте консольный вывод на наличие предупреждений или ошибок
   - Убедитесь, что все названия аниме правильно указаны в CSV файле

5. Импорт на Shikimori:
   - Перейдите на Shikimori.one
   - Используйте файл `shikimori_import.json` для импорта

> **Важные замечания**: 
> - Всегда удаляйте `anime_id_cache.json` перед импортом нового списка аниме
> - Если во время конвертации возникают ошибки, проверьте консольный вывод
> - Скрипт создаёт резервные копии файлов на случай проблем с конвертацией

## Устранение проблем

Если возникли проблемы:
1. Убедитесь, что файл `list-anime.html` валидный и полный
2. Проверьте, что все зависимости установлены корректно
3. Просмотрите сообщения об ошибках в консольном выводе
4. Проверьте содержимое `anime_list.csv` на наличие пропущенных или некорректных данных
5. Обратитесь в техподдержку, если проблемы сохраняются
