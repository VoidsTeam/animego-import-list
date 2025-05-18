import os
import csv
import json
import asyncio
from bs4 import BeautifulSoup
from shikimori_api import update_anime_ids

def parse_anime_list(html_file):
    """Парсинг списка аниме из HTML файла"""
    print("Парсинг HTML файла...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    print("Парсинг HTML файла...")
    anime_list = []
    table = soup.find('table')
    
    if not table:
        print("Таблица не найдена")
        return []

    tbody = table.find('tbody')
    if not tbody:
        print("Тело таблицы не найдено")
        return []

    first_row = tbody.find('tr')
    if first_row:
        print("\nПервая строка данных:")
        print(first_row.prettify())
        
        tds = first_row.find_all('td')
        print("\nАнализ ячеек первой строки данных:")
        for i, td in enumerate(tds):
            print(f"\nЯчейка {i}:")
            print(td.prettify())

    rows = tbody.find_all('tr')
    print(f"\nНайдено {len(rows)} строк с данными")

    for row in rows:
        try:
            cols = row.find_all('td')
            if len(cols) >= 6:  
                title_cell = cols[1]  
                name_link = title_cell.find('a')  
                name_div = title_cell.find('div', class_='text-gray-dark-6')

                if name_link and name_div:
                    russian_name = name_link.get_text(strip=True)
                    english_name = name_div.get_text(strip=True)
                    
                    status = cols[2].find('span')
                    if status:
                        status = status.get_text(strip=True)
                    else:
                        status = cols[2].get_text(strip=True)
                    
                    episodes = cols[4].get_text(strip=True)
                    type_col = cols[5].get_text(strip=True)
                    score = cols[3].get_text(strip=True)

                    print(f"Найдено аниме: {russian_name} / {english_name}")
                    
                    anime_list.append({
                        'russian_name': russian_name,
                        'english_name': english_name,
                        'status': status,
                        'episodes': episodes,
                        'type': type_col,
                        'score': score if score != '–' else '0'
                    })
        except Exception as e:
            print(f"Ошибка при обработке строки: {str(e)}")
            continue
    
    return anime_list

def save_to_csv(anime_list, csv_file):
    """Сохранение списка аниме в CSV файл"""
    print("Сохранение в CSV...")
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['russian_name', 'english_name', 'status', 'score', 'episodes', 'type'])
        writer.writeheader()
        writer.writerows(anime_list)

def convert_to_shikimori(csv_file):
    """Конвертация CSV в формат Shikimori"""
    print("Конвертация в формат Shikimori...")
    
    shikimori_list = []
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            status_map = {
                'Просмотрено': 'completed',
                'Смотрю': 'watching',
                'Брошено': 'dropped',
                'Отложено': 'on_hold',
                'Запланировано': 'planned'
            }
            status = status_map.get(row['status'], 'planned')
            episodes_str = row['episodes'].split('/')[0].strip()
            episodes_str = '0' if episodes_str in ['–', '?'] else episodes_str
            episodes = int(episodes_str) if episodes_str.isdigit() else 0

            if status == 'completed' and episodes == 0:
                total_eps = row['episodes'].split('/')[1].strip() if '/' in row['episodes'] else '0'
                total_eps = total_eps.rstrip('(?)')
                if total_eps.isdigit():
                    episodes = int(total_eps)

            anime_type = {
                'ТВ Сериал': 'tv',
                'Фильм': 'movie',
                'OVA': 'ova',
                'ONA': 'ona',
                'Спешл': 'special'
            }.get(row['type'], 'tv')

            entry = {
                'target_title': row['russian_name'],
                'target_title_eng': row['english_name'],
                'target_type': 'Anime',
                'target_id': 0,
                'status': status,
                'score': int(row['score']) if row['score'].isdigit() else 0,
                'episodes': episodes,
                'type': anime_type
            }
            shikimori_list.append(entry)
    
    with open('shikimori_import.json', 'w', encoding='utf-8') as file:
        json.dump(shikimori_list, file, ensure_ascii=False, indent=2)
    
    return 'shikimori_import.json'

async def main():
    html_file = 'list-anime.html'
    csv_file = 'anime_list.csv'

    if not os.path.exists(html_file):
        print(f"Ошибка: файл {html_file} не найден")
        return

    anime_list = parse_anime_list(html_file)

    save_to_csv(anime_list, csv_file)

    json_file = convert_to_shikimori(csv_file)

    await update_anime_ids(json_file)
    
    print("\nКонвертация завершена! Файл shikimori_import.json готов к импорту.")

if __name__ == "__main__":
    asyncio.run(main())
