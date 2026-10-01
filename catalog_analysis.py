from math import *

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1
def average_rating(movies):
    ratings = [movie['rating'] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)

def catalog_age_stats(movies, current_year=2026):
    age = [current_year - movie['year'] for movie in movies]
    return max(age), min(age), ceil(sum(age) / len(age))

def duration_in_hours(minutes):
    return f'{minutes // 60}ч {minutes %60}м'

# Этап 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"
    
def decade_label(year):
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case _:
            return "старые"
        
# Этап 3
print('Названия всех фильмов, которые не относятся к жанру "comedy":')
for movie in movies:
    if "comedy" in movie['genres']:
        continue 
    print(movie['title'])

print('\nПоиск шедевров:')
i = 0
while i < len(movies):
    if movies[i]['rating'] >= 9.0:
        print(f'{movies[i]['title']} с рейтингом {movies[i]['rating']}')
        break
    i += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    counter = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            counter += 1
    return counter

# Этап 4
def normalize_title(title: str) -> str:
    words = title.split(' ')
    new_title = ''
    for word in words:
        new_title += word[0].upper() + word[1:] + ' '
    return new_title[:-1]

def make_slug(title: str) -> str:
    return title.lower().replace(' ', '-')

def format_report_line(movie: dict) -> str:
    return (f'"{normalize_title(movie["title"])}" ({movie["year"]}) - {movie["rating"]}/10, ' +
            f'{duration_in_hours(movie["duration_min"])}, жанры: {", ".join(sorted(movie["genres"]))}')