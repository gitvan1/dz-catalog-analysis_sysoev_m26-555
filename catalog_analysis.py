import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", 
                                                    "O. Isaac"]},
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
    return max(age), min(age), math.ceil(sum(age) / len(age))

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
    return (f'"{normalize_title(movie["title"])}" ({movie["year"]}) - ' +
            f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}' +
            f', жанры: {", ".join(sorted(movie["genres"]))}')

# Этап 5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    return [movie['title'] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    return [(movie['title'], movie['rating']) for movie in sorted_movies[:n]]

# Этап 6
def count_by_genre(movies):
    dict_genres = {}
    for movie in movies:
        for genre in movie['genres']:
            dict_genres[genre] = dict_genres.get(genre, 0) + 1
    return dict_genres

def actor_filmography(movies):
    dict_actors = {}
    for movie in movies:
        for actor in movie['actors']:
            current_films = dict_actors.get(actor, [])
            current_films.append(movie['title'])
            dict_actors[actor]  = current_films
    return dict_actors

def titles_above_average(movies):
    return {m['title']: 
            m['rating'] for m in movies if m['rating'] > average_rating(movies)}

# Этап 7
def all_genres(movies):
    set_genres = set()
    for m in movies:
        set_genres = set_genres | m['genres']
    return set_genres

def common_actors(movie1, movie2):
    return set(movie1['actors']) & set(movie2['actors'])

def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)

# Этап 8
def iter_high_rated(movies, min_rating=8.0):
    for m in movies:
        if m['rating'] >= min_rating:
            yield m

def check_iter_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    return sum(m["duration_min"] for m in iter_high_rated(movies, 7))

# Этап 9
def build_report(movies):
    print('\nОТЧЕТ ПО КАТАЛОГУ')
    print(f'Средний рейтинг: {average_rating(movies)}')
    print(f'Средний возраст фильмов: {catalog_age_stats(movies)[-1]} лет')

    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    print('\nТоп-3 фильма:')
    print(' ', '\n  '.join(map(format_report_line, sorted_movies[:3])))

    print('\nФильмов по жанрам:')
    for g in sorted(count_by_genre(movies).items(), key=lambda g: -g[1]):
        print(f'  {g[0]} - {g[1]}')

    print(f'\nВсе жанры каталога: {", ".join(all_genres(movies))}')

# Вывод отчета
if __name__ == "__main__":
    build_report(movies)