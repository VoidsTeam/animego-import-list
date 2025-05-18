 [ For English](#English) - | --- | - [ Для Русских](#Русский)

## en - Need help? Contact the technical support of "VoidTeam" - ru Нужна помощь? Свяжитесь с технической поддержкой "VoidTeam"

## English

# animego-import-list

A tool for importing anime lists from Animego.org to Shikimori.one. Convert and transfer your anime collection with preserved watching status, episode counts, and ratings.

## Features

- Parsing HTML file with anime list from Animego.org
- Saving data to intermediate CSV file
- Converting to JSON format for Shikimori import
- Automatic anime ID retrieval via Shikimori API
- Correct mapping of watching statuses between platforms
- Processing various anime types (TV, movies, OVA, etc.)

## Requirements

- Python 3.x
- Dependencies from requirements.txt:
  - aiohttp>=3.8.0
  - beautifulsoup4>=4.9.3
  - requests>=2.25.1
  - typing-extensions>=4.0.0

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Save your anime list page from Animego.org to `list-anime.html` file
2. If you are importing a new anime list, delete the cache file `anime_id_cache.json` if it exists (this is important to avoid using cached IDs from previous imports)
3. Run the script:
```bash
python anime_converter.py
```
4. After the script completes, `shikimori_import.json` file will be created, ready for import to Shikimori

> **Important**: Always delete `anime_id_cache.json` before importing a different anime list to ensure correct ID matching

## Conversion Process

1. Parse HTML file and extract anime information (titles, status, ratings, episode count)
2. Save data to CSV file for possible intermediate verification
3. Convert data to Shikimori format considering:
   - Status mapping
   - Correct episode count calculation
   - Anime type conversion
4. Get anime IDs via Shikimori API
5. Save final JSON file

## Features

- Automatic error handling during parsing
- Delays between Shikimori API requests to avoid rate limits
- Alternative anime search when exact matches are not found
- Correct handling of various data formats 
                                            Readme is written using AI

---

  ## Русский

# animego-import-list

Инструмент для импорта списка аниме с Animego.org на Shikimori.one. Конвертирует и переносит вашу коллекцию аниме с сохранением статусов просмотра, количества эпизодов и оценок.

## Возможности

- Парсинг HTML-файла со списком аниме с Animego.org
- Сохранение данных в промежуточный CSV-файл
- Конвертация в JSON-формат для импорта на Shikimori
- Автоматическое получение ID аниме через API Shikimori
- Корректное сопоставление статусов просмотра между платформами
- Обработка различных типов аниме (ТВ, фильмы, OVA и т.д.)

## Требования

- Python 3.x
- Зависимости из requirements.txt:
  - aiohttp>=3.8.0
  - beautifulsoup4>=4.9.3
  - requests>=2.25.1
  - typing-extensions>=4.0.0

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

1. Сохраните страницу со своим списком аниме с Animego.org в файл `list-anime.html`
2. Если вы импортируете новый список аниме, удалите файл кэша `anime_id_cache.json`, если он существует (это важно, чтобы избежать использования кэшированных ID от предыдущих импортов)
3. Запустите скрипт:
```bash
python anime_converter.py
```
4. После завершения работы скрипта будет создан файл `shikimori_import.json`, готовый к импорту на Shikimori

> **Важно**: Всегда удаляйте файл `anime_id_cache.json` перед импортом нового списка аниме, чтобы обеспечить корректное сопоставление ID

## Процесс конвертации

1. Парсинг HTML-файла и извлечение информации об аниме (названия, статус, оценки, количество эпизодов)
2. Сохранение данных в CSV-файл для возможности промежуточной проверки
3. Конвертация данных в формат Shikimori с учетом:
   - Сопоставления статусов
   - Корректного подсчета просмотренных эпизодов
   - Преобразования типов аниме
4. Получение ID аниме через API Shikimori
5. Сохранение финального JSON-файла

## Особенности

- Автоматическая обработка ошибок при парсинге
- Задержки между запросами к API Shikimori во избежание превышения лимитов
- Альтернативный поиск аниме при отсутствии точных совпадений
- Корректная обработка различных форматов данных
                                            Readme написан с помощью ии
